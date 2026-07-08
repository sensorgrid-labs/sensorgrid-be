from copy import deepcopy
from datetime import datetime, timezone
from uuid import uuid4

from app.services.seed_data import ANOMALY_EVENTS, RULES


class AnomalyService:
    async def list_events(self, status=None):
        if status:
            return [event for event in ANOMALY_EVENTS if event["status"] == status]
        return ANOMALY_EVENTS

    async def list_rules(self):
        return RULES

    async def create_rule(self, payload):
        rule = {
            "id": "r-" + uuid4().hex[:8],
            "sensorId": payload["sensorId"],
            "metricKey": payload.get("metricKey", "unknown"),
            "operator": payload["operator"],
            "threshold": float(payload["threshold"]),
            "windowSec": int(payload.get("windowSec", 60)),
            "enabled": bool(payload.get("enabled", True)),
            "updatedAt": datetime.now(timezone.utc).isoformat(),
        }
        RULES.append(rule)
        return rule

    async def update_rule(self, rule_id, payload):
        for rule in RULES:
            if rule["id"] == rule_id:
                before = deepcopy(rule)
                rule.update(payload)
                rule["updatedAt"] = datetime.now(timezone.utc).isoformat()
                return {"before": before, "after": rule}
        return None

    async def evaluate_metric(self, sensor_id, value):
        for rule in RULES:
            if rule["sensorId"] != sensor_id or not rule["enabled"]:
                continue
            breached = value > rule["threshold"] if rule["operator"] == "gt" else value < rule["threshold"]
            if breached:
                event = {
                    "id": "a-" + uuid4().hex[:8],
                    "sensorId": sensor_id,
                    "machineName": "unknown",
                    "startedAt": datetime.now(timezone.utc).isoformat(),
                    "endedAt": None,
                    "maxValue": value,
                    "status": "open",
                }
                ANOMALY_EVENTS.append(event)
                return event
        return None


anomaly_service = AnomalyService()
