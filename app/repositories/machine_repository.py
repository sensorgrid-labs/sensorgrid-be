from sqlalchemy import select

from app.db import async_session
from app.models.machine import Machine


class MachineRepository:
    async def list_machines(self):
        async with async_session() as session:
            result = await session.execute(select(Machine).order_by(Machine.line_code, Machine.name))
            return result.scalars().all()
