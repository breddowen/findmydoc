# backend\app\modules\services\models.py

import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    CheckConstraint,
    Column,
    Numeric,
    UniqueConstraint,
)
from sqlmodel import Field, Relationship, SQLModel

from app.modules.services.enums import ServiceCurrency
from app.modules.services.utils import (
    calculate_final_price,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class MedicalService(SQLModel, table=True):
    __tablename__ = "medical_services"
    __table_args__ = (
        UniqueConstraint(
            "code",
            name="uq_medical_service_code",
        ),
        CheckConstraint(
            (
                "price_amount IS NULL "
                "OR price_amount >= 0"
            ),
            name="ck_medical_service_price_non_negative",
        ),
        CheckConstraint(
            (
                "discount_percent >= 0 "
                "AND discount_percent <= 100"
            ),
            name="ck_medical_service_discount_range",
        ),
        CheckConstraint(
            (
                "("
                "price_amount IS NULL "
                "AND currency IS NULL "
                "AND discount_percent = 0"
                ") OR ("
                "price_amount IS NOT NULL "
                "AND currency IS NOT NULL"
                ")"
            ),
            name="ck_medical_service_pricing_consistency",
        ),
        CheckConstraint(
            (
                "price_amount IS NULL "
                "OR price_amount > 0 "
                "OR discount_percent = 0"
            ),
            name="ck_medical_service_free_discount",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    code: str = Field(
        index=True,
        max_length=50,
    )
    title: str = Field(
        index=True,
        max_length=300,
    )
    description: Optional[str] = Field(
        default=None,
    )

    # NULL означает «цена по запросу».
    price_amount: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(
            Numeric(12, 2),
            nullable=True,
        ),
    )
    currency: Optional[ServiceCurrency] = Field(
        default=None,
    )

    discount_percent: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    is_hidden: bool = Field(
        default=False,
        index=True,
    )
    hidden_at: Optional[datetime] = Field(
        default=None,
    )

    created_at: datetime = Field(
        default_factory=utc_now,
    )
    updated_at: datetime = Field(
        default_factory=utc_now,
    )

    programs: list["Program"] = Relationship(
        back_populates="service",
    )

    @property
    def final_price_amount(self) -> Decimal | None:
        # Итоговая цена не хранится в БД,
        # чтобы не рассинхронизироваться со скидкой.
        return calculate_final_price(
            price_amount=self.price_amount,
            discount_percent=self.discount_percent,
        )