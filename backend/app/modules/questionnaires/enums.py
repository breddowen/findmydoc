# ./backend/app/modules/questionnaires/enums.py
from enum import Enum


class QuestionType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"

    SCALE = "scale"
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"


class QuestionnaireSubmissionStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"