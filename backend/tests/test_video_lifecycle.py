# ./backend/tests/test_video_lifecycle.py

import unittest
import uuid
from dataclasses import replace
from types import SimpleNamespace

from pydantic import ValidationError

from app.modules.programs.enums import ProgramItemType
from app.modules.programs.utils import get_stage_task_items
from app.modules.videos.lifecycle import (
    VideoReference,
    make_usage_token,
)
from app.modules.videos.lifecycle_schemas import VideoDeleteRequest


class VideoUsageTokenTests(unittest.TestCase):
    def setUp(self):
        self.video_id = uuid.uuid4()

        self.first = VideoReference(
            program_id=uuid.uuid4(),
            program_title="Программа А",
            program_hidden=False,
            stage_id=uuid.uuid4(),
            stage_title="Первый этап",
            item_id=uuid.uuid4(),
        )

        self.second = VideoReference(
            program_id=uuid.uuid4(),
            program_title="Программа Б",
            program_hidden=False,
            stage_id=uuid.uuid4(),
            stage_title="Второй этап",
            item_id=uuid.uuid4(),
        )

    def token(self, references):
        return make_usage_token(
            video_id=self.video_id,
            references=references,
        )

    def test_reference_order_does_not_change_token(self):
        self.assertEqual(
            self.token([self.first, self.second]),
            self.token([self.second, self.first]),
        )

    def test_new_reference_changes_token(self):
        self.assertNotEqual(
            self.token([self.first]),
            self.token([self.first, self.second]),
        )

    def test_program_rename_changes_token(self):
        changed = replace(
            self.first,
            program_title="Новое название",
        )

        self.assertNotEqual(
            self.token([self.first]),
            self.token([changed]),
        )

    def test_different_video_changes_token(self):
        self.assertNotEqual(
            self.token([self.first]),
            make_usage_token(
                video_id=uuid.uuid4(),
                references=[self.first],
            ),
        )

    def test_explicit_confirmation_is_required(self):
        with self.assertRaises(ValidationError):
            VideoDeleteRequest(
                expected_version=1,
                expected_usage_token=self.token([]),
            )

    def test_false_confirmation_is_rejected(self):
        with self.assertRaises(ValidationError):
            VideoDeleteRequest(
                expected_version=1,
                expected_usage_token=self.token([]),
                confirm=False,
            )


class VideoStageTaskTests(unittest.TestCase):
    def test_hidden_video_is_not_a_task(self):
        visible_video = SimpleNamespace(
            item_type=ProgramItemType.VIDEO,
            video=SimpleNamespace(is_hidden=False),
        )

        hidden_video = SimpleNamespace(
            item_type=ProgramItemType.VIDEO,
            video=SimpleNamespace(is_hidden=True),
        )

        article = SimpleNamespace(
            item_type=ProgramItemType.ARTICLE,
        )

        consultation = SimpleNamespace(
            item_type=ProgramItemType.CONSULTATION,
        )

        stage = SimpleNamespace(
            items=[
                visible_video,
                hidden_video,
                article,
                consultation,
            ]
        )

        self.assertEqual(
            get_stage_task_items(stage),
            [visible_video, article],
        )


if __name__ == "__main__":
    unittest.main()