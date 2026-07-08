from flask import Blueprint, request

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/signin")
async def signin():
    payload = request.get_json(silent=True) or {}
    return {
        "accessToken": "demo-access-token",
        "refreshToken": "demo-refresh-token",
        "user": {"id": "u-demo", "email": payload.get("email", "operator@sensorgrid.local")},
    }


@auth_bp.post("/refresh")
async def refresh():
    return {"accessToken": "demo-access-token"}
