"""Default and suggested RSS feed catalogs."""

from __future__ import annotations

SAO_CARLOS_RSS = (
    "https://news.google.com/rss/search?q=S%C3%A3o+Carlos+SP&hl=pt-BR&gl=BR&ceid=BR:pt-419"
)

DEFAULT_FEEDS: list[str] = [
    # Esportes
    "https://ge.globo.com/futebol/times/corinthians/rss/",
    "https://ge.globo.com/rss/ge/",
    "https://www.lance.com.br/rss",
    # Notícias Brasil
    "https://g1.globo.com/rss/g1/",
    "https://www.metropoles.com/feed",
    "https://www.cnnbrasil.com.br/feed/",
    "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
    "https://www.estadao.com.br/rss/ultimas",
    "https://rss.uol.com.br/feed/noticias.xml",
    "https://www.terra.com.br/rss",
    "https://oantagonista.com.br/feed/",
    "https://www.istoedinheiro.com.br/feed/",
    "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419",
    # Economia & mercado
    "https://valor.globo.com/rss/loja/valor",
    "https://www.infomoney.com.br/feed/",
    "https://www.bloomberglinea.com.br/arc/outboundfeeds/rss/?outputType=xml",
    "https://br.cointelegraph.com/rss",
    "https://www.forbes.com/most-popular/feed/",
    "https://br.tradingview.com/feed/",
    # Internacional
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://www.bbc.com/portuguese/index.xml",
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "http://rss.cnn.com/rss/edition.rss",
    "https://www.economist.com/the-world-this-week/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.washingtonpost.com/rss/world",
    "https://www.yahoo.com/news/rss",
    # Tech, games & ciência
    "https://olhardigital.com.br/feed/",
    "https://www.techtudo.com.br/rss/google/plantao.xml",
    "https://www.tecmundo.com.br/rss",
    "https://canaltech.com.br/rss/",
    "https://br.ign.com/feed.xml",
    "https://jovemnerd.com.br/feed/",
    "https://ourworldindata.org/atom.xml",
    # Local
    SAO_CARLOS_RSS,
]

SUGGESTED_FEEDS: dict[str, list[str]] = {
    "Corinthians": ["https://ge.globo.com/futebol/times/corinthians/rss/"],
    "Notícias BR": [
        "https://g1.globo.com/rss/g1/",
        "https://www.cnnbrasil.com.br/feed/",
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
        "https://oantagonista.com.br/feed/",
    ],
    "Economia & Crypto": [
        "https://www.infomoney.com.br/feed/",
        "https://br.cointelegraph.com/rss",
        "https://valor.globo.com/rss/loja/valor",
    ],
    "Tech & Games": [
        "https://olhardigital.com.br/feed/",
        "https://www.tecmundo.com.br/rss",
        "https://br.ign.com/feed.xml",
    ],
    "Internacional": [
        "http://feeds.bbci.co.uk/news/rss.xml",
        "http://rss.cnn.com/rss/edition.rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    ],
}


def is_valid_feed_url(url: str) -> bool:
    """Basic URL validation for RSS feed input."""
    value = (url or "").strip()
    if not value or len(value) > 2048:
        return False
    lower = value.lower()
    return lower.startswith("http://") or lower.startswith("https://")
