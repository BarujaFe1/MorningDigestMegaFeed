# Architecture

## Overview

Morning Digest is a **desktop ETL-lite pipeline** for news:

```text
RSS feeds → fetch/parse → clean → filter → dedupe/sort → prompt template → clipboard/export
```

The UI (CustomTkinter) is a thin control surface over domain modules. Network and prompt logic can be exercised without opening the window (see tests + demo mode).

## Package layout

```text
MorningDigestMegaFeed/
├── main.py                      # Entry point
├── morning_digest/
│   ├── app.py                   # CustomTkinter UI
│   ├── collector.py             # RSS fetch + orchestration
│   ├── config.py                # JSON persistence
│   ├── demo_data.py             # Offline sample entries
│   ├── feeds.py                 # Default / suggested catalogs
│   ├── filters.py               # Include/exclude + dedupe
│   ├── html_utils.py            # Summary cleanup
│   ├── prompts.py               # Templates + prompt assembly
│   └── theme.py                 # Visual tokens
├── tests/                       # Unit tests (no GUI required)
├── docs/                        # Architecture, audit, handoff
└── .github/workflows/ci.yml
```

## Layers

| Layer | Responsibility | Module(s) |
|---|---|---|
| UI | Tabs, buttons, status, clipboard, file dialogs | `app.py` |
| Application | Threaded collect → build prompt → present | `app.py` + `collector.py` |
| Domain | Filters, templates, cleaning, config merge | `filters`, `prompts`, `html_utils`, `config` |
| Adapters | HTTP RSS fetch, feedparser, demo fixtures | `collector`, `demo_data` |

## Data model

`NewsItem` (TypedDict):

- `src` — source domain label  
- `title` — headline  
- `desc` — cleaned summary (truncated)  
- `link` — article URL  
- `date` — `datetime` for sorting  

Config (`news_config.json`, local-only):

- `feeds: string[]`
- `prompt_template: string`
- `keywords_include: string[]`
- `keywords_exclude: string[]`

## Concurrency

Collection runs on a **daemon thread**. All UI mutations go through `widget.after(0, ...)` / `set_status` to keep Tk thread-safe.

## Failure isolation

Each feed is isolated: one timeout/parse failure increments `errors` and continues. The UI reports `N notícias · M feed(s) com falha`.

## Why not a web app?

The original product intent is a **local morning ritual** with clipboard handoff to ChatGPT/Claude. CustomTkinter keeps the stack small (no backend/auth/hosting). Trade-off: no public URL demo — mitigated by **DEMO OFFLINE** and screenshots.
