# backend\app\modules\services\schemas.py

import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from app.modules.services.enums import ServiceCurrency
from app.modules.services.utils import (
    normalize_required_text,
    normalize_service_code,
    validate_service_pricing,
)


class MedicalServiceCreateRequest(BaseModel):
    code: str = Field(
        min_length=1,
        max_length=50,
    )
    title: str = Field(
        min_length=1,
        max_length=300,
    )
    description: str | None = None

    price_amount: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=12,
        decimal_places=2,
    )
    currency: ServiceCurrency | None = None

    discount_percent: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    @field_validator("code")
    @classmethod
    def validate_code(cls, value: str) -> str:
        return normalize_service_code(value)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        return normalize_required_text(
            value,
            field_label="Название услуги",
        )

    @model_validator(mode="after")
    def validate_pricing(self):
        validate_service_pricing(
            price_amount=self.price_amount,
            currency=self.currency,
            discount_percent=self.discount_percent,
        )
        return self


class MedicalServiceUpdateRequest(BaseModel):
    code: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )
    description: str | None = None

    price_amount: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=12,
        decimal_places=2,
    )
    currency: ServiceCurrency | None = None

    discount_percent: int | None = Field(
        default=None,
        ge=0,
        le=100,
    )

    @field_validator("code")
    @classmethod
    def validate_code(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        return normalize_service_code(value)

    @field_validator("title")
    @classmethod
    def validate_title(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        return normalize_required_text(
            value,
            field_label="Название услуги",
        )


class MedicalServiceVisibilityRequest(BaseModel):
    is_hidden: bool


class MedicalServicePatientResponse(BaseModel):
    """
    Представление услуги для пациента.

    Технический код и служебные поля намеренно
    не возвращаются.
    """

    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str | None

    price_amount: Decimal | None
    currency: ServiceCurrency | None
    discount_percent: int
    final_price_amount: Decimal | None


class MedicalServiceStaffResponse(
    MedicalServicePatientResponse
):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    code: str

    is_hidden: bool
    hidden_at: datetime | None

    created_at: datetime
    updated_at: datetime