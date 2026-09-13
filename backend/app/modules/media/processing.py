# backend\app\modules\media\processing.py

import io
from dataclasses import dataclass

from PIL import (
    Image,
    ImageOps,
    UnidentifiedImageError,
)

from app.core.config import settings
from app.modules.media.constants import ImagePreset


ALLOWED_IMAGE_FORMATS = {
    "JPEG",
    "PNG",
    "WEBP",
}


class ImageProcessingError(ValueError):
    pass


@dataclass(frozen=True)
class CropRectangle:
    left: int
    top: int
    width: int
    height: int


@dataclass(frozen=True)
class ProcessedImage:
    data: bytes
    width: int
    height: int


def validate_source(image: Image.Image) -> None:
    if image.format not in ALLOWED_IMAGE_FORMATS:
        raise ImageProcessingError(
            "Поддерживаются только JPEG, PNG и WebP"
        )

    width, height = image.size

    if width <= 0 or height <= 0:
        raise ImageProcessingError(
            "Некорректный размер изображения"
        )

    if width * height > settings.MEDIA_IMAGE_MAX_PIXELS:
        raise ImageProcessingError(
            "Слишком большое разрешение изображения"
        )

    if getattr(image, "n_frames", 1) != 1:
        raise ImageProcessingError(
            "Анимированные изображения не поддерживаются"
        )


def validate_crop(
    *,
    image: Image.Image,
    crop: CropRectangle,
    preset: ImagePreset,
) -> None:
    if (
        crop.left < 0
        or crop.top < 0
        or crop.width <= 0
        or crop.height <= 0
    ):
        raise ImageProcessingError(
            "Некорректная область обрезки"
        )

    if (
        crop.left + crop.width > image.width
        or crop.top + crop.height > image.height
    ):
        raise ImageProcessingError(
            "Область обрезки выходит за границы изображения"
        )

    # Допускаем округление координат кроппера
    # примерно на один пиксель.
    difference = abs(
        crop.width * preset.ratio_height
        - crop.height * preset.ratio_width
    )

    tolerance = max(
        preset.ratio_width,
        preset.ratio_height,
    )

    if difference > tolerance:
        raise ImageProcessingError(
            "Область обрезки имеет неверные пропорции"
        )


def process_image(
    *,
    source: bytes,
    crop: CropRectangle,
    preset: ImagePreset,
) -> ProcessedImage:
    if not source:
        raise ImageProcessingError(
            "Загружен пустой файл"
        )

    if len(source) > settings.MEDIA_IMAGE_MAX_BYTES:
        raise ImageProcessingError(
            "Файл превышает допустимый размер"
        )

    try:
        # Сначала проверяем формат и структуру.
        with Image.open(io.BytesIO(source)) as probe:
            validate_source(probe)
            probe.verify()

        # После verify файл требуется открыть заново.
        with Image.open(io.BytesIO(source)) as original:
            validate_source(original)
            original.load()

            oriented = ImageOps.exif_transpose(original)

            try:
                validate_crop(
                    image=oriented,
                    crop=crop,
                    preset=preset,
                )

                cropped = oriented.crop(
                    (
                        crop.left,
                        crop.top,
                        crop.left + crop.width,
                        crop.top + crop.height,
                    )
                )

                try:
                    has_alpha = (
                        "A" in cropped.getbands()
                        or "transparency" in cropped.info
                    )

                    converted = cropped.convert(
                        "RGBA" if has_alpha else "RGB"
                    )

                    try:
                        # thumbnail уменьшает большие изображения,
                        # но не увеличивает маленькие.
                        converted.thumbnail(
                            (
                                preset.max_width,
                                preset.max_height,
                            ),
                            Image.Resampling.LANCZOS,
                        )

                        # Не переносим EXIF, комментарии
                        # и прочие метаданные исходника.
                        converted.info.clear()

                        output = io.BytesIO()

                        converted.save(
                            output,
                            format="WEBP",
                            quality=settings.MEDIA_WEBP_QUALITY,
                            method=4,
                            exif=b"",
                        )

                        return ProcessedImage(
                            data=output.getvalue(),
                            width=converted.width,
                            height=converted.height,
                        )
                    finally:
                        converted.close()
                finally:
                    cropped.close()
            finally:
                if oriented is not original:
                    oriented.close()

    except ImageProcessingError:
        raise
    except (
        UnidentifiedImageError,
        Image.DecompressionBombError,
        OSError,
        ValueError,
        SyntaxError,
        EOFError,
    ) as error:
        raise ImageProcessingError(
            "Не удалось прочитать изображение. "
            "Файл повреждён или имеет неподдерживаемый формат."
        ) from error