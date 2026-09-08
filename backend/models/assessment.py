from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.database import Base

if TYPE_CHECKING:
    from backend.models.target import Target
    from backend.models.finding import Finding


class Assessment(Base):
    __tablename__ = "assessments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="planned")
    target_id: Mapped[int] = mapped_column(ForeignKey("targets.id"), nullable=False)

    target: Mapped["Target"] = relationship(back_populates="assessments")
    findings: Mapped[list["Finding"]] = relationship(
    back_populates="assessment",
    cascade="all, delete-orphan",
)