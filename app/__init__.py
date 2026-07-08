from flask import Flask

from app.controllers.anomaly_controller import anomaly_bp
from app.controllers.auth_controller import auth_bp
from app.controllers.machine_controller import machine_bp
from app.controllers.metric_controller import metric_bp
from app.controllers.sensor_controller import sensor_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(machine_bp, url_prefix="/api/v1")
    app.register_blueprint(sensor_bp, url_prefix="/api/v1")
    app.register_blueprint(metric_bp, url_prefix="/api/v1")
    app.register_blueprint(anomaly_bp, url_prefix="/api/v1")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
