# ./backend/app/modules/notifications/enums.py
from enum import Enum


class NotificationChannel(str, Enum):
    IN_APP = "in_app"
    EMAIL = "email"
    BROWSER = "browser"


class NotificationType(str, Enum):
    GENERAL = "general"

    PATIENT_REGISTERED = "patient_registered"

    ARTICLE_ASSIGNED = "article_assigned"
    QUESTIONNAIRE_ASSIGNED = "questionnaire_assigned"

    QUESTIONNAIRE_COMPLETED = (
        "questionnaire_completed"
    )

    CONTACT_REQUESTED = "contact_requested"

    PROGRAM_PURCHASE_REQUESTED = (
        "program_purchase_requested"
    )
    PROGRAM_ACCESS_GRANTED = (
        "program_access_granted"
    )