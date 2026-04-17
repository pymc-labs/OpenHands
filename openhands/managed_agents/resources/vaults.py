"""Vault resource: per-org OAuth credential store with automatic refresh.

Referenced at session creation via `vault_ids`; credentials are injected into
MCP server environments at sandbox boot.
"""

from __future__ import annotations


class VaultResource:
    """Stub. See docs/managed-agents/SPEC.md §Vaults."""


def create_vault(*args, **kwargs) -> VaultResource:
    raise NotImplementedError


def get_vault(vault_id: str) -> VaultResource:
    raise NotImplementedError


def list_vaults() -> list[VaultResource]:
    raise NotImplementedError


def delete_vault(vault_id: str) -> None:
    raise NotImplementedError
