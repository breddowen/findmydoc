# ./backend/app/modules/invitations/enums.py
from enum import Enum


class InvitationType(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    RELATIVE = "relative"


class InvitationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REVOKED = "revoked"
    EXPIRED = "expired"