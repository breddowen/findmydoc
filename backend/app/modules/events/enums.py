# ./backend/app/modules/events/enums.py
from enum import Enum


class EventType(str, Enum):
    REFERRAL_CREATED = "referral_created"
    LINK_SENT = "link_sent"
    LINK_OPENED = "link_opened"

    REGISTRATION_COMPLETED = "registration_completed"
    CONSENT_GIVEN = "consent_given"

    QUESTIONNAIRE_STARTED = "questionnaire_started"
    QUESTIONNAIRE_COMPLETED = "questionnaire_completed"
    ARTICLE_READ = "article_read"

    CONTACT_REQUESTED = "contact_requested"
    ASSISTANT_CALL_ATTEMPTED = "assistant_call_attempted"
    ASSISTANT_CONTACTED = "assistant_contacted"

    APPOINTMENT_BOOKED = "appointment_booked"
    APPOINTMENT_ATTENDED = "appointment_attended"

    PACKAGE_OFFERED = "package_offered"
    PAYMENT_LINK_SENT = "payment_link_sent"
    PACKAGE_PURCHASED = "package_purchased"
    REFUND_CREATED = "refund_created"

    PROGRAM_STARTED = "program_started"
    PROGRAM_COMPLETED = "program_completed"
    PROGRAM_IN_PROGRESS = "program_in_progress"