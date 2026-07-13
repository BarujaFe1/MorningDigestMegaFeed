"""HTML/text cleanup helpers for RSS summaries."""

from __future__ import annotations

import html
import re

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def clean_html(text: str, max_len: int = 200) -> str:
    """Strip tags, unescape entities and normalize whitespace."""
    if not text:
        return ""
    plain = _TAG_RE.sub(" ", html.unescape(text))
    plain = _WS_RE.sub(" ", plain).strip()
    if max_len > 0 and len(plain) > max_len:
        return plain[:max_len].rstrip() + "..."
    return plain


def parse_keyword_list(raw: str) -> list[str]:
    """Split a comma-separated keyword string into a clean list."""
    return [part.strip() for part in (raw or "").split(",") if part.strip()]
