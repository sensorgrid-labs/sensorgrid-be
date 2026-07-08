from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class SensorMetric(Base):
    __tablename__ = "sensor_metrics"
    __table_args__ = (
        Index("idx_sensor_metrics_sensor_time", "sensor_id", "time"),
    )

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    sensor_id: Mapped[str] = mapped_column(ForeignKey("sensors.id"), primary_key=True)
    value: Mapped[float] = mapped_column(Float)
    quality: Mapped[str] = mapped_column(String(24), default="good")
