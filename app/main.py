from fastapi import FastAPI

from app.db import Base, engine
from app import models

Base.metadata.create_all(engine)

app = FastAPI(title="Sweep")


@app.get("/health")
def health():
    return {"status": "ok"}