from datetime import datetime, timezone
from typing import Any
from fastapi import APIRouter, Request

router = APIRouter(tags=["Root"])


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
