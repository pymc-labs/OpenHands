"""Skill resource: versioned, addressable, attached to agents."""

from __future__ import annotations


class SkillResource:
    """Stub. See docs/managed-agents/SPEC.md §Skills."""


def create_skill(*args, **kwargs) -> SkillResource:
    raise NotImplementedError


def get_skill(skill_id: str, version: int | None = None) -> SkillResource:
    raise NotImplementedError


def list_skills() -> list[SkillResource]:
    raise NotImplementedError


def delete_skill(skill_id: str) -> None:
    raise NotImplementedError
