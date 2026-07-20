"""API REST FastAPI pour Kibaru."""

from fastapi import FastAPI

app = FastAPI(title="Kibaru API", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Kibaru API — Agrégateur d'actualités tech africaines"}
