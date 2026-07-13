"""CustomTkinter desktop UI for Morning Digest."""

from __future__ import annotations

import logging
import threading
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
import pyperclip

from morning_digest.collector import collect_news
from morning_digest.config import ConfigManager
from morning_digest.demo_data import DEMO_FEED_URLS
from morning_digest.feeds import SUGGESTED_FEEDS, is_valid_feed_url
from morning_digest.html_utils import parse_keyword_list
from morning_digest.prompts import (
    PROMPT_TEMPLATES,
    build_prompt,
    empty_collector_message,
    get_template,
)
from morning_digest.theme import (
    FONT_BOLD,
    FONT_HEADER,
    FONT_MONO,
    FONT_SUB,
    THEME,
)

logger = logging.getLogger(__name__)


class UltimateNewsApp(ctk.CTk):
    def __init__(self, config_path: str | Path | None = None) -> None:
        super().__init__()
        self.title("Morning Digest // MEGA FEED")
        self.geometry("1200x850")
        self.minsize(960, 700)
        self.configure(fg_color=THEME["bg"])

        self.config_manager = ConfigManager(config_path)
        self.current_feeds = list(self.config_manager.config["feeds"])
        self.current_template_name = self.config_manager.config["prompt_template"]
        self.keywords_include = list(self.config_manager.config.get("keywords_include", []))
        self.keywords_exclude = list(self.config_manager.config.get("keywords_exclude", []))
        self._last_prompt = ""
        self._busy = False

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self.tabview = ctk.CTkTabview(self, fg_color="transparent")
        self.tabview.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")
        self.tab_collector = self.tabview.add("Coletor")
        self.tab_settings = self.tabview.add("Configurações")
        self.build_collector_tab()
        self.build_settings_tab()
        self._build_footer()

    def _build_header(self) -> None:
        self.header_frame = ctk.CTkFrame(
            self, fg_color=THEME["sidebar"], corner_radius=0, height=90
        )
        self.header_frame.grid(row=0, column=0, sticky="ew")

        title_wrap = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        title_wrap.pack(side="left", padx=25, pady=18)
        self.title_lbl = ctk.CTkLabel(
            title_wrap,
            text="MORNING DIGEST // MEGA FEED",
            font=FONT_HEADER,
            text_color=THEME["purple"],
        )
        self.title_lbl.pack(anchor="w")
        self.subtitle_lbl = ctk.CTkLabel(
            title_wrap,
            text="RSS → filtros → prompt Markdown (handoff local)",
            font=FONT_SUB,
            text_color=THEME["comment"],
        )
        self.subtitle_lbl.pack(anchor="w")

        self.status_lbl = ctk.CTkLabel(
            self.header_frame,
            text="Pronto",
            font=FONT_BOLD,
            text_color=THEME["comment"],
        )
        self.status_lbl.pack(side="right", padx=25)

    def _build_footer(self) -> None:
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.grid(row=2, column=0, padx=25, pady=(0, 25), sticky="ew")

        self.btn_run = ctk.CTkButton(
            self.footer,
            text="RASTREAR TUDO",
            font=FONT_BOLD,
            fg_color=THEME["cyan"],
            text_color=THEME["bg"],
            hover_color=THEME["green"],
            height=50,
            command=self.run_scraper,
        )
        self.btn_run.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.btn_demo = ctk.CTkButton(
            self.footer,
            text="DEMO OFFLINE",
            font=FONT_BOLD,
            fg_color=THEME["purple"],
            text_color=THEME["fg"],
            hover_color=THEME["pink"],
            height=50,
            width=160,
            command=self.run_demo,
        )
        self.btn_demo.pack(side="left", padx=(0, 8))

        self.btn_export = ctk.CTkButton(
            self.footer,
            text="EXPORTAR .MD",
            font=FONT_BOLD,
            fg_color=THEME["card"],
            text_color=THEME["fg"],
            hover_color=THEME["comment"],
            border_width=1,
            border_color=THEME["border"],
            height=50,
            width=140,
            command=self.export_markdown,
        )
        self.btn_export.pack(side="left", padx=(0, 8))

        self.btn_copy = ctk.CTkButton(
            self.footer,
            text="COPIAR PROMPT",
            font=FONT_BOLD,
            fg_color=THEME["orange"],
            text_color=THEME["bg"],
            hover_color=THEME["pink"],
            height=50,
            command=self.copy_to_clipboard,
        )
        self.btn_copy.pack(side="right", fill="x", expand=True, padx=(8, 0))

    def build_collector_tab(self) -> None:
        template_frame = ctk.CTkFrame(self.tab_collector, fg_color="transparent")
        template_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(template_frame, text="Template de Prompt:", font=FONT_BOLD).pack(
            side="left", padx=10
        )
        self.template_var = ctk.StringVar(value=self.current_template_name)
        template_menu = ctk.CTkOptionMenu(
            template_frame,
            values=[t.name for t in PROMPT_TEMPLATES],
            variable=self.template_var,
            fg_color=THEME["card"],
            button_color=THEME["purple"],
            command=self._on_template_change,
        )
        template_menu.pack(side="left", padx=10)

        self.hint_lbl = ctk.CTkLabel(
            template_frame,
            text=f"{len(self.current_feeds)} feeds ativos",
            font=FONT_SUB,
            text_color=THEME["comment"],
        )
        self.hint_lbl.pack(side="right", padx=10)

        self.textbox = ctk.CTkTextbox(
            self.tab_collector,
            fg_color=THEME["card"],
            text_color=THEME["fg"],
            font=FONT_MONO,
            corner_radius=15,
            border_width=1,
            border_color=THEME["border"],
        )
        self.textbox.pack(fill="both", expand=True, pady=10)
        self.textbox.insert("1.0", empty_collector_message())

    def build_settings_tab(self) -> None:
        main_frame = ctk.CTkFrame(self.tab_settings, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(main_frame, text="Feeds RSS Ativos:", font=FONT_BOLD).pack(anchor="w")
        self.feeds_listbox = ctk.CTkTextbox(main_frame, height=150, fg_color=THEME["card"])
        self.feeds_listbox.pack(fill="x", pady=5)
        self.update_feeds_display()

        btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=5)

        ctk.CTkButton(
            btn_frame,
            text="Adicionar Feed",
            fg_color=THEME["green"],
            text_color=THEME["bg"],
            command=self.add_feed_dialog,
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            btn_frame,
            text="Remover Linha",
            fg_color=THEME["red"],
            command=self.remove_selected_feed,
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            btn_frame,
            text="Restaurar Padrão",
            fg_color=THEME["comment"],
            command=self.restore_defaults,
        ).pack(side="left", padx=5)
        ctk.CTkButton(
            btn_frame,
            text="Salvar Configurações",
            fg_color=THEME["purple"],
            command=self.save_settings,
        ).pack(side="left", padx=5)

        ctk.CTkLabel(main_frame, text="Sugestões de Feeds:", font=FONT_BOLD).pack(
            anchor="w", pady=(15, 5)
        )
        sugg_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        sugg_frame.pack(fill="x")

        row = 0
        col = 0
        for category, feeds in SUGGESTED_FEEDS.items():
            btn = ctk.CTkButton(
                sugg_frame,
                text=category,
                fg_color=THEME["comment"],
                command=lambda f=feeds: self.add_suggested_feeds(f),
            )
            btn.grid(row=row, column=col, padx=5, pady=2, sticky="w")
            col += 1
            if col > 2:
                col = 0
                row += 1

        ctk.CTkLabel(
            main_frame,
            text="Palavras-chave para INCLUIR (separadas por vírgula):",
            font=FONT_BOLD,
        ).pack(anchor="w", pady=(15, 2))
        self.include_entry = ctk.CTkEntry(main_frame, fg_color=THEME["card"])
        self.include_entry.pack(fill="x", pady=2)
        self.include_entry.insert(0, ", ".join(self.keywords_include))

        ctk.CTkLabel(
            main_frame,
            text="Palavras-chave para EXCLUIR (separadas por vírgula):",
            font=FONT_BOLD,
        ).pack(anchor="w", pady=(5, 2))
        self.exclude_entry = ctk.CTkEntry(main_frame, fg_color=THEME["card"])
        self.exclude_entry.pack(fill="x", pady=2)
        self.exclude_entry.insert(0, ", ".join(self.keywords_exclude))

        tip = ctk.CTkLabel(
            main_frame,
            text="Dica: deixe INCLUIR vazio para aceitar todos os temas; EXCLUIR remove ruído.",
            font=FONT_SUB,
            text_color=THEME["comment"],
        )
        tip.pack(anchor="w", pady=(10, 0))

    def update_feeds_display(self) -> None:
        self.feeds_listbox.delete("1.0", "end")
        for url in self.current_feeds:
            self.feeds_listbox.insert("end", url + "\n")
        if hasattr(self, "hint_lbl"):
            self.hint_lbl.configure(text=f"{len(self.current_feeds)} feeds ativos")

    def add_feed_dialog(self) -> None:
        dialog = ctk.CTkInputDialog(text="Digite a URL do feed RSS:", title="Adicionar Feed")
        url = (dialog.get_input() or "").strip()
        if not url:
            return
        if not is_valid_feed_url(url):
            messagebox.showerror("URL inválida", "Informe uma URL http:// ou https:// válida.")
            return
        if url in self.current_feeds:
            messagebox.showinfo("Já existe", "Este feed já está na lista.")
            return
        self.current_feeds.append(url)
        self.update_feeds_display()

    def remove_selected_feed(self) -> None:
        try:
            index = self.feeds_listbox.index("insert").split(".")[0]
            line_start = f"{index}.0"
            line_end = f"{index}.end"
            url = self.feeds_listbox.get(line_start, line_end).strip()
        except (AttributeError, ValueError, TypeError):
            messagebox.showerror("Erro", "Posicione o cursor na linha do feed a remover.")
            return

        if not url:
            messagebox.showerror("Erro", "Posicione o cursor na linha do feed a remover.")
            return
        if url in self.current_feeds:
            self.current_feeds.remove(url)
            self.update_feeds_display()

    def add_suggested_feeds(self, feeds: list[str]) -> None:
        added = 0
        for url in feeds:
            if url not in self.current_feeds:
                self.current_feeds.append(url)
                added += 1
        self.update_feeds_display()
        if added:
            self.set_status(f"{added} feed(s) adicionados. Salve para persistir.")
        else:
            self.set_status("Sugestões já estavam na lista.")

    def restore_defaults(self) -> None:
        if not messagebox.askyesno(
            "Restaurar padrão",
            "Substituir feeds e filtros pelos valores padrão?",
        ):
            return
        self.config_manager.restore_defaults()
        self.current_feeds = list(self.config_manager.config["feeds"])
        self.keywords_include = list(self.config_manager.config["keywords_include"])
        self.keywords_exclude = list(self.config_manager.config["keywords_exclude"])
        self.current_template_name = self.config_manager.config["prompt_template"]
        self.template_var.set(self.current_template_name)
        self.include_entry.delete(0, "end")
        self.exclude_entry.delete(0, "end")
        self.update_feeds_display()
        self.set_status("Configuração padrão restaurada.")

    def save_settings(self) -> None:
        self.config_manager.config["feeds"] = list(self.current_feeds)
        self.config_manager.config["prompt_template"] = self.template_var.get()
        incl = parse_keyword_list(self.include_entry.get())
        excl = parse_keyword_list(self.exclude_entry.get())
        self.config_manager.config["keywords_include"] = incl
        self.config_manager.config["keywords_exclude"] = excl
        self.config_manager.save()
        self.keywords_include = incl
        self.keywords_exclude = excl
        self.current_template_name = self.template_var.get()
        self.update_feeds_display()
        messagebox.showinfo("Sucesso", "Configurações salvas!")

    def _on_template_change(self, _value: str) -> None:
        self.current_template_name = self.template_var.get()

    def set_status(self, text: str) -> None:
        self.after(0, lambda: self.status_lbl.configure(text=text))

    def _set_busy(self, busy: bool, label: str | None = None) -> None:
        self._busy = busy
        state = "disabled" if busy else "normal"
        self.btn_run.configure(state=state)
        self.btn_demo.configure(state=state)
        if label:
            self.btn_run.configure(text=label)

    def run_scraper(self) -> None:
        if self._busy:
            return
        if not self.current_feeds:
            messagebox.showwarning(
                "Sem feeds",
                "Adicione ao menos um feed RSS ou use DEMO OFFLINE.",
            )
            return
        self._start_collection(demo=False)

    def run_demo(self) -> None:
        if self._busy:
            return
        self._start_collection(demo=True)

    def _start_collection(self, *, demo: bool) -> None:
        self._set_busy(True, "COLETANDO..." if not demo else "DEMO...")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", "Coletando notícias...\n")
        threading.Thread(
            target=self._fetch_worker,
            kwargs={"demo": demo},
            daemon=True,
        ).start()

    def _fetch_worker(self, *, demo: bool) -> None:
        feeds = list(DEMO_FEED_URLS) if demo else list(self.current_feeds)
        try:
            items, errors = collect_news(
                feeds,
                include=self.keywords_include,
                exclude=self.keywords_exclude,
                demo=demo,
                on_progress=self.set_status,
            )
            template = get_template(self.template_var.get())
            prompt = build_prompt(items[:250], template)
            self.after(0, lambda: self.finish(prompt, len(items), errors, demo=demo))
        except Exception as exc:  # noqa: BLE001
            logger.exception("Falha na coleta")
            message = str(exc)
            self.after(0, lambda msg=message: self.fail(msg))

    def finish(self, text: str, count: int, errors: int, *, demo: bool = False) -> None:
        self._last_prompt = text
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
        mode = "Demo" if demo else "Concluído"
        err_bit = f" · {errors} feed(s) com falha" if errors else ""
        self.status_lbl.configure(text=f"{mode}! {count} notícias{err_bit}")
        self._set_busy(False, "ATUALIZAR TUDO")

    def fail(self, message: str) -> None:
        self.textbox.delete("1.0", "end")
        self.textbox.insert(
            "1.0",
            "Falha na coleta.\n\n"
            f"{message}\n\n"
            "Verifique a conexão, os feeds em Configurações ou use DEMO OFFLINE.",
        )
        self.status_lbl.configure(text="Erro na coleta")
        self._set_busy(False, "RASTREAR TUDO")

    def copy_to_clipboard(self) -> None:
        content = self.textbox.get("1.0", "end").strip()
        if not content or content == empty_collector_message().strip():
            messagebox.showinfo("Nada para copiar", "Gere um digest antes de copiar.")
            return
        try:
            pyperclip.copy(content)
        except pyperclip.PyperclipException as exc:
            messagebox.showerror("Clipboard", f"Não foi possível copiar: {exc}")
            return
        self.btn_copy.configure(text="COPIADO!", fg_color=THEME["green"])
        self.after(
            2000,
            lambda: self.btn_copy.configure(text="COPIAR PROMPT", fg_color=THEME["orange"]),
        )

    def export_markdown(self) -> None:
        content = self.textbox.get("1.0", "end").strip()
        if not content or content.startswith("Morning Digest // MEGA FEED\n"):
            messagebox.showinfo("Nada para exportar", "Gere um digest antes de exportar.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown", "*.md"), ("Texto", "*.txt"), ("Todos", "*.*")],
            title="Exportar digest",
        )
        if not path:
            return
        try:
            Path(path).write_text(content + "\n", encoding="utf-8")
        except OSError as exc:
            messagebox.showerror("Exportação", f"Falha ao salvar: {exc}")
            return
        self.set_status(f"Exportado: {Path(path).name}")


def run_app(config_path: str | Path | None = None) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    ctk.set_appearance_mode("Dark")
    app = UltimateNewsApp(config_path=config_path)
    app.mainloop()
