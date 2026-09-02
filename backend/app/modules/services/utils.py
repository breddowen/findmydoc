# backend\app\modules\services\utils.py
import re
from decimal import Decimal, ROUND_HALF_UP

from app.modules.services.enums import ServiceCurrency


SERVICE_CODE_PATTERN = re.compile(
    r"^[A-Z0-9_-]+$"
)


def normalize_service_code(value: str) -> str:
    normalized = value.strip().upper()

    if not normalized:
        raise ValueError(
            "Код услуги не может быть пустым"
        )

    if not SERVICE_CODE_PATTERN.fullmatch(normalized):
        raise ValueError(
            "Код услуги может содержать только "
            "латинские буквы, цифры, дефис "
            "и нижнее подчёркивание"
        )

    return normalized


def normalize_required_text(
    value: str,
    *,
    field_label: str,
) -> str:
    normalized = value.strip()

    if not normalized:
        raise ValueError(
            f"{field_label} не может быть пустым"
        )

    return normalized


def clean_optional_text(
    value: str | None,
) -> str | None:
    if value is None:
        return None

    normalized = value.strip()
    return normalized or None


def validate_service_pricing(
    *,
    price_amount: Decimal | None,
    currency: ServiceCurrency | None,
    discount_percent: int,
) -> None:
    """
    Проверяет согласованность цены, валюты и скидки.

    NULL-цена означает «цена по запросу».
    Нулевая цена означает бесплатную услугу.
    """
    if price_amount is None:
        if currency is not None:
            raise ValueError(
                "Валюта не может быть указана "
                "без стоимости"
            )

        if discount_percent != 0:
            raise ValueError(
                "Для услуги с ценой по запросу "
                "скидка должна быть равна 0"
            )

        return

    if price_amount < 0:
        raise ValueError(
            "Стоимость не может быть отрицательной"
        )

    if currency is None:
        raise ValueError(
            "Для стоимости необходимо указать валюту"
        )

    if price_amount == 0 and discount_percent != 0:
        raise ValueError(
            "Для бесплатной услуги "
            "скидка должна быть равна 0"
        )


def calculate_final_price(
    *,
    price_amount: Decimal | None,
    discount_percent: int,
) -> Decimal | None:
    if price_amount is None:
        return None

    multiplier = (
        Decimal(100 - discount_percent)
        / Decimal(100)
    )

    return (
        price_amount * multiplier
    ).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )