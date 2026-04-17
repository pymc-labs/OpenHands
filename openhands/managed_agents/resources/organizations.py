"""Organization + membership + API-key scoping. All managed-agents resources are org-scoped."""

from __future__ import annotations


class OrganizationResource:
    """Stub. See docs/managed-agents/SPEC.md §Organizations."""


class ApiKey:
    """Stub."""


def create_organization(*args, **kwargs) -> OrganizationResource:
    raise NotImplementedError


def issue_api_key(org_id: str) -> ApiKey:
    raise NotImplementedError


def revoke_api_key(key_id: str) -> None:
    raise NotImplementedError
