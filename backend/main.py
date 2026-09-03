
from fastapi import FastAPI

app = FastAPI(
    title="Stealth Red Team Evaluation Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Stealth Red Team Evaluation Platform",
        "status": "online"
    }