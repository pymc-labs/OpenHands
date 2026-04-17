"""Events: typed append-only log adapter over `openhands.events.EventStream`.

User event types: `user.message`, `user.interrupt`, `user.tool_confirmation`.
Agent/tool/status events are projected from EventStream Actions/Observations.
"""

from __future__ import annotations

from enum import StrEnum


class UserEventType(StrEnum):
    MESSAGE = "user.message"
    INTERRUPT = "user.interrupt"
    TOOL_CONFIRMATION = "user.tool_confirmation"


def send_events(session_id: str, events: list[dict]) -> None:
    raise NotImplementedError


def list_events(session_id: str, after: str | None = None) -> list[dict]:
    raise NotImplementedError


async def stream_events(session_id: str):
    """SSE generator yielding events from the underlying EventStream."""
    raise NotImplementedError
