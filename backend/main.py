from fastapi import FastAPI
from backend.api.routes.health import router as health_router
from backend.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(health_router)