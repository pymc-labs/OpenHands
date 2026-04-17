"""Bearer API-key auth + per-org scoping. Stub."""

from __future__ import annotations

from fastapi import Header, HTTPException


async def require_api_key(authorization: str | None = Header(default=None)) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "missing bearer token")
    raise HTTPException(501, "api-key validation not implemented")
