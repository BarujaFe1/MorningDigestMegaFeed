# Changelog

## 1.1.1 — 2026-07-13 (portfolio evidence pass)

### Added
- Real GUI screenshots under `docs/screenshots/` (demo fixtures, no PII)
- `scripts/capture_screenshots.py` to regenerate captures
- `docs/PORTFOLIO_POSITIONING.md` (lab vs NewsWeave)
- `docs/DEMO_SCRIPT.md` (3–5 min interview demo)
- `docs/PORTFOLIO_HANDOFF.md`
- Sample digest artifact `docs/samples/demo_digest.md`

### Fixed / clarified
- README claim of “coleta em paralelo” corrected to sequential fetch with per-feed isolation
- Portfolio copy softened: prompt handoff ≠ “app de IA”
- GitHub description/topics aligned with lab desktop role

### Quality
- Baseline re-verified: ruff + pytest (20) + compileall

## 1.1.0 — 2026-07-13 (portfolio quality pass)

- Domain package `morning_digest/`
- DEMO OFFLINE, Markdown export, restore defaults
- pytest + ruff + GitHub Actions
- Docs: architecture, testing, deployment, audit, handoff
