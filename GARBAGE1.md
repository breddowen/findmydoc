У меня такой проект:

# Project Structure

> Generated: 2026-08-27 21:11

---

## AI Backend

```
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (41 lines)
backend/app/core/db.py (115 lines)
backend/app/core/email.py (27 lines)
backend/app/core/security.py (232 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (84 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/models.py (115 lines)
backend/app/modules/articles/routers.py (644 lines)
backend/app/modules/articles/schemas.py (89 lines)
backend/app/modules/articles/utils.py (177 lines)
backend/app/modules/assignments/__init__.py (0 lines)
backend/app/modules/assignments/enums.py (14 lines)
backend/app/modules/assignments/models.py (81 lines)
backend/app/modules/assignments/routers.py (302 lines)
backend/app/modules/assignments/schemas.py (56 lines)
backend/app/modules/assignments/utils.py (106 lines)
backend/app/modules/auth/__init__.py (0 lines)
backend/app/modules/auth/models.py (73 lines)
backend/app/modules/auth/routers.py (753 lines)
backend/app/modules/auth/schemas.py (97 lines)
backend/app/modules/auth/utils.py (148 lines)
backend/app/modules/consents/__init__.py (0 lines)
backend/app/modules/consents/enums.py (15 lines)
backend/app/modules/consents/models.py (83 lines)
backend/app/modules/consents/routers.py (277 lines)
backend/app/modules/consents/schemas.py (38 lines)
backend/app/modules/consents/utils.py (37 lines)
backend/app/modules/content/__init__.py (0 lines)
backend/app/modules/content/utils.py (108 lines)
backend/app/modules/events/__init__.py (0 lines)
backend/app/modules/events/enums.py (31 lines)
backend/app/modules/events/models.py (83 lines)
backend/app/modules/events/routers.py (69 lines)
backend/app/modules/events/schemas.py (32 lines)
backend/app/modules/events/service.py (54 lines)
backend/app/modules/invitations/__init__.py (0 lines)
backend/app/modules/invitations/enums.py (15 lines)
backend/app/modules/invitations/models.py (121 lines)
backend/app/modules/invitations/routers.py (957 lines)
backend/app/modules/invitations/schemas.py (143 lines)
backend/app/modules/invitations/utils.py (215 lines)
backend/app/modules/notifications/__init__.py (0 lines)
backend/app/modules/notifications/enums.py (30 lines)
backend/app/modules/notifications/models.py (64 lines)
backend/app/modules/notifications/routers.py (288 lines)
backend/app/modules/notifications/schemas.py (47 lines)
backend/app/modules/notifications/service.py (163 lines)
backend/app/modules/patients/__init__.py (0 lines)
backend/app/modules/patients/enums.py (7 lines)
backend/app/modules/patients/routers.py (511 lines)
backend/app/modules/patients/schemas.py (138 lines)
backend/app/modules/patients/utils.py (231 lines)
backend/app/modules/programs/__init__.py (0 lines)
backend/app/modules/programs/enums.py (27 lines)
backend/app/modules/programs/models.py (332 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1509 lines)
backend/app/modules/programs/schemas.py (296 lines)
backend/app/modules/programs/utils.py (576 lines)
backend/app/modules/questionnaires/__init__.py (0 lines)
backend/app/modules/questionnaires/enums.py (17 lines)
backend/app/modules/questionnaires/json_q/audit.json (272 lines)
backend/app/modules/questionnaires/models.py (226 lines)
backend/app/modules/questionnaires/Readme.md (61 lines)
backend/app/modules/questionnaires/routers.py (1197 lines)
backend/app/modules/questionnaires/schemas.py (213 lines)
backend/app/modules/questionnaires/utils.py (303 lines)
backend/app/modules/referrals/__init__.py (0 lines)
backend/app/modules/referrals/enums.py (19 lines)
backend/app/modules/referrals/models.py (114 lines)
backend/app/modules/referrals/routers.py (463 lines)
backend/app/modules/referrals/schemas.py (83 lines)
backend/app/modules/referrals/utils.py (42 lines)
backend/app/modules/relationships/__init__.py (0 lines)
backend/app/modules/relationships/routers.py (580 lines)
backend/app/modules/relationships/schemas.py (79 lines)
backend/app/modules/specialities/__init__.py (0 lines)
backend/app/modules/specialities/routers.py (191 lines)
backend/app/modules/specialities/schemas.py (44 lines)
backend/app/modules/tags/__init__.py (0 lines)
backend/app/modules/tags/enums.py (7 lines)
backend/app/modules/tags/models.py (124 lines)
backend/app/modules/tags/routers.py (610 lines)
backend/app/modules/tags/schemas.py (73 lines)
backend/app/modules/tags/utils.py (214 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (331 lines)
backend/app/modules/users/routers.py (239 lines)
backend/app/modules/users/schemas.py (89 lines)
backend/app/modules/users/utils.py (126 lines)
backend/requirements.txt (39 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database.db (1193 lines)
```

*Files: 104*

---

## Frontend

### components

```
frontend/app/components/articles/Form.vue (233 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (291 lines)
frontend/app/components/assignments/ContentPicker.vue (181 lines)
frontend/app/components/assignments/CreateDialog.vue (345 lines)
frontend/app/components/assignments/PatientList.vue (108 lines)
frontend/app/components/assignments/PickerItem.vue (130 lines)
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (295 lines)
frontend/app/components/content/RichTextEditor.vue (469 lines)
frontend/app/components/content/RichTextRenderer.vue (136 lines)
frontend/app/components/content/TagSelector.vue (80 lines)
frontend/app/components/invitations/LinkDialog.vue (162 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (87 lines)
frontend/app/components/layout/Footer.vue (48 lines)
frontend/app/components/layout/Navbar.vue (384 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (107 lines)
frontend/app/components/patients/List.vue (242 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/programs/configurator/Editor.vue (694 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (272 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/PatientAccess.vue (231 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (380 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (529 lines)
frontend/app/components/questionnaires/JsonImporter.vue (264 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/ui/BottomSheet.vue (203 lines)
frontend/app/components/ui/ContentSkeleton.vue (73 lines)
frontend/app/components/ui/Modal.vue (150 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (90 lines)
```
*Files: 40*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (43 lines)
frontend/app/pages/content/articles/index.vue (169 lines)
frontend/app/pages/content/articles/new.vue (49 lines)
frontend/app/pages/content/questionnaires/[id].vue (319 lines)
frontend/app/pages/content/questionnaires/index.vue (166 lines)
frontend/app/pages/content/questionnaires/new.vue (9 lines)
frontend/app/pages/dashboard.vue (168 lines)
frontend/app/pages/forgot-password.vue (102 lines)
frontend/app/pages/index.vue (3 lines)
frontend/app/pages/login.vue (238 lines)
frontend/app/pages/patients/[id]/index.vue (465 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (30 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (359 lines)
frontend/app/pages/programs/index.vue (284 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (364 lines)
frontend/app/pages/questionnaires/index.vue (151 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/settings/security.vue (323 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 23*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (18 lines)
```
*Files: 2*

### composables

```
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useProgramPrice.js (67 lines)
frontend/app/composables/useReadingProgress.js (178 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 6*

### stores

```
frontend/app/stores/articles.js (106 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/notifications.js (312 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (174 lines)
frontend/app/stores/ui.js (62 lines)
frontend/app/stores/user.js (71 lines)
```
*Files: 9*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/program-manager.js (19 lines)
```
*Files: 2*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*


--------------
проблема в том, что после заполнения опросника внутри программы, у варча/суперпользователя пишет, что пациент не начинал заполнение опросника

(venv_emc_commercial) PS F:\Soft\!Laptops\~~EMC_projects\COMMERCIAL\COMMERCIAL_PROJ_0\backend> python -c "from sqlmodel import Session, select; from app.core.db import sqlite_engine; from app.modules.questionnaires.models import QuestionnaireSubmission; s=Session(sqlite_engine); rows=s.exec(select(QuestionnaireSubmission).order_by(QuestionnaireSubmission.started_at.desc()).limit(5)).all(); print([(str(x.id), str(x.program_id), str(x.program_stage_id), x.status) for x in rows]); s.close()"
[('d1234741-e276-4abe-b5a5-dda91ea8beb4', 'None', 'None', <QuestionnaireSubmissionStatus.COMPLETED: 'completed'>), ('e0fee7fb-5f6c-4ae9-aac1-7ab7b7bd066b', 'None', 'None', <QuestionnaireSubmissionStatus.COMPLETED: 'completed'>), ('7890681a-09dc-4021-a01f-53d66b3eabb4', 'None', 'None', <QuestionnaireSubmissionStatus.COMPLETED: 'completed'>), ('dd8a330f-daa6-4bcb-ac42-c0e8c1123ed9', 'None', 'None', <QuestionnaireSubmissionStatus.IN_PROGRESS: 'in_progress'>), ('0f75e476-3482-40f8-bf67-56a70a561169', 'None', 'None', <QuestionnaireSubmissionStatus.COMPLETED: 'completed'>)]

снчала напиши, какие файлы тебе надо прислать, чтобы их проверить

----------------------------
































супер! все работает!
Теперь надо добавить функционал для добавления файлов: картинок и видео

1. Директория с медиа пусть будет в ./app/backend/media/ или как ты посоветуешь...
2. Картинки: фото врачей - открытый путь, тизеры для карточек статей и оросников... ну, давай тоже сделаем открытым путем
3. Видео: планируются короткие ролики для описания статей/опросников/программ/этапов программ. Для широких экранов - одно разрешение видео, для мобильных устройств - другое. Я думаю, тут надо сделать пути видео закрытыми, чтобы если пациент не имеет доступа к программе/статье/опроснику, он не мог возспользоваться url со ссылкой к видео
4. Желательно, чтобы при загрузке изображения, всплывало модальное окно либо bottomsheet на мобильных устройствах с возможностью обрезки изображения по каким-то параметрам. Давай сделаем фото врачей, наверное, 4:3, а для статей ну, как то, горизонтально. Пусть редактор фото будет в отдельном компоненте и в параметрах там будут отдельно прописано разрешение для разных задач. Желательно сделать компонент по редактированию изображения переиспользуемым, чтобы потом, например, если я захочу сделать еще и изображения внутрь статей, я мог минимально там писать код.
Модальное окно (для широких дисплеев) компонент такой:
<!-- ./frontend/app/components/ui/Modal.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true,
  },
  showCloseButton: {
    type: Boolean,
    default: true,
  },
  maxWidthClass: {
    type: String,
    default: 'max-w-lg',
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

useBodyScrollLock(opened)

function close() {
  model.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
    emit('opened')
  }
})

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'keydown',
    handleKeydown,
  )
})
</script>

<template>
  <Teleport to="body">
    <Transition name="ui-modal">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 relative flex max-h-[calc(100dvh-2rem)] w-full flex-col overflow-hidden rounded-2xl shadow-2xl"
          :class="maxWidthClass"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-5 py-4"
          >
            <slot name="header">
              <h2 class="min-w-0 flex-1 text-lg font-semibold">
                {{ title }}
              </h2>
            </slot>

            <button
              v-if="showCloseButton"
              type="button"
              class="btn btn-circle btn-ghost btn-sm shrink-0"
              aria-label="Закрыть"
              @click="close"
            >
              <Icon
                name="lucide:x"
                class="size-5"
              />
            </button>
          </header>

          <div class="min-h-0 flex-1 overflow-y-auto px-5 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-5 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-modal-enter-active,
.ui-modal-leave-active {
  transition: opacity 180ms ease;
}

.ui-modal-enter-active section,
.ui-modal-leave-active section {
  transition:
    transform 180ms ease,
    opacity 180ms ease;
}

.ui-modal-enter-from,
.ui-modal-leave-to {
  opacity: 0;
}

.ui-modal-enter-from section,
.ui-modal-leave-to section {
  opacity: 0;
  transform: scale(0.96) translateY(0.5rem);
}
</style>
bottomsheet для мобильных устройств такое:
<!-- ./frontend/app/components/ui/BottomSheet.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true,
  },
  showCloseButton: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

const translateY = ref(0)
const dragging = ref(false)

let pointerStartY = 0

useBodyScrollLock(opened)

const sheetStyle = computed(() => ({
  transform: translateY.value
    ? `translateY(${translateY.value}px)`
    : undefined,
  transition: dragging.value
    ? 'none'
    : 'transform 180ms ease',
}))

function close() {
  model.value = false
  translateY.value = 0
  dragging.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handlePointerDown(event) {
  dragging.value = true
  pointerStartY = event.clientY

  event.currentTarget.setPointerCapture?.(
    event.pointerId,
  )
}

function handlePointerMove(event) {
  if (!dragging.value) return

  translateY.value = Math.max(
    0,
    event.clientY - pointerStartY,
  )
}

function handlePointerUp() {
  if (!dragging.value) return

  dragging.value = false

  if (translateY.value > 100) {
    close()
    return
  }

  translateY.value = 0
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
    translateY.value = 0
    emit('opened')
  }
})

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'keydown',
    handleKeydown,
  )
})
</script>

<template>
  <Teleport to="body">
    <Transition name="ui-sheet">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-end bg-black/50 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 safe-area-bottom flex max-h-[92dvh] w-full flex-col overflow-hidden rounded-t-3xl shadow-2xl"
          :style="sheetStyle"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <div
            class="flex shrink-0 touch-none justify-center py-3"
            @pointerdown="handlePointerDown"
            @pointermove="handlePointerMove"
            @pointerup="handlePointerUp"
            @pointercancel="handlePointerUp"
          >
            <div
              class="bg-base-300 h-1.5 w-12 rounded-full"
            />
          </div>

          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-4 pb-4"
          >
            <slot name="header">
              <h2 class="min-w-0 flex-1 text-lg font-semibold">
                {{ title }}
              </h2>
            </slot>

            <button
              v-if="showCloseButton"
              type="button"
              class="btn btn-circle btn-ghost btn-sm shrink-0"
              aria-label="Закрыть"
              @click="close"
            >
              <Icon
                name="lucide:x"
                class="size-5"
              />
            </button>
          </header>

          <div class="min-h-0 flex-1 overflow-y-auto px-4 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-4 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-sheet-enter-active,
.ui-sheet-leave-active {
  transition: opacity 220ms ease;
}

.ui-sheet-enter-active section,
.ui-sheet-leave-active section {
  transition: transform 220ms ease;
}

.ui-sheet-enter-from,
.ui-sheet-leave-to {
  opacity: 0;
}

.ui-sheet-enter-from section,
.ui-sheet-leave-to section {
  transform: translateY(100%);
}
</style>

Фото желательно при загрузке сразу конвертировать в webp

функционал для media давай сделаем в виде отдельного модуля на бекенде. Пусть путь к медиа папке будет прописан в .env, чтобы если я решу его изменить, я пог это задать в одном месте.

Хотелось бы, сделать также опитмальную загрузку для видео, но я не знаю, насколко это оправдано. Ролики планируются короткие. Хотелось бы иметь возможность делать drag and drop видео в этапы программы также, как я это делаю со статьями и опросниками, чтобы все было гибко. Главное видео к программе даже не знаю как сделать... ну, можно тоже drag and drop или по кнопке, это как решишь.

Еще очень хочется дселать разное соотношение сторон видео отдельно для мобильных устройств и для широких экранов. Разумеется, я сам буду обрезать видео под 2 разных рарешения и грузить их отдельно. Но надо как-то предусмотреть функционал раздельной загрузки и воспроизведения разного видео. 

Плюс, лучше сделать какую-то защиту от слишком больших файлоы, которые будут тормозить вервис (если они будут его торомозить). У меня вообще нет опыта разоты с видеоконтентом. Я знаю, что картинки для веб-приложения опитально .webp, а как правильно работать с видео - вообще не знаю... Поэтому, как ты посоветуешь.

Если тебе нужны какие-то файлы проекта, попроси их прислать. не надо гадать

И для начала, задай мне вопросы по функционалу, если они у тебя есть. И опиши примерный объем работы и вообще, осуществимо ли загрузка видео, как я описал.