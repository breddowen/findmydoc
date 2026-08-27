# ./backend/app/modules/tags/enums.py
from enum import Enum


class DoctorTagOverrideAction(str, Enum):
    ADD = "add"
    REMOVE = "remove"