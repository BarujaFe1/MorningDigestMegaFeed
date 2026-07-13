"""Persistent JSON configuration management."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from morning_digest.feeds import DEFAULT_FEEDS

logger = logging.getLogger(__name__)

CONFIG_FILENAME = "news_config.json"

DEFAULT_CONFIG: dict[str, Any] = {
    "feeds": DEFAULT_FEEDS.copy(),
    "prompt_template": "Padrão",
    "keywords_include": [],
    "keywords_exclude": [],
}


def default_config() -> dict[str, Any]:
    return {
        "feeds": list(DEFAULT_FEEDS),
        "prompt_template": "Padrão",
        "keywords_include": [],
        "keywords_exclude": [],
    }


class ConfigManager:
    """Load and save user settings to a local JSON file."""

    def __init__(self, path: str | Path | None = None) -> None:
        self.path = Path(path) if path else Path(CONFIG_FILENAME)
        self.config = self.load()

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return default_config()
        try:
            with self.path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Config inválida em %s (%s); usando defaults.", self.path, exc)
            return default_config()

        if not isinstance(data, dict):
            return default_config()

        merged = default_config()
        feeds = data.get("feeds")
        if isinstance(feeds, list):
            merged["feeds"] = [str(item).strip() for item in feeds if str(item).strip()]
        template = data.get("prompt_template")
        if isinstance(template, str) and template.strip():
            merged["prompt_template"] = template.strip()
        for key in ("keywords_include", "keywords_exclude"):
            values = data.get(key)
            if isinstance(values, list):
                merged[key] = [str(item).strip() for item in values if str(item).strip()]
        return merged

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(self.config, handle, indent=4, ensure_ascii=False)

    def restore_defaults(self) -> dict[str, Any]:
        self.config = default_config()
        self.save()
        return self.config
