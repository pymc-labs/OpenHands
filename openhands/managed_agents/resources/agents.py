"""Agent resource: versioned `{model, system_prompt, tools, mcp_servers, skills}` bundle."""

from __future__ import annotations


class AgentResource:
    """Stub. See docs/managed-agents/SPEC.md §Agents."""


def create_agent(*args, **kwargs) -> AgentResource:
    raise NotImplementedError


def get_agent(agent_id: str, version: int | None = None) -> AgentResource:
    raise NotImplementedError


def list_agents() -> list[AgentResource]:
    raise NotImplementedError


def update_agent(agent_id: str, *args, **kwargs) -> AgentResource:
    raise NotImplementedError


def delete_agent(agent_id: str) -> None:
    raise NotImplementedError
