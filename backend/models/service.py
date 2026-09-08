from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.database import Base
from backend.models.target import Target


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    port: Mapped[int | None] = mapped_column(nullable=True)
    protocol: Mapped[str | None] = mapped_column(String(20), nullable=True)
    target_id: Mapped[int] = mapped_column(ForeignKey("targets.id"), nullable=False)

    target: Mapped["Target"] = relationship(back_populates="services")