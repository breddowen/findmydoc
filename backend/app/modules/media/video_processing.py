# ./backend/app/modules/media/video_processing.py

import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

from app.core.config import settings
from app.modules.media.video_container import (
    VideoValidationError,
    validate_mp4_container,
)
from app.modules.media.video_probe import probe_video


ALLOWED_H264_PROFILES = {
    "Baseline",
    "Constrained Baseline",
    "Main",
    "High",
}

HDR_TRANSFERS = {
    "smpte2084",
    "arib-std-b67",
}


@dataclass(frozen=True)
class VideoMetadata:
    width: int
    height: int
    rotation_degrees: int

    duration_seconds: float
    fps: float
    size_bytes: int

    has_audio: bool


def positive_number(
    value: Any,
    *,
    field_name: str,
) -> float:
    try:
        result = float(value)
    except (ValueError, TypeError, OverflowError) as error:
        raise VideoValidationError(
            f"Не удалось определить: {field_name}."
        ) from error

    if not math.isfinite(result) or result <= 0:
        raise VideoValidationError(
            f"Некорректное значение: {field_name}."
        )

    return result


def positive_integer(
    value: Any,
    *,
    field_name: str,
) -> int:
    number = positive_number(
        value,
        field_name=field_name,
    )

    if not number.is_integer():
        raise VideoValidationError(
            f"Некорректное значение: {field_name}."
        )

    return int(number)


def parse_frame_rate(value: Any) -> float:
    if not isinstance(value, str) or len(value) > 64:
        raise VideoValidationError(
            "Не удалось определить частоту кадров."
        )

    try:
        result = float(Fraction(value))
    except (
        ValueError,
        ZeroDivisionError,
        OverflowError,
    ) as error:
        raise VideoValidationError(
            "Не удалось определить частоту кадров."
        ) from error

    if not math.isfinite(result) or result <= 0:
        raise VideoValidationError(
            "Некорректная частота кадров."
        )

    return result


def get_rotation(stream: dict[str, Any]) -> int:
    side_data = stream.get("side_data_list") or []

    if not isinstance(side_data, list):
        raise VideoValidationError(
            "Некорректные метаданные поворота."
        )

    rotations = []

    for item in side_data:
        if not isinstance(item, dict):
            raise VideoValidationError(
                "Некорректные метаданные поворота."
            )

        if "rotation" not in item:
            continue

        try:
            rotation = float(item["rotation"])
        except (ValueError, TypeError, OverflowError) as error:
            raise VideoValidationError(
                "Некорректный поворот видео."
            ) from error

        if not math.isfinite(rotation):
            raise VideoValidationError(
                "Некорректный поворот видео."
            )

        normalized = rotation % 360
        nearest = round(normalized / 90) * 90

        if abs(normalized - nearest) > 0.01:
            raise VideoValidationError(
                "Поддерживается поворот только на "
                "0, 90, 180 или 270 градусов. "
                "Исправьте ориентацию при экспорте."
            )

        rotations.append(int(nearest) % 360)

    if len(set(rotations)) > 1:
        raise VideoValidationError(
            "В файле противоречивые данные о повороте."
        )

    return rotations[0] if rotations else 0


def validate_probe_data(
    *,
    data: dict[str, Any],
    size_bytes: int,
) -> VideoMetadata:
    if (
        size_bytes <= 0
        or size_bytes > settings.MEDIA_VIDEO_MAX_BYTES
    ):
        raise VideoValidationError(
            "Размер видео превышает допустимый лимит "
            "или файл пустой."
        )

    streams = data.get("streams")
    container = data.get("format")

    if (
        not isinstance(streams, list)
        or not isinstance(container, dict)
        or not streams
        or not all(isinstance(item, dict) for item in streams)
    ):
        raise VideoValidationError(
            "Не удалось прочитать дорожки видео."
        )

    video_streams = [
        item
        for item in streams
        if item.get("codec_type") == "video"
    ]
    audio_streams = [
        item
        for item in streams
        if item.get("codec_type") == "audio"
    ]

    if len(video_streams) != 1:
        raise VideoValidationError(
            "Файл должен содержать ровно одну видеодорожку."
        )

    if len(audio_streams) > 1:
        raise VideoValidationError(
            "Поддерживается не более одной звуковой дорожки."
        )

    if len(streams) != len(video_streams) + len(audio_streams):
        raise VideoValidationError(
            "Удалите дополнительные дорожки данных "
            "и встроенные субтитры при экспорте MP4."
        )

    video = video_streams[0]

    if video.get("codec_name") != "h264":
        raise VideoValidationError(
            "Нужен видеокодек H.264. "
            "HEVC/H.265, AV1 и другие кодеки "
            "для загрузки не поддерживаются."
        )

    if video.get("profile") not in ALLOWED_H264_PROFILES:
        raise VideoValidationError(
            "Нужен профиль H.264 Baseline, Main или High."
        )

    if video.get("pix_fmt") != "yuv420p":
        raise VideoValidationError(
            "Нужен восьмибитный формат цвета YUV 4:2:0 "
            "(yuv420p). Экспортируйте обычное SDR-видео."
        )

    if video.get("color_transfer") in HDR_TRANSFERS:
        raise VideoValidationError(
            "HDR-видео не поддерживается. "
            "Экспортируйте ролик в SDR."
        )

    level = positive_integer(
        video.get("level"),
        field_name="уровень H.264",
    )

    if level > 41:
        raise VideoValidationError(
            "Используйте H.264 Level 4.1 или ниже."
        )

    sample_aspect_ratio = video.get("sample_aspect_ratio")

    if sample_aspect_ratio not in {
        None,
        "N/A",
        "1:1",
    }:
        raise VideoValidationError(
            "Используйте квадратные пиксели "
            "(Pixel aspect ratio 1:1)."
        )

    width = positive_integer(
        video.get("width"),
        field_name="ширина кадра",
    )
    height = positive_integer(
        video.get("height"),
        field_name="высота кадра",
    )

    rotation = get_rotation(video)

    if rotation in {90, 270}:
        width, height = height, width

    if (
        max(width, height)
        > settings.MEDIA_VIDEO_MAX_LONG_SIDE
        or min(width, height)
        > settings.MEDIA_VIDEO_MAX_SHORT_SIDE
    ):
        raise VideoValidationError(
            "Слишком большое разрешение. "
            "Максимум 1920×1080 или 1080×1920."
        )

    average_fps = parse_frame_rate(
        video.get("avg_frame_rate"),
    )
    nominal_fps = parse_frame_rate(
        video.get("r_frame_rate"),
    )

    if (
        max(average_fps, nominal_fps)
        > settings.MEDIA_VIDEO_MAX_FPS + 0.001
    ):
        raise VideoValidationError(
            "Частота кадров превышает допустимый лимит. "
            "Экспортируйте ролик с частотой до 30 кадров/с."
        )

    duration = positive_number(
        container.get("duration"),
        field_name="длительность видео",
    )

    # При несовпадении длительности контейнера и дорожек
    # ориентируемся на наибольшее известное значение.
    durations = [duration]

    for stream in streams:
        stream_duration = stream.get("duration")

        if stream_duration not in {None, "N/A"}:
            durations.append(
                positive_number(
                    stream_duration,
                    field_name="длительность дорожки",
                )
            )

    duration = max(durations)

    if duration > settings.MEDIA_VIDEO_MAX_DURATION_SECONDS:
        raise VideoValidationError(
            "Видео слишком длинное. "
            "Максимальная длительность — 10 минут."
        )

    if audio_streams:
        audio = audio_streams[0]

        if (
            audio.get("codec_name") != "aac"
            or audio.get("profile") != "LC"
        ):
            raise VideoValidationError(
                "Звуковая дорожка должна использовать AAC-LC."
            )

        channels = positive_integer(
            audio.get("channels"),
            field_name="количество звуковых каналов",
        )
        sample_rate = positive_integer(
            audio.get("sample_rate"),
            field_name="частота дискретизации звука",
        )

        if channels > 2:
            raise VideoValidationError(
                "Поддерживается моно или стерео. "
                "Многоканальный звук нужно убрать при экспорте."
            )

        if sample_rate not in {44100, 48000}:
            raise VideoValidationError(
                "Используйте частоту звука 44,1 или 48 кГц."
            )

    return VideoMetadata(
        width=width,
        height=height,
        rotation_degrees=rotation,
        duration_seconds=duration,
        fps=average_fps,
        size_bytes=size_bytes,
        has_audio=bool(audio_streams),
    )


def inspect_video(path: Path) -> VideoMetadata:
    size_bytes = path.stat().st_size

    if (
        size_bytes <= 0
        or size_bytes > settings.MEDIA_VIDEO_MAX_BYTES
    ):
        raise VideoValidationError(
            "Файл пустой или превышает допустимый размер."
        )

    validate_mp4_container(path)

    return validate_probe_data(
        data=probe_video(path),
        size_bytes=size_bytes,
    )