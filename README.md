# Kibaru

**Agrégateur automatique d'actualités tech africaines.**

**[ytilikan.github.io/Kibaru](https://ytilikan.github.io/Kibaru/)** (live)

Kibaru scrape les actualités technologiques du continent africain depuis 4 sources (TechCabal, Techpoint Africa, WeeTracker, Agence Ecofin) et les affiche sur une page web légère. C'est le complément automatique d'[AfroTech-Pulse](https://github.com/YTILIKAN/AfroTech-Pulse) : AfroTech-Pulse apporte la curation éditoriale, Kibaru fournit le flux brut et exhaustif.

*Kibaru* = information / nouvelle en bambara.

## Mission

Centraliser l'information tech africaine dispersée sur des centaines de sources — blogs, journaux, réseaux sociaux, communiqués — et la rendre navigable en un seul endroit.

## Architecture

```
Kibaru/
├── src/
│   └── kibaru/
│       ├── __init__.py
│       ├── scraper.py        # RSS multi-sources (4 flux, normalisation)
│       ├── feeder.py         # Pipeline: scrape → JSON + HTML
│       └── api.py            # API REST FastAPI (à venir)
├── config/
│   └── sources.yaml          # Sources RSS
├── output/                   # Généré: feed.json + index.html
├── requirements.txt
└── README.md
```

## Stack

- **Scraping** : Python, feedparser
- **Sortie** : JSON + HTML statique autonome
- **Hébergement** : GitHub Pages (branche `gh-pages`)
- **À venir** : FastAPI, clustering, traduction, dashboard Next.js

## Sources cibles (phase 1)

- Médias tech africains (TechCabal, Disrupt Africa, Techpoint, WeeTracker)
- Blogs et newsletters tech francophones
- Communiqués de startups et incubateurs
- Réseaux sociaux (X/Twitter, LinkedIn) — comptes clés

## Démarrage rapide

```bash
git clone https://github.com/YTILIKAN/Kibaru.git
cd Kibaru
pip install feedparser

# Lancer le scraper (génère output/feed.json + output/index.html)
PYTHONPATH=src python3 -m kibaru.feeder
```

Le site live est déployé sur GitHub Pages depuis la branche `gh-pages`.

## Contribuer

Contributions bienvenues :
- Ajouter une nouvelle source africaine dans `config/sources.yaml`
- Améliorer les extracteurs de contenu
- Travailler sur le dashboard frontend
- Aider au clustering et à la déduplication

## Licence

MIT — voir [LICENSE](LICENSE).

---

Projet [Y'TILIKAN](https://ytilikan-site.vercel.app) — La tech et l'IA à la portée de l'Afrique francophone.
