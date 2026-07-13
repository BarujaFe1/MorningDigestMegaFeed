<div align="center">
  <img src="./icon.png" alt="Morning Digest Logo" width="120" height="120" />

  <h1>Morning Digest // MEGA FEED</h1>
  <p><strong>Lab desktop local-first:</strong> RSS → limpeza → filtros → dedupe → prompt Markdown para handoff.</p>
  <p><em>Predecessor de laboratório do produto web <a href="https://github.com/BarujaFe1/NewsWeave">NewsWeave</a> — não compete como case principal.</em></p>

  <p>
    <img src="https://img.shields.io/badge/Role-Lab%20desktop-64748B.svg" alt="Lab desktop" />
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-0EA5E9.svg" alt="CustomTkinter" />
    <img src="https://img.shields.io/badge/Tests-pytest-0F172A.svg" alt="pytest" />
    <img src="https://img.shields.io/badge/CI-GitHub%20Actions-2088FF.svg" alt="CI" />
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
  </p>

  <p>
    <a href="https://github.com/BarujaFe1">GitHub</a> ·
    <a href="https://barujafe.vercel.app/">Portfólio</a> ·
    <a href="https://www.linkedin.com/in/barujafe/">LinkedIn</a> ·
    <a href="./docs/PORTFOLIO_POSITIONING.md">Posicionamento</a>
  </p>
</div>

---

## Screenshots (reais, demo fixtures, sem PII)

| Empty / onboarding | DEMO OFFLINE | Configurações |
|---|---|---|
| ![empty](./docs/screenshots/01-collector-empty.png) | ![demo](./docs/screenshots/02-collector-demo.png) | ![settings](./docs/screenshots/03-settings.png) |

Regenerar: `python scripts/capture_screenshots.py` (requer display + Pillow).

---

## Problema e público

**Público:** quem monta briefing matinal a partir de muitas fontes (estudantes, creators, analistas).

**Problema:** informação demais, organização de menos — feeds em abas, duplicatas, ruído temático e prompts montados à mão.

## Solução e fluxo

App **desktop** Python que executa um mini-pipeline:

```text
Feeds RSS (ou fixtures DEMO)
  → fetch sequencial com timeout / isolamento de falha
  → limpeza HTML
  → filtros include/exclude
  → dedupe por título + ordenação por data
  → template de prompt
  → clipboard ou export .md
```

**Não** chama APIs de modelo de linguagem. A saída é texto estruturado para colar em uma ferramenta externa.

Amostra gerada pelo mesmo pipeline: [`docs/samples/demo_digest.md`](./docs/samples/demo_digest.md).

---

## O que este projeto demonstra

- Pipeline de dados local (ingest → transform → deliver)
- Separação UI × domínio testável
- Resiliência: config JSON inválida, falha por feed, empty state
- DX de demonstração: **DEMO OFFLINE** + screenshots reproduzíveis
- Honestidade de escopo: lab desktop, não “plataforma de produção”

## Arquitetura

Pacote `morning_digest/`: `collector`, `filters`, `prompts`, `config`, `app` (CustomTkinter).  
Detalhes: [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md).

### Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.10+ |
| UI | CustomTkinter |
| RSS | urllib + feedparser |
| Clipboard | pyperclip |
| Config | JSON local (`news_config.json`, gitignored) |
| Qualidade | pytest, ruff, GitHub Actions |

---

## Relação com NewsWeave

| | Morning Digest | NewsWeave |
|---|---|---|
| Papel | **Laboratório / legado desktop** | **Selecionado (web)** |
| Stack | CustomTkinter | FastAPI + Next.js |
| Entrega | Prompt Markdown local | Briefing / ranking web |

Ver [`docs/PORTFOLIO_POSITIONING.md`](./docs/PORTFOLIO_POSITIONING.md).

---

## Estado real, demo e limitações

| Item | Status |
|---|---|
| Instala e roda localmente | Sim (`python main.py`) |
| Demo sem rede | Sim (**DEMO OFFLINE**) |
| Testes de domínio + CI | Sim (GUI não sobe no CI) |
| Deploy web / URL pública | **Não** — app desktop |
| Binário empacotado | Opcional (docs), não é release automatizado |
| Coleta paralela | **Não** — sequencial com isolamento |

## Quick start

```bash
git clone https://github.com/BarujaFe1/MorningDigestMegaFeed.git
cd MorningDigestMegaFeed
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Depois: **DEMO OFFLINE** → revisar digest → **COPIAR PROMPT** ou **EXPORTAR .MD**.

## Variáveis de ambiente

Nenhuma chave obrigatória. Ver [`.env.example`](./.env.example).

## Testes / gates

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q
python -m compileall morning_digest main.py
```

Roteiro de entrevista (3–5 min): [`docs/DEMO_SCRIPT.md`](./docs/DEMO_SCRIPT.md).

## Decisões e trade-offs

- Desktop local → zero hosting; sem demo URL
- Sem chamada a LLM → privacidade/custo; handoff manual
- JSON local → simples; sem sync multi-dispositivo
- Fixtures demo → entrevista estável; não é notícia ao vivo

Mais: [`docs/TECHNICAL_DECISIONS.md`](./docs/TECHNICAL_DECISIONS.md).

## Roadmap (lab)

- Health-check visual por feed
- Toggle enable/disable por fonte
- Empacotamento PyInstaller opcional

Não planejado neste repo: substituir o NewsWeave.

---

## Roteiro de entrevista (resumo)

1. Problema de dispersão de feeds (30s)  
2. Demo Offline → mostrar Markdown (60s)  
3. Mostrar `collector` / `filters` / testes (60s)  
4. Trade-off desktop vs NewsWeave web (30s)  

## Docs

- [PORTFOLIO_HANDOFF](./docs/PORTFOLIO_HANDOFF.md) · [AUDIT](./docs/AUDIT_REPORT.md) · [HANDOFF](./docs/HANDOFF.md)
- [ARCHITECTURE](./docs/ARCHITECTURE.md) · [TESTING](./docs/TESTING.md) · [DEPLOYMENT](./docs/DEPLOYMENT.md)
- [CHANGELOG](./CHANGELOG.md)

## Autor

**Felipe Alírio Baruja** — desenvolvedor de software; estudante de Estatística/Ciência de Dados (USP).  
[Portfólio](https://barujafe.vercel.app/) · [GitHub](https://github.com/BarujaFe1) · [LinkedIn](https://www.linkedin.com/in/barujafe/)

## License

MIT — [LICENSE](./LICENSE).
