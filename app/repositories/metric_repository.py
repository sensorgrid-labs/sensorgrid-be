from sqlalchemy import select

from app.db import async_session
from app.models.metric import SensorMetric


class MetricRepository:
    async def list_sensor_metrics(self, sensor_id, start_at, end_at):
        async with async_session() as session:
            result = await session.execute(
                select(SensorMetric)
                .where(SensorMetric.sensor_id == sensor_id)
                .where(SensorMetric.time >= start_at)
                .where(SensorMetric.time <= end_at)
                .order_by(SensorMetric.time)
            )
            return result.scalars().all()
