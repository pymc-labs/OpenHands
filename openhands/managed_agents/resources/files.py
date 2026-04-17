"""File resource: independent of session lifecycle, mountable into environments."""

from __future__ import annotations


class FileResource:
    """Stub. See docs/managed-agents/SPEC.md §Files."""


def upload_file(*args, **kwargs) -> FileResource:
    raise NotImplementedError


def get_file(file_id: str) -> FileResource:
    raise NotImplementedError


def list_files() -> list[FileResource]:
    raise NotImplementedError


def delete_file(file_id: str) -> None:
    raise NotImplementedError
