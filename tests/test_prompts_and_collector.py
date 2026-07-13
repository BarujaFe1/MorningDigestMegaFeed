"""Tests for prompt building and demo collection."""

from datetime import date, datetime

from morning_digest.collector import collect_news
from morning_digest.demo_data import DEMO_FEED_URLS
from morning_digest.prompts import build_prompt, get_template, stoic_quote_for


def test_get_template_fallback():
    assert get_template("inexistente").name == "Padrão"
    assert get_template("Crypto & Mercado").name == "Crypto & Mercado"


def test_stoic_quote_stable_for_day():
    assert stoic_quote_for(date(2026, 7, 13)) == stoic_quote_for(date(2026, 7, 13))


def test_build_prompt_empty_state():
    text = build_prompt([], get_template("Padrão"), day=date(2026, 7, 13))
    assert "Sem notícias" in text
    assert "Padrão" in text


def test_build_prompt_with_items():
    items = [
        {
            "src": "DEMO",
            "title": f"Título {i}",
            "desc": "Resumo curto",
            "link": f"https://example.com/{i}",
            "date": datetime(2026, 7, 13, 10, i % 60),
        }
        for i in range(20)
    ]
    text = build_prompt(items, get_template("Estoico & Resumido"), day=date(2026, 7, 13))
    assert "15 DESTAQUES" in text
    assert "RADAR RÁPIDO" in text
    assert "Título 0" in text


def test_demo_collection_offline():
    items, errors = collect_news(DEMO_FEED_URLS, demo=True)
    assert errors == 0
    assert len(items) >= 5
    assert all(item["title"] for item in items)


def test_demo_collection_respects_exclude():
    items, _errors = collect_news(
        DEMO_FEED_URLS,
        demo=True,
        exclude=["Bitcoin", "bitcoin"],
    )
    titles = " ".join(item["title"] for item in items).lower()
    assert "bitcoin" not in titles
