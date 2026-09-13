# backend\app\modules\media\schemas.py

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.media.constants import ImagePurpose


class MediaImageUploadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    purpose: ImagePurpose

    width: int
    height: int
    size_bytes: int

    created_at: datetime

    # Только закрытый API, не путь на диске.
    preview_path: str

class EntityImageUpdateRequest(BaseModel):
    # Обязательное поле. null означает удалить обложку.
    image_id: uuid.UUID | None

    # Изображение, которое пользователь видел,
    # когда открыл редактор.
    #
    # Защищает от незаметной перезаписи изменения,
    # сделанного другим сотрудником.
    expected_image_id: uuid.UUID | None


class EntityImageResponse(BaseModel):
    purpose: ImagePurpose
    entity_id: uuid.UUID

    image_id: uuid.UUID | None
    width: int | None
    height: int | None
    size_bytes: int | None

    file_path: str | None