from flask import Blueprint, request

from app.services.metric_service import metric_service

metric_bp = Blueprint("metrics", __name__)


@metric_bp.post("/metrics/ingest")
async def ingest_metric():
    payload = request.get_json(silent=True) or {}
    result, status = await metric_service.ingest(payload)
    return result, status


@metric_bp.get("/sensors/<sensor_id>/metrics")
async def query_sensor_metrics(sensor_id):
    return await metric_service.query_sensor_metrics(sensor_id, request.args.get("bucket", "2m"))


@metric_bp.get("/query-lab")
async def query_lab():
    return await metric_service.query_lab()
