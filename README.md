<div align="center">
  <img src="./icon.png" alt="Morning Digest Logo" width="120" height="120" />

  <h1>Morning Digest // MEGA FEED</h1>
  <p><strong>De dezenas de feeds RSS a um prompt pronto para IA — em um clique.</strong></p>
  <p><em>From scattered RSS noise to an interview-ready, AI-ready news digest.</em></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-0EA5E9.svg" alt="CustomTkinter" />
    <img src="https://img.shields.io/badge/Tests-pytest-0F172A.svg" alt="pytest" />
    <img src="https://img.shields.io/badge/Lint-ruff-D7FF64.svg" alt="ruff" />
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
  </p>

  <p>
    <a href="https://github.com/BarujaFe1">GitHub</a> ·
    <a href="https://barujafe.vercel.app/">Portfólio</a> ·
    <a href="https://www.linkedin.com/in/barujafe/">LinkedIn</a>
  </p>
</div>

---

## Screenshot

> **Placeholder:** adicione capturas reais em `docs/screenshots/` e substitua o bloco abaixo.

```text
┌──────────────────────────────────────────────────────────────┐
│  MORNING DIGEST // MEGA FEED          Demo! 9 notícias       │
│  RSS → filtros → prompt pronto para IA                       │
├──────────────────────────────────────────────────────────────┤
│  [ Coletor ]  [ Configurações ]                              │
│  Template: [ Padrão ▼ ]                   35 feeds ativos    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ ☀️ BOM DIA!                                            │  │
│  │ ### 15 DESTAQUES / RADAR RÁPIDO                        │  │
│  │ (prompt estruturado para ChatGPT / Claude)             │  │
│  └────────────────────────────────────────────────────────┘  │
│  [ RASTREAR TUDO ] [ DEMO OFFLINE ] [ EXPORTAR ] [ COPIAR ]  │
└──────────────────────────────────────────────────────────────┘
```

![App screenshot placeholder](./icon.png)

---

## Problema real

Quem acompanha tech, mercado, esportes, política e notícias locais ao mesmo tempo não sofre com *falta* de informação — sofre com **dispersão**:

- feeds espalhados em abas;
- manchetes duplicadas entre portais;
- ruído temático;
- prompts montados manualmente toda manhã;
- nenhuma rotina repetível de curadoria.

## Solução

**Morning Digest** é um app desktop que:

1. coleta dezenas de RSS em paralelo (com timeout e isolamento de falhas);
2. limpa HTML dos resumos;
3. aplica filtros include/exclude;
4. remove duplicatas e ordena por data;
5. aplica um **template de prompt**;
6. entrega o resultado para **copiar** ou **exportar Markdown** — pronto para colar em uma IA.

Não chama APIs de LLM: o produto é o **pipeline de curadoria + handoff**, o que reduz custo, chave de API e atrito de privacidade.

---

## Principais funcionalidades

- **Coleta massiva de RSS** com catálogo padrão (30+ fontes) e feeds customizados
- **Templates de prompt** (Padrão, Tech/Games, Corinthians & Política, Crypto & Mercado, Estoico)
- **Filtros por palavra-chave** (incluir / excluir)
- **Deduplicação** e ordenação temporal
- **Persistência local** em `news_config.json`
- **DEMO OFFLINE** para entrevistas e CI mental (sem rede)
- **Exportar .md** + copiar para clipboard
- **Restaurar configuração padrão**
- **Validação de URL** ao adicionar feeds

---

## Arquitetura

```text
UI (CustomTkinter)
   ↓
Collector (urllib + feedparser | demo fixtures)
   ↓
Clean → Filter → Dedupe/Sort
   ↓
Prompt Template Engine
   ↓
Clipboard / Markdown export
```

Detalhes: [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md)

### Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.10+ |
| UI | CustomTkinter |
| RSS | feedparser + urllib |
| Clipboard | pyperclip |
| Config | JSON local |
| Qualidade | pytest, ruff, GitHub Actions |

---

## Demo local

```bash
git clone https://github.com/BarujaFe1/MorningDigestMegaFeed.git
cd MorningDigestMegaFeed
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

No app: clique **DEMO OFFLINE** para gerar um digest sem depender de feeds externos.

Dev / qualidade:

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q
```

---

## Variáveis de ambiente

Nenhuma chave é obrigatória. Veja [`.env.example`](./.env.example) para opções futuras documentadas.  
Estado do usuário: `news_config.json` (gitignored).

Exemplo de config gerada:

```json
{
  "feeds": ["https://g1.globo.com/rss/g1/"],
  "prompt_template": "Padrão",
  "keywords_include": ["python", "IA"],
  "keywords_exclude": ["BBB"]
}
```

---

## Testes

```bash
pytest -q
```

Cobertura focada em filtros, limpeza HTML, config resiliente, prompts e coleta demo.  
Guia: [`docs/TESTING.md`](./docs/TESTING.md)

---

## Decisões técnicas e trade-offs

| Decisão | Trade-off |
|---|---|
| Desktop em vez de web | Zero hosting; sem URL pública de demo |
| Sem chamada a LLM | Privacidade/custo ↑; “resumo mágico” fica no ChatGPT |
| JSON local | Simples; sem sync multi-dispositivo |
| Demo fixtures | Demo estável; conteúdo ilustrativo |

Mais em [`docs/TECHNICAL_DECISIONS.md`](./docs/TECHNICAL_DECISIONS.md).

---

## Roadmap

- [ ] Health-check visual por feed  
- [ ] Enable/disable por fonte  
- [ ] Editor de templates persistente  
- [ ] Agendamento diário  
- [ ] Build PyInstaller one-click  
- [ ] Preview / abrir link no navegador  

## Status atual

**Ativo / portfolio-ready (v1.1).** Pipeline testado, CI configurada, demo offline disponível. Empacotamento binário ainda é opcional (ver [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md)).

---

## O que este projeto demonstra

- Modelagem de um **pipeline de dados** (ingest → transform → deliver) em Python  
- Separação **UI × domínio** com testes unitários  
- Tratamento de falhas de rede e config corrompida  
- UX de produto: empty state, loading, demo, export  
- Documentação e CI pensadas para avaliação técnica  
- Sensibilidade a **privacidade** (sem API keys; config local gitignored)

## Como eu apresentaria em entrevista

1. **Problema (30s):** “Eu perdia tempo montando briefing matinal a partir de 30 abas.”  
2. **Solução (30s):** “App local que transforma RSS em prompt estruturado para IA.”  
3. **Arquitetura (60s):** Desenhar o fluxo collector → filters → prompt; mostrar `morning_digest/`.  
4. **Demo (60s):** Abrir o app → **DEMO OFFLINE** → copiar prompt.  
5. **Engenharia (60s):** Thread-safety no Tk, isolamento por feed, testes sem GUI, CI.  
6. **Próximo passo (20s):** “Empacotar executável e health-check de feeds.”

---

## Docs

- [Audit Report](./docs/AUDIT_REPORT.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Technical Decisions](./docs/TECHNICAL_DECISIONS.md)
- [Testing](./docs/TESTING.md)
- [Deployment](./docs/DEPLOYMENT.md)
- [Handoff](./docs/HANDOFF.md)

## Autor

**Felipe Alirio Baruja (BarujaFe1)**  
[Portfólio](https://barujafe.vercel.app/) · [GitHub](https://github.com/BarujaFe1) · [LinkedIn](https://www.linkedin.com/in/barujafe/)

## License

MIT — ver [LICENSE](./LICENSE).
