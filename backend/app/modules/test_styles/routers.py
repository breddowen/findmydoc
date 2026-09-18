# ./backend/app/modules/test_styles/routers.py
import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.config import settings
from app.core.email import send_console_email
from app.core.security import AuthContext, require_roles
from app.modules.test_styles.schemas import (
    SendStylesRequest,
    SendStylesResponse,
)
from app.modules.users.enums import UserRole


logger = logging.getLogger(__name__)

DEVELOPER_EMAIL = "maxim-titkov@yandex.ru"

router = APIRouter(
    prefix="/api/v1/test-styles",
    tags=["Temporary: style studio"],
)


@router.post(
    "/send",
    response_model=SendStylesResponse,
)
def send_styles(
    data: SendStylesRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
) -> SendStylesResponse:
    if settings.EMAIL_BACKEND.strip().lower() != "smtp":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Отправка почты недоступна: "
                "на сервере не включён SMTP"
            ),
        )

    message = "\n".join([
        "Вариант оформления из студии стилей.",
        "",
        f"Название: {data.name or 'Не указано'}",
        "",
        "Комментарий:",
        data.comment or "Не указан",
        "",
        "Готовое содержимое frontend/app/assets/css/main.css:",
        "",
        "========== НАЧАЛО MAIN.CSS ==========",
        data.css,
        "========== КОНЕЦ MAIN.CSS ==========",
    ])

    try:
        send_console_email(
            recipient=DEVELOPER_EMAIL,
            subject="MentalConnect — вариант оформления",
            message=message,
        )
    except Exception as error:
        logger.exception("Failed to send style studio email")

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                "Не удалось отправить письмо. "
                "Попробуйте позже или скачайте main.css."
            ),
        ) from error

    return SendStylesResponse(
        message="Письмо передано почтовому серверу",
    )