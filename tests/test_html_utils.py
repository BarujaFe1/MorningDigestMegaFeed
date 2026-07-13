"""Tests for HTML cleanup and keyword parsing."""

from morning_digest.html_utils import clean_html, parse_keyword_list


def test_clean_html_strips_tags_and_entities():
    raw = "<p>Olá&nbsp;<b>mundo</b></p>"
    assert clean_html(raw) == "Olá mundo"


def test_clean_html_truncates():
    text = "x" * 250
    result = clean_html(text, max_len=100)
    assert result.endswith("...")
    assert len(result) == 103


def test_clean_html_short_text_no_ellipsis():
    assert clean_html("curto") == "curto"


def test_parse_keyword_list():
    assert parse_keyword_list(" a, b , ,c ") == ["a", "b", "c"]
    assert parse_keyword_list("") == []
