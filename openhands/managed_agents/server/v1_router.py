"""FastAPI router mounting the Claude-Managed-Agents-compatible `/v1/*` surface.

Endpoints are stubs; implementation tracked in docs/managed-agents/SPEC.md and
the scaffold tracking issue.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from openhands.managed_agents.server.auth import require_api_key

router = APIRouter(prefix="/v1", dependencies=[Depends(require_api_key)])


# --- Agents ---
@router.post("/agents")
async def create_agent(): raise HTTPException(501)

@router.get("/agents")
async def list_agents(): raise HTTPException(501)

@router.get("/agents/{agent_id}")
async def get_agent(agent_id: str): raise HTTPException(501)

@router.post("/agents/{agent_id}/versions")
async def create_agent_version(agent_id: str): raise HTTPException(501)

@router.delete("/agents/{agent_id}")
async def delete_agent(agent_id: str): raise HTTPException(501)


# --- Environments ---
@router.post("/environments")
async def create_environment(): raise HTTPException(501)

@router.get("/environments")
async def list_environments(): raise HTTPException(501)

@router.get("/environments/{environment_id}")
async def get_environment(environment_id: str): raise HTTPException(501)

@router.delete("/environments/{environment_id}")
async def delete_environment(environment_id: str): raise HTTPException(501)


# --- Sessions ---
@router.post("/sessions")
async def create_session(): raise HTTPException(501)

@router.get("/sessions")
async def list_sessions(): raise HTTPException(501)

@router.get("/sessions/{session_id}")
async def get_session(session_id: str): raise HTTPException(501)

@router.post("/sessions/{session_id}/archive")
async def archive_session(session_id: str): raise HTTPException(501)

@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str): raise HTTPException(501)


# --- Events ---
@router.post("/sessions/{session_id}/events")
async def send_events(session_id: str): raise HTTPException(501)

@router.get("/sessions/{session_id}/events")
async def list_events(session_id: str): raise HTTPException(501)

@router.get("/sessions/{session_id}/events/stream")
async def stream_events(session_id: str): raise HTTPException(501)


# --- Vaults / Skills / Files / Orgs ---
@router.post("/vaults")
async def create_vault(): raise HTTPException(501)

@router.post("/skills")
async def create_skill(): raise HTTPException(501)

@router.post("/files")
async def upload_file(): raise HTTPException(501)

@router.post("/organizations")
async def create_organization(): raise HTTPException(501)

@router.post("/organizations/{org_id}/api-keys")
async def issue_api_key(org_id: str): raise HTTPException(501)
