# ./backend/app/modules/programs/enums.py
from enum import Enum


class ProgramItemType(str, Enum):
    ARTICLE = "article"
    QUESTIONNAIRE = "questionnaire"
    CONSULTATION = "consultation"


class ProgramCurrency(str, Enum):
    RUB = "RUB"
    UNIT = "UNIT"


class ProgramEnrollmentStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ProgramStageStatus(str, Enum):
    UPCOMING = "upcoming"
    AVAILABLE = "available"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"