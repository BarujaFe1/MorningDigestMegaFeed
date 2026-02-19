
```markdown
# ☀️ Morning Digest // MEGA FEED

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-ff69b4)

**Morning Digest** é um agregador de notícias inteligente que coleta informações de dezenas de fontes RSS e gera prompts prontos para serem usados em IAs como ChatGPT, Claude, etc. A interface moderna em tema escuro permite que você customize os feeds, escolha entre 5 estilos de prompt, filtre por palavras‑chave e tenha uma visão completa do que importa para você.

Ideal para quem quer montar newsletters, resumos diários ou simplesmente se manter informado com curadoria personalizada.

---

## 📋 Índice

- [✨ Funcionalidades](#-funcionalidades)
- [📸 Screenshots](#-screenshots)
- [🚀 Instalação](#-instalação)
- [🎮 Como Usar](#-como-usar)
  - [Aba Coletor](#aba-coletor)
  - [Aba Configurações](#aba-configurações)
- [⚙️ Configurações Avançadas](#️-configurações-avançadas)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## ✨ Funcionalidades

- **Coleta massiva de RSS** – Mais de 30 feeds pré‑configurados (esportes, política, economia, tech, internacional, local).
- **5 templates de prompt** – Escolha o estilo da sua newsletter: Padrão, Tech/Games, Corinthians & Política, Crypto/Mercado, Estoico/Resumido.
- **Filtros por palavra‑chave** – Inclua ou exclua notícias baseado em termos personalizados.
- **Gerenciamento visual de feeds** – Adicione, remova ou restaure feeds com um clique.
- **Sugestões rápidas** – Botões para adicionar feeds de categorias comuns (Corinthians, Notícias BR, Crypto, Tech, Internacional).
- **Ordenação por data e remoção de duplicatas** – Notícias mais recentes primeiro, sem repetição.
- **Interface com abas** – Separador entre Coletor e Configurações para organização.
- **Cópia para área de transferência** – Botão para copiar o prompt gerado e colar diretamente na IA.
- **Persistência de configurações** – Tudo salvo em `news_config.json`.

---


## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior instalado.
- Conexão com a internet (para acessar os feeds RSS).

### Passo a passo

1. **Clone o repositório** (ou baixe o ZIP):
   ```bash
   git clone https://github.com/seu-usuario/Morning-Digest-Mega-Feed.git
   cd Morning-Digest-Mega-Feed
   ```

2. **(Opcional) Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install customtkinter feedparser pyperclip
   ```

4. **Execute o programa**:
   ```bash
   python main.py
   ```

> **Nota:** Na primeira execução, o arquivo `news_config.json` será criado automaticamente com os feeds padrão.

---

## 🎮 Como Usar

### Aba Coletor

1. Na parte superior, escolha um dos **5 templates de prompt**.
2. Clique em **🔍 RASTREAR TUDO**. O programa começará a ler todos os feeds ativos.
3. Após a coleta (pode levar alguns segundos), o prompt completo será exibido na caixa de texto.
4. Clique em **📋 COPIAR PROMPT** para copiar o conteúdo para a área de transferência e cole na sua IA favorita.

### Aba Configurações

1. **Feeds RSS Ativos** – Lista todas as URLs atualmente em uso. Você pode:
   - **Adicionar Feed**: digite a URL de um feed RSS.
   - **Remover Selecionado**: clique em uma linha da lista e depois no botão vermelho.
   - **Salvar Configurações**: após qualquer alteração, clique para persistir.
2. **Sugestões de Feeds** – Botões rápidos para adicionar feeds de categorias predefinidas.
3. **Palavras-chave** – Defina termos para **incluir** (notícias que **devem** conter alguma dessas palavras) ou **excluir** (notícias que **não podem** conter). Separe por vírgula.

> 💡 **Dica**: Use palavras‑chave para focar em assuntos específicos, ex.: `GTA VI, CBLOL, Corinthians` para incluir; `novela, BBB` para excluir.

---

## ⚙️ Configurações Avançadas

O arquivo `news_config.json` é gerado automaticamente na pasta do programa. Você pode editá‑lo manualmente:

```json
{
    "feeds": [
        "https://ge.globo.com/futebol/times/corinthians/rss/",
        "https://g1.globo.com/rss/g1/",
        ...
    ],
    "prompt_template": "Padrão",
    "keywords_include": ["corinthians", "gta"],
    "keywords_exclude": ["fofoca", "bbb"]
}
```

- **feeds**: lista de URLs de RSS.
- **prompt_template**: nome do template ativo (deve corresponder a um dos templates do código).
- **keywords_include**: lista de palavras que a notícia **deve** conter (vazio = sem filtro).
- **keywords_exclude**: lista de palavras que a notícia **não pode** conter.

---

## 📁 Estrutura do Projeto

```
Morning-Digest-Mega-Feed/
├── main.py                  # Código principal
├── news_config.json         # Configurações salvas (gerado automaticamente)
├── requirements.txt         # Dependências (opcional)
├── README.md                # Este arquivo
└── .gitignore               # Ignora arquivos desnecessários
```

Se quiser, crie um `requirements.txt` com o conteúdo:
```
customtkinter
feedparser
pyperclip
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – Interface gráfica moderna com tema escuro.
- [feedparser](https://pythonhosted.org/feedparser/) – Parse de feeds RSS.
- [pyperclip](https://pypi.org/project/pyperclip/) – Cópia para a área de transferência.

---

## 🤝 Contribuição

Contribuições são bem‑vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

Por favor, mantenha o código limpo e documentado.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido com ☕ e muito ☀️ por [BarujaFe] (https://github.com/BarujaFe1).**  
Se gostou, deixe uma ⭐ no repositório!
```
