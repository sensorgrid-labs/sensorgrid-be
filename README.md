# SensorGrid BE

설비/센서 registry, metric ingest, anomaly rule, query lab을 제공하는 Flask REST API입니다.

## 주요 기능

- 로그인/refresh 인증
- 설비 목록과 센서 조회
- metric ingest
- 센서 metric time-range 조회
- anomaly event/rule 조회와 생성/수정
- query lab 데이터 제공

## 기술 스택

- Flask
- MVC 구조: controllers, services, models, repositories
- SQLAlchemy 2.0 Async Mode 모델
- PostgreSQL/TimescaleDB schema intent
- seeded local data

## 실행

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

API:

```text
http://localhost:5002
```

## 검증

```bash
python -m compileall app tests
pytest
```

## API

- `POST /api/v1/auth/signin`
- `POST /api/v1/auth/refresh`
- `GET /api/v1/machines`
- `GET /api/v1/sensors`
- `POST /api/v1/metrics/ingest`
- `GET /api/v1/sensors/<id>/metrics`
- `GET /api/v1/anomaly-events`
- `GET /api/v1/anomaly-rules`
- `POST /api/v1/anomaly-rules`
- `PATCH /api/v1/anomaly-rules/<id>`
- `GET /api/v1/query-lab`

## 포트폴리오 포인트

Flask MVC와 SQLAlchemy async 모델로 제조 센서 데이터를 서비스 레이어별로 분리했습니다. 실제 DB 없이도 smoke test가 가능하도록 seeded data를 사용합니다.
