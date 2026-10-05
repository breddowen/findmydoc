# ./backend/app/modules/media/video_posters.py

import io
import math
import os
import subprocess
import tempfile
import threading
import time
import uuid
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from app.core.config import settings
from app.modules.media.video_storage import video_path


POSTER_WIDTH = 1600
POSTER_HEIGHT = 900

MAX_PNG_BYTES = 16 * 1024 * 1024
MAX_DIAGNOSTIC_BYTES = 256 * 1024

POSTER_SLOT = threading.BoundedSemaphore(1)


class VideoPosterError(RuntimeError):
    """Безопасное для показа пользователю сообщение."""


@dataclass(frozen=True)
class PreparedVideoPoster:
    source_file_id: uuid.UUID
    data: bytes
    width: int = POSTER_WIDTH
    height: int = POSTER_HEIGHT


def extract_frame(
    *,
    source: Path,
    destination: Path,
    seek_seconds: float,
) -> None:
    command = [
        settings.MEDIA_VIDEO_FFMPEG_BIN,
        "-hide_banner",
        "-loglevel",
        "error",
        "-nostdin",
        "-y",
        "-max_alloc",
        str(64 * 1024 * 1024),
        "-protocol_whitelist",
        "file",
        "-threads",
        "1",
        "-ss",
        f"{seek_seconds:.3f}",
        "-i",
        str(source.resolve()),
        "-map",
        "0:v:0",
        "-an",
        "-sn",
        "-dn",
        "-vf",
        (
            f"scale={POSTER_WIDTH}:{POSTER_HEIGHT}:"
            "force_original_aspect_ratio=decrease:"
            "force_divisible_by=2,"
            f"pad={POSTER_WIDTH}:{POSTER_HEIGHT}:"
            "(ow-iw)/2:(oh-ih)/2:color=black,"
            "setsar=1"
        ),
        "-frames:v",
        "1",
        "-c:v",
        "png",
        "-threads",
        "1",
        "-update",
        "1",
        str(destination),
    ]

    with tempfile.TemporaryFile(mode="w+b") as errors:
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=errors,
                shell=False,
            )
        except OSError as error:
            raise VideoPosterError(
                "Не удалось запустить создание автообложки. "
                "Проверьте установку ffmpeg."
            ) from error

        deadline = (
            time.monotonic()
            + settings.MEDIA_VIDEO_POSTER_TIMEOUT_SECONDS
        )

        try:
            while process.poll() is None:
                if time.monotonic() >= deadline:
                    raise VideoPosterError(
                        "Создание автообложки заняло "
                        "слишком много времени."
                    )

                if (
                    os.fstat(errors.fileno()).st_size
                    > MAX_DIAGNOSTIC_BYTES
                ):
                    raise VideoPosterError(
                        "Не удалось извлечь кадр из видео."
                    )

                if (
                    destination.exists()
                    and destination.stat().st_size > MAX_PNG_BYTES
                ):
                    raise VideoPosterError(
                        "Получен слишком большой кадр."
                    )

                time.sleep(0.05)

            if process.returncode != 0:
                raise VideoPosterError(
                    "Не удалось извлечь кадр. "
                    "Можно загрузить обложку вручную."
                )

        finally:
            if process.poll() is None:
                process.kill()

            process.wait()

    if (
        not destination.is_file()
        or destination.stat().st_size <= 0
        or destination.stat().st_size > MAX_PNG_BYTES
    ):
        raise VideoPosterError(
            "Не удалось получить изображение из видео."
        )


def prepare_video_poster(
    *,
    file_id: uuid.UUID,
    duration_seconds: float,
) -> PreparedVideoPoster:
    if (
        not math.isfinite(duration_seconds)
        or duration_seconds <= 0
    ):
        raise VideoPosterError(
            "Некорректная длительность видео."
        )

    source = video_path(file_id)

    if not source.is_file():
        raise VideoPosterError(
            "Исходный видеофайл отсутствует."
        )

    if not POSTER_SLOT.acquire(blocking=False):
        raise VideoPosterError(
            "Сейчас создаётся другая автообложка. "
            "Повторите действие позже."
        )

    try:
        # Для ролика короче двух секунд берём
        # середину, чтобы не попасть за конец файла.
        seek_seconds = min(
            1.0,
            duration_seconds / 2,
        )

        with tempfile.TemporaryDirectory(
            prefix="findmydoc-video-poster-",
        ) as directory:
            png_path = Path(directory) / "frame.png"

            extract_frame(
                source=source,
                destination=png_path,
                seek_seconds=seek_seconds,
            )

            with Image.open(png_path) as original:
                if original.size != (
                    POSTER_WIDTH,
                    POSTER_HEIGHT,
                ):
                    raise VideoPosterError(
                        "Получен кадр неожиданного размера."
                    )

                original.load()

                with original.convert("RGB") as image:
                    image.info.clear()

                    output = io.BytesIO()

                    image.save(
                        output,
                        format="WEBP",
                        quality=settings.MEDIA_WEBP_QUALITY,
                        method=4,
                        exif=b"",
                    )

                    data = output.getvalue()

        if len(data) > settings.MEDIA_IMAGE_MAX_BYTES:
            raise VideoPosterError(
                "Автоматическая обложка слишком большая."
            )

        return PreparedVideoPoster(
            source_file_id=file_id,
            data=data,
        )

    except VideoPosterError:
        raise

    except (OSError, ValueError) as error:
        raise VideoPosterError(
            "Не удалось подготовить автообложку. "
            "Можно загрузить изображение вручную."
        ) from error

    finally:
        POSTER_SLOT.release()