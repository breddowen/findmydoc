<!-- ./frontend/app/components/test-styles/Editor.vue -->
<script setup>
import {
  FONT_OPTIONS,
  cloneStyles,
  createDefaultStyles,
  downloadStyles,
} from '~/utils/test-styles'

const styles = useTestStylesStore()

const theme = ref('light')
const draft = ref(createDefaultStyles())
const name = ref('')
const comment = ref('')

const error = ref('')
const notice = ref('')
const deleteOpen = ref(false)

function loadSaved() {
  draft.value = styles.saved
    ? cloneStyles(styles.saved.settings)
    : createDefaultStyles()

  name.value = styles.saved?.name || ''
  comment.value = styles.saved?.comment || ''
}

loadSaved()

const savedState = computed(() => JSON.stringify({
  settings: styles.saved?.settings || createDefaultStyles(),
  name: styles.saved?.name || '',
  comment: styles.saved?.comment || '',
}))

const draftState = computed(() => JSON.stringify({
  settings: draft.value,
  name: name.value,
  comment: comment.value,
}))

const dirty = computed(() =>
  draftState.value !== savedState.value,
)

const statusLabel = computed(() => {
  if (!styles.hasCustomStyles) {
    return 'Используется исходное оформление'
  }

  return styles.enabled
    ? 'Сохранённый вариант применяется на сайте'
    : 'Исходное оформление · ваш вариант сохранён'
})

function clearMessages() {
  error.value = ''
  notice.value = ''
}

function save() {
  clearMessages()

  try {
    styles.save(
      draft.value,
      name.value,
      comment.value,
    )

    loadSaved()

    notice.value = styles.hasCustomStyles
      ? 'Сохранено. Оформление применяется на всех страницах.'
      : 'Сохранено исходное оформление.'
  } catch (cause) {
    error.value = cause.message
  }
}

function cancelDraft() {
  clearMessages()
  loadSaved()
  notice.value = 'Несохранённые изменения отменены.'
}

function useOriginalInDraft() {
  clearMessages()
  draft.value = createDefaultStyles()

  notice.value = (
    'Исходные значения загружены в предпросмотр. '
    + 'Сайт изменится только после сохранения.'
  )
}

function toggleStyles() {
  clearMessages()

  try {
    styles.toggle()
  } catch (cause) {
    error.value = cause.message
  }
}

function removeStyles() {
  clearMessages()

  try {
    styles.remove()
    loadSaved()
    deleteOpen.value = false
    notice.value = 'Локальная настройка удалена.'
  } catch (cause) {
    deleteOpen.value = false
    error.value = cause.message
  }
}

async function copyCss() {
  clearMessages()

  try {
    if (!navigator.clipboard?.writeText) {
      throw new Error(
        'Копирование недоступно. Используйте «Скачать main.css».',
      )
    }

    await navigator.clipboard.writeText(styles.exportCss)
    notice.value = 'CSS сохранённого варианта скопирован.'
  } catch (cause) {
    error.value = cause.message || (
      'Браузер запретил копирование. '
      + 'Используйте «Скачать main.css».'
    )
  }
}

function downloadCss() {
  clearMessages()

  try {
    downloadStyles(styles.exportCss)
  } catch {
    error.value = 'Не удалось скачать файл.'
  }
}

function beforeUnload(event) {
  if (!dirty.value) return

  event.preventDefault()
  event.returnValue = ''
}

onMounted(() => {
  window.addEventListener('beforeunload', beforeUnload)
})

onBeforeUnmount(() => {
  window.removeEventListener('beforeunload', beforeUnload)
})

onBeforeRouteLeave(() => {
  if (!dirty.value) return true

  return window.confirm(
    'Есть несохранённые изменения. Покинуть студию?',
  )
})
</script>

<template>
  <div v-if="styles.available" class="space-y-6">
    <header class="space-y-3">
      <div class="flex flex-wrap items-center gap-3">
        <div class="bg-primary/10 text-primary flex size-11 items-center justify-center rounded-2xl">
          <Icon name="lucide:palette" class="size-6" />
        </div>

        <div>
          <h1 class="text-2xl font-bold">
            Студия оформления
          </h1>

          <p class="text-base-content/60 text-sm">
            Локальный вариант · только в вашем браузере
          </p>
        </div>
      </div>

      <p class="text-base-content/70 max-w-3xl text-sm">
        Изменяйте светлую и тёмную темы, проверяйте результат
        в предпросмотре, затем сохраняйте. Другие пользователи
        и исходный файл сайта не изменяются.
      </p>
    </header>

    <div
      v-if="styles.storageError"
      class="alert alert-warning"
      role="alert"
    >
      <span>{{ styles.storageError }}</span>
    </div>

    <div v-if="error" class="alert alert-error" role="alert">
      <span>{{ error }}</span>
    </div>

    <div v-if="notice" class="alert alert-info" role="status">
      <span>{{ notice }}</span>
    </div>

    <section class="bg-base-100 border-base-300 space-y-4 rounded-2xl border p-4 sm:p-5">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div>
          <p class="font-medium">{{ statusLabel }}</p>

          <p class="text-base-content/60 mt-1 text-sm">
            {{ dirty ? 'Есть несохранённые изменения' : 'Черновик совпадает с сохранённым вариантом' }}
          </p>
        </div>

        <button
          v-if="styles.hasCustomStyles"
          type="button"
          class="btn btn-outline btn-sm"
          @click="toggleStyles"
        >
          <Icon name="lucide:rotate-ccw" class="size-4" />
          {{ styles.enabled ? 'Сбросить стили' : 'Вернуть стили' }}
        </button>
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          type="button"
          class="btn btn-primary"
          :disabled="!dirty && Boolean(styles.saved)"
          @click="save"
        >
          <Icon name="lucide:save" class="size-4" />
          Сохранить и применить
        </button>

        <button
          type="button"
          class="btn btn-ghost"
          :disabled="!dirty"
          @click="cancelDraft"
        >
          Отменить изменения
        </button>
      </div>
    </section>

    <div class="grid items-start gap-6 xl:grid-cols-[minmax(0,1.1fr)_minmax(0,0.9fr)]">
      <div class="min-w-0 space-y-6">
        <section class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-5">
          <div class="mb-6 flex flex-wrap items-center justify-between gap-3">
            <h2 class="font-semibold">Настройка темы</h2>

            <div class="join" role="group" aria-label="Редактируемая тема">
              <button
                type="button"
                class="btn btn-sm join-item"
                :class="theme === 'light' ? 'btn-primary' : 'btn-ghost'"
                :aria-pressed="theme === 'light'"
                @click="theme = 'light'"
              >
                <Icon name="lucide:sun" class="size-4" />
                Светлая
              </button>

              <button
                type="button"
                class="btn btn-sm join-item"
                :class="theme === 'dark' ? 'btn-primary' : 'btn-ghost'"
                :aria-pressed="theme === 'dark'"
                @click="theme = 'dark'"
              >
                <Icon name="lucide:moon" class="size-4" />
                Тёмная
              </button>
            </div>
          </div>

          <TestStylesThemeFields
            :key="theme"
            v-model="draft.themes[theme]"
          />
        </section>

        <section class="bg-base-100 border-base-300 space-y-4 rounded-2xl border p-4 sm:p-5">
          <label class="flex items-center justify-between gap-4">
            <span>
              <span class="block font-semibold">Типографика</span>

              <span class="text-base-content/60 mt-1 block text-sm">
                Общая для обеих тем
              </span>
            </span>

            <input
              v-model="draft.typography.enabled"
              type="checkbox"
              class="toggle toggle-primary"
              aria-label="Изменять типографику"
            >
          </label>

          <p class="text-base-content/60 text-sm">
            Если выключено, сохраняются исходные шрифты.
            Размер влияет на корневую единицу rem, поэтому
            после применения могут измениться и размеры элементов.
          </p>

          <div v-if="draft.typography.enabled" class="space-y-5">
            <label class="block">
              <span class="mb-2 block text-sm">Шрифт</span>

              <select
                v-model="draft.typography.font"
                class="select w-full"
              >
                <option
                  v-for="font in FONT_OPTIONS"
                  :key="font.id"
                  :value="font.id"
                >
                  {{ font.label }}
                </option>
              </select>
            </label>

            <label class="block">
              <span class="mb-3 flex justify-between gap-3 text-sm">
                <span>Базовый размер текста</span>
                <span>{{ draft.typography.size }} px</span>
              </span>

              <input
                v-model.number="draft.typography.size"
                type="range"
                class="range range-primary range-sm w-full"
                min="12"
                max="22"
                step="1"
              >
            </label>

            <label class="block">
              <span class="mb-3 flex justify-between gap-3 text-sm">
                <span>Межстрочный интервал</span>
                <span>{{ draft.typography.lineHeight }}</span>
              </span>

              <input
                v-model.number="draft.typography.lineHeight"
                type="range"
                class="range range-primary range-sm w-full"
                min="1.2"
                max="2"
                step="0.05"
              >
            </label>
          </div>
        </section>

        <section class="bg-base-100 border-base-300 space-y-4 rounded-2xl border p-4 sm:p-5">
          <h2 class="font-semibold">Описание варианта</h2>

          <label class="block">
            <span class="mb-2 block text-sm">
              Название — необязательно
            </span>

            <input
              v-model="name"
              type="text"
              maxlength="120"
              class="input w-full"
              placeholder="Вариант оформления"
            >
          </label>

          <label class="block">
            <span class="mb-2 block text-sm">
              Комментарий — необязательно
            </span>

            <textarea
              v-model="comment"
              maxlength="3000"
              rows="3"
              class="textarea w-full"
              placeholder="Пожелания для разработчика"
            />
          </label>

          <button
            type="button"
            class="btn btn-primary w-full sm:w-auto"
            :disabled="!dirty && Boolean(styles.saved)"
            @click="save"
          >
            Сохранить и применить
          </button>
        </section>
      </div>

      <aside class="min-w-0 space-y-5 xl:sticky xl:top-24">
        <div>
          <h2 class="mb-3 font-semibold">
            Предпросмотр · {{ theme === 'light' ? 'светлая тема' : 'тёмная тема' }}
          </h2>

          <TestStylesPreview
            :settings="draft"
            :theme="theme"
          />

          <p class="text-base-content/60 mt-3 text-xs">
            Предпросмотр не меняет сайт. Размер текста показан
            в образцах; окончательное влияние rem на элементы
            проверяется после применения.
          </p>
        </div>

        <section class="bg-base-100 border-base-300 space-y-4 rounded-2xl border p-4">
          <div>
            <h2 class="font-semibold">Передать разработчику</h2>

            <p class="text-base-content/60 mt-1 text-sm">
              Экспортируется последний сохранённый вариант
              обеих тем, независимо от переключателя «Сбросить».
            </p>

            <p v-if="dirty" class="text-warning mt-2 text-sm">
              Сначала сохраните изменения, если хотите включить их в экспорт.
            </p>
          </div>

          <div class="flex flex-wrap gap-2">
            <button
              type="button"
              class="btn btn-outline btn-sm"
              :disabled="!styles.saved"
              @click="copyCss"
            >
              <Icon name="lucide:copy" class="size-4" />
              Скопировать CSS
            </button>

            <button
              type="button"
              class="btn btn-outline btn-sm"
              :disabled="!styles.saved"
              @click="downloadCss"
            >
              <Icon name="lucide:download" class="size-4" />
              Скачать main.css
            </button>

            <TestStylesSendButton />
          </div>
        </section>

        <section class="bg-base-100 border-base-300 space-y-3 rounded-2xl border p-4">
          <h2 class="font-semibold">Исходное оформление</h2>

          <div class="flex flex-wrap gap-2">
            <button
              type="button"
              class="btn btn-ghost btn-sm"
              @click="useOriginalInDraft"
            >
              Исходные значения в черновик
            </button>

            <button
              type="button"
              class="btn btn-ghost btn-sm text-error"
              :disabled="!styles.saved && !styles.storageError"
              @click="deleteOpen = true"
            >
              Удалить мою настройку
            </button>
          </div>
        </section>
      </aside>
    </div>

    <UiResponsiveDialog
      v-model="deleteOpen"
      title="Удалить локальную настройку?"
    >
      <p>
        Сохранённый вариант и текущий черновик будут удалены.
        Сайт вернётся к исходному оформлению.
        Вернуть удалённый вариант кнопкой в navbar будет нельзя.
      </p>

      <template #footer>
        <div class="flex justify-end gap-2">
          <button
            type="button"
            class="btn btn-ghost"
            @click="deleteOpen = false"
          >
            Отмена
          </button>

          <button
            type="button"
            class="btn btn-error"
            @click="removeStyles"
          >
            Удалить
          </button>
        </div>
      </template>
    </UiResponsiveDialog>
  </div>

  <p v-else class="text-base-content/60 py-8 text-center">
    Студия оформления доступна только суперпользователю.
  </p>
</template>