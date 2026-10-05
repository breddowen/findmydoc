# ./backend/tests/test_video_posters.py
# python -m unittest discover -s tests -p "test_video*.py" -v

import io
import shutil
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from app.core.config import settings
from app.modules.media.video_posters import (
    VideoPosterError,
    prepare_video_poster,
)
from app.modules.media.video_storage import video_path


class VideoPosterTests(unittest.TestCase):
    def test_missing_video(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(
                settings,
                "MEDIA_ROOT",
                Path(directory),
            ):
                with self.assertRaises(VideoPosterError):
                    prepare_video_poster(
                        file_id=uuid.uuid4(),
                        duration_seconds=2.0,
                    )

    def test_real_video_to_webp(self):
        ffmpeg = shutil.which(
            settings.MEDIA_VIDEO_FFMPEG_BIN
        )

        if not ffmpeg:
            self.skipTest("Для теста нужен ffmpeg")

        with tempfile.TemporaryDirectory() as directory:
            with patch.object(
                settings,
                "MEDIA_ROOT",
                Path(directory),
            ):
                file_id = uuid.uuid4()
                source = video_path(file_id)

                source.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                subprocess.run(
                    [
                        ffmpeg,
                        "-hide_banner",
                        "-loglevel",
                        "error",
                        "-nostdin",
                        "-f",
                        "lavfi",
                        "-i",
                        "color=c=blue:s=180x320:r=25",
                        "-t",
                        "2",
                        "-an",
                        "-c:v",
                        "libx264",
                        "-threads",
                        "1",
                        "-pix_fmt",
                        "yuv420p",
                        "-movflags",
                        "+faststart",
                        str(source),
                    ],
                    check=True,
                    timeout=30,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

                prepared = prepare_video_poster(
                    file_id=file_id,
                    duration_seconds=2.0,
                )

                self.assertEqual(
                    prepared.source_file_id,
                    file_id,
                )
                self.assertGreater(len(prepared.data), 0)

                with Image.open(
                    io.BytesIO(prepared.data)
                ) as image:
                    self.assertEqual(image.format, "WEBP")
                    self.assertEqual(image.size, (1600, 900))


if __name__ == "__main__":
    unittest.main()