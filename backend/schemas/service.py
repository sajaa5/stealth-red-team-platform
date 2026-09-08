from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ServiceBase(BaseModel):
    name: str
    port: int | None = Field(default=None, ge=1, le=65535)
    protocol: Literal["TCP", "UDP", "ICMP"] | None = None


class ServiceCreate(ServiceBase):
    target_id: int


class ServiceResponse(ServiceBase):
    id: int
    target_id: int

    model_config = ConfigDict(from_attributes=True)