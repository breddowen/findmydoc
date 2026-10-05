# ./backend/tests/test_video_processing.py

# python -m unittest discover -s tests -p "test_video_processing.py" -v
# alembic upgrade head

import copy
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from app.core.config import settings
from app.modules.media.video_container import (
    VideoValidationError,
    validate_mp4_container,
)
from app.modules.media.video_processing import (
    inspect_video,
    validate_probe_data,
)


def valid_probe_data() -> dict:
    return {
        "format": {
            "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
            "duration": "10.0",
        },
        "streams": [
            {
                "codec_type": "video",
                "codec_name": "h264",
                "profile": "High",
                "level": 40,
                "width": 1920,
                "height": 1080,
                "pix_fmt": "yuv420p",
                "avg_frame_rate": "30/1",
                "r_frame_rate": "30/1",
                "sample_aspect_ratio": "1:1",
                "color_transfer": "bt709",
                "duration": "10.0",
            },
            {
                "codec_type": "audio",
                "codec_name": "aac",
                "profile": "LC",
                "channels": 2,
                "sample_rate": "48000",
                "duration": "10.0",
            },
        ],
    }


def mp4_box(box_type: bytes, payload: bytes = b"") -> bytes:
    return (
        struct.pack(
            ">I4s",
            8 + len(payload),
            box_type,
        )
        + payload
    )


def fake_mp4(*, faststart: bool) -> bytes:
    ftyp = mp4_box(
        b"ftyp",
        b"isom" + b"\x00\x00\x00\x00" + b"isommp42",
    )
    moov = mp4_box(b"moov")
    mdat = mp4_box(b"mdat", b"\x00" * 32)

    if faststart:
        return ftyp + moov + mdat

    return ftyp + mdat + moov


class VideoMetadataTests(unittest.TestCase):
    def validate(self, data: dict):
        return validate_probe_data(
            data=data,
            size_bytes=1024 * 1024,
        )

    def test_accepts_h264_aac(self):
        result = self.validate(valid_probe_data())

        self.assertEqual(result.width, 1920)
        self.assertEqual(result.height, 1080)
        self.assertTrue(result.has_audio)
        self.assertEqual(result.fps, 30.0)

    def test_accepts_video_without_audio(self):
        data = valid_probe_data()
        data["streams"] = data["streams"][:1]

        result = self.validate(data)

        self.assertFalse(result.has_audio)

    def test_accepts_vertical_video(self):
        data = valid_probe_data()
        data["streams"][0]["width"] = 1080
        data["streams"][0]["height"] = 1920

        result = self.validate(data)

        self.assertEqual(
            (result.width, result.height),
            (1080, 1920),
        )

    def test_respects_rotation(self):
        data = valid_probe_data()
        data["streams"][0]["side_data_list"] = [
            {"rotation": -90}
        ]

        result = self.validate(data)

        self.assertEqual(
            (result.width, result.height),
            (1080, 1920),
        )
        self.assertEqual(result.rotation_degrees, 270)

    def test_rejects_hevc(self):
        data = valid_probe_data()
        data["streams"][0]["codec_name"] = "hevc"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_ten_bit(self):
        data = valid_probe_data()
        data["streams"][0]["pix_fmt"] = "yuv420p10le"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_hdr(self):
        data = valid_probe_data()
        data["streams"][0]["color_transfer"] = "smpte2084"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_sixty_fps(self):
        data = valid_probe_data()
        data["streams"][0]["avg_frame_rate"] = "60/1"
        data["streams"][0]["r_frame_rate"] = "60/1"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_long_video(self):
        data = valid_probe_data()
        data["format"]["duration"] = "601"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_non_finite_duration(self):
        data = valid_probe_data()
        data["format"]["duration"] = "NaN"

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_multiple_video_tracks(self):
        data = valid_probe_data()
        data["streams"].append(
            copy.deepcopy(data["streams"][0])
        )

        with self.assertRaises(VideoValidationError):
            self.validate(data)

    def test_rejects_extra_data_track(self):
        data = valid_probe_data()
        data["streams"].append(
            {"codec_type": "data"}
        )

        with self.assertRaises(VideoValidationError):
            self.validate(data)


class Mp4ContainerTests(unittest.TestCase):
    def check_file(self, content: bytes):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.mp4"
            path.write_bytes(content)

            validate_mp4_container(path)

    def test_accepts_faststart_structure(self):
        # Проверяет только структуру контейнера,
        # не валидность видеодорожки.
        self.check_file(fake_mp4(faststart=True))

    def test_rejects_missing_faststart(self):
        with self.assertRaises(VideoValidationError):
            self.check_file(fake_mp4(faststart=False))

    def test_rejects_random_file(self):
        with self.assertRaises(VideoValidationError):
            self.check_file(b"not a video")

    def test_rejects_truncated_box(self):
        content = (
            fake_mp4(faststart=True)
            + struct.pack(">I4s", 1000, b"free")
        )

        with self.assertRaises(VideoValidationError):
            self.check_file(content)


class VideoIntegrationTests(unittest.TestCase):
    def test_real_mp4(self):
        ffmpeg = shutil.which(
            settings.MEDIA_VIDEO_FFMPEG_BIN
        )
        ffprobe = shutil.which(
            settings.MEDIA_VIDEO_FFPROBE_BIN
        )

        if not ffmpeg or not ffprobe:
            self.skipTest(
                "Для интеграционного теста нужны ffmpeg и ffprobe."
            )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.mp4"

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
                    "color=c=black:s=320x180:r=25",
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
                    str(path),
                ],
                check=True,
                timeout=30,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            result = inspect_video(path)

            self.assertEqual(result.width, 320)
            self.assertEqual(result.height, 180)
            self.assertAlmostEqual(result.fps, 25.0)
            self.assertFalse(result.has_audio)
            self.assertGreater(result.size_bytes, 0)


if __name__ == "__main__":
    unittest.main()