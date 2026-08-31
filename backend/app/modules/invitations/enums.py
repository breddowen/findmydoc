# ./backend/app/modules/invitations/enums.py
from enum import Enum


class InvitationType(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    RELATIVE = "relative"
    MED_ASSISTANT = "med_assistant"
    SUPERUSER = "superuser"


class InvitationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REVOKED = "revoked"
    EXPIRED = "expired"