"""Regression: public claims that must stay true in code."""

from pathlib import Path

from morning_digest.collector import collect_news
from morning_digest.demo_data import DEMO_FEED_URLS


def test_demo_pipeline_produces_markdown_headings():
    items, errors = collect_news(DEMO_FEED_URLS, demo=True)
    assert errors == 0
    assert len(items) >= 5
    from morning_digest.prompts import build_prompt, get_template

    text = build_prompt(items, get_template("Padrão"))
    assert "BOM DIA" in text or "BOM DIA!" in text
    assert "DESTAQUES" in text
    assert "DEMO.LOCAL" in text or "example.com" in text


def test_collector_is_sequential_not_threaded():
    """Documented behavior: feeds are processed one-by-one (isolation, not parallel)."""
    import inspect

    from morning_digest import collector

    source = inspect.getsource(collector.collect_news)
    assert "for index, url in enumerate" in source
    assert "ThreadPoolExecutor" not in source
    assert "concurrent.futures" not in inspect.getsource(collector)


def test_screenshots_exist_for_portfolio():
    root = Path(__file__).resolve().parents[1] / "docs" / "screenshots"
    for name in (
        "01-collector-empty.png",
        "02-collector-demo.png",
        "03-settings.png",
    ):
        path = root / name
        assert path.exists(), f"missing {path}"
        assert path.stat().st_size > 10_000
