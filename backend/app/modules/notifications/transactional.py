# ./backend/app/modules/notifications/transactional.py
import logging
import uuid
from typing import Any

from sqlmodel import Session

from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.models import Notification
from app.modules.notifications.service import serialize_notification


logger = logging.getLogger(__name__)


def create_in_app_notification(
    *,
    session: Session,
    user_id: uuid.UUID,
    title: str,
    message: str,
    notification_type: NotificationType,
    action_url: str | None = None,
    payload: dict[str, Any] | None = None,
) -> Notification:
    """
    Только добавляет уведомление в текущую транзакцию.
    Не делает commit и не выполняет сетевую отправку.
    """
    notification = Notification(
        user_id=user_id,
        notification_type=notification_type,
        title=title.strip(),
        message=message.strip(),
        action_url=action_url,
        payload_json=payload or {},
        channels_json=[
            NotificationChannel.IN_APP.value,
            NotificationChannel.BROWSER.value,
        ],
    )

    session.add(notification)

    return notification


def snapshot_notifications(
    *,
    session: Session,
    notifications: list[Notification],
) -> list[dict[str, Any]]:
    """
    Подготовить данные до commit, пока ошибки сериализации
    ещё могут откатить всю операцию.
    """
    session.flush()

    return [
        serialize_notification(notification)
        for notification in notifications
    ]


async def publish_saved_notifications(
    snapshots: list[dict[str, Any]],
) -> None:
    """
    Вызывать только после успешного commit.

    Сбой WebSocket не отменяет уже сохранённую заявку
    и не превращает успешную операцию в ошибку API.
    """
    for snapshot in snapshots:
        try:
            await websocket_manager.send_to_user(
                user_id=uuid.UUID(snapshot["user_id"]),
                message={
                    "type": "notification",
                    "notification": snapshot,
                },
            )
        except Exception:
            logger.exception(
                "WebSocket delivery failed for notification %s",
                snapshot["id"],
            )