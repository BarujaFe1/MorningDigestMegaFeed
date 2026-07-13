# Portfolio positioning — Morning Digest vs NewsWeave

## Recommendation: **laboratório (lab / legado desktop)**

| Projeto | Papel no portfólio | Superfície | Quando citar |
|---|---|---|---|
| **NewsWeave** | Selecionado / produto web de curadoria | FastAPI + Next.js | Vagas full-stack analítico, produto de dados, ranking |
| **MorningDigestMegaFeed** | Laboratório / predecessor desktop | Python + CustomTkinter | Entrevistas sobre ETL local, DX desktop, prompts sem API |

## Por que não competir como “destaque”

1. **Sobreposição temática** com NewsWeave (RSS → curadoria → briefing).
2. **Sem deploy web** — demo exige máquina local (mitigado por DEMO OFFLINE + screenshots).
3. **Tier C** — útil como evidência de engenharia, não como case principal de dados.

## Como apresentar sem canibalizar NewsWeave

- Morning Digest = **pipeline local** (ingest → clean → filter → dedupe → prompt Markdown).
- NewsWeave = **produto web** com ranking/rules e briefing diário.
- Frase canônica: *“Morning Digest foi o lab desktop que validou o fluxo; NewsWeave é a evolução web.”*

## Claims permitidos

- Agregador RSS desktop com filtros e templates de prompt.
- Gera texto Markdown para colar em ferramentas externas de linguagem.
- Demo offline estável; testes e CI no domínio (sem GUI no CI).
- Separação UI × domínio após refatoração.

## Claims proibidos

- “Produto enterprise / produção em escala”.
- “App de IA” ou “usa LLM” (não chama APIs de modelo).
- “Coleta em paralelo” (a coleta é **sequencial** com isolamento por feed).
- “Substituto do NewsWeave” ou “melhor que o NewsWeave”.
