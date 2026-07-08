import math
from datetime import datetime, timezone

from app.services.anomaly_service import anomaly_service
from app.services.seed_data import SENSORS


class MetricService:
    async def ingest(self, payload):
        sensor_id = payload["sensorId"]
        value = float(payload["value"])
        sensor = next((item for item in SENSORS if item["id"] == sensor_id), None)
        if sensor is None:
            return {"error": "unknown sensor"}, 404

        sensor["latestValue"] = value
        sensor["quality"] = payload.get("quality", "good")
        event = await anomaly_service.evaluate_metric(sensor_id, value)
        return {
            "accepted": True,
            "sensorId": sensor_id,
            "time": payload.get("time") or datetime.now(timezone.utc).isoformat(),
            "anomalyEvent": event,
        }, 202

    async def query_sensor_metrics(self, sensor_id, bucket="2m"):
        sensor = next((item for item in SENSORS if item["id"] == sensor_id), None)
        if sensor is None:
            return []

        return [
            {
                "time": "09:" + str(index * 2).zfill(2),
                "value": round(sensor["latestValue"] - 1.2 + math.sin(index / 3) * 0.9, 2),
                "quality": "late" if index % 13 == 0 else "good",
            }
            for index in range(36)
        ]

    async def query_lab(self):
        return [
            {
                "mode": "raw_scan",
                "rows": 200000,
                "durationMs": 1284,
                "indexPlan": "Seq Scan on sensor_metrics",
                "explain": ["Filter: sensor_id + time range", "Rows removed by filter: 184,392", "No bucket aggregation"],
            },
            {
                "mode": "timescale_bucket",
                "rows": 1440,
                "durationMs": 86,
                "indexPlan": "Index Scan using idx_sensor_metrics_sensor_time",
                "explain": ["time_bucket('1 minute', time)", "Hypertable chunk pruning", "Partial aggregate by sensor_id"],
            },
        ]


metric_service = MetricService()
