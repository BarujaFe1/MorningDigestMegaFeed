"""Tests for keyword filters and deduplication."""

from datetime import datetime, timedelta

from morning_digest.filters import dedupe_by_title, matches_filters, sort_by_date_desc


def test_matches_include_filter():
    assert matches_filters("Bitcoin sobe", "mercado", include=["bitcoin"])
    assert not matches_filters("Ações sobem", "mercado", include=["bitcoin"])


def test_matches_exclude_filter():
    assert not matches_filters("BBB final", "reality", exclude=["bbb"])
    assert matches_filters("Mercado fecha", "bolsa", exclude=["bbb"])


def test_empty_filters_pass_everything():
    assert matches_filters("Qualquer título", "desc")


def test_dedupe_by_title_keeps_first():
    now = datetime.now()
    items = [
        {"src": "A", "title": "Mesma manchete longa aqui", "desc": "1", "link": "1", "date": now},
        {"src": "B", "title": "Mesma manchete longa aqui", "desc": "2", "link": "2", "date": now},
        {"src": "C", "title": "Outra manchete", "desc": "3", "link": "3", "date": now},
    ]
    unique = dedupe_by_title(items)
    assert len(unique) == 2
    assert unique[0]["src"] == "A"


def test_sort_by_date_desc():
    base = datetime(2026, 7, 13, 12, 0, 0)
    items = [
        {"src": "A", "title": "old", "desc": "", "link": "", "date": base - timedelta(hours=2)},
        {"src": "B", "title": "new", "desc": "", "link": "", "date": base},
    ]
    sorted_items = sort_by_date_desc(items)
    assert sorted_items[0]["title"] == "new"
