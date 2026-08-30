# ./backend/app/core/email.py

import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr

from app.core.config import settings


def build_action_url(
    *,
    action_path: str | None,
    token: str | None,
    action_url: str | None,
) -> str | None:
    if action_url:
        return action_url

    if not action_path:
        return None

    frontend_url = settings.FRONTEND_URL.rstrip("/")
    path = action_path if action_path.startswith("/") else f"/{action_path}"

    result = f"{frontend_url}{path}"

    if token:
        separator = "&" if "?" in result else "?"
        result = f"{result}{separator}token={token}"

    return result


def build_email_body(
    *,
    message: str,
    action_url: str | None,
) -> str:
    parts = [message.strip()]

    if action_url:
        parts.extend([
            "",
            action_url,
        ])

    parts.extend([
        "",
        "Если вы не выполняли это действие, проигнорируйте письмо.",
    ])

    return "\n".join(parts)


def send_console_email(
    *,
    recipient: str,
    subject: str,
    message: str,
    action_path: str | None = None,
    token: str | None = None,
    action_url: str | None = None,
) -> None:
    resolved_action_url = build_action_url(
        action_path=action_path,
        token=token,
        action_url=action_url,
    )

    body = build_email_body(
        message=message,
        action_url=resolved_action_url,
    )

    email_backend = settings.EMAIL_BACKEND.strip().lower()

    if email_backend == "console":
        print()
        print("=" * 80)
        print("EMAIL")
        print(f"Backend: {settings.EMAIL_BACKEND}")
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print()
        print(body)
        print("=" * 80)
        print()
        return

    if email_backend != "smtp":
        raise RuntimeError(
            f"Неизвестный EMAIL_BACKEND: {settings.EMAIL_BACKEND}"
        )

    # if settings.EMAIL_BACKEND.lower() != "smtp":
    #     raise RuntimeError(
    #         f"Неизвестный EMAIL_BACKEND: {settings.EMAIL_BACKEND}"
    #     )

    if not settings.SMTP_USERNAME:
        raise RuntimeError("SMTP_USERNAME не настроен")

    if not settings.SMTP_PASSWORD:
        raise RuntimeError("SMTP_PASSWORD не настроен")

    email = EmailMessage()
    email["From"] = formataddr(
        (
            settings.EMAIL_FROM_NAME,
            settings.EMAIL_FROM_ADDRESS,
        )
    )
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(body)

    ssl_context = ssl.create_default_context()

    if settings.SMTP_USE_SSL:
        with smtplib.SMTP_SSL(
            host=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            timeout=settings.SMTP_TIMEOUT_SECONDS,
            context=ssl_context,
        ) as smtp:
            smtp.login(
                settings.SMTP_USERNAME,
                settings.SMTP_PASSWORD,
            )
            smtp.send_message(email)

        return

    with smtplib.SMTP(
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        timeout=settings.SMTP_TIMEOUT_SECONDS,
    ) as smtp:
        smtp.ehlo()

        if settings.SMTP_USE_STARTTLS:
            smtp.starttls(context=ssl_context)
            smtp.ehlo()

        smtp.login(
            settings.SMTP_USERNAME,
            settings.SMTP_PASSWORD,
        )
        smtp.send_message(email)
