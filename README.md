# SensorGrid BE

Flask REST API for manufacturing sensor registry, metric ingest, anomaly rules, and query-lab evidence.

## Stack

- Flask REST controllers
- MVC-ish modules: `controllers`, `services`, `models`, `repositories`
- SQLAlchemy 2.0 async models for PostgreSQL/TimescaleDB schema shape
- Seeded service data so local smoke checks run without Postgres

## API

- `POST /api/v1/auth/signin`
- `POST /api/v1/auth/refresh`
- `GET /api/v1/machines`
- `GET /api/v1/sensors?machineId=`
- `POST /api/v1/metrics/ingest`
- `GET /api/v1/sensors/<id>/metrics?from=&to=&bucket=`
- `GET /api/v1/anomaly-events?status=`
- `GET /api/v1/anomaly-rules`
- `POST /api/v1/anomaly-rules`
- `PATCH /api/v1/anomaly-rules/<id>`
- `GET /api/v1/query-lab`

## Local

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m app.main
pytest
```

API runs on `http://localhost:5002`.

## TimescaleDB schema intent

`sensor_metrics` is modeled as the TSDB table:

```sql
SELECT create_hypertable('sensor_metrics', 'time');
CREATE INDEX idx_sensor_metrics_sensor_time ON sensor_metrics(sensor_id, time DESC);
```

`/api/v1/query-lab` exposes the portfolio comparison:

- raw PostgreSQL time-range scan over `200,000` points
- TimescaleDB `time_bucket` + sensor/time index plan

## Limitation

Persistence is scaffolded, not required for local verification. Services use seeded data until `DATABASE_URL` and migrations are wired.
