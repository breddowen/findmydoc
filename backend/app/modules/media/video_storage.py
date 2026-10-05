# ./backend/app/modules/media/video_storage.py

import os
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import BinaryIO

from app.core.config import settings
from app.modules.media.storage import media_root
from app.modules.media.video_container import (
    VideoValidationError,
)
from app.modules.media.video_processing import (
    VideoMetadata,
    inspect_video,
)


COPY_CHUNK_BYTES = 1024 * 1024


class VideoStorageCapacityError(OSError):
    """Недостаточно свободного места."""


@dataclass(frozen=True)
class StoredVideo:
    id: uuid.UUID
    metadata: VideoMetadata


def video_path(file_id: uuid.UUID) -> Path:
    identifier = file_id.hex

    return (
        media_root()
        / "videos"
        / identifier[:2]
        / f"{identifier}.mp4"
    )


def automatic_video_poster_path(
    file_id: uuid.UUID,
) -> Path:
    identifier = file_id.hex

    return (
        media_root()
        / "video-posters"
        / identifier[:2]
        / f"{identifier}.webp"
    )


def incoming_video_directory() -> Path:
    directory = media_root() / "videos" / ".incoming"

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def ensure_video_storage_capacity(directory: Path) -> None:
    required_bytes = (
        settings.MEDIA_VIDEO_MIN_FREE_BYTES
        + settings.MEDIA_VIDEO_MAX_BYTES
    )

    if shutil.disk_usage(directory).free < required_bytes:
        raise VideoStorageCapacityError(
            "Недостаточно свободного места "
            "для загрузки видео."
        )


def open_temporary_video():
    directory = incoming_video_directory()

    ensure_video_storage_capacity(directory)

    return NamedTemporaryFile(
        mode="wb",
        prefix=".upload-",
        suffix=".mp4",
        dir=directory,
        delete=False,
    )


def flush_video_upload(file: BinaryIO) -> None:
    file.flush()
    os.fsync(file.fileno())


def publish_staged_video_upload(path: Path) -> StoredVideo:
    """
    Проверяет готовый временный файл и публикует его
    под новым неизменяемым UUID.

    Временный файл удаляет вызывающий код.
    """
    metadata = inspect_video(path)

    file_id = uuid.uuid4()
    destination = video_path(file_id)

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # В Docker backend работает с GID 10001.
    # Nginx получит чтение через эту группу.
    os.chmod(path, 0o640)

    # Атомарно создаём конечный файл без перезаписи.
    # Оба пути находятся на одной файловой системе.
    os.link(path, destination)

    return StoredVideo(
        id=file_id,
        metadata=metadata,
    )


def store_video_upload(source: BinaryIO) -> StoredVideo:
    """
    Вариант для уже открытого синхронного источника.
    Сам source не закрываем.
    """
    temporary_path: Path | None = None

    try:
        with open_temporary_video() as temporary:
            temporary_path = Path(temporary.name)
            total_bytes = 0

            while True:
                remaining = (
                    settings.MEDIA_VIDEO_MAX_BYTES
                    - total_bytes
                )

                chunk = source.read(
                    min(
                        COPY_CHUNK_BYTES,
                        remaining + 1,
                    )
                )

                if not chunk:
                    break

                total_bytes += len(chunk)

                if total_bytes > settings.MEDIA_VIDEO_MAX_BYTES:
                    raise VideoValidationError(
                        "Видео превышает допустимый размер."
                    )

                temporary.write(chunk)

            if total_bytes == 0:
                raise VideoValidationError(
                    "Загружен пустой файл."
                )

            flush_video_upload(temporary)

        return publish_staged_video_upload(
            temporary_path,
        )

    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)