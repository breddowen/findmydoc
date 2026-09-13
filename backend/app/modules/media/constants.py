# backend\app\modules\media\constants.py

from dataclasses import dataclass
from typing import Literal


ImagePurpose = Literal[
    "doctor",
    "article",
    "questionnaire",
    "program",
    "life_aspect",
]


@dataclass(frozen=True)
class ImagePreset:
    ratio_width: int
    ratio_height: int
    max_width: int
    max_height: int


IMAGE_PRESETS: dict[str, ImagePreset] = {
    "doctor": ImagePreset(
        ratio_width=1,
        ratio_height=1,
        max_width=512,
        max_height=512,
    ),
    "article": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "questionnaire": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "program": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "life_aspect": ImagePreset(
        ratio_width=3,
        ratio_height=1,
        max_width=1800,
        max_height=600,
    ),
}