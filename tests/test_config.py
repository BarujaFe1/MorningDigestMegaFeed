"""Tests for config load/save and corrupt file recovery."""

import json

from morning_digest.config import ConfigManager
from morning_digest.feeds import DEFAULT_FEEDS, is_valid_feed_url


def test_default_config_when_missing(tmp_path):
    path = tmp_path / "missing.json"
    mgr = ConfigManager(path)
    assert mgr.config["feeds"] == list(DEFAULT_FEEDS)
    assert mgr.config["prompt_template"] == "Padrão"


def test_corrupt_json_falls_back(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{not-json", encoding="utf-8")
    mgr = ConfigManager(path)
    assert isinstance(mgr.config["feeds"], list)
    assert mgr.config["keywords_include"] == []


def test_save_and_reload(tmp_path):
    path = tmp_path / "cfg.json"
    mgr = ConfigManager(path)
    mgr.config["feeds"] = ["https://example.com/feed.xml"]
    mgr.config["keywords_include"] = ["python"]
    mgr.save()

    reloaded = ConfigManager(path)
    assert reloaded.config["feeds"] == ["https://example.com/feed.xml"]
    assert reloaded.config["keywords_include"] == ["python"]


def test_restore_defaults(tmp_path):
    path = tmp_path / "cfg.json"
    mgr = ConfigManager(path)
    mgr.config["feeds"] = ["https://example.com/x"]
    mgr.save()
    mgr.restore_defaults()
    assert mgr.config["feeds"] == list(DEFAULT_FEEDS)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["feeds"] == list(DEFAULT_FEEDS)


def test_is_valid_feed_url():
    assert is_valid_feed_url("https://g1.globo.com/rss/g1/")
    assert is_valid_feed_url("http://feeds.bbci.co.uk/news/rss.xml")
    assert not is_valid_feed_url("ftp://bad")
    assert not is_valid_feed_url("")
    assert not is_valid_feed_url("not-a-url")
