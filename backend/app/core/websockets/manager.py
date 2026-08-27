# ./backend/app/core/websockets/manager.py
import uuid
from collections import defaultdict

from fastapi import WebSocket


class WebSocketConnectionManager:
    def __init__(self) -> None:
        self._connections: dict[
            uuid.UUID,
            set[WebSocket],
        ] = defaultdict(set)

    async def connect(
        self,
        *,
        user_id: uuid.UUID,
        websocket: WebSocket,
    ) -> None:
        self._connections[user_id].add(websocket)

    def disconnect(
        self,
        *,
        user_id: uuid.UUID,
        websocket: WebSocket,
    ) -> None:
        connections = self._connections.get(user_id)

        if not connections:
            return

        connections.discard(websocket)

        if not connections:
            self._connections.pop(user_id, None)

    async def send_to_user(
        self,
        *,
        user_id: uuid.UUID,
        message: dict,
    ) -> None:
        connections = list(
            self._connections.get(user_id, set())
        )

        disconnected: list[WebSocket] = []

        for websocket in connections:
            try:
                await websocket.send_json(message)
            except Exception:
                disconnected.append(websocket)

        for websocket in disconnected:
            self.disconnect(
                user_id=user_id,
                websocket=websocket,
            )

    def get_connections_count(
        self,
        user_id: uuid.UUID,
    ) -> int:
        return len(
            self._connections.get(user_id, set())
        )


websocket_manager = WebSocketConnectionManager()