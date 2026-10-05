# ./backend/app/modules/media/video_probe.py

import os
import json
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from app.core.config import settings
from app.modules.media.video_container import (
    VideoValidationError,
)


class VideoProbeUnavailableError(RuntimeError):
    """Сервер не может выполнить проверку видео."""


MAX_PROBE_OUTPUT_BYTES = 256 * 1024


def probe_video(path: Path) -> dict[str, Any]:
    command = [
        settings.MEDIA_VIDEO_FFPROBE_BIN,
        "-v",
        "error",
        "-max_alloc",
        str(64 * 1024 * 1024),
        "-protocol_whitelist",
        "file",
        "-threads",
        "1",
        "-show_entries",
        (
            "format=format_name,duration:"
            "stream=codec_type,codec_name,profile,level,"
            "width,height,pix_fmt,avg_frame_rate,"
            "r_frame_rate,sample_aspect_ratio,"
            "color_transfer,duration,channels,sample_rate:"
            "stream_side_data=rotation"
        ),
        "-of",
        "json",
        str(path.resolve()),
    ]

    with (
        tempfile.TemporaryFile(mode="w+b") as output,
        tempfile.TemporaryFile(mode="w+b") as errors,
    ):
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.DEVNULL,
                stdout=output,
                stderr=errors,
                shell=False,
            )
        except OSError as error:
            raise VideoProbeUnavailableError(
                "Проверка видео временно недоступна."
            ) from error

        deadline = (
            time.monotonic()
            + settings.MEDIA_VIDEO_PROBE_TIMEOUT_SECONDS
        )

        try:
            while process.poll() is None:
                if time.monotonic() >= deadline:
                    raise VideoValidationError(
                        "Проверка видео заняла слишком много времени. "
                        "Повторно экспортируйте MP4."
                    )

                output_size = os.fstat(output.fileno()).st_size
                error_size = os.fstat(errors.fileno()).st_size

                if (
                    output_size > MAX_PROBE_OUTPUT_BYTES
                    or error_size > MAX_PROBE_OUTPUT_BYTES
                ):
                    raise VideoValidationError(
                        "Файл содержит слишком сложные "
                        "или повреждённые метаданные."
                    )

                time.sleep(0.05)

            output_size = os.fstat(output.fileno()).st_size
            error_size = os.fstat(errors.fileno()).st_size

            if (
                output_size > MAX_PROBE_OUTPUT_BYTES
                or error_size > MAX_PROBE_OUTPUT_BYTES
            ):
                raise VideoValidationError(
                    "Файл содержит слишком большой "
                    "объём метаданных."
                )

            if process.returncode != 0:
                raise VideoValidationError(
                    "Не удалось прочитать видео. "
                    "Файл повреждён или имеет "
                    "неподдерживаемую структуру."
                )

            output.seek(0)
            raw_result = output.read(
                MAX_PROBE_OUTPUT_BYTES + 1
            )

        finally:
            if process.poll() is None:
                process.kill()

            process.wait()

    try:
        result = json.loads(raw_result)
    except (ValueError, UnicodeDecodeError) as error:
        raise VideoValidationError(
            "Не удалось прочитать параметры видео."
        ) from error

    if not isinstance(result, dict):
        raise VideoValidationError(
            "Некорректные параметры видео."
        )

    return result