"""RSS collection pipeline (network + demo)."""

from __future__ import annotations

import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from datetime import datetime
from typing import Any

import feedparser

from morning_digest.demo_data import DEMO_ENTRIES_BY_FEED, DEMO_FEED_URLS
from morning_digest.filters import (
    NewsItem,
    dedupe_by_title,
    matches_filters,
    sort_by_date_desc,
)
from morning_digest.html_utils import clean_html

logger = logging.getLogger(__name__)

ProgressCallback = Callable[[str], None]

USER_AGENT = "MorningDigestMegaFeed/1.1 (+https://github.com/BarujaFe1/MorningDigestMegaFeed)"
DEFAULT_TIMEOUT = 8
DEFAULT_LIMIT = 6
PRIORITY_LIMIT = 12


def domain_from_url(url: str) -> str:
    netloc = urllib.parse.urlparse(url).netloc.replace("www.", "")
    return netloc.upper() if netloc else "FEED"


def entry_limit_for(url: str) -> int:
    return PRIORITY_LIMIT if "corinthians" in url.lower() else DEFAULT_LIMIT


def _entry_field(entry: Any, *names: str) -> Any:
    for name in names:
        if isinstance(entry, dict) and name in entry:
            return entry[name]
        value = getattr(entry, name, None)
        if value is not None:
            return value
    return None


def _parse_entry_date(entry: Any) -> datetime:
    published = _entry_field(entry, "published_parsed", "updated_parsed")
    if published:
        try:
            return datetime.fromtimestamp(time.mktime(published))
        except (OverflowError, ValueError, OSError, TypeError):
            pass
    return datetime.now()


def entry_to_news_item(entry: Any, source: str) -> NewsItem:
    title = _entry_field(entry, "title") or "N/A"
    link = _entry_field(entry, "link") or ""
    raw_desc = _entry_field(entry, "summary", "description") or ""
    return {
        "src": source,
        "title": str(title).strip() or "N/A",
        "desc": clean_html(str(raw_desc)),
        "link": str(link).strip(),
        "date": _parse_entry_date(entry),
    }


def fetch_feed_bytes(url: str, timeout: int = DEFAULT_TIMEOUT) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def parse_feed_entries(url: str, *, demo: bool = False, timeout: int = DEFAULT_TIMEOUT) -> list[Any]:
    if demo:
        return list(DEMO_ENTRIES_BY_FEED.get(url, []))

    try:
        payload = fetch_feed_bytes(url, timeout=timeout)
        parsed = feedparser.parse(payload)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        logger.info("Falha ao buscar %s: %s", url, exc)
        # Fallback: let feedparser attempt its own fetch (some feeds need it)
        try:
            parsed = feedparser.parse(url)
        except Exception as inner:  # noqa: BLE001 — network boundary
            logger.info("Fallback feedparser falhou para %s: %s", url, inner)
            return []

    return list(getattr(parsed, "entries", []) or [])


def collect_news(
    feed_urls: list[str],
    *,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
    demo: bool = False,
    on_progress: ProgressCallback | None = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> tuple[list[NewsItem], int]:
    """
    Collect, filter, sort and dedupe news from RSS feeds.

    Returns (items, error_count).
    """
    all_news: list[NewsItem] = []
    errors = 0
    urls = list(feed_urls)
    if demo and not urls:
        urls = list(DEMO_FEED_URLS)

    total = len(urls)
    for index, url in enumerate(urls):
        source = domain_from_url(url)
        if on_progress:
            mode = "DEMO" if demo else "Lendo"
            on_progress(f"{mode} ({index + 1}/{total}): {source}...")

        try:
            entries = parse_feed_entries(url, demo=demo, timeout=timeout)
            if not entries:
                errors += 1
                continue

            limit = entry_limit_for(url)
            for entry in entries[:limit]:
                item = entry_to_news_item(entry, source)
                if not matches_filters(item["title"], item["desc"], include, exclude):
                    continue
                all_news.append(item)
        except Exception as exc:  # noqa: BLE001 — per-feed isolation
            logger.warning("Erro em %s: %s", url, exc)
            errors += 1

    sorted_items = sort_by_date_desc(all_news)
    unique = dedupe_by_title(sorted_items)
    return unique, errors
