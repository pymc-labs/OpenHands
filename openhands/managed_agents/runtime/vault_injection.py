"""At sandbox boot, resolve vault_ids and inject credentials into MCP server env."""

from __future__ import annotations


def inject_vault_credentials(session_id: str, vault_ids: list[str]) -> dict[str, str]:
    raise NotImplementedError
