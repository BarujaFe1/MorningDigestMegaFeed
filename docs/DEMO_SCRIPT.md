# Demo guiada (3–5 minutos)

Roteiro para entrevista ou gravação de tela. Use **DEMO OFFLINE** para estabilidade.

## Setup (30s)

```bash
git clone https://github.com/BarujaFe1/MorningDigestMegaFeed.git
cd MorningDigestMegaFeed
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Minuto a minuto

| Tempo | Ação | O que dizer |
|---|---|---|
| 0:00–0:40 | Mostrar empty state no Coletor | “Problema: briefing matinal disperso em dezenas de abas.” |
| 0:40–1:20 | Clicar **DEMO OFFLINE** | “Pipeline: ingest → limpeza HTML → filtros → dedupe → template de prompt.” |
| 1:20–2:20 | Rolar o digest | “Saída é Markdown estruturado para colar numa ferramenta de linguagem — sem API key neste app.” |
| 2:20–3:10 | Aba Configurações | “Feeds persistidos em JSON local; include/exclude; restaurar padrão.” |
| 3:10–3:50 | **EXPORTAR .MD** ou **COPIAR PROMPT** | “Handoff para o fluxo de escrita; privacidade local-first.” |
| 3:50–4:30 | Abrir `morning_digest/` + `tests/` | “Domínio testável separado da UI; CI com ruff + pytest.” |
| 4:30–5:00 | Posicionar vs NewsWeave | “Lab desktop predecessor; NewsWeave é a linha web selecionada.” |

## Checklist anti-surpresa

- [ ] Rede pode falhar → preferir DEMO OFFLINE  
- [ ] Não abrir `news_config.json` pessoal na tela  
- [ ] Não afirmar chamada a LLM  
- [ ] Não afirmar coleta paralela  
