from flask import Blueprint, request

from app.services.sensor_service import sensor_service

sensor_bp = Blueprint("sensors", __name__)


@sensor_bp.get("/sensors")
async def list_sensors():
    return await sensor_service.list_sensors(request.args.get("machineId"))
