"""Attach media images to doctors and content."""

from alembic import op
import sqlalchemy as sa


revision = "f7a2d9c103b8"
down_revision = "e4b7c2a901f6"
branch_labels = None
depends_on = None


TABLES = (
    "doctor_profiles",
    "articles",
    "questionnaires",
    "programs",
    "life_aspects",
)


def upgrade() -> None:
    for table_name in TABLES:
        with op.batch_alter_table(table_name) as batch:
            batch.add_column(
                sa.Column(
                    "image_id",
                    sa.Uuid(),
                    nullable=True,
                )
            )

            batch.create_foreign_key(
                f"fk_{table_name}_image_id_media_images",
                "media_images",
                ["image_id"],
                ["id"],
                ondelete="RESTRICT",
            )

            batch.create_index(
                f"ix_{table_name}_image_id",
                ["image_id"],
                unique=False,
            )


def downgrade() -> None:
    for table_name in reversed(TABLES):
        with op.batch_alter_table(table_name) as batch:
            batch.drop_index(
                f"ix_{table_name}_image_id",
            )

            batch.drop_constraint(
                f"fk_{table_name}_image_id_media_images",
                type_="foreignkey",
            )

            batch.drop_column("image_id")