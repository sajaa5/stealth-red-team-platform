from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.assessment import Assessment
from backend.schemas.assessment import AssessmentCreate
from backend.models.target import Target

router = APIRouter(prefix="/assessments", tags=["Assessments"])


@router.post("/")
def create_assessment(
   assessment: AssessmentCreate,
    db: Session = Depends(get_db),
):

    target = db.query(Target).filter(Target.id == assessment.target_id).first()

    if target is None:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )
    
    new_assessment = Assessment(**assessment.model_dump())

    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)

    return new_assessment


@router.get("/")
def get_assessments(
    db: Session = Depends(get_db),
):
    assessments = db.query(Assessment).all()

    severity_points = {
        "low": 1,
        "medium": 3,
        "high": 5,
        "critical": 10,
    }

   
    result = []

  
    for assessment in assessments:
        risk_score = sum(
            severity_points.get(finding.severity.lower(), 0)
            for finding in assessment.findings
        )
        if risk_score >= 10:
              risk_level = "critical"
        elif risk_score >= 6:
            risk_level = "high"
        elif risk_score >= 3:
            risk_level = "medium"
        else:
            risk_level = "low"

        result.append({
            "id": assessment.id,
            "name": assessment.name,
            "description": assessment.description,
            "status": assessment.status,
            "target_id": assessment.target_id,
            "risk_score": risk_score,
            "findings": assessment.findings,
            "risk_level": risk_level,
        })

    return result




@router.delete("/{assessment_id}")
def delete_assessment(
    assessment_id: int,
    db: Session = Depends(get_db),
):
    assessment = db.query(Assessment).filter(
        Assessment.id == assessment_id
    ).first()

    if assessment is None:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found",
        )

    db.delete(assessment)
    db.commit()

    return {
        "message": "Assessment deleted successfully"
    }