# backend\seed\check_program_progress.py
# python -m seed.check_program_progress
import uuid

from sqlmodel import Session, select

from app.core.db import (
    import_all_models,
    sqlite_engine,
)
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import (
    Program,
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
)
from app.modules.questionnaires.models import (
    QuestionnaireSubmission,
)


ENROLLMENT_ID = uuid.UUID(
    "858e71c3-b9e6-4318-8da3-8a162731704c"
)


def main() -> None:
    import_all_models()

    # Только чтение:
    # не создаём таблицы, не меняем записи,
    # не вызываем commit.
    with Session(sqlite_engine) as session:
        enrollment = session.get(
            ProgramEnrollment,
            ENROLLMENT_ID,
        )

        if enrollment is None:
            raise SystemExit(
                "Участие не найдено. "
                "Проверьте выбранную базу и ENROLLMENT_ID."
            )

        program = session.get(
            Program,
            enrollment.program_id,
        )

        if program is None:
            raise SystemExit("Программа не найдена.")

        print(f"Программа: {program.id}")
        print(f"Участие: {enrollment.id}")
        print(f"Статус: {enrollment.status.value}")
        print(f"Завершена: {enrollment.completed_at}")

        rows = session.exec(
            select(ProgramStageItem, ProgramStage)
            .join(
                ProgramStage,
                ProgramStage.id
                == ProgramStageItem.stage_id,
            )
            .where(
                ProgramStage.program_id == program.id,
                ProgramStageItem.item_type
                == ProgramItemType.QUESTIONNAIRE,
            )
            .order_by(
                ProgramStage.order_index,
                ProgramStageItem.order_index,
            )
        ).all()

        if not rows:
            print("\nВ программе нет опросников.")
            return

        for item, stage in rows:
            print("\n" + "-" * 60)
            print(f"Опросник: {item.questionnaire_id}")
            print(f"Текущий этап: {stage.id}")

            # Намеренно ищем шире рабочего алгоритма:
            # все попытки этого пациента по опроснику.
            # Так увидим попытки со старым этапом,
            # другой программой или без привязки.
            submissions = session.exec(
                select(QuestionnaireSubmission)
                .where(
                    QuestionnaireSubmission.patient_id
                    == enrollment.patient_id,
                    QuestionnaireSubmission.questionnaire_id
                    == item.questionnaire_id,
                )
                .order_by(
                    QuestionnaireSubmission.started_at.desc()
                )
            ).all()

            if not submissions:
                print("Попыток не найдено.")
                continue

            for submission in submissions:
                matches_current_context = (
                    submission.program_id == program.id
                    and submission.program_stage_id == stage.id
                )

                print(
                    "\nПопытка:",
                    submission.id,
                )
                print(
                    "  Статус:",
                    submission.status.value,
                )
                print(
                    "  Программа:",
                    submission.program_id,
                )
                print(
                    "  Этап:",
                    submission.program_stage_id,
                )
                print(
                    "  Завершена:",
                    submission.completed_at,
                )
                print(
                    "  Совпадает с текущей программой и этапом:",
                    matches_current_context,
                )


if __name__ == "__main__":
    main()