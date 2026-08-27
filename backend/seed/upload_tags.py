# ./backend/seed/upload_tags.py
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlmodel import Session, select


BACKEND_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = Path(__file__).resolve().parent / "data" / "tags.json"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.core.db import init_sqlite_db, sqlite_engine  # noqa: E402
from app.modules.tags.models import (  # noqa: E402
    SpecialityTagLink,
    Tag,
)
from app.modules.users.models import Speciality  # noqa: E402


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def load_seed_data() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def upload_tags() -> None:
    init_sqlite_db()
    data = load_seed_data()

    with Session(sqlite_engine) as session:
        tags_by_name: dict[str, Tag] = {}

        for tag_data in data["tags"]:
            normalized_name = tag_data["name"].strip().lower()

            tag = session.exec(
                select(Tag).where(Tag.name == normalized_name)
            ).first()

            if not tag:
                tag = Tag(
                    name=normalized_name,
                    description=tag_data.get("description"),
                    is_system=bool(
                        tag_data.get("is_system", False)
                    ),
                )
                session.add(tag)
                session.flush()
            else:
                tag.description = tag_data.get("description")
                tag.is_system = bool(
                    tag_data.get("is_system", False)
                )
                tag.updated_at = utc_now()
                session.add(tag)

            tags_by_name[normalized_name] = tag
            print(f"✓ Tag synchronized: {normalized_name}")

        for speciality_name, tag_names in data[
            "speciality_tags"
        ].items():
            speciality = session.exec(
                select(Speciality).where(
                    Speciality.name == speciality_name
                )
            ).first()

            if not speciality:
                print(
                    "⚠ Speciality not found, skipped: "
                    f"{speciality_name}"
                )
                continue

            for tag_name in tag_names:
                normalized_tag_name = tag_name.strip().lower()
                tag = tags_by_name.get(normalized_tag_name)

                if not tag:
                    print(
                        "⚠ Tag not found, skipped: "
                        f"{normalized_tag_name}"
                    )
                    continue

                link = session.exec(
                    select(SpecialityTagLink).where(
                        SpecialityTagLink.speciality_id
                        == speciality.id,
                        SpecialityTagLink.tag_id == tag.id,
                    )
                ).first()

                if not link:
                    session.add(
                        SpecialityTagLink(
                            speciality_id=speciality.id,
                            tag_id=tag.id,
                        )
                    )

                print(
                    f"✓ {speciality.name} -> {tag.name}"
                )

        session.commit()

    print()
    print("Tag seed completed successfully.")


if __name__ == "__main__":
    upload_tags()