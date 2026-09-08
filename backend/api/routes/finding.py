from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.finding import Finding
from backend.schemas.finding import FindingCreate, FindingResponse


router = APIRouter(prefix="/findings", tags=["Findings"])


@router.post("/", response_model=FindingResponse)
def create_finding(finding: FindingCreate, db: Session = Depends(get_db)):
    new_finding = Finding(**finding.model_dump())

    db.add(new_finding)
    db.commit()
    db.refresh(new_finding)

    return new_finding


@router.get("/", response_model=list[FindingResponse])
def get_findings(db: Session = Depends(get_db)):
    return db.query(Finding).all()