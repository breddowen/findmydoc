# backend\app\modules\media\storage.py

import os
import uuid
from pathlib import Path
from tempfile import NamedTemporaryFile

from app.core.config import settings


def media_root() -> Path:
    configured = Path(settings.MEDIA_ROOT).expanduser()

    if not configured.is_absolute():
        # Такой же принцип, как у относительного
        # пути SQLite: относительно backend.
        backend_dir = Path(__file__).resolve().parents[3]
        configured = backend_dir / configured

    return configured.resolve()


def image_path(image_id: uuid.UUID) -> Path:
    identifier = image_id.hex

    return (
        media_root()
        / "images"
        / identifier[:2]
        / f"{identifier}.webp"
    )


def write_image(
    *,
    image_id: uuid.UUID,
    data: bytes,
) -> Path:
    destination = image_path(image_id)
    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary_path: Path | None = None

    try:
        # Временный файл создаём на той же файловой
        # системе, чтобы os.replace был атомарным.
        with NamedTemporaryFile(
            mode="wb",
            prefix=".upload-",
            suffix=".tmp",
            dir=destination.parent,
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)

            temporary.write(data)
            temporary.flush()
            os.fsync(temporary.fileno())

        os.replace(
            temporary_path,
            destination,
        )

        return destination
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)