"""Tool-confirmation gate: pauses Action execution until a user.tool_confirmation arrives."""

from __future__ import annotations


async def await_confirmation(session_id: str, action_id: str, timeout: float) -> bool:
    raise NotImplementedError
