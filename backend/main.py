from fastapi import FastAPI

from backend.api.routes.health import router as health_router
from backend.api.routes.targets import router as targets_router
from backend.api.routes.services import router as services_router
from backend.api.routes.assessments import router as assessments_router
from backend.api.routes.finding import router as finding_router
from backend.api.routes.auth import router as auth_router
from backend.core.config import settings
from backend.core.database import Base, engine
from backend.models.target import Target
from backend.models.service import Service
from backend.models.assessment import Assessment
from backend.models.finding import Finding
from backend.models.user import User

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(health_router)
app.include_router(targets_router)
app.include_router(services_router)
app.include_router(assessments_router)
app.include_router(finding_router)
app.include_router(auth_router)