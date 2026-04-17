"""Session resource: running agent instance. Status: idle | running | rescheduling | terminated."""

from __future__ import annotations

from enum import StrEnum


class SessionStatus(StrEnum):
    IDLE = "idle"
    RUNNING = "running"
    RESCHEDULING = "rescheduling"
    TERMINATED = "terminated"


class SessionResource:
    """Stub wrapper over `openhands.server.session.Session` / `ConversationManager`.

    See docs/managed-agents/SPEC.md §Sessions.
    """


def create_session(agent_id: str, environment_id: str, vault_ids: list[str] | None = None) -> SessionResource:
    raise NotImplementedError


def get_session(session_id: str) -> SessionResource:
    raise NotImplementedError


def list_sessions() -> list[SessionResource]:
    raise NotImplementedError


def archive_session(session_id: str) -> None:
    raise NotImplementedError


def delete_session(session_id: str) -> None:
    raise NotImplementedError
