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
    EMAIL_BACKEND:  str = "console"

    SMTP_HOST: str = "smtp.beget.com"
    SMTP_PORT: int = 465
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_USE_SSL: bool = True
    SMTP_USE_STARTTLS: bool = False
    SMTP_TIMEOUT_SECONDS: int = 15

    EMAIL_FROM_ADDRESS: str = "noreply@findmydoc.ru"
    EMAIL_FROM_NAME: str = "FindMyDoc"

    # Локально: backend/media.
    # В Docker переопределяем абсолютным путём.
    MEDIA_ROOT: Path = APP_DIR.parent / "media"

    MEDIA_IMAGE_MAX_BYTES: int = 10 * 1024 * 1024

    # Ограничение исходника до декодирования пикселей.
    MEDIA_IMAGE_MAX_PIXELS: int = 24_000_000

    MEDIA_WEBP_QUALITY: int = 85

    # Несохранённая загрузка доступна для привязки
    # и предпросмотра в течение суток.
    MEDIA_UPLOAD_TTL_HOURS: int = 24

    # VIDEO
    MEDIA_VIDEO_MAX_BYTES: int = 350 * 1024 * 1024
    MEDIA_VIDEO_MAX_DURATION_SECONDS: float = 600.0

    # Ограничения независимо от ориентации.
    MEDIA_VIDEO_MAX_LONG_SIDE: int = 1920
    MEDIA_VIDEO_MAX_SHORT_SIDE: int = 1080
    MEDIA_VIDEO_MAX_FPS: float = 30.0

    MEDIA_VIDEO_FFPROBE_BIN: str = "ffprobe"
    MEDIA_VIDEO_FFMPEG_BIN: str = "ffmpeg"

    MEDIA_VIDEO_PROBE_TIMEOUT_SECONDS: float = 20.0

    # Запас свободного места, который не отдаём под видео.
    # Дополнительно проверяем место под максимально
    # разрешённый файл перед началом сохранения.
    MEDIA_VIDEO_MIN_FREE_BYTES: int = 1024 * 1024 * 1024

    # MEDIA PLAYBACK
    MEDIA_VIDEO_SESSION_SECONDS: int = 1800

    # Локально localhost работает по HTTP.
    # В production обязательно True.
    MEDIA_VIDEO_COOKIE_SECURE: bool = False

    # None: FastAPI отдаёт файл самостоятельно.
    # На сервере: /_private_video/
    MEDIA_VIDEO_X_ACCEL_PREFIX: str | None = None

    # Отвязанные файлы удаляются не немедленно.
    MEDIA_VIDEO_RETIRED_TTL_HOURS: int = 24

    MEDIA_VIDEO_POSTER_TIMEOUT_SECONDS: float = 20.0

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )




@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()