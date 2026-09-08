from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.database import Base

if TYPE_CHECKING:
    from backend.models.service import Service
    from backend.models.assessment import Assessment


class Target(Base):
    __tablename__ = "targets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    target_type: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)

    services: Mapped[list["Service"]] = relationship(
        back_populates="target",
        cascade="all, delete-orphan",
    )

    assessments: Mapped[list["Assessment"]] = relationship(
    back_populates="target",
    cascade="all, delete-orphan",
)