from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    machine_id: Mapped[str] = mapped_column(ForeignKey("machines.id"), index=True)
    metric_key: Mapped[str] = mapped_column(String(80), index=True)
    unit: Mapped[str] = mapped_column(String(24))
    status: Mapped[str] = mapped_column(String(24), default="online")
    normal_min: Mapped[float]
    normal_max: Mapped[float]

    machine: Mapped["Machine"] = relationship(back_populates="sensors")
