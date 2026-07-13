# Portfolio Handoff — MorningDigestMegaFeed

**Data:** 2026-07-13  
**Branch:** `chore/portfolio-quality-pass`  
**Recomendação final:** **laboratório (lab / legado desktop)** — não destaque; complementar a [NewsWeave](https://github.com/BarujaFe1/NewsWeave).

## Resumo

Passagem de evidência e posicionamento sobre a quality pass 1.1.0: screenshots reais, sample digest, demo script, claims corrigidos (sem “paralelo”, sem “app de IA”), README alinhado a tier lab, GitHub description/topics atualizados.

## Before / after (esta passagem)

| Item | Antes | Depois |
|---|---|---|
| Screenshots | Placeholder (`icon.png`) | 3 PNGs reais 1200×850 (demo fixtures) |
| Posicionamento vs NewsWeave | Implícito / risco de overlap | Explícito em docs + README |
| Claim “coleta em paralelo” | Presente no README | Corrigido → sequencial + isolamento |
| Sample digest | Ausente | `docs/samples/demo_digest.md` |
| Demo interview script | Ausente | `docs/DEMO_SCRIPT.md` |
| Testes | 20 | 23 (claims + screenshots) |
| Deploy web | N/A | Continua N/A (desktop); documentado |

## Achados priorizados (confirmação no código)

| ID | Achado | Prioridade | Ação |
|---|---|---|---|
| C1 | Claim falso de coleta paralela | P0 (claim) | Corrigido na docs/README |
| C2 | Linguagem “IA” sem chamada a LLM | P1 | Softened; handoff Markdown |
| C3 | Sobreposição com NewsWeave | P1 (portfólio) | Lab legado explícito |
| C4 | Sem screenshots reais | P2 | Capturados |
| C5 | Sem URL de deploy | P2 | Limitação honesta |
| C6 | GUI fora do CI | P3 | Aceito; domínio coberto |

## Arquivos principais alterados / adicionados

- `README.md`, `CHANGELOG.md`
- `docs/screenshots/*.png`, `MANIFEST.md`
- `docs/PORTFOLIO_POSITIONING.md`, `docs/DEMO_SCRIPT.md`, `docs/PORTFOLIO_HANDOFF.md`
- `docs/samples/demo_digest.md`
- `scripts/capture_screenshots.py`
- `tests/test_portfolio_claims.py`
- `morning_digest/app.py` (subtitle honesto)
- `requirements-dev.txt` (+Pillow)

## Comandos / gates

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q                 # 23 passed
python -m compileall morning_digest main.py
python scripts/capture_screenshots.py   # requer display
```

## Evidências

- Screenshots: `docs/screenshots/01-collector-empty.png`, `02-collector-demo.png`, `03-settings.png`
- Sample: `docs/samples/demo_digest.md`
- CI: `.github/workflows/ci.yml` (já existente; GUI não executada)
- Deploy público: **inexistente** (esperado para desktop)

## Limitações remanescentes

- Sem preview web / Vercel
- Feeds live frágeis (mitigado por DEMO OFFLINE)
- Empacotamento binário não automatizado
- Overlap temático residual com NewsWeave (mitigado por copy de posicionamento)

## Próximos passos

1. Merge PR `chore/portfolio-quality-pass` → `main`
2. No site de portfólio: card **Lab** apontando para este repo; case de notícias = NewsWeave
3. Opcional: GIF 20s do DEMO_SCRIPT

## Supermegaprompt (fora do repo)

`C:\dev\prompts_para_port\morningdigestmegafeed-supermegaprompt-portfolio.md`
