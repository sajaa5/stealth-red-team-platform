from fastapi import FastAPI
from backend.api.routes.health import router as health_router

app = FastAPI(
    title="Stealth Red Team Evaluation Platform",
    version="0.1.0",
)

app.include_router(health_router)