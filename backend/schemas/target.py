from pydantic import BaseModel, ConfigDict


class TargetBase(BaseModel):
    name: str
    target_type: str
    value: str
    description: str | None = None


class TargetCreate(TargetBase):
    pass


class TargetResponse(TargetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)