"""Offline demo feed data for portfolio demos without network."""

from __future__ import annotations

from datetime import datetime, timedelta
from types import SimpleNamespace
from typing import Any

_NOW = datetime.now()


def _entry(title: str, link: str, summary: str, hours_ago: int) -> Any:
    dt = _NOW - timedelta(hours=hours_ago)
    return SimpleNamespace(
        title=title,
        link=link,
        summary=summary,
        published_parsed=dt.timetuple(),
    )


DEMO_FEED_URLS = [
    "https://demo.local/tech.xml",
    "https://demo.local/markets.xml",
    "https://demo.local/sports.xml",
]

DEMO_ENTRIES_BY_FEED: dict[str, list[Any]] = {
    DEMO_FEED_URLS[0]: [
        _entry(
            "Novo modelo open-source rivaliza em benchmarks de código",
            "https://example.com/tech/open-source-model",
            "Comunidade libera pesos e avaliações em tarefas de engenharia de software.",
            2,
        ),
        _entry(
            "Atualização de segurança crítica em bibliotecas Python populares",
            "https://example.com/tech/python-security",
            "Mantenedores recomendam upgrade imediato para corrigir falha de desserialização.",
            5,
        ),
        _entry(
            "Consoles portáteis impulsam mercado indie no Brasil",
            "https://example.com/tech/handheld-gaming",
            "Estúdios locais reportam aumento de downloads após lançamentos recentes.",
            8,
        ),
    ],
    DEMO_FEED_URLS[1]: [
        _entry(
            "Selic e dólar: mercado reage a dados de inflação",
            "https://example.com/markets/selic",
            "Analistas revisam projeções após leitura do IPCA e comunicação do BC.",
            1,
        ),
        _entry(
            "Bitcoin oscila com fluxo institucional e ETFs",
            "https://example.com/markets/bitcoin",
            "Volume sobe com renovado interesse em produtos listados.",
            4,
        ),
        _entry(
            "Startups de IA captam rodadas seed no Brasil",
            "https://example.com/markets/ai-funding",
            "Fundos priorizam produtos B2B com tração de receita recorrente.",
            7,
        ),
    ],
    DEMO_FEED_URLS[2]: [
        _entry(
            "Corinthians estreia reforços em treino coletivo",
            "https://example.com/sports/corinthians",
            "Comissão técnica avalia encaixes táticos para o próximo confronto.",
            3,
        ),
        _entry(
            "Brasileirão: tabela aperta na parte de cima",
            "https://example.com/sports/brasileirao",
            "Empates e viradas redesenham a briga por vaga na Libertadores.",
            6,
        ),
        _entry(
            "Seleção feminina anuncia convocação para amistosos",
            "https://example.com/sports/selecao",
            "Lista mistura base titular e jovens em ascensão no campeonato nacional.",
            9,
        ),
    ],
}
