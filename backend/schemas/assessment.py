from typing import Literal

from pydantic import BaseModel, ConfigDict

from backend.schemas.finding import FindingResponse


class AssessmentBase(BaseModel):
    name: str
    description: str | None = None
    status: Literal["planned", "in_progress", "completed", "cancelled"] = "planned"


class AssessmentCreate(AssessmentBase):
    target_id: int


class AssessmentResponse(AssessmentBase):
    id: int
    target_id: int
    risk_score: int = 0
    risk_level: str = "low"
    findings: list[FindingResponse] = []

    model_config = ConfigDict(from_attributes=True)