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
})

const auth = useAuthStore()
const userStore = useUserStore()
const router = useRouter()
const config = useRuntimeConfig()
const { $api } = useNuxtApp()

const articleElement = ref(null)

const savedProgress = ref(0)
const saving = ref(false)
const completed = ref(false)

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
    [
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
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
let lastSentProgress = 0

async function loadProgress() {
  if (!isPatient.value) return

  try {
    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
    )

    savedProgress.value =
      response.progress_percent || 0

    lastSentProgress = savedProgress.value

    completed.value = Boolean(
      response.completed_at,
    )

    await nextTick()

    if (!completed.value) {
      window.setTimeout(() => {
        restoreProgress(savedProgress.value)
      }, 100)
    }
  } catch {
    // Отсутствие прогресса не должно мешать чтению.
  }
}

async function saveProgress(
  value = progress.value,
) {
  if (!isPatient.value || saving.value) return

  saving.value = true

  try {
    const body = {
      progress_percent: value,
    }

    if (props.interactionId) {
      body.interaction_id =
        props.interactionId

      body.is_trackable =
        isTrackable.value
    }

    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
      {
        method: 'PUT',
        body,
      },
    )

    lastSentProgress = value
    savedProgress.value = value

    completed.value = Boolean(
      response.completed_at,
    )
  } finally {
    saving.value = false
  }
}

function scheduleSave() {
  if (!isPatient.value) return

  window.clearTimeout(saveTimer)

  saveTimer = window.setTimeout(() => {
    saveProgress()
  }, 800)
}

function saveWithKeepalive() {
  if (
    !isPatient.value
    || progress.value === lastSentProgress
  ) {
    return
  }

  const token = localStorage.getItem(
    'mentalme_access_token',
  )

  if (!token) return

  const body = {
    progress_percent: progress.value,
  }

  if (props.interactionId) {
    body.interaction_id =
      props.interactionId

    body.is_trackable =
      isTrackable.value
  }

  fetch(
    `${config.public.apiBase}/api/v1/articles/${props.article.id}/progress`,
    {
      method: 'PUT',
      keepalive: true,
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    },
  ).catch(() => {})
}

async function closeReader() {
  window.clearTimeout(saveTimer)

  if (isPatient.value) {
    await saveProgress()
  }

  if (window.history.length > 1) {
    router.back()
  } else {
    await navigateTo('/content/articles')
  }
}

watch(progress, (value) => {
  if (!isPatient.value) return

  if (
    Math.abs(value - lastSentProgress) >= 5
    || value >= 90
  ) {
    scheduleSave()
  }
})

onMounted(() => {
  loadProgress()

  window.addEventListener(
    'pagehide',
    saveWithKeepalive,
  )
})

onBeforeRouteLeave(() => {
  saveWithKeepalive()
})

onBeforeUnmount(() => {
  window.clearTimeout(saveTimer)

  window.removeEventListener(
    'pagehide',
    saveWithKeepalive,
  )
})
</script>

<template>
  <div>
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

      <button
        type="button"
        class="btn btn-circle btn-sm bg-base-100 shadow-lg"
        aria-label="Закрыть статью"
        @click="closeReader"
      >
        <Icon
          name="lucide:x"
          class="size-5"
        />
      </button>
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
    </article>
  </div>
</template>