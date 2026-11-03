"""
Asynchronous Finite State Machine (FSM) Lifecycle Pipeline
Manages non-blocking state transitions for prospect leads and active client projects.
"""
from enum import Enum
from typing import Dict, Set

class LeadState(str, Enum):
    PENDING = "PENDING"
    PREVIEW_NEEDED = "PREVIEW_NEEDED"
    OUTREACH_SENT = "OUTREACH_SENT"
    CLIENT_REPLIED = "CLIENT_REPLIED"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"

VALID_TRANSITIONS: Dict[LeadState, Set[LeadState]] = {
    LeadState.PENDING: {LeadState.PREVIEW_NEEDED, LeadState.REJECTED},
    LeadState.PREVIEW_NEEDED: {LeadState.OUTREACH_SENT, LeadState.REJECTED},
    LeadState.OUTREACH_SENT: {LeadState.CLIENT_REPLIED, LeadState.REJECTED},
    LeadState.CLIENT_REPLIED: {LeadState.ACTIVE, LeadState.REJECTED},
    LeadState.ACTIVE: {LeadState.REJECTED},
    LeadState.REJECTED: {LeadState.PENDING}
}

class PipelineFSM:
    @staticmethod
    def can_transition(current: LeadState, target: LeadState) -> bool:
        return target in VALID_TRANSITIONS.get(current, set())

    @staticmethod
    def transition(lead_id: str, current: LeadState, target: LeadState) -> LeadState:
        if not PipelineFSM.can_transition(current, target):
            raise ValueError(f"Invalid state transition for lead {lead_id}: {current} -> {target}")
        return target
