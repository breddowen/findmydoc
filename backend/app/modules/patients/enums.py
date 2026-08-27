# ./backend/app/modules/patients/enums.py
from enum import Enum


class PatientRegistrationStatus(str, Enum):
    REGISTERED = "registered"
    EMAIL_NOT_VERIFIED = "email_not_verified"