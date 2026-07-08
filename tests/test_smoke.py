from app import create_app


def test_machine_list_smoke():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/v1/machines")

    assert response.status_code == 200
    assert response.get_json()[0]["id"] == "m-press-01"


def test_metric_ingest_creates_anomaly():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/v1/metrics/ingest",
        json={"sensorId": "s-vib-press-01", "value": 9.9, "quality": "good"},
    )

    body = response.get_json()
    assert response.status_code == 202
    assert body["accepted"] is True
    assert body["anomalyEvent"]["status"] == "open"


def test_query_lab_documents_timescale_improvement():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/v1/query-lab")
    raw, optimized = response.get_json()

    assert response.status_code == 200
    assert raw["durationMs"] > optimized["durationMs"]
    assert "time_bucket" in " ".join(optimized["explain"])
