# ./backend/tests/test_video_schemas.py

# python -m unittest discover -s tests -p "test_video*.py" -v
# alembic upgrade head

import unittest
import uuid

from pydantic import ValidationError

from app.modules.videos.schemas import (
    VideoCreateRequest,
    VideoUpdateRequest,
)


class VideoSchemaTests(unittest.TestCase):
    def test_accepts_single_wide_file(self):
        file_id = uuid.uuid4()

        payload = VideoCreateRequest(
            title="  Первый ролик  ",
            wide_file_id=file_id,
        )

        self.assertEqual(payload.title, "Первый ролик")
        self.assertEqual(payload.wide_file_id, file_id)
        self.assertIsNone(payload.mobile_file_id)
        self.assertTrue(payload.pro_content)

    def test_accepts_single_mobile_file(self):
        file_id = uuid.uuid4()

        payload = VideoCreateRequest(
            title="Вертикальный ролик",
            mobile_file_id=file_id,
        )

        self.assertEqual(payload.mobile_file_id, file_id)
        self.assertIsNone(payload.wide_file_id)

    def test_accepts_two_different_files(self):
        payload = VideoCreateRequest(
            title="Два варианта",
            wide_file_id=uuid.uuid4(),
            mobile_file_id=uuid.uuid4(),
        )

        self.assertNotEqual(
            payload.wide_file_id,
            payload.mobile_file_id,
        )

    def test_rejects_no_files(self):
        with self.assertRaises(ValidationError):
            VideoCreateRequest(
                title="Без файлов",
            )

    def test_rejects_same_file_in_both_slots(self):
        file_id = uuid.uuid4()

        with self.assertRaises(ValidationError):
            VideoCreateRequest(
                title="Повтор",
                wide_file_id=file_id,
                mobile_file_id=file_id,
            )

    def test_rejects_blank_title(self):
        with self.assertRaises(ValidationError):
            VideoCreateRequest(
                title="   ",
                wide_file_id=uuid.uuid4(),
            )

    def test_deduplicates_tags(self):
        tag_id = uuid.uuid4()

        payload = VideoCreateRequest(
            title="Теги",
            wide_file_id=uuid.uuid4(),
            tag_ids=[tag_id, tag_id],
        )

        self.assertEqual(payload.tag_ids, [tag_id])

    def test_update_requires_version(self):
        with self.assertRaises(ValidationError):
            VideoUpdateRequest(
                title="Обновление",
                wide_file_id=uuid.uuid4(),
            )

    def test_accepts_swapped_slots(self):
        first = uuid.uuid4()
        second = uuid.uuid4()

        payload = VideoUpdateRequest(
            title="Перестановка",
            wide_file_id=second,
            mobile_file_id=first,
            expected_version=1,
        )

        self.assertEqual(payload.wide_file_id, second)
        self.assertEqual(payload.mobile_file_id, first)


if __name__ == "__main__":
    unittest.main()