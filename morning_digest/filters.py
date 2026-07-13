"""Keyword filtering and news deduplication."""

from __future__ import annotations

from datetime import datetime
from typing import TypedDict


class NewsItem(TypedDict):
    src: str
    title: str
    desc: str
    link: str
    date: datetime


def matches_filters(
    title: str,
    desc: str,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
) -> bool:
    """Return True when the item passes include/exclude keyword filters."""
    text = f"{title} {desc}".lower()
    include = include or []
    exclude = exclude or []

    if include and not any(kw.lower() in text for kw in include):
        return False
    if exclude and any(kw.lower() in text for kw in exclude):
        return False
    return True


def dedupe_by_title(items: list[NewsItem], prefix_len: int = 50) -> list[NewsItem]:
    """Drop near-duplicate headlines using a lowercased title prefix."""
    unique: list[NewsItem] = []
    seen: set[str] = set()
    for item in items:
        key = item["title"].lower()[:prefix_len]
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def sort_by_date_desc(items: list[NewsItem]) -> list[NewsItem]:
    return sorted(items, key=lambda item: item["date"], reverse=True)
