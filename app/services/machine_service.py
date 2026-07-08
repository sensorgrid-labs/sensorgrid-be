from app.services.seed_data import MACHINES


class MachineService:
    async def list_machines(self):
        return MACHINES


machine_service = MachineService()
