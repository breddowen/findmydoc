теперь смотри, мне надо сделать еще один .ps1 файл, где будет возможность выгружать следующее:
# ./backend/app/modules/ai_agents/actions.py - в каждом файле проекта на первой строке в комментарии указан путь к файлу. его надо выгрузить в самом начале
Далее, все импорты:
from datetime import datetime
import hashlib
import json

from fastapi.encoders import (
    jsonable_encoder
)

from sqlmodel import (
    Session,
    select
)

from ..audit.utils import (
    create_audit_log
)

from ..users.models import (
    User
)

from .enums import (
    AgentActionType,
    AgentActionStatus
)

from .models import (
    AgentAction
)
а далее надо у каждой функции взять начало и конец без тела, но с комментариями в самом начале, например:

def build_action_tool_call_id(
    assistant_message_id: str,
    payload: dict
) -> str:
"""
тут какой-то комментарий
"""
    serialized = json.dumps(
        jsonable_encoder(payload),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":")
    )

    digest = hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()[:24]

    return (
        f"{assistant_message_id}:"
        f"{digest}"
    )

надо сделать так:
def build_action_tool_call_id(
    assistant_message_id: str,
    payload: dict
) -> str:
    
тут написать что-то типа: FUNCTION BODY

    return (
        f"{assistant_message_id}:"
        f"{digest}"
    )

Если у нас модели, то их надо выгружать полностью
Если schemas, то тоже полностью
Если routers, то верх тоже надо:
@router.post(
    "/message",
    response_model=ChatMessageResult
)
async def agent_message(
    data: ChatMessageRequest,
    session: Session = Depends(
        get_session
    ),
    current_user: User = Depends(
        get_current_user
    )
):
"""
тут какой-то комментарий
"""
    тут написать что-то типа: FUNCTION BODY

        return {
            "content": result.content,
            "chat_id": chat.id,
            "user_message_id": (
                user_message.id
            ),
            "assistant_message_id": (
                assistant_message.id
            ),
            "model_name": (
                generation_context
                .model
                .name
            ),
            "prompt_id": None
        }

    except Exception as error:
        error_traceback = (
            traceback.format_exc()
        )

        logger.exception(
            "Agent message failed. "
            "chat_id=%s user_id=%s",
            chat.id,
            current_user.id
        )

        fail_assistant_message(
            session=session,
            chat=chat,
            message=assistant_message,
            error_message=error_traceback
        )

        raise HTTPException(
            status_code=(
                status.HTTP_500_INTERNAL_SERVER_ERROR
            ),
            detail=(
                str(error)
                or error.__class__.__name__
            )
        ) from error

аналогично, если это @tool

@tool
def find_patients(
    runtime: ToolRuntime[
        AgentRuntimeContext
    ],
    query: str,
    limit: int = 20
) -> list[dict]:
    """
    Найти пациентов по ФИО, отдельной
    части имени, email или номеру карты.

    Если найдено несколько пациентов,
    не выбирать одного самостоятельно.
    """
 тут написать что-то типа: FUNCTION BODY
return [
            serialize_patient(
                user=user,
                profile=profile
            )
            for user, profile in rows
        ]
если class, то полностью:
class SuperuserAgentState(
    TypedDict,
    total=False
):
    """
    Состояние родительского графа.

    В отличие от состояния subgraphs,
    messages не использует add_messages.
    Каждый запуск заменяет его новым
    ограниченным контекстом.
    """

    source_message_id: str

    assistant_message_id: str

    conversation_messages: list[
        BaseMessage
    ]

    messages: list[BaseMessage]

    route: SuperuserAgentRoute

    previous_route: (
        SuperuserAgentRoute | None
    )

    intent_summary: str

    handoff_context: str

    clarification_question: (
        str | None
    )

    patient_context_active: bool

    patient_profile_id: str | None

    patient_name: str | None

    patient_record_id: str | None

    context_version: str

    memory_items: list[
        dict[str, Any]
    ]

    recent_tool_results: list[
        dict[str, Any]
    ]

    web_sources: list[
        WebSourceState
    ]

    final_response: str

    tool_iterations: int

Плюс, хотелось бы, в виде дополнительного параметра указывать предел строк кода. Допустим, я укажу верхний предел 1000, значит, если строк кода меньше 1000, то файл выгружается полностью, а если больше 1000, то только так, как я описал выше. Если параметр не указан, то все выгружаются в урезанном формате (как я описал выше)

Напиши сразу готовый файл. Наверное, давай сделаем его в .py формате и пусть будет такой функционал:
Он будет поддерживать примерно такой интерфейс:

PowerShell

python export_context.py
или

PowerShell

python export_context.py backend
или

PowerShell

python export_context.py backend/app/modules
или

PowerShell

python export_context.py backend/app/modules --max-lines 1000
или

PowerShell

python export_context.py backend/app/modules/ai_agents
Логика будет такой:

если файл ≤ --max-lines → выгружается полностью;
если файл > --max-lines → сокращенный режим;
если --max-lines не указан → все файлы в сокращенном режиме.
Для сокращенного режима:

первая строка (# ./path/to/file.py);
затем все imports;
затем:
class — полностью;
models.py — полностью;
schemas.py — полностью;
BaseModel, SQLModel, TypedDict, Enum и любые другие классы — полностью;
функции:
decorators;
сигнатура;
docstring;
FUNCTION BODY;
последний return/raise/yield, если есть.