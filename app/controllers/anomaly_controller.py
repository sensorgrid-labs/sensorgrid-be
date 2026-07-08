from flask import Blueprint, request

from app.services.anomaly_service import anomaly_service

anomaly_bp = Blueprint("anomalies", __name__)


@anomaly_bp.get("/anomaly-events")
async def list_events():
    return await anomaly_service.list_events(request.args.get("status"))


@anomaly_bp.get("/anomaly-rules")
async def list_rules():
    return await anomaly_service.list_rules()


@anomaly_bp.post("/anomaly-rules")
async def create_rule():
    payload = request.get_json(silent=True) or {}
    return await anomaly_service.create_rule(payload), 201


@anomaly_bp.patch("/anomaly-rules/<rule_id>")
async def update_rule(rule_id):
    payload = request.get_json(silent=True) or {}
    result = await anomaly_service.update_rule(rule_id, payload)
    if result is None:
        return {"error": "rule not found"}, 404
    return result
