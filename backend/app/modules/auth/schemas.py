# ./backend/app/modules/auth/schemas.py
import uuid
from typing import Any, Literal

from pydantic import BaseModel, EmailStr, Field

from app.modules.users.enums import UserRole
from app.modules.users.schemas import RoleResponse


class PasswordLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class RoleSelectionRequiredResponse(BaseModel):
    status: Literal["role_selection_required"]
    role_selection_token: str
    roles: list[RoleResponse]


class TokenResponse(BaseModel):
    status: Literal["authenticated"] = "authenticated"
    access_token: str
    token_type: Literal["bearer"] = "bearer"
    active_role: UserRole


class LoginResponse(BaseModel):
    status: Literal["authenticated", "role_selection_required"]
    access_token: str | None = None
    token_type: Literal["bearer"] | None = None
    active_role: UserRole | None = None

    role_selection_token: str | None = None
    roles: list[RoleResponse] = []


class SelectRoleRequest(BaseModel):
    role_selection_token: str
    role: UserRole


class PasswordChangeRequest(BaseModel):
    current_password: str = Field(min_length=1, max_length=128)
    new_password: str = Field(min_length=8, max_length=128)
    new_password_confirmation: str = Field(min_length=8, max_length=128)


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8, max_length=128)
    new_password_confirmation: str = Field(min_length=8, max_length=128)


class EmailVerificationConfirmRequest(BaseModel):
    token: str


class MessageResponse(BaseModel):
    message: str


class PasskeyRegistrationOptionsRequest(BaseModel):
    name: str = Field(default="Passkey", min_length=1, max_length=100)


class PasskeyRegistrationOptionsResponse(BaseModel):
    challenge_id: uuid.UUID
    options: dict[str, Any]


class PasskeyRegistrationVerifyRequest(BaseModel):
    challenge_id: uuid.UUID
    name: str = Field(default="Passkey", min_length=1, max_length=100)
    credential: dict[str, Any]


class PasskeyAuthenticationOptionsResponse(BaseModel):
    challenge_id: uuid.UUID
    options: dict[str, Any]


class PasskeyAuthenticationVerifyRequest(BaseModel):
    challenge_id: uuid.UUID
    credential: dict[str, Any]


class PasskeyResponse(BaseModel):
    id: uuid.UUID
    name: str
    created_at: str
    last_used_at: str | None