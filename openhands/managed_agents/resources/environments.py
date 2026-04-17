"""Environment resource: container template `{base_image, packages, network_rules, mounted_files}`."""

from __future__ import annotations


class EnvironmentResource:
    """Stub. See docs/managed-agents/SPEC.md §Environments."""


def create_environment(*args, **kwargs) -> EnvironmentResource:
    raise NotImplementedError


def get_environment(environment_id: str) -> EnvironmentResource:
    raise NotImplementedError


def list_environments() -> list[EnvironmentResource]:
    raise NotImplementedError


def delete_environment(environment_id: str) -> None:
    raise NotImplementedError
