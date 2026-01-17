from fastapi import FastAPI
import asyncpg
import os
app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.connect(DATABASE_URL)
    await app.state.db.execute(
        "CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT)"
    )

@app.get("/items")
async def get_items():
    rows = await app.state.db.fetch("SELECT name FROM items")
    return {"items": [r["name"] for r in rows]}
