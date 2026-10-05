# ./backend/seed/cleanup_video_media.py

# У скрипта два режима:

# обычный — можно запускать при работающем backend: очищает истёкшие загрузки с записью в БД, давно отвязанные файлы и просроченные медиасессии;
# --offline-orphans — дополнительно ищет старые файлы без записи в БД. Этот режим запускается только при остановленных backend-процессах, записывающих в это хранилище

import argparse
import logging
import uuid
from datetime import timedelta
from pathlib import Path

from sqlalchemy import and_, delete, or_, update
from sqlmodel import Session, select

from app.core.config import settings
from app.core.db import import_all_models, sqlite_engine
from app.modules.media.models import utc_now_naive
from app.modules.media.session_models import (
    MediaPlaybackSession,
)
from app.modules.media.storage import media_root
from app.modules.media.video_models import MediaVideoFile
from app.modules.media.video_storage import video_path
from app.modules.videos.models import Video

from app.modules.media.models import MediaImage
from app.modules.media.storage import image_path

logger = logging.getLogger(__name__)


def has_no_video_reference():
    return ~(
        select(Video.id)
        .where(
            or_(
                Video.wide_file_id == MediaVideoFile.id,
                Video.mobile_file_id == MediaVideoFile.id,
            )
        )
        .correlate(MediaVideoFile)
        .exists()
    )


def safely_unlink(path: Path) -> None:
    try:
        path.unlink(missing_ok=True)
    except OSError:
        logger.exception(
            "Cannot remove media file: %s",
            path,
        )


def cleanup_database_backed_files(
    *,
    apply: bool,
    batch_size: int,
) -> None:
    now = utc_now_naive()

    upload_cutoff = now - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )
    retired_cutoff = now - timedelta(
        hours=settings.MEDIA_VIDEO_RETIRED_TTL_HOURS,
    )

    unmarked_condition = and_(
        MediaVideoFile.is_attached.is_(True),
        MediaVideoFile.retired_at.is_(None),
        has_no_video_reference(),
    )

    expired_condition = and_(
        has_no_video_reference(),
        or_(
            and_(
                MediaVideoFile.is_attached.is_(False),
                MediaVideoFile.created_at <= upload_cutoff,
            ),
            and_(
                MediaVideoFile.is_attached.is_(True),
                MediaVideoFile.retired_at.is_not(None),
                MediaVideoFile.retired_at <= retired_cutoff,
            ),
        ),
    )

    removed_ids: list[uuid.UUID] = []

    with Session(sqlite_engine) as session:
        unmarked_ids = list(
            session.exec(
                select(MediaVideoFile.id)
                .where(unmarked_condition)
                .limit(batch_size)
            ).all()
        )

        candidate_ids = list(
            session.exec(
                select(MediaVideoFile.id)
                .where(expired_condition)
                .limit(batch_size)
            ).all()
        )

        print(
            "Unreferenced files requiring retirement mark:",
            len(unmarked_ids),
        )
        print(
            "Expired file records eligible for removal:",
            len(candidate_ids),
        )

        if not apply:
            session.rollback()
            return

        try:
            # Файлы, отвязанные старой версией кода,
            # сначала только помечаем.
            # Они получат полный период ожидания с этого момента.
            if unmarked_ids:
                session.execute(
                    update(MediaVideoFile)
                    .where(
                        MediaVideoFile.id.in_(unmarked_ids),
                        unmarked_condition,
                    )
                    .values(retired_at=now)
                    .execution_options(synchronize_session=False)
                )

            for file_id in candidate_ids:
                # Условие повторяется непосредственно в DELETE.
                # Не полагаемся только на предыдущий SELECT.
                result = session.execute(
                    delete(MediaVideoFile)
                    .where(
                        MediaVideoFile.id == file_id,
                        expired_condition,
                    )
                    .execution_options(synchronize_session=False)
                )

                if result.rowcount == 1:
                    removed_ids.append(file_id)

            session.execute(
                delete(MediaPlaybackSession).where(
                    MediaPlaybackSession.expires_at <= now
                )
            )

            session.commit()

        except Exception:
            session.rollback()
            # При неопределённом результате commit
            # физические файлы не трогаем.
            raise

    # Удаление с диска только после успешного commit.
    for file_id in removed_ids:
        safely_unlink(video_path(file_id))

    print("Removed file records:", len(removed_ids))


def cleanup_offline_orphans(*, apply: bool) -> None:
    root = media_root() / "videos"

    if not root.is_dir():
        return

    # Дополнительный консервативный период ожидания.
    grace_hours = 2 * max(
        24,
        settings.MEDIA_UPLOAD_TTL_HOURS,
        settings.MEDIA_VIDEO_RETIRED_TTL_HOURS,
    )

    cutoff = (
        utc_now_naive()
        - timedelta(hours=grace_hours)
    )

    # Файловая mtime представлена Unix timestamp.
    from datetime import timezone

    cutoff_timestamp = cutoff.replace(
        tzinfo=timezone.utc
    ).timestamp()

    orphan_count = 0
    temporary_count = 0

    with Session(sqlite_engine) as session:
        for path in root.glob("[0-9a-f][0-9a-f]/*.mp4"):
            if not path.is_file() or path.is_symlink():
                continue

            try:
                file_id = uuid.UUID(hex=path.stem)
            except ValueError:
                continue

            if (
                path.stem != file_id.hex
                or path.parent.name != file_id.hex[:2]
            ):
                continue

            if path.stat().st_mtime > cutoff_timestamp:
                continue

            if session.get(MediaVideoFile, file_id) is not None:
                continue

            orphan_count += 1

            if apply:
                safely_unlink(path)

    incoming = root / ".incoming"

    if incoming.is_dir():
        for path in incoming.glob(".upload-*.mp4"):
            if not path.is_file() or path.is_symlink():
                continue

            if path.stat().st_mtime > cutoff_timestamp:
                continue

            temporary_count += 1

            if apply:
                safely_unlink(path)

    print("Old files without database records:", orphan_count)
    print("Old incomplete uploads:", temporary_count)

def cleanup_video_images(
    *,
    apply: bool,
    batch_size: int,
) -> None:
    now = utc_now_naive()

    upload_cutoff = now - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )
    retired_cutoff = now - timedelta(
        hours=settings.MEDIA_VIDEO_RETIRED_TTL_HOURS,
    )

    no_reference = ~(
        select(Video.id)
        .where(
            or_(
                Video.image_id == MediaImage.id,
                Video.automatic_image_id == MediaImage.id,
            )
        )
        .correlate(MediaImage)
        .exists()
    )

    unmarked_condition = and_(
        MediaImage.purpose == "video",
        MediaImage.is_attached.is_(True),
        MediaImage.retired_at.is_(None),
        no_reference,
    )

    expired_condition = and_(
        MediaImage.purpose == "video",
        no_reference,
        or_(
            and_(
                MediaImage.is_attached.is_(False),
                MediaImage.created_at <= upload_cutoff,
            ),
            and_(
                MediaImage.is_attached.is_(True),
                MediaImage.retired_at.is_not(None),
                MediaImage.retired_at <= retired_cutoff,
            ),
        ),
    )

    removed_ids = []

    with Session(sqlite_engine) as session:
        unmarked_ids = list(
            session.exec(
                select(MediaImage.id)
                .where(unmarked_condition)
                .limit(batch_size)
            ).all()
        )

        candidate_ids = list(
            session.exec(
                select(MediaImage.id)
                .where(expired_condition)
                .limit(batch_size)
            ).all()
        )

        print(
            "Video images requiring retirement mark:",
            len(unmarked_ids),
        )
        print(
            "Expired video images eligible for removal:",
            len(candidate_ids),
        )

        if not apply:
            session.rollback()
            return

        try:
            if unmarked_ids:
                session.execute(
                    update(MediaImage)
                    .where(
                        MediaImage.id.in_(unmarked_ids),
                        unmarked_condition,
                    )
                    .values(retired_at=now)
                    .execution_options(synchronize_session=False)
                )

            for image_id in candidate_ids:
                result = session.execute(
                    delete(MediaImage)
                    .where(
                        MediaImage.id == image_id,
                        expired_condition,
                    )
                    .execution_options(synchronize_session=False)
                )

                if result.rowcount == 1:
                    removed_ids.append(image_id)

            session.commit()

        except Exception:
            session.rollback()
            raise

    for image_id in removed_ids:
        safely_unlink(image_path(image_id))

    print("Removed video image records:", len(removed_ids))

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean up unused video media safely.",
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes. Without this flag: dry run.",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=500,
    )

    parser.add_argument(
        "--offline-orphans",
        action="store_true",
        help=(
            "Also clean files without DB records. "
            "All backends writing to this storage MUST be stopped."
        ),
    )

    args = parser.parse_args()

    if not 1 <= args.batch_size <= 10000:
        parser.error("--batch-size must be between 1 and 10000")

    logging.basicConfig(level=logging.INFO)

    import_all_models()

    print("Mode:", "APPLY" if args.apply else "DRY RUN")

    cleanup_database_backed_files(
        apply=args.apply,
        batch_size=args.batch_size,
    )

    cleanup_video_images(
        apply=args.apply,
        batch_size=args.batch_size,
    )

    if args.offline_orphans:
        print(
            "OFFLINE MODE: all writers to this media storage "
            "must be stopped."
        )

        cleanup_offline_orphans(
            apply=args.apply,
        )


if __name__ == "__main__":
    main()