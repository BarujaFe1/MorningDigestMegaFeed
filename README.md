<div align="center">
  <img src="./icon.png" alt="Morning Digest // MEGA FEED Logo" width="120" height="120" />

  <h1>Morning Digest // MEGA FEED</h1>

  <p><strong>Desktop lab (CustomTkinter): RSS → filtro → dedupe → prompt Markdown para IA.</strong></p>
  <p><strong>Desktop lab (CustomTkinter): RSS → filter → dedupe → Markdown prompt handoff for AI.</strong></p>

  <p>
    <a href="#pt-br">PT-BR</a>
     · 
    <a href="#english">English</a>
     · 
    <a href="#stack">Stack</a>
     · 
    <a href="#architecture">Architecture</a>
     · 
    <a href="#quick-start">Quick Start</a>
     · 
    <a href="#author">Author</a>
  </p>

  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="CustomTkinter" src="https://img.shields.io/badge/CustomTkinter-1F2937?style=for-the-badge" />
    <img alt="Status-Lab%20desktop" src="https://img.shields.io/badge/Status-Lab%20desktop-22C55E?style=for-the-badge" />
    <img alt="License-MIT" src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  </p>

  <p>
    <a href="https://github.com/BarujaFe1/MorningDigestMegaFeed"><strong>Repo</strong></a>
     · 
    <a href="https://barujafe.vercel.app/"><strong>Portfolio</strong></a>
     · 
    <a href="https://www.linkedin.com/in/barujafe/"><strong>LinkedIn</strong></a>
  </p>
</div>


> **Lab caveat:** this is a **desktop** CustomTkinter app — **not** a Vercel web deploy. GitHub homepage currently points at the portfolio site; there is no product web demo. Successor/web product direction: **NewsWeave**.

---

## PT-BR

### Visão geral
O **Morning Digest // MEGA FEED** agrega dezenas de feeds RSS, filtra por palavras-chave, organiza itens e gera texto/prompt Markdown pronto para colar em uma IA — tudo em app desktop Python.

### Problema
Começar o dia com 30 abas de notícia sem filtro gera ruído; falta um coletor local simples que prepare um prompt de curadoria.

### Para quem
Usuários power que querem um **coletor RSS local** e handoff rápido para LLMs (sem produto web).

### Funcionalidades
- Coleta massiva de RSS (`feedparser`)
- Filtros por palavra-chave
- Organização / dedupe no fluxo do app
- Templates de prompt e cópia para clipboard (`pyperclip`)
- Config persistente em JSON (`news_config.json`)
- Tema visual “Midnight” em CustomTkinter

### Escopo e limites (honestos)
- Desktop-only — **sem** demo web do produto
- Não hospeda nem republica conteúdo — apenas agrega feeds
- Predecessor de laboratório em relação ao **NewsWeave**

---

## English

### Overview
**Morning Digest // MEGA FEED** aggregates many RSS feeds, keyword-filters, organizes items and builds Markdown prompts ready to paste into an AI — as a Python desktop app.

### Problem
Starting the day with 30 news tabs is noise; a simple local collector that prepares a curation prompt is missing.

### Who it is for
Power users who want a **local RSS collector** and fast LLM handoff (no web product).

### Features
- Massive RSS collection (`feedparser`)
- Keyword filters
- Organization / dedupe in the app flow
- Prompt templates + clipboard copy (`pyperclip`)
- Persistent JSON config (`news_config.json`)
- Midnight-themed CustomTkinter UI

### Scope and honest limits
- Desktop-only — **no** product web demo
- Does not host/republish content — aggregates feeds
- Lab predecessor relative to **NewsWeave**

---

## Stack

| Layer | Technology |
|---|---|
| UI | CustomTkinter |
| Ingest | feedparser, urllib |
| Utils | pyperclip, JSON config |

---

## Architecture

Single-module desktop app: `main.py` (UI + collector + config). Flow: feeds → filter/dedupe → Markdown prompt → clipboard.

---

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

---

## Technical decisions

- **Desktop GUI** for fast local iteration before a web stack
- **Prompt handoff** instead of building a full news reader product here
- Keep configuration in JSON for easy edits

---

## Roadmap

- Share more filter presets
- Export history improvements
- Point users to NewsWeave for the web briefing experience

---

## Author

**Felipe Alirio Baruja** — data / product / full-stack portfolio.

- Portfolio: [https://barujafe.vercel.app/](https://barujafe.vercel.app/)
- GitHub: [https://github.com/BarujaFe1](https://github.com/BarujaFe1)
- LinkedIn: [https://www.linkedin.com/in/barujafe/](https://www.linkedin.com/in/barujafe/)


## License

MIT — see [`LICENSE`](./LICENSE).
