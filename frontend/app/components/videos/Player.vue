<!-- ./frontend/app/components/videos/Player.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'
import { videoApiUrl } from '~/utils/videos'

const props = defineProps({
  video: {
    type: Object,
    required: true,
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

const emit = defineEmits([
  'started',
  'progress',
  'paused',
  'ended',
])

function emitProgress() {
  const video = element.value

  if (
    !video
    || !Number.isFinite(video.duration)
    || video.duration <= 0
  ) {
    return
  }

  emit(
    'progress',
    Math.min(100, Math.max(
      0,
      video.currentTime / video.duration * 100,
    )),
  )
}

function handlePlaying() {
  emit('started')
  emitProgress()
}

function handlePause() {
  emitProgress()
  emit('paused')
}

function handleEnded() {
  emitProgress()
  emit('ended')
}

const config = useRuntimeConfig()
const auth = useAuthStore()
const playback = useVideoPlaybackStore()

const element = ref(null)
const mounted = ref(false)
const selectedFile = ref(null)
const source = ref('')
const loading = ref(true)
const errorMessage = ref('')

let generation = 0
let retryUsed = false
let restoreTime = 0
let refreshTimer = null

const posterRequest = computed(() => {
  const imageId = props.video.poster_image_id

  if (!imageId) return null

  return {
    path: `/api/v1/videos/${props.video.id}/poster`,
    query: {
      image_id: imageId,
      program_id: props.programId || undefined,
      program_stage_id: props.programStageId || undefined,
    },
  }
})

const { src: poster } = usePrivateImage(
  posterRequest,
  mounted,
)

const portrait = computed(() =>
  selectedFile.value
  && selectedFile.value.height > selectedFile.value.width,
)

function stopElement() {
  const video = element.value

  if (!video) return

  video.pause()
  video.removeAttribute('src')
  video.load()
}

function chooseFile() {
  const mobile = window.matchMedia(
    '(max-width: 767px)',
  ).matches

  return mobile
    ? props.video.mobile_file || props.video.wide_file
    : props.video.wide_file || props.video.mobile_file
}

async function loadSource({
  forceSession = false,
  resumeAt = 0,
} = {}) {
  const version = ++generation

  source.value = ''
  stopElement()

  loading.value = true
  errorMessage.value = ''
  restoreTime = resumeAt

  try {
    if (!selectedFile.value) {
      throw new Error('У видео нет доступного файла')
    }

    await playback.ensureSession(forceSession)

    if (version !== generation || !mounted.value) return

    source.value = videoApiUrl(
      config.public.apiBase,
      `/api/v1/videos/${props.video.id}`
        + `/files/${selectedFile.value.id}`,
      {
        program_id: props.programId,
        program_stage_id: props.programStageId,
      },
    )
  } catch (error) {
    if (version !== generation || !mounted.value) return

    loading.value = false

    if (error?.name !== 'AbortError') {
      errorMessage.value = mediaErrorText(
        error,
        error?.message || 'Не удалось открыть видео',
      )
    }
  }
}

function handleMetadata() {
  loading.value = false

  if (
    restoreTime > 0
    && element.value
    && Number.isFinite(element.value.duration)
  ) {
    element.value.currentTime = Math.min(
      restoreTime,
      Math.max(0, element.value.duration - 0.1),
    )
  }

  restoreTime = 0
}

function handlePlaybackError() {
  if (!source.value || !mounted.value) return

  // Одна попытка обновить cookie и повторить запрос.
  // Например, сессия могла быть удалена в другой вкладке.
  if (!retryUsed) {
    retryUsed = true

    const position = element.value?.currentTime || 0

    void loadSource({
      forceSession: true,
      resumeAt: position,
    })

    return
  }

  loading.value = false
  errorMessage.value = (
    'Видео не удалось воспроизвести. '
    + 'Возможно, файл изменён, доступ закрыт '
    + 'или соединение прервано.'
  )
}

function retry() {
  retryUsed = false

  void loadSource({
    forceSession: true,
  })
}

function start() {
  if (!mounted.value) return

  // Выбираем вариант при открытии, не на каждом resize.
  selectedFile.value = chooseFile()
  retryUsed = false

  void loadSource()
}

watch(
  [
    () => props.video.id,
    () => props.video.wide_file?.id,
    () => props.video.mobile_file?.id,
    () => auth.accessToken,
    () => auth.activeRole,
  ],
  start,
)

onMounted(() => {
  mounted.value = true
  start()

  refreshTimer = window.setInterval(() => {
    if (!source.value || document.hidden) return

    void playback.ensureSession().catch(() => {
      // Если следующий запрос файла не пройдёт,
      // сработает обработчик ошибки проигрывателя.
    })
  }, 30000)
})

onBeforeUnmount(() => {
  mounted.value = false
  generation += 1

  window.clearInterval(refreshTimer)

  source.value = ''
  stopElement()
})
</script>

<template>
  <section class="space-y-4">
    <div
      v-if="errorMessage"
      class="alert alert-error"
      role="alert"
    >
      <div class="space-y-3">
        <p>{{ errorMessage }}</p>

        <button
          type="button"
          class="btn btn-sm"
          @click="retry"
        >
          Повторить
        </button>
      </div>
    </div>

    <div class="relative overflow-hidden rounded-2xl bg-black">
      <div
        v-if="loading"
        class="flex min-h-32 items-center justify-center p-6"
        aria-label="Загрузка видео"
      >
        <span class="loading loading-spinner loading-lg text-white" />
      </div>

      <video
        v-if="source"
        ref="element"
        :src="source"
        :poster="poster || undefined"
        controls
        playsinline
        preload="metadata"
        crossorigin="use-credentials"
        class="mx-auto block max-h-[75dvh] w-full"
        :class="portrait ? 'max-w-md' : ''"
        @loadedmetadata="handleMetadata"
        @error="handlePlaybackError"
        @playing="handlePlaying"
        @timeupdate="emitProgress"
        @pause="handlePause"
        @ended="handleEnded"
      />
    </div>

    <p class="text-base-content/50 text-xs">
      Вариант видео выбирается при открытии страницы.
      Поворот устройства не прерывает просмотр.
    </p>
  </section>
</template>