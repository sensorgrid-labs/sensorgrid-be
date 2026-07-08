from flask import Blueprint

from app.services.machine_service import machine_service

machine_bp = Blueprint("machines", __name__)


@machine_bp.get("/machines")
async def list_machines():
    return await machine_service.list_machines()
