# ./backend/app/modules/consents/enums.py
from enum import Enum


class ConsentType(str, Enum):
    PERSONAL_DATA_PROCESSING = (
        "personal_data_processing"
    )
    MEDICAL_DATA_PROCESSING = (
        "medical_data_processing"
    )
    ASSISTANT_CONTACT = "assistant_contact"

    # Зарезервировано, но пока не используется.
    ANALYTICS_PROCESSING = "analytics_processing"