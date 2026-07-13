"""Prompt templates and digest assembly."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from morning_digest.filters import NewsItem

STOIC_PHRASES = [
    "A alma é tingida da cor de seus pensamentos. – Marco Aurélio",
    "Não é que tenhamos pouco tempo, é que perdemos muito. – Sêneca",
    "O homem sábio não se aflige com o que não tem, mas alegra-se com o que tem. – Epicteto",
]


@dataclass(frozen=True)
class PromptTemplate:
    name: str
    header_emoji: str
    instruction: str


PROMPT_TEMPLATES: list[PromptTemplate] = [
    PromptTemplate(
        "Padrão",
        "☀️",
        "Crie uma newsletter com 15 destaques (manchete + 5 linhas de análise) "
        "e um radar rápido com 50 bullets. Use linguagem direta e gírias da internet.",
    ),
    PromptTemplate(
        "Foco em Tech/Games",
        "🎮",
        "Priorize notícias de tecnologia, games e hardware. Inclua análises curtas "
        "sobre lançamentos e rumores. Use emojis de computador e console.",
    ),
    PromptTemplate(
        "Corinthians & Política",
        "⚽🏛️",
        "Destaque tudo sobre o Corinthians e o cenário político nacional. "
        "Use analogias de futebol e tom ácido.",
    ),
    PromptTemplate(
        "Crypto & Mercado",
        "📈",
        "Foco em criptomoedas, ações, macroeconomia e fusões. "
        "Use linguagem de investidor (high risk, airdrops, etc.).",
    ),
    PromptTemplate(
        "Estoico & Resumido",
        "📜",
        "Resumo extremamente conciso, com uma citação estoica no início e apenas "
        "bullets diretos. Máximo de 20 itens.",
    ),
]


def get_template(name: str) -> PromptTemplate:
    for template in PROMPT_TEMPLATES:
        if template.name == name:
            return template
    return PROMPT_TEMPLATES[0]


def stoic_quote_for(day: date | None = None) -> str:
    target = day or date.today()
    index = hash(target.strftime("%Y%m%d")) % len(STOIC_PHRASES)
    return STOIC_PHRASES[index]


def build_prompt(
    news_list: list[NewsItem],
    template: PromptTemplate,
    *,
    day: date | None = None,
) -> str:
    """Build a structured AI prompt from curated news items."""
    header = (
        f"{template.header_emoji} BOM DIA!\n"
        f"> {stoic_quote_for(day)}\n\n"
    )
    body = f"**{template.name}** – {template.instruction}\n\n"

    if not news_list:
        return (
            header
            + body
            + "### Sem notícias\n"
            + "Nenhuma notícia passou pelos filtros. Ajuste feeds ou palavras-chave e tente novamente.\n"
        )

    destaques = "### 🔥 15 DESTAQUES\n"
    for item in news_list[:15]:
        destaques += f"📌 **{item['title']}** ({item['src']})\n"
        destaques += f"   {item['desc']}\n"
        destaques += f"   [Leia mais]({item['link']})\n\n"

    radar_items = news_list[15:65]
    radar = "### ⚡ RADAR RÁPIDO\n"
    if not radar_items:
        radar += "_Nenhum item adicional além dos destaques._\n"
    else:
        for item in radar_items:
            snippet = item["desc"][:50]
            radar += (
                f"• **{item['src']}:** {item['title']} – {snippet}"
                f"{'...' if len(item['desc']) > 50 else ''} [link]({item['link']})\n"
            )

    return header + body + destaques + radar


def empty_collector_message() -> str:
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    return (
        "Morning Digest // MEGA FEED\n"
        "────────────────────────────\n\n"
        "Nenhuma coleta ainda.\n\n"
        "1. Escolha um template de prompt\n"
        "2. Clique em RASTREAR TUDO (ou use DEMO OFFLINE)\n"
        "3. Revise o digest gerado\n"
        "4. Copie o prompt para a IA\n\n"
        f"Pronto em {now}.\n"
    )
