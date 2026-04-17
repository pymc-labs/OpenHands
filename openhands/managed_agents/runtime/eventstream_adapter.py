"""Maps MA event types <-> OpenHands EventStream Actions/Observations.

- user.message        -> MessageAction
- user.interrupt      -> ChangeAgentStateAction(STOPPED) or equivalent
- user.tool_confirmation -> unblocks pending gated Action
"""

from __future__ import annotations


def ma_event_to_openhands_action(event: dict):
    raise NotImplementedError


def openhands_event_to_ma_event(event) -> dict:
    raise NotImplementedError
