"""Scraping de flux RSS pour sources tech africaines."""

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser


def strip_html(text: str) -> str:
    """Enlève les balises HTML et nettoie le texte."""
    clean = re.sub(r"<[^>]+>", " ", text)
    clean = re.sub(r"\s+", " ", clean)
    return clean.strip()


def make_id(url: str) -> str:
    """Génère un ID court basé sur l'URL."""
    return hashlib.md5(url.encode()).hexdigest()[:12]


# Sources en dur — pas de dépendance PyYAML
SOURCES = [
    {"name": "TechCabal", "url": "https://techcabal.com/feed/", "lang": "en", "region": "Nigeria / Pan-Afrique"},
    {"name": "Techpoint Africa", "url": "https://techpoint.africa/feed/", "lang": "en", "region": "Nigeria"},
    {"name": "WeeTracker", "url": "https://weetracker.com/feed/", "lang": "en", "region": "Afrique de l'Est"},
    {"name": "Agence Ecofin", "url": "https://www.agenceecofin.com/feed", "lang": "fr", "region": "Pan-Afrique francophone"},
]


def fetch_feed(source: dict) -> list[dict]:
    """Fetch un flux RSS et retourne les articles normalisés."""
    feed = feedparser.parse(source["url"])
    articles = []

    for entry in feed.entries:
        published = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).isoformat()

        summary = entry.get("summary") or entry.get("description") or ""
        articles.append(
            {
                "id": make_id(entry.link),
                "title": entry.title.strip(),
                "url": entry.link,
                "summary": strip_html(summary)[:300],
                "source": source["name"],
                "region": source.get("region", ""),
                "lang": source.get("lang", "en"),
                "published": published,
            }
        )

    return articles


def fetch_all() -> list[dict]:
    """Fetch tous les flux et retourne les articles triés par date."""
    all_articles = []
    for src in SOURCES:
        try:
            articles = fetch_feed(src)
            print(f"  {src['name']}: {len(articles)} articles")
            all_articles.extend(articles)
        except Exception as e:
            print(f"  ECHEC {src['name']}: {e}")

    all_articles.sort(key=lambda a: a["published"] or "1970", reverse=True)
    return all_articles
