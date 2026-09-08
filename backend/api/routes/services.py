from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.service import Service
from backend.models.target import Target
from backend.schemas.service import ServiceCreate, ServiceResponse


router = APIRouter(
    prefix="/services",
    tags=["Services"],
)


@router.post("/", response_model=ServiceResponse)
def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
):
    target = db.get(Target, service.target_id)

    if not target:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    new_service = Service(
        name=service.name,
        port=service.port,
        protocol=service.protocol,
        target_id=service.target_id,
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service