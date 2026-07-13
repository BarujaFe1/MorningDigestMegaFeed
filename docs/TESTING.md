# Testing

## Philosophy

Test the **domain pipeline** (clean → filter → dedupe → prompt → config) without opening the GUI. Network is mocked via **demo mode**.

## Commands

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements-dev.txt
ruff check .
pytest -q
python -m compileall morning_digest main.py
```

## What is covered

| Area | File |
|---|---|
| Keyword filters / dedupe / sort | `tests/test_filters.py` |
| HTML cleanup / keyword parsing | `tests/test_html_utils.py` |
| Config load/save/corrupt/restore | `tests/test_config.py` |
| Prompt build + demo collection | `tests/test_prompts_and_collector.py` |

## Manual GUI checklist

1. `python main.py`
2. Empty state visible in Coletor
3. **DEMO OFFLINE** produces digest without network
4. Copy prompt + export `.md`
5. Add invalid URL → error
6. Restore defaults
7. Save keywords; restart app; confirm persistence
8. **RASTREAR TUDO** with live feeds (network required)

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs Ruff + Pytest on Python 3.10 and 3.12. The GUI is **not** launched in CI.
