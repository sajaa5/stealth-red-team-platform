from pydantic import BaseModel, ConfigDict

from backend.schemas.service import ServiceResponse
from backend.schemas.assessment import AssessmentResponse


class TargetBase(BaseModel):
    name: str
    target_type: str
    value: str
    description: str | None = None


class TargetCreate(TargetBase):
    pass


class TargetResponse(TargetBase):
    id: int
    services: list[ServiceResponse] = []
    assessments: list[AssessmentResponse] = []

    model_config = ConfigDict(from_attributes=True)