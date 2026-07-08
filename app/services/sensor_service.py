from app.services.seed_data import SENSORS


class SensorService:
    async def list_sensors(self, machine_id=None):
        if machine_id:
            return [sensor for sensor in SENSORS if sensor["machineId"] == machine_id]
        return SENSORS


sensor_service = SensorService()
