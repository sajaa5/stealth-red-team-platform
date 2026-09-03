from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.target import Target
from backend.schemas.target import TargetCreate, TargetResponse


router = APIRouter(prefix="/targets", tags=["Targets"])


@router.post("/", response_model=TargetResponse)
def create_target(target: TargetCreate, db: Session = Depends(get_db)):
    new_target = Target(**target.model_dump())

    db.add(new_target)
    db.commit()
    db.refresh(new_target)

    return new_target


@router.get("/", response_model=list[TargetResponse])
def get_targets(db: Session = Depends(get_db)):
    return db.query(Target).all()

@router.get("/{target_id}", response_model=TargetResponse)
def get_target(target_id: int, db: Session = Depends(get_db)):
    return db.query(Target).filter(Target.id == target_id).first()

@router.delete("/{target_id}")
def delete_target(target_id: int, db: Session = Depends(get_db)):
    target = db.query(Target).filter(Target.id == target_id).first()

    if target is None:
        return {"message": "Target not found"}

    db.delete(target)
    db.commit()

    return {"message": "Target deleted successfully"}