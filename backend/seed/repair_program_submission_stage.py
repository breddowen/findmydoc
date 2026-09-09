# backend\seed\repair_program_submission_stage.py

import argparse
import uuid

from sqlmodel import Session, select

from app.core.db import (
    import_all_models,
    sqlite_engine,
)
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import (
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)
from app.modules.questionnaires.models import (
    QuestionnaireSubmission,
)


ENROLLMENT_ID = uuid.UUID(
    "858e71c3-b9e6-4318-8da3-8a162731704c"
)

SUBMISSION_ID = uuid.UUID(
    "811aa378-5383-4523-a6b9-946d65ac4ef5"
)

OLD_STAGE_ID = uuid.UUID(
    "1590c02e-a60f-41af-b600-d2c775be48df"
)

NEW_STAGE_ID = uuid.UUID(
    "36247047-9c6b-45bb-93ef-e5755d8ad19e"
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Точечное восстановление связи "
            "попытки опросника с этапом программы."
        )
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Сохранить изменение. Без флага — только проверка.",
    )
    args = parser.parse_args()

    import_all_models()

    with Session(sqlite_engine) as session:
        enrollment = session.get(
            ProgramEnrollment,
            ENROLLMENT_ID,
        )
        submission = session.get(
            QuestionnaireSubmission,
            SUBMISSION_ID,
        )
        target_stage = session.get(
            ProgramStage,
            NEW_STAGE_ID,
        )

        if enrollment is None:
            raise SystemExit("Участие не найдено.")

        if submission is None:
            raise SystemExit("Попытка не найдена.")

        if target_stage is None:
            raise SystemExit("Целевой этап не найден.")

        if submission.patient_id != enrollment.patient_id:
            raise SystemExit(
                "Отказ: попытка принадлежит другому пациенту."
            )

        if (
            submission.program_id != enrollment.program_id
            or target_stage.program_id != enrollment.program_id
        ):
            raise SystemExit(
                "Отказ: программа попытки, участия "
                "и целевого этапа должна совпадать."
            )

        if (
            submission.status
            != QuestionnaireSubmissionStatus.COMPLETED
        ):
            raise SystemExit(
                "Отказ: выбранная попытка не завершена."
            )

        # Не допускаем неоднозначного переноса, если
        # тот же опросник встречается в программе несколько раз.
        matching_items = session.exec(
            select(ProgramStageItem)
            .join(
                ProgramStage,
                ProgramStage.id == ProgramStageItem.stage_id,
            )
            .where(
                ProgramStage.program_id == enrollment.program_id,
                ProgramStageItem.item_type
                == ProgramItemType.QUESTIONNAIRE,
                ProgramStageItem.questionnaire_id
                == submission.questionnaire_id,
            )
        ).all()

        if (
            len(matching_items) != 1
            or matching_items[0].stage_id != target_stage.id
        ):
            raise SystemExit(
                "Отказ: нет единственного подходящего "
                "задания в целевом этапе."
            )

        if submission.program_stage_id == target_stage.id:
            print("Связь уже восстановлена. Изменений нет.")
            return

        if submission.program_stage_id != OLD_STAGE_ID:
            raise SystemExit(
                "Отказ: этап попытки изменился "
                "с момента диагностики."
            )

        if session.get(ProgramStage, OLD_STAGE_ID) is not None:
            raise SystemExit(
                "Отказ: прежний этап ещё существует. "
                "Нельзя считать его потерянным."
            )

        other_completed_id = session.exec(
            select(QuestionnaireSubmission.id)
            .where(
                QuestionnaireSubmission.id != submission.id,
                QuestionnaireSubmission.patient_id
                == submission.patient_id,
                QuestionnaireSubmission.questionnaire_id
                == submission.questionnaire_id,
                QuestionnaireSubmission.program_id
                == submission.program_id,
                QuestionnaireSubmission.program_stage_id
                == target_stage.id,
                QuestionnaireSubmission.status
                == QuestionnaireSubmissionStatus.COMPLETED,
            )
            .limit(1)
        ).first()

        if other_completed_id is not None:
            raise SystemExit(
                "Отказ: в целевом этапе уже есть "
                "другая завершённая попытка. Нужна проверка."
            )

        print(f"Попытка: {submission.id}")
        print(f"Программа: {submission.program_id}")
        print(f"Старый этап: {submission.program_stage_id}")
        print(f"Новый этап: {target_stage.id}")
        print("Ответы, статус и даты не изменяются.")

        if not args.apply:
            print(
                "\nПроверка пройдена. Изменений в базе нет."
            )
            print(
                "Для сохранения повторите запуск с --apply."
            )
            return

        submission.program_stage_id = target_stage.id
        session.add(submission)
        session.commit()

        print("\nСвязь сохранена.")


if __name__ == "__main__":
    main()