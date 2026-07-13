# Deployment / Distribution

This is a **local desktop app**, not a web service. “Deploy” means making it runnable for demos and packaging for end users.

## Local run (primary)

```bash
git clone https://github.com/BarujaFe1/MorningDigestMegaFeed.git
cd MorningDigestMegaFeed
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Offline portfolio demo: click **DEMO OFFLINE** inside the app.

## Optional packaging (PyInstaller)

Not committed as a binary (keeps the repo lean). Suggested one-file build:

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --name MorningDigestMegaFeed \
  --add-data "icon.png;." \
  main.py
```

On macOS/Linux, replace `;` with `:` in `--add-data`.

Deliverable appears under `dist/`. Do **not** commit `dist/` or `.spec` artifacts with secrets.

## Environment

No API keys are required. See `.env.example` for optional future knobs. Local state lives in `news_config.json` (gitignored).

## Screenshots for portfolio

Place captures under `docs/screenshots/` (gitignored patterns optional) or update the README placeholder:

- Collector with generated prompt  
- Settings with feeds + keywords  
- Demo offline result  

Suggested filenames:

- `docs/screenshots/collector.png`
- `docs/screenshots/settings.png`
