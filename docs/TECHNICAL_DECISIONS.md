# Technical Decisions

## 1. CustomTkinter over web UI

**Decision:** Keep a desktop GUI.  
**Why:** Matches the original product, zero hosting cost, fast local loop for clipboard workflows.  
**Trade-off:** Harder to share a live demo URL; mitigated with offline demo + packaging docs.

## 2. Domain package vs single `main.py`

**Decision:** Split into `morning_digest/*` with a thin `main.py`.  
**Why:** Recruiters and CI need testable units without spawning a GUI.  
**Trade-off:** Slightly more files; clearer ownership.

## 3. feedparser + explicit urllib fetch

**Decision:** Prefer fetching bytes with `urllib` (timeout + User-Agent), then `feedparser.parse(payload)`.  
**Why:** Avoids mutating global `socket.setdefaulttimeout` and improves failure diagnostics.  
**Trade-off:** Some exotic feeds may still need the feedparser fallback path (kept).

## 4. JSON config, no database

**Decision:** Persist settings in `news_config.json`.  
**Why:** Zero ops, portable, enough for feed lists and keywords.  
**Trade-off:** No multi-profile sync; acceptable for v1.

## 5. No API keys required

**Decision:** The app generates prompts for *external* AIs; it does not call LLM APIs.  
**Why:** Privacy, cost, and simplicity for portfolio demos.  
**Trade-off:** No one-click “summarize inside the app” yet (roadmap).

## 6. Demo fixtures instead of recorded HTTP cassettes

**Decision:** Ship `demo_data.py` with synthetic entries.  
**Why:** Stable tests and interview demos without flaky third-party RSS.  
**Trade-off:** Demo content is illustrative, not live news.

## 7. Ruff + Pytest, skip mypy initially

**Decision:** CI runs Ruff + Pytest + compileall.  
**Why:** High signal, low friction on a small typed-but-not-strict codebase.  
**Trade-off:** Gradual typing can be tightened later with mypy.

## 8. Neutral feed catalog copy

**Decision:** Remove editorial/political commentary from feed comments and suggestion labels.  
**Why:** Portfolio repos are public professional artifacts.
