from fastapi import FastAPI

app = FastAPI(title="Sweep")


@app.get("/health")
def health():
    return {"status": "working"}