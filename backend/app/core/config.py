# ./backend/app/core/config.py
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


APP_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = APP_DIR / ".env"


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test_database.db"

    SECRET_KEY: str = "your-super-secret-key-change-in-production-123456789"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    ROLE_SELECTION_TOKEN_EXPIRE_MINUTES: int = 5
    ACTION_TOKEN_EXPIRE_MINUTES: int = 60
    INVITATION_EXPIRE_HOURS: int = 72

    FRONTEND_URL: str = "http://localhost:3000"

    WEBAUTHN_RP_ID: str = "localhost"
    WEBAUTHN_RP_NAME: str = "MentalMe"
    WEBAUTHN_ORIGIN: str = "http://localhost:3000"
    WEBAUTHN_CHALLENGE_EXPIRE_SECONDS: int = 300


    # EMAIL
    EMAIL_BACKEND: str = "console"

    SMTP_HOST: str = "smtp.beget.com"
    SMTP_PORT: int = 465
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_USE_SSL: bool = True
    SMTP_USE_STARTTLS: bool = False
    SMTP_TIMEOUT_SECONDS: int = 15

    EMAIL_FROM_ADDRESS: str = "noreply@findmydoc.ru"
    EMAIL_FROM_NAME: str = "FindMyDoc"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )




@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()