# ./backend/app/modules/assignments/enums.py
from enum import Enum


class AssignmentType(str, Enum):
    ARTICLE = "article"
    QUESTIONNAIRE = "questionnaire"


class AssignmentStatus(str, Enum):
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"