# ./backend/alembic/versions/3ea801c72d94_video_playback_sessions.py

"""Add playback sessions and retirement time for video files."""

from alembic import op
import sqlalchemy as sa


revision = "3ea801c72d94"
down_revision = "2d78a4c901be"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("media_video_files") as batch:
        batch.add_column(
            sa.Column(
                "retired_at",
                sa.DateTime(),
                nullable=True,
            )
        )

        batch.create_index(
            "ix_media_video_files_retired_at",
            ["retired_at"],
        )

    op.create_table(
        "media_playback_sessions",
        sa.Column(
            "token_hash",
            sa.String(length=64),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "active_role",
            sa.String(length=32),
            nullable=False,
        ),
        sa.Column(
            "auth_version",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "expires_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "token_hash",
            name="pk_media_playback_sessions",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_media_playback_sessions_user",
            ondelete="CASCADE",
        ),
    )

    op.create_index(
        "ix_media_playback_sessions_user_id",
        "media_playback_sessions",
        ["user_id"],
    )

    op.create_index(
        "ix_media_playback_sessions_expires_at",
        "media_playback_sessions",
        ["expires_at"],
    )


def downgrade() -> None:
    op.drop_table("media_playback_sessions")

    with op.batch_alter_table("media_video_files") as batch:
        batch.drop_index(
            "ix_media_video_files_retired_at",
        )
        batch.drop_column("retired_at")