from datetime import datetime, timezone
from typing import Any
from fastapi import APIRouter, Request
from src.config.settings import settings


router = APIRouter(tags=["Root"])
api_key = settings.gemini_api_key


@router.get("/")
async def root(request: Request) -> dict[str, Any]:
    """ """
    client_info: dict[str, Any] = {
        "host": request.client.host if request.client else None,
        "port": request.client.port if request.client else None,
    }

    return {
        "message": "Welcome to Askademic API",
        "request": {
            "client": client_info,
            "headers": dict(request.headers.items()),
            "time": datetime.now(timezone.utc).isoformat(),
            "method": request.method,
        },
    }


@router.get("/ping")
async def ping() -> dict[str, str]:
    """
    Returns a simple pong response.
    """

    return {"message": "pong from Askademic"}


@router.get("/health")
async def health() -> dict[str, str]:
    """
    Returns a simple health status.
    """

    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/api-key")
def test_env() -> dict[str, str]:
    return {"api_key": str(api_key)}
