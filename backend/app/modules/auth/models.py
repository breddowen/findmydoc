# ./backend/app/modules/auth/models.py
import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ActionTokenType(str, Enum):
    EMAIL_VERIFICATION = "email_verification"
    PASSWORD_RESET = "password_reset"


class WebAuthnChallengeType(str, Enum):
    REGISTRATION = "registration"
    AUTHENTICATION = "authentication"


class ActionToken(SQLModel, table=True):
    __tablename__ = "action_tokens"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)

    token_hash: str = Field(unique=True, index=True, max_length=64)
    token_type: ActionTokenType = Field(index=True)

    expires_at: datetime = Field(index=True)
    consumed_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)


class PasskeyCredential(SQLModel, table=True):
    __tablename__ = "passkey_credentials"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)

    credential_id: str = Field(unique=True, index=True)
    public_key: bytes
    sign_count: int = Field(default=0)

    name: str = Field(default="Passkey", max_length=100)
    transports_json: Optional[str] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    last_used_at: Optional[datetime] = Field(default=None)


class WebAuthnChallenge(SQLModel, table=True):
    __tablename__ = "webauthn_challenges"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    challenge: str = Field(unique=True, index=True)
    challenge_type: WebAuthnChallengeType = Field(index=True)

    user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    expires_at: datetime = Field(index=True)
    consumed_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)