# ./backend/alembic/versions/49b2d70c8e16_video_posters.py

"""Add manual and automatic video posters."""

from alembic import op
import sqlalchemy as sa


revision = "49b2d70c8e16"
down_revision = "3ea801c72d94"
branch_labels = None
depends_on = None


OLD_PURPOSE_CHECK = (
    "purpose IN ("
    "'doctor', "
    "'article', "
    "'questionnaire', "
    "'program', "
    "'life_aspect'"
    ")"
)

NEW_PURPOSE_CHECK = (
    "purpose IN ("
    "'doctor', "
    "'article', "
    "'questionnaire', "
    "'program', "
    "'life_aspect', "
    "'video'"
    ")"
)


def upgrade() -> None:
    with op.batch_alter_table("media_images") as batch:
        batch.drop_constraint(
            "ck_media_images_purpose",
            type_="check",
        )

        batch.create_check_constraint(
            "ck_media_images_purpose",
            NEW_PURPOSE_CHECK,
        )

        batch.add_column(
            sa.Column(
                "retired_at",
                sa.DateTime(),
                nullable=True,
            )
        )

        batch.create_index(
            "ix_media_images_retired_at",
            ["retired_at"],
        )

    with op.batch_alter_table("videos") as batch:
        for column_name in ("image_id", "automatic_image_id"):
            batch.add_column(
                sa.Column(
                    column_name,
                    sa.Uuid(),
                    nullable=True,
                )
            )

            batch.create_foreign_key(
                f"fk_videos_{column_name}_media_images",
                "media_images",
                [column_name],
                ["id"],
                ondelete="RESTRICT",
            )

            batch.create_index(
                f"ix_videos_{column_name}",
                [column_name],
            )


def downgrade() -> None:
    # Не удаляем пользовательские обложки молча.
    count = op.get_bind().execute(
        sa.text(
            "SELECT COUNT(*) FROM media_images "
            "WHERE purpose = 'video'"
        )
    ).scalar_one()

    if count:
        raise RuntimeError(
            "Нельзя откатить миграцию, пока существуют "
            "изображения с purpose='video'. "
            "Сначала требуется отдельный план удаления "
            "или переноса этих данных."
        )

    with op.batch_alter_table("videos") as batch:
        for column_name in ("automatic_image_id", "image_id"):
            batch.drop_index(
                f"ix_videos_{column_name}",
            )

            batch.drop_constraint(
                f"fk_videos_{column_name}_media_images",
                type_="foreignkey",
            )

            batch.drop_column(column_name)

    with op.batch_alter_table("media_images") as batch:
        batch.drop_index(
            "ix_media_images_retired_at",
        )
        batch.drop_column("retired_at")

        batch.drop_constraint(
            "ck_media_images_purpose",
            type_="check",
        )

        batch.create_check_constraint(
            "ck_media_images_purpose",
            OLD_PURPOSE_CHECK,
        )