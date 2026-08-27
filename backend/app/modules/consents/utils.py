# ./backend/app/modules/consents/utils.py
from app.modules.consents.enums import ConsentType


CONSENT_DOCUMENTS = {
    ConsentType.PERSONAL_DATA_PROCESSING: {
        "title": "Обработка персональных данных",
        "version": "1.0",
        "description": (
            "Я даю согласие на обработку моих "
            "персональных данных для работы сервиса."
        ),
    },
    ConsentType.MEDICAL_DATA_PROCESSING: {
        "title": "Обработка медицинских данных",
        "version": "1.0",
        "description": (
            "Я даю согласие на обработку предоставленных "
            "мной медицинских данных в рамках работы сервиса."
        ),
    },
    ConsentType.ASSISTANT_CONTACT: {
        "title": "Связаться со мной",
        "version": "1.0",
        "description": (
            "Я разрешаю медицинскому ассистенту связаться "
            "со мной, чтобы помочь с записью и ответить "
            "на организационные вопросы."
        ),
    },
}


def get_consent_document(
    consent_type: ConsentType,
) -> dict[str, str] | None:
    return CONSENT_DOCUMENTS.get(consent_type)