import customtkinter as ctk
import feedparser
import threading
import pyperclip
import time
import json
import urllib.parse
import socket
import os
from datetime import datetime
from tkinter import messagebox, filedialog

# =============================================================================
# 🎨 TEMA MIDNIGHT (inalterado)
# =============================================================================
THEME = {
    "bg": "#13141f", "card": "#1e1f29", "sidebar": "#0f1019", "fg": "#f8f8f2",
    "cyan": "#8be9fd", "green": "#50fa7b", "orange": "#ffb86c",
    "pink": "#ff79c6", "purple": "#bd93f9", "red": "#ff5555", "comment": "#6272a4"
}

FONT_FAMILY = "Segoe UI"
FONT_BOLD = (FONT_FAMILY, 13, "bold")
FONT_HEADER = (FONT_FAMILY, 22, "bold")
FONT_MONO = ("Consolas", 12)

# =============================================================================
# ⚙️ GERENCIADOR DE CONFIGURAÇÃO (JSON)
# =============================================================================
CONFIG_FILE = "news_config.json"

# --- TODAS AS SUAS FONTES RSS (ORIGINAIS) ---
SAO_CARLOS_RSS = "https://news.google.com/rss/search?q=S%C3%A3o+Carlos+SP&hl=pt-BR&gl=BR&ceid=BR:pt-419"

DEFAULT_FEEDS = [
    # --- 🏟️ ESPORTES (Corinthians + Geral) ---
    "https://ge.globo.com/futebol/times/corinthians/rss/",  # Foco Timão
    "https://ge.globo.com/rss/ge/",  # Geral GE
    "https://www.lance.com.br/rss",

    # --- 📰 NOTÍCIAS BRASIL (Gerais) ---
    "https://g1.globo.com/rss/g1/",
    "https://www.metropoles.com/feed",
    "https://www.cnnbrasil.com.br/feed/",
    "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
    "https://www.estadao.com.br/rss/ultimas",
    "https://rss.uol.com.br/feed/noticias.xml",
    "https://www.terra.com.br/rss",
    "https://oantagonista.com.br/feed/",  # Política/MBL Friendly
    "https://www.istoedinheiro.com.br/feed/",
    "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419",  # Google News Top BR

    # --- 💰 ECONOMIA & MERCADO ---
    "https://valor.globo.com/rss/loja/valor",
    "https://www.infomoney.com.br/feed/",
    "https://www.bloomberglinea.com.br/arc/outboundfeeds/rss/?outputType=xml",
    "https://br.cointelegraph.com/rss",  # Crypto
    "https://www.forbes.com/most-popular/feed/",
    "https://br.tradingview.com/feed/",

    # --- 🌍 INTERNACIONAL (Grandes Jornais) ---
    "http://feeds.bbci.co.uk/news/rss.xml",  # BBC World
    "https://www.bbc.com/portuguese/index.xml",  # BBC Brasil
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "http://rss.cnn.com/rss/edition.rss",  # CNN US
    "https://www.economist.com/the-world-this-week/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.washingtonpost.com/rss/world",
    "https://www.yahoo.com/news/rss",

    # --- 💻 TECH, GAMES & CIÊNCIA ---
    "https://olhardigital.com.br/feed/",
    "https://www.techtudo.com.br/rss/google/plantao.xml",
    "https://www.tecmundo.com.br/rss",
    "https://canaltech.com.br/rss/",
    "https://br.ign.com/feed.xml",  # IGN Brasil (Games)
    "https://jovemnerd.com.br/feed/",  # Nerd/Geek
    "https://ourworldindata.org/atom.xml",  # Dados/Ciência

    # --- 🏡 LOCAL ---
    SAO_CARLOS_RSS
]

# Sugestões de feeds por categoria (para adicionar rapidamente)
SUGGESTED_FEEDS = {
    "⚽ Corinthians": ["https://ge.globo.com/futebol/times/corinthians/rss/"],
    "📰 Notícias BR": [
        "https://g1.globo.com/rss/g1/",
        "https://www.cnnbrasil.com.br/feed/",
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
        "https://oantagonista.com.br/feed/"
    ],
    "💰 Economia & Crypto": [
        "https://www.infomoney.com.br/feed/",
        "https://br.cointelegraph.com/rss",
        "https://valor.globo.com/rss/loja/valor"
    ],
    "💻 Tech & Games": [
        "https://olhardigital.com.br/feed/",
        "https://www.tecmundo.com.br/rss",
        "https://br.ign.com/feed.xml"
    ],
    "🌍 Internacional": [
        "http://feeds.bbci.co.uk/news/rss.xml",
        "http://rss.cnn.com/rss/edition.rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    ]
}

class ConfigManager:
    def __init__(self):
        self.config = self.load()

    def load(self):
        if not os.path.exists(CONFIG_FILE):
            return {
                "feeds": DEFAULT_FEEDS.copy(),
                "prompt_template": "Padrão",
                "keywords_include": [],
                "keywords_exclude": []
            }
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

# =============================================================================
# 📝 TEMPLATES DE PROMPT
# =============================================================================
class PromptTemplate:
    def __init__(self, name, header_emoji, instruction):
        self.name = name
        self.header_emoji = header_emoji
        self.instruction = instruction

PROMPT_TEMPLATES = [
    PromptTemplate("Padrão", "☀️",
        "Crie uma newsletter com 15 destaques (manchete + 5 linhas de análise) e um radar rápido com 50 bullets. Use linguagem direta e gírias da internet."),
    PromptTemplate("Foco em Tech/Games", "🎮",
        "Priorize notícias de tecnologia, games e hardware. Inclua análises curtas sobre lançamentos e rumores. Use emojis de computador e console."),
    PromptTemplate("Corinthians & Política", "⚽🏛️",
        "Destaque tudo sobre o Corinthians e o cenário político nacional (MBL, CPI, etc.). Use analogias de futebol e tom ácido."),
    PromptTemplate("Crypto & Mercado", "📈",
        "Foco em criptomoedas, ações, macroeconomia e fusões. Use linguagem de investidor (high risk, airdrops, etc.)."),
    PromptTemplate("Estoico & Resumido", "📜",
        "Resumo extremamente conciso, com uma citação estoica no início e apenas bullets diretos. Máximo de 20 itens."),
]

# =============================================================================
# 🧠 APLICATIVO PRINCIPAL (REFATORADO)
# =============================================================================
class UltimateNewsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Morning Digest // MEGA EDITION")
        self.geometry("1200x850")
        self.configure(fg_color=THEME["bg"])

        self.config_manager = ConfigManager()
        self.current_feeds = self.config_manager.config["feeds"]
        self.current_template_name = self.config_manager.config["prompt_template"]
        self.keywords_include = self.config_manager.config.get("keywords_include", [])
        self.keywords_exclude = self.config_manager.config.get("keywords_exclude", [])

        # Grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color=THEME["sidebar"], corner_radius=0, height=90)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.title_lbl = ctk.CTkLabel(self.header_frame, text="MORNING DIGEST // MEGA FEED", font=FONT_HEADER, text_color=THEME["purple"])
        self.title_lbl.pack(side="left", padx=25, pady=25)
        self.status_lbl = ctk.CTkLabel(self.header_frame, text="Pronto", font=FONT_BOLD, text_color=THEME["comment"])
        self.status_lbl.pack(side="right", padx=25)

        # TabView (abas)
        self.tabview = ctk.CTkTabview(self, fg_color="transparent")
        self.tabview.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")

        # Aba 1: Coletor
        self.tab_collector = self.tabview.add("📡 Coletor")
        self.build_collector_tab()

        # Aba 2: Configurações
        self.tab_settings = self.tabview.add("⚙️ Configurações")
        self.build_settings_tab()

        # Footer com botões de ação
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.grid(row=2, column=0, padx=25, pady=(0, 25), sticky="ew")

        self.btn_run = ctk.CTkButton(
            self.footer, text="🔍 RASTREAR TUDO", font=FONT_BOLD,
            fg_color=THEME["cyan"], text_color=THEME["bg"], hover_color=THEME["green"], height=50,
            command=self.run_scraper
        )
        self.btn_run.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn_copy = ctk.CTkButton(
            self.footer, text="📋 COPIAR PROMPT", font=FONT_BOLD,
            fg_color=THEME["orange"], text_color=THEME["bg"], hover_color=THEME["pink"], height=50,
            command=self.copy_to_clipboard
        )
        self.btn_copy.pack(side="right", fill="x", expand=True, padx=(10, 0))

    # -------------------------------------------------------------------------
    # ABA COLETOR
    # -------------------------------------------------------------------------
    def build_collector_tab(self):
        # Frame para seleção de template
        template_frame = ctk.CTkFrame(self.tab_collector, fg_color="transparent")
        template_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(template_frame, text="Template de Prompt:", font=FONT_BOLD).pack(side="left", padx=10)
        self.template_var = ctk.StringVar(value=self.current_template_name)
        template_menu = ctk.CTkOptionMenu(
            template_frame,
            values=[t.name for t in PROMPT_TEMPLATES],
            variable=self.template_var,
            fg_color=THEME["card"],
            button_color=THEME["purple"]
        )
        template_menu.pack(side="left", padx=10)

        # Área de texto (resultado)
        self.textbox = ctk.CTkTextbox(
            self.tab_collector, fg_color=THEME["card"], text_color=THEME["fg"],
            font=FONT_MONO, corner_radius=15, border_width=1, border_color="#2a2b3d"
        )
        self.textbox.pack(fill="both", expand=True, pady=10)

    # -------------------------------------------------------------------------
    # ABA CONFIGURAÇÕES
    # -------------------------------------------------------------------------
    def build_settings_tab(self):
        main_frame = ctk.CTkFrame(self.tab_settings, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Lista de feeds atuais
        ctk.CTkLabel(main_frame, text="Feeds RSS Ativos:", font=FONT_BOLD).pack(anchor="w")
        self.feeds_listbox = ctk.CTkTextbox(main_frame, height=150, fg_color=THEME["card"])
        self.feeds_listbox.pack(fill="x", pady=5)
        self.update_feeds_display()

        # Botões para gerenciar feeds
        btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=5)

        ctk.CTkButton(btn_frame, text="➕ Adicionar Feed", fg_color=THEME["green"],
                      command=self.add_feed_dialog).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="❌ Remover Selecionado", fg_color=THEME["red"],
                      command=self.remove_selected_feed).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="💾 Salvar Configurações", fg_color=THEME["purple"],
                      command=self.save_settings).pack(side="left", padx=5)

        # Sugestões de feeds
        ctk.CTkLabel(main_frame, text="Sugestões de Feeds:", font=FONT_BOLD).pack(anchor="w", pady=(15,5))
        sugg_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        sugg_frame.pack(fill="x")

        row = 0
        col = 0
        for category, feeds in SUGGESTED_FEEDS.items():
            btn = ctk.CTkButton(sugg_frame, text=category, fg_color=THEME["comment"],
                                command=lambda f=feeds: self.add_suggested_feeds(f))
            btn.grid(row=row, column=col, padx=5, pady=2, sticky="w")
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Filtros por palavra-chave
        ctk.CTkLabel(main_frame, text="Palavras-chave para INCLUIR (separadas por vírgula):", font=FONT_BOLD).pack(anchor="w", pady=(15,2))
        self.include_entry = ctk.CTkEntry(main_frame, fg_color=THEME["card"])
        self.include_entry.pack(fill="x", pady=2)
        self.include_entry.insert(0, ", ".join(self.keywords_include))

        ctk.CTkLabel(main_frame, text="Palavras-chave para EXCLUIR (separadas por vírgula):", font=FONT_BOLD).pack(anchor="w", pady=(5,2))
        self.exclude_entry = ctk.CTkEntry(main_frame, fg_color=THEME["card"])
        self.exclude_entry.pack(fill="x", pady=2)
        self.exclude_entry.insert(0, ", ".join(self.keywords_exclude))

    def update_feeds_display(self):
        self.feeds_listbox.delete("1.0", "end")
        for url in self.current_feeds:
            self.feeds_listbox.insert("end", url + "\n")

    def add_feed_dialog(self):
        dialog = ctk.CTkInputDialog(text="Digite a URL do feed RSS:", title="Adicionar Feed")
        url = dialog.get_input()
        if url and url not in self.current_feeds:
            self.current_feeds.append(url)
            self.update_feeds_display()

    def remove_selected_feed(self):
        try:
            index = self.feeds_listbox.index("insert").split(".")[0]
            line_start = f"{index}.0"
            line_end = f"{index}.end"
            url = self.feeds_listbox.get(line_start, line_end).strip()
            if url in self.current_feeds:
                self.current_feeds.remove(url)
                self.update_feeds_display()
        except:
            messagebox.showerror("Erro", "Selecione uma linha para remover.")

    def add_suggested_feeds(self, feeds):
        for url in feeds:
            if url not in self.current_feeds:
                self.current_feeds.append(url)
        self.update_feeds_display()

    def save_settings(self):
        # Salva feeds, template escolhido e palavras‑chave
        self.config_manager.config["feeds"] = self.current_feeds
        self.config_manager.config["prompt_template"] = self.template_var.get()
        incl = [kw.strip() for kw in self.include_entry.get().split(",") if kw.strip()]
        excl = [kw.strip() for kw in self.exclude_entry.get().split(",") if kw.strip()]
        self.config_manager.config["keywords_include"] = incl
        self.config_manager.config["keywords_exclude"] = excl
        self.config_manager.save()
        self.keywords_include = incl
        self.keywords_exclude = excl
        self.current_template_name = self.template_var.get()
        messagebox.showinfo("Sucesso", "Configurações salvas!")

    # -------------------------------------------------------------------------
    # LÓGICA DE COLETA E GERAÇÃO DO PROMPT
    # -------------------------------------------------------------------------
    def run_scraper(self):
        self.btn_run.configure(state="disabled", text="COLETANDO FEEDS...")
        self.textbox.delete("1.0", "end")
        threading.Thread(target=self.fetch_rss, daemon=True).start()

    def update_status(self, txt):
        self.status_lbl.configure(text=txt)

    def fetch_rss(self):
        all_news = []
        total = len(self.current_feeds)
        errors = 0
        socket.setdefaulttimeout(5)

        for i, url in enumerate(self.current_feeds):
            try:
                domain = urllib.parse.urlparse(url).netloc.replace("www.", "").upper()
                if not domain:
                    domain = "FEED"
                self.update_status(f"Lendo ({i+1}/{total}): {domain}...")

                feed = feedparser.parse(url)
                limit = 12 if "corinthians" in url else 6  # prioridade para Corinthians

                if not feed.entries:
                    errors += 1
                    continue

                for entry in feed.entries[:limit]:
                    title = entry.title if hasattr(entry, 'title') else "N/A"
                    link = entry.link if hasattr(entry, 'link') else ""
                    desc = entry.summary if hasattr(entry, 'summary') else entry.description if hasattr(entry, 'description') else ""
                    desc = desc.replace("<p>", "").replace("</p>", "").replace("<br>", " ").replace("&nbsp;", " ")[:200] + "..."

                    published = entry.get("published_parsed", entry.get("updated_parsed"))
                    dt = datetime.fromtimestamp(time.mktime(published)) if published else datetime.now()

                    # Filtro por palavras‑chave
                    text_to_check = (title + " " + desc).lower()
                    if self.keywords_include and not any(kw.lower() in text_to_check for kw in self.keywords_include):
                        continue
                    if self.keywords_exclude and any(kw.lower() in text_to_check for kw in self.keywords_exclude):
                        continue

                    all_news.append({"src": domain, "title": title, "desc": desc, "link": link, "date": dt})

            except Exception as e:
                print(f"Erro em {url}: {e}")
                errors += 1

        # Ordenar por data (mais recente primeiro)
        all_news.sort(key=lambda x: x['date'], reverse=True)

        # Remover duplicatas (baseado no título)
        unique = []
        seen = set()
        for n in all_news:
            key = n['title'].lower()[:50]
            if key not in seen:
                unique.append(n)
                seen.add(key)

        # Gerar prompt conforme template selecionado
        template = next((t for t in PROMPT_TEMPLATES if t.name == self.template_var.get()), PROMPT_TEMPLATES[0])
        prompt = self.build_prompt(unique[:250], template)

        self.after(0, lambda: self.finish(prompt, len(unique)))

    def build_prompt(self, news_list, template):
        # Cabeçalho com frase estoica
        stoic_phrases = [
            "A alma é tingida da cor de seus pensamentos. – Marco Aurélio",
            "Não é que tenhamos pouco tempo, é que perdemos muito. – Sêneca",
            "O homem sábio não se aflige com o que não tem, mas alegra-se com o que tem. – Epicteto"
        ]
        header = f"{template.header_emoji} BOM DIA!\n> {stoic_phrases[hash(datetime.now().strftime('%Y%m%d')) % len(stoic_phrases)]}\n\n"

        # Instrução do template
        body = f"**{template.name}** – {template.instruction}\n\n"

        # 15 Destaques (se houver)
        destaques = ""
        if news_list:
            destaques = "### 🔥 15 DESTAQUES\n"
            for item in news_list[:15]:
                destaques += f"📌 **{item['title']}** ({item['src']})\n"
                destaques += f"   {item['desc']}\n"
                destaques += f"   [Leia mais]({item['link']})\n\n"

        # Radar rápido (50 bullets)
        radar = "### ⚡ RADAR RÁPIDO\n"
        for i, item in enumerate(news_list[15:65]):  # até 50
            radar += f"• **{item['src']}:** {item['title']} – {item['desc'][:50]}... [link]({item['link']})\n"

        return header + body + destaques + radar

    def finish(self, text, count):
        self.textbox.insert("1.0", text)
        self.status_lbl.configure(text=f"Concluído! {count} notícias coletadas.")
        self.btn_run.configure(state="normal", text="🔄 ATUALIZAR TUDO")

    def copy_to_clipboard(self):
        pyperclip.copy(self.textbox.get("1.0", "end"))
        self.btn_copy.configure(text="✅ COPIADO!", fg_color=THEME["green"])
        self.after(2000, lambda: self.btn_copy.configure(text="📋 COPIAR PROMPT", fg_color=THEME["orange"]))

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = UltimateNewsApp()
    app.mainloop()
