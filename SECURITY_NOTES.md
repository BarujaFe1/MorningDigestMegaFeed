# Security Notes

**Date:** 2026-07-13  
**Scope:** Portfolio quality pass on `MorningDigestMegaFeed`

## Findings

- **No API keys, tokens, or `.env` secrets** were present in tracked source files.
- The application does **not** call third-party LLM APIs; it only builds prompts locally.
- User configuration (`news_config.json`) and export files are **gitignored** to avoid committing personal feed lists or digests.
- Network requests use a dedicated User-Agent and per-request timeouts.

## Residual considerations

- RSS URLs in the default catalog are public publisher feeds; availability and ToS are controlled by each publisher.
- Clipboard contents may include article titles/links — treat digests as potentially sensitive if keywords reveal private interests.
- If packaging with PyInstaller, do not embed personal `news_config.json` into the binary.
