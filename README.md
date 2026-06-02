<div align="center">
  <img src="./icon.png" alt="Morning Digest Logo" width="120" height="120" />

  <h1>Morning Digest // MEGA FEED</h1>

  <p><strong>Agregador RSS inteligente para curadoria de notícias e geração de prompts prontos para IA</strong></p>
  <p><strong>Smart RSS aggregator for news curation and AI-ready prompt generation</strong></p>

  <p>
    <a href="#pt-br">PT-BR</a> •
    <a href="#en">English</a> •
    <a href="#stack--tecnologias">Stack</a> •
    <a href="#quick-start--início-rápido">Quick Start</a> •
    <a href="#configuração--configuration">Configuração</a> •
    <a href="#autor--author">Autor</a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-FF69B4.svg" alt="CustomTkinter" />
    <img src="https://img.shields.io/badge/RSS-feedparser-F97316.svg" alt="feedparser" />
    <img src="https://img.shields.io/badge/Clipboard-pyperclip-8B5CF6.svg" alt="pyperclip" />
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
  </p>

  <p>
    <a href="https://github.com/BarujaFe1"><strong>🐙 GitHub</strong></a> •
    <a href="https://barujafe.vercel.app/"><strong>🌐 Portfólio</strong></a> •
    <a href="https://www.linkedin.com/in/barujafe/"><strong>💼 LinkedIn</strong></a>
  </p>
</div>

---

<a id="pt-br"></a>

## 🇧🇷 PT-BR

## ☀️ Visão geral

**Morning Digest // MEGA FEED** é um aplicativo desktop para coleta, filtragem e curadoria de notícias via RSS, com geração automática de prompts prontos para uso em IAs como ChatGPT, Claude e outras ferramentas de escrita/análise.

O sistema reúne feeds de diferentes categorias, remove duplicatas, aplica filtros por palavras-chave, organiza as notícias por relevância temporal e gera um prompt estruturado para transformar o volume bruto de notícias em um resumo acionável.

A proposta é simples: em vez de abrir dezenas de sites, copiar links manualmente e montar prompts do zero, o usuário centraliza tudo em uma interface visual, escolhe um estilo de saída e copia o prompt final em um clique.

> **Objetivo:** transformar coleta manual de notícias em um fluxo rápido, personalizável e pronto para IA.

---

## 🎯 Problema que resolve

Quem acompanha muitos assuntos ao mesmo tempo — tecnologia, mercado, política, esportes, cripto, games ou notícias locais — lida diariamente com excesso de fontes e baixa organização.

O problema não é falta de informação. O problema é transformar esse volume em algo útil:

- feeds espalhados;
- notícias repetidas;
- temas irrelevantes;
- excesso de abas abertas;
- prompts montados manualmente;
- dificuldade para manter uma rotina diária de curadoria;
- pouco controle sobre o que entra e o que sai do resumo.

O **Morning Digest** resolve esse atrito centralizando a coleta, aplicando filtros e entregando uma base organizada para geração de newsletters, resumos diários e análises assistidas por IA.

---

## ✨ Funcionalidades principais

### 📰 Coleta massiva de RSS

- Mais de 30 feeds pré-configurados.
- Suporte a categorias como:
  - esportes;
  - política;
  - economia;
  - tecnologia;
  - internacional;
  - mercado;
  - notícias locais.
- Possibilidade de adicionar feeds personalizados.
- Restauração dos feeds padrão.

### 🧠 Templates de prompt

O app permite escolher entre diferentes estilos de prompt, como:

- **Padrão:** resumo geral equilibrado.
- **Tech/Games:** foco em tecnologia, games e cultura digital.
- **Corinthians & Política:** combinação de esportes e política.
- **Crypto/Mercado:** foco em mercado financeiro e cripto.
- **Estoico/Resumido:** saída curta, objetiva e reflexiva.

Cada template muda o estilo de instrução enviado para a IA, mantendo a coleta estruturada.

### 🔎 Filtros por palavra-chave

- Termos de inclusão.
- Termos de exclusão.
- Filtros separados por vírgula.
- Útil para focar em temas específicos ou remover ruído.
- Exemplos:
  - incluir: `GTA VI, Corinthians, Bitcoin`
  - excluir: `BBB, novela, fofoca`

### 🧹 Organização automática

- Ordenação por data.
- Remoção de duplicatas.
- Priorização de notícias recentes.
- Consolidação de múltiplas fontes em um único prompt.
- Separação clara entre coleta e configuração.

### 📋 Copiar para área de transferência

- Botão para copiar o prompt gerado.
- Fluxo direto para colar em ChatGPT, Claude, Notion, editor de newsletter ou outro ambiente.
- Menos retrabalho ao montar resumos e newsletters.

### ⚙️ Configurações persistentes

- Feeds ativos.
- Template de prompt escolhido.
- Palavras-chave de inclusão.
- Palavras-chave de exclusão.
- Tudo salvo em `news_config.json`.

---

## 🧩 Casos de uso

- Criar briefing diário de notícias.
- Montar newsletter personalizada.
- Preparar pauta para canal, blog ou rede social.
- Gerar resumo de mercado.
- Acompanhar Corinthians, política, cripto, tecnologia ou temas locais.
- Criar prompts longos e estruturados para análise com IA.
- Ter uma rotina matinal de leitura sem abrir dezenas de fontes.

---

<a id="en"></a>

## 🇺🇸 English

## ☀️ Overview

**Morning Digest // MEGA FEED** is a desktop application for collecting, filtering and curating news through RSS feeds, with automatic generation of prompts ready to use in AI tools such as ChatGPT, Claude and other writing or analysis assistants.

The system gathers feeds from different categories, removes duplicates, applies keyword filters, organizes news by recency and generates a structured prompt to transform raw news volume into an actionable summary.

The idea is simple: instead of opening dozens of websites, manually copying links and writing prompts from scratch, the user centralizes everything in a visual interface, selects an output style and copies the final prompt with one click.

> **Goal:** turn manual news collection into a fast, customizable and AI-ready workflow.

---

## 🎯 Problem solved

Anyone who follows many subjects at once — technology, markets, politics, sports, crypto, games or local news — deals daily with too many sources and too little organization.

The problem is not lack of information. The problem is turning that volume into something useful:

- scattered feeds;
- repeated news;
- irrelevant topics;
- too many open tabs;
- manually assembled prompts;
- difficulty maintaining a daily curation routine;
- little control over what enters and leaves the summary.

**Morning Digest** solves this friction by centralizing collection, applying filters and delivering an organized base for newsletters, daily summaries and AI-assisted analysis.

---

## ✨ Key features

### 📰 Massive RSS collection

- 30+ preconfigured feeds.
- Support for categories such as:
  - sports;
  - politics;
  - economy;
  - technology;
  - international;
  - markets;
  - local news.
- Add custom feeds.
- Restore default feeds.

### 🧠 Prompt templates

The app provides different prompt styles, such as:

- **Default:** balanced general summary.
- **Tech/Games:** focus on technology, games and digital culture.
- **Corinthians & Politics:** mix of sports and politics.
- **Crypto/Market:** focus on financial markets and crypto.
- **Stoic/Short:** short, objective and reflective output.

Each template changes the instruction style sent to the AI while keeping the collected data structured.

### 🔎 Keyword filters

- Include terms.
- Exclude terms.
- Comma-separated filters.
- Useful to focus on specific topics or remove noise.
- Examples:
  - include: `GTA VI, Corinthians, Bitcoin`
  - exclude: `reality show, gossip`

### 🧹 Automatic organization

- Sort by date.
- Duplicate removal.
- Recent news prioritization.
- Consolidation of multiple sources into one prompt.
- Clear separation between collection and settings.

### 📋 Copy to clipboard

- Button to copy the generated prompt.
- Direct workflow to paste into ChatGPT, Claude, Notion, newsletter editor or another environment.
- Less rework when creating summaries and newsletters.

### ⚙️ Persistent settings

- Active feeds.
- Selected prompt template.
- Include keywords.
- Exclude keywords.
- Everything saved in `news_config.json`.

---

## 🧩 Use cases

- Create a daily news briefing.
- Build a personalized newsletter.
- Prepare topics for a channel, blog or social media.
- Generate a market summary.
- Track sports, politics, crypto, technology or local topics.
- Create long, structured prompts for AI analysis.
- Maintain a morning reading routine without opening dozens of sources.

---

<a id="stack--tecnologias"></a>

## 🛠️ Stack / Tecnologias

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| GUI | CustomTkinter |
| RSS parsing | feedparser |
| Clipboard | pyperclip |
| Config | Local JSON file |
| Interface style | Dark desktop UI |

---

## 🏗️ Arquitetura / Architecture

```txt
User Action
   ↓
CustomTkinter UI
   ↓
Feed Manager
   ↓
RSS Collector
   ↓
Keyword Filter
   ↓
Deduplication + Sorting
   ↓
Prompt Template Engine
   ↓
Generated Prompt
   ↓
Clipboard
```

### Fluxo principal / Main flow

```txt
Feeds RSS
  ↓
Coleta
  ↓
Parse
  ↓
Filtro por palavras-chave
  ↓
Remoção de duplicatas
  ↓
Ordenação por data
  ↓
Aplicação de template
  ↓
Prompt final para IA
```

---

## 📁 Estrutura do projeto / Project structure

```txt
Morning-Digest-Mega-Feed/
├── main.py                  # Main application
├── news_config.json         # Auto-generated local settings
├── requirements.txt         # Python dependencies
├── README.md
├── LICENSE
└── .gitignore
```

Suggested `requirements.txt`:

```txt
customtkinter
feedparser
pyperclip
```

---

<a id="quick-start--início-rápido"></a>

## 🚀 Quick Start / Início rápido

### Requirements / Pré-requisitos

- Python 3.10+
- Internet connection to access RSS feeds

### Installation / Instalação

```bash
git clone https://github.com/BarujaFe1/Morning-Digest-Mega-Feed.git
cd Morning-Digest-Mega-Feed
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If the repository does not include `requirements.txt`, install manually:

```bash
pip install customtkinter feedparser pyperclip
```

Run the app:

```bash
python main.py
```

> On first execution, `news_config.json` will be created automatically with the default feed list.

---

## 🎮 Como usar / How to use

### Coletor / Collector

1. Choose one of the prompt templates.
2. Click **Rastrear Tudo / Track Everything**.
3. Wait for the active feeds to be read.
4. Review the generated prompt.
5. Click **Copiar Prompt / Copy Prompt**.
6. Paste it into your preferred AI tool.

### Configurações / Settings

1. Manage active RSS feeds.
2. Add custom feed URLs.
3. Remove selected feeds.
4. Restore default categories.
5. Define include keywords.
6. Define exclude keywords.
7. Save settings.

---

<a id="configuração--configuration"></a>

## ⚙️ Configuração / Configuration

The app creates `news_config.json` automatically.

Example:

```json
{
  "feeds": [
    "https://ge.globo.com/futebol/times/corinthians/rss/",
    "https://g1.globo.com/rss/g1/"
  ],
  "prompt_template": "Padrão",
  "keywords_include": ["corinthians", "gta"],
  "keywords_exclude": ["fofoca", "bbb"]
}
```

| Key | Description |
|---|---|
| `feeds` | List of active RSS feed URLs |
| `prompt_template` | Active prompt template name |
| `keywords_include` | Terms that news should include; empty means no include filter |
| `keywords_exclude` | Terms that news should not include |

---

## 🧪 Quality and testing / Qualidade e testes

Recommended checks:

```bash
python -m compileall .
pip check
```

Suggested manual test checklist:

- Open the application.
- Confirm default feeds are loaded.
- Add a custom RSS feed.
- Remove a selected feed.
- Save and reload settings.
- Add include and exclude keywords.
- Run the collector.
- Copy the generated prompt.
- Paste it into an AI tool.

---

## 🛡️ Notes about sources / Observações sobre fontes

Morning Digest reads RSS feeds made available by their publishers. Availability, structure, timestamps and titles may vary by source.

Recommended practices:

- Prefer official RSS feeds.
- Avoid adding unreliable or spammy sources.
- Review generated prompts before publishing summaries.
- Cite sources when producing public newsletters or articles.
- Respect each publisher's terms of use.

---

## 🗺️ Roadmap

- Add feed health check.
- Add per-feed enable/disable toggle.
- Add categories and tags.
- Add article preview panel.
- Add export to Markdown.
- Add export to `.txt`.
- Add scheduled daily digest.
- Add source reliability score.
- Add prompt template editor.
- Add packaged executable build.

---

## 🤝 Contributing / Contribuição

Contributions are welcome.

```bash
git checkout -b feature/new-feature
git commit -m "feat: describe your change"
git push origin feature/new-feature
```

Then open a Pull Request.

Please keep the project aligned with clean RSS curation, source respect and transparent prompt generation.

---

<a id="autor--author"></a>

## 👤 Autor / Author

Developed by **BarujaFe1**.

- **Portfolio:** [https://barujafe.vercel.app/](https://barujafe.vercel.app/)
- **GitHub:** [github.com/BarujaFe1](https://github.com/BarujaFe1)
- **LinkedIn:** [linkedin.com/in/barujafe](https://www.linkedin.com/in/barujafe/)

---

## 📄 License / Licença

MIT License.

See [LICENSE](./LICENSE) for details.

---

## 🙏 Acknowledgments / Agradecimentos

Built with open-source tools:

[Python](https://www.python.org/) · [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) · [feedparser](https://pythonhosted.org/feedparser/) · [pyperclip](https://pypi.org/project/pyperclip/)

---

<div align="center">
  <p><strong>Morning Digest // MEGA FEED</strong></p>
  <p>Feeds entram. Curadoria sai. Prompt pronto para IA.</p>
  <p><em>Feeds in. Curation out. AI-ready prompt.</em></p>
</div>
