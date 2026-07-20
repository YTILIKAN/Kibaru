# Kibaru

**Agrégateur automatique d'actualités tech africaines.**

Kibaru scrape, traduit et clusterise les actualités technologiques du continent africain. C'est le complément automatique d'[AfroTech-Pulse](https://github.com/YTILIKAN/AfroTech-Pulse) : AfroTech-Pulse apporte la curation éditoriale, Kibaru fournit le flux brut et exhaustif.

*Kibaru* = information / nouvelle en bambara.

## Mission

Centraliser l'information tech africaine dispersée sur des centaines de sources — blogs, journaux, réseaux sociaux, communiqués — et la rendre navigable en un seul endroit.

## Architecture

```
Kibaru/
├── src/
│   ├── kibaru/
│   │   ├── __init__.py
│   │   ├── scraper.py        # Scraping multi-sources
│   │   ├── clusterer.py      # Clustering par thème (TF-IDF + embeddings)
│   │   ├── translator.py     # Traduction automatique (via Tondo/NLLB)
│   │   ├── feeder.py         # Pipeline principal (scrape → cluster → stocke)
│   │   └── api.py            # API REST FastAPI
│   └── dashboard/            # Frontend Next.js
├── config/
│   └── sources.yaml          # Liste des sources à scraper
├── tests/
├── requirements.txt
└── README.md
```

## Stack

- **Backend** : Python, FastAPI, PostgreSQL
- **Scraping** : httpx + BeautifulSoup / Playwright
- **NLP** : sentence-transformers (clustering), NLLB (traduction)
- **Frontend** : Next.js (dashboard filtrable)
- **Orchestration** : cron / GitHub Actions

## Sources cibles (phase 1)

- Médias tech africains (TechCabal, Disrupt Africa, Techpoint, WeeTracker)
- Blogs et newsletters tech francophones
- Communiqués de startups et incubateurs
- Réseaux sociaux (X/Twitter, LinkedIn) — comptes clés

## Démarrage rapide

```bash
git clone https://github.com/YTILIKAN/Kibaru.git
cd Kibaru
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Lancer un scrape de test
python -m kibaru.feeder --dry-run
```

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
