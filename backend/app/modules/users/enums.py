# ./backend/app/modules/users/enums.py
from enum import Enum


class UserRole(str, Enum):
    SUPERUSER = "superuser"
    PATIENT = "patient"
    DOCTOR = "doctor"
    RELATIVE = "relative"
    MED_ASSISTANT = "med_assistant"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class DoctorPatientStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    REJECTED = "rejected"
    DETACHED = "detached"


class RelativePatientStatus(str, Enum):
    ACTIVE = "active"
    DETACHED = "detached"