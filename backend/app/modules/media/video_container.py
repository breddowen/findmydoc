# ./backend/app/modules/media/video_container.py

import struct
from pathlib import Path


class VideoValidationError(ValueError):
    """Ошибка файла, которую можно показать пользователю."""


MP4_BRANDS = {
    b"isom",
    b"iso2",
    b"iso3",
    b"iso4",
    b"iso5",
    b"iso6",
    b"iso7",
    b"iso8",
    b"iso9",
    b"mp41",
    b"mp42",
    b"avc1",
    b"M4V ",
}

MAX_TOP_LEVEL_BOXES = 4096
MAX_FTYP_BYTES = 4096


def validate_mp4_container(path: Path) -> None:
    file_size = path.stat().st_size

    if file_size < 24:
        raise VideoValidationError(
            "Файл пустой или не является корректным MP4."
        )

    found_ftyp = False
    moov_offset: int | None = None
    mdat_offset: int | None = None

    offset = 0
    box_count = 0

    with path.open("rb") as source:
        while offset < file_size:
            box_count += 1

            if box_count > MAX_TOP_LEVEL_BOXES:
                raise VideoValidationError(
                    "Слишком сложная структура MP4. "
                    "Повторно экспортируйте ролик."
                )

            if file_size - offset < 8:
                raise VideoValidationError(
                    "Повреждён заголовок MP4."
                )

            source.seek(offset)
            header = source.read(8)

            if len(header) != 8:
                raise VideoValidationError(
                    "Не удалось прочитать MP4."
                )

            box_size, box_type = struct.unpack(
                ">I4s",
                header,
            )
            header_size = 8

            if box_size == 1:
                extended_size = source.read(8)

                if len(extended_size) != 8:
                    raise VideoValidationError(
                        "Повреждён заголовок MP4."
                    )

                box_size = struct.unpack(
                    ">Q",
                    extended_size,
                )[0]
                header_size = 16

            elif box_size == 0:
                box_size = file_size - offset

            if (
                box_size < header_size
                or box_size > file_size - offset
            ):
                raise VideoValidationError(
                    "В MP4 указаны некорректные размеры данных."
                )

            payload_size = box_size - header_size

            if box_type == b"ftyp":
                if found_ftyp:
                    raise VideoValidationError(
                        "Некорректная структура MP4."
                    )

                if (
                    payload_size < 8
                    or payload_size > MAX_FTYP_BYTES
                    or (payload_size - 8) % 4 != 0
                ):
                    raise VideoValidationError(
                        "Некорректное описание формата MP4."
                    )

                payload = source.read(payload_size)

                if len(payload) != payload_size:
                    raise VideoValidationError(
                        "Повреждено описание формата MP4."
                    )

                major_brand = payload[:4]

                brands = {
                    major_brand,
                    *(
                        payload[index:index + 4]
                        for index in range(
                            8,
                            len(payload),
                            4,
                        )
                    ),
                }

                if (
                    major_brand == b"qt  "
                    or not brands.intersection(MP4_BRANDS)
                ):
                    raise VideoValidationError(
                        "Нужен контейнер MP4, а не MOV "
                        "или другой формат."
                    )

                found_ftyp = True

            elif box_type == b"moov":
                if moov_offset is not None:
                    raise VideoValidationError(
                        "В MP4 обнаружены повторные метаданные."
                    )

                moov_offset = offset

            elif box_type == b"mdat":
                if mdat_offset is None:
                    mdat_offset = offset

            elif box_type == b"moof":
                raise VideoValidationError(
                    "Фрагментированный MP4 пока не поддерживается. "
                    "Экспортируйте обычный MP4 с faststart."
                )

            offset += box_size

    if (
        not found_ftyp
        or moov_offset is None
        or mdat_offset is None
    ):
        raise VideoValidationError(
            "Файл не содержит необходимую структуру MP4."
        )

    if moov_offset > mdat_offset:
        raise VideoValidationError(
            "MP4 не подготовлен для быстрого воспроизведения. "
            "Включите при экспорте Web optimized / "
            "Fast start / Оптимизация для интернета."
        )