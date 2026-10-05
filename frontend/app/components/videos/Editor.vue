<!-- ./frontend/app/components/videos/Editor.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

const props = defineProps({
  videoId: {
    type: String,
    default: null,
  },
})

const store = useVideosStore()

const initialValue = ref(null)
const loading = ref(Boolean(props.videoId))
const errorMessage = ref('')

const controller = new AbortController()
let disposed = false

async function save(payload) {
  errorMessage.value = ''

  try {
    const video = props.videoId
      ? await store.updateVideo(props.videoId, payload)
      : await store.createVideo(payload)

    if (disposed) return

    await navigateTo(`/content/videos/${video.id}`)
  } catch (error) {
    if (disposed) return

    errorMessage.value = mediaErrorText(
      error,
      error?.message || 'Не удалось сохранить видео',
    )

    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

function cancel() {
  return navigateTo(
    props.videoId
      ? `/content/videos/${props.videoId}`
      : '/content/videos',
  )
}

onMounted(async () => {
  if (!props.videoId) return

  try {
    const video = await store.fetchVideo(props.videoId, {
      manage: true,
      signal: controller.signal,
    })

    if (!disposed) initialValue.value = video
  } catch (error) {
    if (!disposed) {
      errorMessage.value = mediaErrorText(
        error,
        'Не удалось загрузить видео',
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
</script>

<template>
  <div class="space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        {{ videoId ? 'Редактирование видео' : 'Добавить видео' }}
      </h1>
    </header>

    <div v-if="errorMessage" class="alert alert-error" role="alert">
      {{ errorMessage }}
    </div>

    <UiContentSkeleton v-if="loading" variant="card" :count="3" />

    <VideosForm
      v-else-if="!videoId || initialValue"
      :initial-value="initialValue"
      :saving="store.saving"
      @submit="save"
      @cancel="cancel"
    />
  </div>
</template>