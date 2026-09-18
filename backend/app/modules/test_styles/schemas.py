# ./backend/app/modules/test_styles/schemas.py
from pydantic import BaseModel, ConfigDict, Field, field_validator


class SendStylesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(default="", max_length=120)
    comment: str = Field(default="", max_length=3000)
    css: str = Field(min_length=100, max_length=60000)

    @field_validator("name", "comment", "css")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if any(
            ord(character) < 32
            and character not in "\n\r\t"
            for character in value
        ):
            raise ValueError("Недопустимые управляющие символы")

        return value.strip()

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if "\n" in value or "\r" in value:
            raise ValueError("Название должно быть одной строкой")

        return value


class SendStylesResponse(BaseModel):
    message: str