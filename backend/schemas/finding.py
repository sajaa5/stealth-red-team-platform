from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class FindingBase(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    description: str | None = Field(default=None, max_length=1000)
    severity: Literal["low", "medium", "high", "critical"] = "low"
    status: Literal["open", "in_progress", "resolved", "closed"] = "open"


class FindingCreate(FindingBase):
    assessment_id: int


class FindingResponse(FindingBase):
    id: int
    assessment_id: int

    model_config = ConfigDict(from_attributes=True)