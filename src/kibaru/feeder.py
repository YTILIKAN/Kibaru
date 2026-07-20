"""Pipeline Kibaru — scrape, sauvegarde JSON + HTML."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from kibaru.scraper import fetch_all

SRC_DIR = Path(__file__).resolve().parent.parent.parent / "src"
OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "output"
OUTPUT_JSON = OUTPUT_DIR / "feed.json"
OUTPUT_HTML = OUTPUT_DIR / "index.html"


def generate_html(articles: list[dict], output_path: Path) -> None:
    """Génère une page HTML simple avec les articles."""
    items_html = ""
    for a in articles[:50]:
        date_str = a["published"][:10] if a["published"] else "—"
        lang_flag = "&#x1F1EB;&#x1F1F7;" if a["lang"] == "fr" else "&#x1F1EC;&#x1F1E7;"
        items_html += f"""\
    <article class="item">
      <div class="meta">
        <span class="source">{a['source']}</span>
        <span class="region">{a['region']}</span>
        <span class="lang">{lang_flag}</span>
        <time>{date_str}</time>
      </div>
      <h3><a href="{a['url']}" target="_blank" rel="noopener">{a['title']}</a></h3>
      <p>{a['summary']}</p>
    </article>
"""

    now = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
    html = f"""\
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kibaru — Actualites tech africaines</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #faf9f6; color: #0a0806; line-height: 1.6; }}
    header {{ background: #0a0806; color: #faf9f6; padding: 1.5rem 2rem; }}
    header h1 {{ font-size: 1.5rem; font-weight: 700; }}
    header .sub {{ font-size: 0.85rem; color: #ffa726; margin-top: 0.25rem; }}
    main {{ max-width: 800px; margin: 0 auto; padding: 2rem 1rem; }}
    .item {{ padding: 1rem 1rem; border-bottom: 1px solid #e5e0d8; transition: background 0.15s; }}
    .item:hover {{ background: #f2efea; }}
    .meta {{ font-size: 0.75rem; color: #5b5854; margin-bottom: 0.25rem; display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }}
    .source {{ font-weight: 600; color: #ffa726; }}
    .region {{ color: #8a8580; }}
    .item h3 {{ font-size: 1rem; font-weight: 600; margin-bottom: 0.25rem; }}
    .item h3 a {{ color: #0a0806; text-decoration: none; }}
    .item h3 a:hover {{ text-decoration: underline; color: #ffa726; }}
    .item p {{ font-size: 0.85rem; color: #5b5854; }}
    footer {{ text-align: center; padding: 2rem; font-size: 0.75rem; color: #8a8580; }}
    footer a {{ color: #ffa726; }}
  </style>
</head>
<body>
  <header>
    <h1>Kibaru</h1>
    <div class="sub">Actualites tech africaines — mis a jour le {now}</div>
  </header>
  <main>
{items_html}
  </main>
  <footer>
    {len(articles)} articles — Projet <a href="https://github.com/YTILIKAN/Kibaru">Kibaru</a> par <a href="https://ytilikan-site.vercel.app">Y'TILIKAN</a>
  </footer>
</body>
</html>
"""
    output_path.write_text(html, encoding="utf-8")


def run_pipeline() -> None:
    """Execute le pipeline complet."""
    print("Kibaru — scraping...")
    articles = fetch_all()
    print(f"  Total: {len(articles)} articles")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # JSON
    OUTPUT_JSON.write_text(
        json.dumps(articles, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    print(f"  JSON -> {OUTPUT_JSON}")

    # HTML
    generate_html(articles, OUTPUT_HTML)
    print(f"  HTML -> {OUTPUT_HTML}")
    print("Termine.")


if __name__ == "__main__":
    run_pipeline()
