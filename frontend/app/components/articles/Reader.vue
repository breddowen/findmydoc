<!-- ./frontend/app/components/articles/Reader.vue -->
<script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  },
  interactionId: {
    type: String,
    default: null,
  },
  programId: {
    type: String,
    default: null,
  },
  programStageId: {
    type: String,
    default: null,
  },
})

const auth = useAuthStore()
const userStore = useUserStore()
const router = useRouter()
const closing = ref(false)
const config = useRuntimeConfig()
const { $api } = useNuxtApp()

const articleElement = ref(null)

const savedProgress = ref(0)
const saving = ref(false)
const completed = ref(false)
const progressReady = ref(false)
const saveError = ref('')

const {
  progress,
  isTrackable,
  restoreProgress,
} = useReadingProgress(articleElement)

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canEdit = computed(() => {
  if (
    ['superuser', 'med_assistant'].includes(
      auth.activeRole,
    )
  ) {
    return true
  }

  return (
    auth.activeRole === 'doctor'
    && props.article.created_by_user_id
      === userStore.user?.id
  )
})

let saveTimer = null
let restoreTimer = null
let restoreFrame = null

let disposed = false
let lastSentProgress = null
let pendingBody = null
let savePromise = null

function createProgressBody(value) {
  return {
    progress_percent: value,
    interaction_id: props.interactionId,
    is_trackable: Boolean(
      props.interactionId && isTrackable.value,
    ),
    program_id: props.programId,
    program_stage_id: props.programStageId,
  }
}

async function loadProgress() {
  if (!isPatient.value) return

  try {
    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
      {
        query: {
          program_id: props.programId || undefined,
          program_stage_id:
            props.programStageId || undefined,
        },
      },
    )

    if (disposed) return

    savedProgress.value =
      Number(response.progress_percent) || 0

    lastSentProgress = savedProgress.value
    completed.value = Boolean(response.completed_at)

    await nextTick()

    if (disposed) return

    restoreTimer = window.setTimeout(() => {
      if (disposed) return

      if (!completed.value) {
        restoreProgress(savedProgress.value)
      }

      restoreFrame = window.requestAnimationFrame(() => {
        if (!disposed) {
          progressReady.value = true
        }
      })
    }, 100)
  } catch {
    if (disposed) return

    saveError.value =
      'Не удалось загрузить сохранённую позицию. '
      + 'Вы можете читать материал и повторить загрузку.'

    // Не отправляем случайный нулевой прогресс
    // поверх состояния, которое не удалось загрузить.
    progressReady.value = false
  }
}

async function drainSaveQueue() {
  saving.value = true
  let successful = true

  try {
    while (pendingBody && !disposed) {
      const body = pendingBody
      pendingBody = null

      try {
        const response = await $api(
          `/api/v1/articles/${props.article.id}/progress`,
          {
            method: 'PUT',
            body,
          },
        )

        lastSentProgress = body.progress_percent

        if (!disposed) {
          savedProgress.value =
            body.progress_percent

          completed.value = Boolean(
            response.completed_at,
          )

          saveError.value = ''
        }
      } catch {
        successful = false

        // Не делаем бесконечные автоматические повторы.
        // Следующее действие сохранит актуальное значение.
        pendingBody = null

        if (!disposed) {
          saveError.value =
            'Не удалось сохранить прогресс. '
            + 'Проверьте соединение и попробуйте ещё раз.'
        }

        break
      }
    }
  } finally {
    saving.value = false
  }

  return successful
}

async function saveProgress(
  value = progress.value,
) {
  if (
    !isPatient.value
    || !progressReady.value
    || disposed
  ) {
    return false
  }

  // Пока выполняется запрос, запоминаем последнее
  // состояние вместо потери очередного сохранения.
  pendingBody = createProgressBody(value)

  if (!savePromise) {
    savePromise = drainSaveQueue().finally(() => {
      savePromise = null
    })
  }

  return await savePromise
}

function scheduleSave() {
  if (!isPatient.value || !progressReady.value) return

  window.clearTimeout(saveTimer)

  saveTimer = window.setTimeout(() => {
    void saveProgress()
  }, 800)
}

function saveWithKeepalive() {
  if (
    !isPatient.value
    || !progressReady.value
    || progress.value === lastSentProgress
  ) {
    return
  }

  const token = localStorage.getItem(
    'mentalme_access_token',
  )

  if (!token) return

  const baseURL = String(
    config.public.apiBase || '',
  ).replace(/\/$/, '')

  fetch(
    `${baseURL}/api/v1/articles/${props.article.id}/progress`,
    {
      method: 'PUT',
      keepalive: true,
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(
        createProgressBody(progress.value),
      ),
    },
  ).catch(() => {})
}

function handleVisibilityChange() {
  if (document.visibilityState === 'hidden') {
    saveWithKeepalive()
  }
}

async function retryProgress() {
  if (!progressReady.value) {
    saveError.value = ''
    await loadProgress()
    return
  }

  await saveProgress()
}

async function closeReader() {
  if (closing.value) return

  closing.value = true
  window.clearTimeout(saveTimer)

  try {
    if (isPatient.value && progressReady.value) {
      const saved = await saveProgress()

      if (!saved) return
    }

    if (props.programId) {
      await navigateTo({
        path: `/programs/${props.programId}`,
        query: props.programStageId
          ? { stage: props.programStageId }
          : {},
      })

      return
    }

    // Не используем history.back():
    // предыдущей страницей могла быть форма редактирования
    // или вообще внешняя страница.
    await navigateTo('/content/articles')
  } finally {
    closing.value = false
  }
}

watch(progress, value => {
  if (!isPatient.value || !progressReady.value) return

  if (
    lastSentProgress === null
    || Math.abs(value - lastSentProgress) >= 5
    || value >= 90
  ) {
    scheduleSave()
  }
})

onMounted(() => {
  void loadProgress()

  window.addEventListener(
    'pagehide',
    saveWithKeepalive,
  )

  document.addEventListener(
    'visibilitychange',
    handleVisibilityChange,
  )
})

onBeforeRouteLeave(() => {
  saveWithKeepalive()
})

onBeforeUnmount(() => {
  disposed = true
  pendingBody = null

  window.clearTimeout(saveTimer)
  window.clearTimeout(restoreTimer)

  if (restoreFrame !== null) {
    window.cancelAnimationFrame(restoreFrame)
  }

  window.removeEventListener(
    'pagehide',
    saveWithKeepalive,
  )

  document.removeEventListener(
    'visibilitychange',
    handleVisibilityChange,
  )
})
</script>

<template>
  <div class="pb-24">
    <progress
      class="progress progress-secondary fixed inset-x-0 top-0 z-[70] h-1 w-full rounded-none"
      :value="progress"
      max="100"
      aria-label="Прогресс чтения статьи"
    />

    <div
      class="fixed right-3 top-3 z-[60] flex items-center gap-2 sm:right-5 sm:top-4"
    >
      <NuxtLink
        v-if="canEdit"
        :to="`/content/articles/${article.id}/edit`"
        class="btn btn-sm btn-primary shadow-lg"
      >
        <Icon
          name="lucide:pencil"
          class="size-4"
        />

        <span class="hidden sm:inline">
          Редактировать
        </span>
      </NuxtLink>

      <!-- <button
        type="button"
        class="btn btn-circle btn-sm bg-base-100 shadow-lg"
        aria-label="Закрыть статью"
        :disabled="saving"
        @click="closeReader"
      >
        <Icon
          name="lucide:x"
          class="size-5"
        />
      </button> -->
    </div>

    <article
      ref="articleElement"
      class="bg-base-100 border-base-300 mx-auto max-w-4xl rounded-3xl border p-5 sm:p-8 lg:p-10"
    >
      <div class="mb-5 flex flex-wrap gap-2">
        <span
          v-if="article.pro_content"
          class="badge badge-secondary"
        >
          Pro
        </span>

        <span
          v-for="tag in article.tags"
          :key="tag.id"
          class="badge badge-outline"
        >
          {{ tag.name }}
        </span>
      </div>

      <h1
        class="mb-8 text-3xl font-bold leading-tight sm:text-4xl"
      >
        {{ article.title }}
      </h1>

      <ContentRichTextRenderer
        :content="article.content"
      />

      <div
        v-if="saveError && isPatient"
        class="alert alert-warning mt-6"
        role="alert"
      >
        <div>
          <p>{{ saveError }}</p>

          <button
            type="button"
            class="btn btn-sm mt-3"
            :disabled="saving"
            @click="retryProgress"
          >
            Повторить
          </button>
        </div>
      </div>

      <div
        class="border-base-300 mt-10 border-t pt-6"
      >
        <div class="flex items-center justify-between gap-4">
          <span class="text-sm font-medium">
            Прочитано {{ progress }}%
          </span>

          <span
            v-if="completed && isPatient"
            class="badge badge-success gap-1"
          >
            <Icon
              name="lucide:check"
              class="size-3"
            />
            Завершено
          </span>
        </div>

        <progress
          class="progress progress-secondary mt-3 w-full"
          :value="progress"
          max="100"
        />
      </div>

      <ArticlesReaderAction
        :target="articleElement"
        :disabled="closing"
        @close="closeReader"
      />
    </article>
  </div>
</template>