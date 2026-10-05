<!-- ./frontend/app/pages/content/videos/[id]/index.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

definePageMeta({
  key: route => route.fullPath,
})

const route = useRoute()
const auth = useAuthStore()
const store = useVideosStore()

const video = ref(null)
const loading = ref(true)
const errorMessage = ref('')

const controller = new AbortController()
let disposed = false

function queryString(value) {
  return typeof value === 'string' && value ? value : null
}

const programId = computed(() =>
  queryString(route.query.program_id)
  || queryString(route.query.program),
)

const stageId = computed(() =>
  queryString(route.query.program_stage_id)
  || queryString(route.query.stage),
)

const progress = useVideoProgress({
  video,
  programId,
  programStageId: stageId,
})

const canManage = computed(() =>
  ['superuser', 'med_assistant'].includes(auth.activeRole),
)

const warning = computed(() =>
  store.notice?.videoId === video.value?.id
    ? store.notice.message
    : '',
)

const backLink = computed(() =>
  programId.value
    ? {
        path: `/programs/${programId.value}`,
        query: { stage: stageId.value || undefined },
      }
    : '/content/videos',
)

async function finishVideo() {
  if (
    progress.enabled.value
    && !progress.completed.value
  ) {
    const successful = await progress.complete()

    if (!successful) return
  }

  await navigateTo(backLink.value)
}

onMounted(async () => {
  try {
    const response = await store.fetchVideo(route.params.id, {
      programId: programId.value,
      programStageId: stageId.value,
      signal: controller.signal,
    })

    if (!disposed) video.value = response
  } catch (error) {
    if (!disposed) {
      errorMessage.value = mediaErrorText(
        error,
        'Не удалось открыть видео',
      )
    }
  } finally {
    if (!disposed) loading.value = false
  }
})

onBeforeUnmount(() => {
  disposed = true
  controller.abort()
})

const deleteDialogOpen = ref(false)

async function handleVideoDeleted() {
  await navigateTo(backLink.value)
}
</script>

<template>
  <div class="space-y-6">
    <NuxtLink :to="backLink" class="btn btn-ghost btn-sm">
      <Icon name="lucide:arrow-left" class="size-4" />
      Назад
    </NuxtLink>

    <UiContentSkeleton v-if="loading" variant="card" :count="1" />

    <div v-else-if="errorMessage" class="alert alert-error" role="alert">
      {{ errorMessage }}
    </div>

    <template v-else-if="video">
      <header class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div class="mb-2 flex gap-2">
            <span v-if="video.pro_content" class="badge badge-secondary">
              Pro
            </span>
            <span v-if="video.is_hidden" class="badge badge-warning">
              Скрыто
            </span>
          </div>

          <h1 class="text-2xl font-bold sm:text-3xl">
            {{ video.title }}
          </h1>
        </div>

        <div
          v-if="canManage"
          class="flex shrink-0 flex-wrap gap-2"
        >
          <NuxtLink
            :to="`/content/videos/${video.id}/edit`"
            class="btn btn-outline btn-sm"
          >
            <Icon name="lucide:pencil" class="size-4" />
            Редактировать
          </NuxtLink>

          <button
            type="button"
            class="btn btn-ghost btn-sm text-error"
            :disabled="store.saving"
            @click="deleteDialogOpen = true"
          >
            <Icon name="lucide:trash-2" class="size-4" />
            Удалить
          </button>
        </div>
      </header>

      <div v-if="warning" class="alert alert-warning" role="status">
        Видео сохранено. {{ warning }}
      </div>

      <VideosPlayer
        :video="video"
        :program-id="programId"
        :program-stage-id="stageId"
        @started="progress.started"
        @progress="progress.report"
        @paused="progress.flush"
        @ended="progress.ended"
      />

      <section
        v-if="progress.enabled.value"
        class="border-base-300 space-y-4 rounded-2xl border p-4 sm:p-5"
      >
        <div class="flex flex-wrap items-center justify-between gap-3">
          <span class="text-base-content/60 text-sm">
            Максимальная достигнутая позиция:
            {{ Math.round(progress.maxPercent.value) }}%
          </span>

          <span
            v-if="progress.completed.value"
            class="badge badge-success"
          >
            Завершено
          </span>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="progress.maxPercent.value"
          max="100"
        />

        <p
          v-if="progress.errorMessage.value"
          class="text-warning text-sm"
          role="status"
        >
          {{ progress.errorMessage.value }}
        </p>

        <button
          type="button"
          class="btn btn-primary w-full sm:w-auto"
          :disabled="progress.completing.value"
          @click="finishVideo"
        >
          <span
            v-if="progress.completing.value"
            class="loading loading-spinner loading-sm"
          />

          <Icon v-else name="lucide:check" class="size-4" />

          {{
            progress.completed.value
              ? 'Вернуться'
              : 'Завершить'
          }}
        </button>
      </section>
    </template>
  </div>

  <VideosDeleteDialog
    v-if="video && canManage"
    v-model="deleteDialogOpen"
    :video="video"
    @deleted="handleVideoDeleted"
  />
</template>