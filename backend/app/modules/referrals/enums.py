# ./backend/app/modules/referrals/enums.py
from enum import Enum


class ReferralSource(str, Enum):
    KVB_DOCTOR = "kvb_doctor"
    PSYCHIATRY_EXISTING = "psychiatry_existing"

    # Эти источники может установить ассистент постфактум.
    CHECKUP = "checkup"
    OTHER = "other"


class ReferralStatus(str, Enum):
    CREATED = "created"
    LINK_SENT = "link_sent"
    OPENED = "opened"
    REGISTERED = "registered"
    CANCELLED = "cancelled"