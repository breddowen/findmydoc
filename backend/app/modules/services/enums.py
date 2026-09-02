# backend\app\modules\services\enums.py

from enum import Enum


class ServiceCurrency(str, Enum):
    RUB = "RUB"
    UNIT = "UNIT"