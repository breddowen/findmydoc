<!-- ./frontend/app/components/videos/Form.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'
import { videoSize } from '~/utils/videos'

const props = defineProps({
  initialValue: { type: Object, default: null },
  saving: { type: Boolean, default: false },
})

const emit = defineEmits(['submit', 'cancel'])

const { $api } = useNuxtApp()
const uploader = useVideoUpload()

const tags = ref([])
const limits = ref(null)
const loading = ref(true)
const imageBusy = ref(false)
const errorMessage = ref('')
const uploadingKey = ref(null)
const entries = ref([])

let sequence = 0
let disposed = false

const resourceController = new AbortController()

const form = reactive({
  title: '',
  tag_ids: [],
  pro_content: true,
  is_library_hidden: false,
  image_id: null,
})

const busy = computed(() =>
  props.saving
  || loading.value
  || imageBusy.value
  || uploader.uploading.value,
)

function emptyEntry(format = null) {
  return {
    key: ++sequence,
    format,
    file: null,
    previewUrl: null,
  }
}

function releasePreview(entry) {
  if (entry.previewUrl) {
    URL.revokeObjectURL(entry.previewUrl)
    entry.previewUrl = null
  }
}

function applyInitialValue(video) {
  entries.value.forEach(releasePreview)

  form.title = video?.title || ''
  form.tag_ids = (video?.tags || []).map(tag => tag.id)
  form.pro_content = video ? Boolean(video.pro_content) : true
  form.is_library_hidden = Boolean(video?.is_library_hidden)
  form.image_id = video?.image_id || null

  const next = []

  if (video?.wide_file) {
    next.push({
      ...emptyEntry('wide'),
      file: video.wide_file,
    })
  }

  if (video?.mobile_file) {
    next.push({
      ...emptyEntry('mobile'),
      file: video.mobile_file,
    })
  }

  entries.value = next.length ? next : [emptyEntry()]
}

function changeFormat(entry, format) {
  if (busy.value) return

  const other = entries.value.find(item => item !== entry)

  entry.format = format

  if (other) {
    other.format = format === 'wide' ? 'mobile' : 'wide'
  }
}

function addVariant() {
  if (busy.value || entries.value.length >= 2) return

  const first = entries.value[0]

  entries.value.push(
    emptyEntry(
      first.format === 'wide' ? 'mobile' : 'wide',
    ),
  )
}

function removeVariant(entry) {
  if (busy.value) return

  releasePreview(entry)
  entries.value = entries.value.filter(item => item !== entry)

  if (!entries.value.length) {
    entries.value = [emptyEntry()]
  }
}

async function uploadToEntry(entry, file) {
  if (busy.value || !limits.value) return

  errorMessage.value = ''

  if (!/\.mp4$/i.test(file.name)) {
    errorMessage.value = 'Выберите файл MP4'
    return
  }

  if (!file.size || file.size > limits.value.max_bytes) {
    errorMessage.value =
      `Размер файла должен быть больше нуля и не превышать `
      + videoSize(limits.value.max_bytes)
    return
  }

  uploadingKey.value = entry.key

  try {
    const response = await uploader.upload(file)

    if (disposed) return

    releasePreview(entry)

    entry.file = response
    entry.previewUrl = URL.createObjectURL(file)

    const other = entries.value.find(item => item !== entry)

    if (!entry.format) {
      entry.format = other?.format
        ? (other.format === 'wide' ? 'mobile' : 'wide')
        : response.suggested_slot
    }

    if (other && other.format === entry.format) {
      other.format = entry.format === 'wide' ? 'mobile' : 'wide'
    }
  } catch (error) {
    if (disposed || error?.name === 'AbortError') return

    errorMessage.value = mediaErrorText(
      error,
      error?.message || 'Не удалось загрузить видео',
    )
  } finally {
    if (!disposed) uploadingKey.value = null
  }
}

function submit() {
  if (busy.value) return

  errorMessage.value = ''

  const files = entries.value.filter(entry => entry.file)

  if (!form.title.trim()) {
    errorMessage.value = 'Введите название видео'
    return
  }

  if (!files.length) {
    errorMessage.value = 'Загрузите хотя бы один видеофайл'
    return
  }

  emit('submit', {
    title: form.title.trim(),
    tag_ids: form.tag_ids,
    pro_content: form.pro_content,
    is_library_hidden: form.is_library_hidden,
    image_id: form.image_id,
    wide_file_id:
      files.find(entry => entry.format === 'wide')?.file.id || null,
    mobile_file_id:
      files.find(entry => entry.format === 'mobile')?.file.id || null,
    ...(props.initialValue
      ? { expected_version: props.initialValue.version }
      : {}),
  })
}

watch(
  () => props.initialValue,
  applyInitialValue,
  { immediate: true },
)

onMounted(async () => {
  try {
    const [tagItems, uploadLimits] = await Promise.all([
      $api('/api/v1/tags', {
        signal: resourceController.signal,
        retry: 0,
      }),
      $api('/api/v1/media/video-uploads/limits', {
        signal: resourceController.signal,
        retry: 0,
      }),
    ])

    if (disposed) return

    tags.value = tagItems
    limits.value = uploadLimits
  } catch (error) {
    if (disposed) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось загрузить настройки формы',
    )
  } finally {
    if (!disposed) loading.value = false
  }
})

onBeforeUnmount(() => {
  disposed = true
  resourceController.abort()
  uploader.cancel()
  entries.value.forEach(releasePreview)
})
</script>

<template>
  <form class="space-y-6" @submit.prevent="submit">
    <div v-if="errorMessage" class="alert alert-error" role="alert">
      {{ errorMessage }}
    </div>

    <UiContentSkeleton v-if="loading" variant="card" :count="2" />

    <template v-else>
      <section class="border-base-300 bg-base-100 space-y-5 rounded-2xl border p-4 sm:p-6">
        <label class="form-control block">
          <span class="mb-2 block font-medium">Название видео</span>

          <input
            v-model="form.title"
            type="text"
            maxlength="300"
            required
            class="input input-bordered w-full"
            :disabled="saving"
          >
        </label>

        <div class="grid items-start gap-4 lg:grid-cols-2">
          <VideosSourceField
            v-for="entry in entries"
            :key="entry.key"
            :file="entry.file"
            :format="entry.format"
            :preview-url="entry.previewUrl"
            :disabled="busy"
            :uploading="uploadingKey === entry.key"
            :progress="uploader.progress.value"
            :checking="uploader.checking.value"
            :can-remove="Boolean(entry.file) || entries.length > 1"
            @select="uploadToEntry(entry, $event)"
            @format="changeFormat(entry, $event)"
            @remove="removeVariant(entry)"
            @cancel-upload="uploader.cancel"
          />
        </div>

        <button
          v-if="entries.length < 2"
          type="button"
          class="btn btn-outline btn-sm"
          :disabled="busy || !entries[0]?.file"
          @click="addVariant"
        >
          <Icon name="lucide:plus" class="size-4" />
          Добавить второй вариант
        </button>

        <div class="text-base-content/60 space-y-1 text-sm">
          <p>
            Один файл используется на всех устройствах.
            Если файлов два — выбирается подходящий вариант.
          </p>

          <p v-if="limits">
            MP4, H.264, AAC-LC, faststart.
            До {{ Math.floor(limits.max_duration_seconds / 60) }} минут,
            {{ limits.max_fps }} кадров/с,
            {{ videoSize(limits.max_bytes) }} на файл.
          </p>

          <p>
            Переключатель меняет назначение, а не обрезает и не поворачивает ролик.
          </p>
        </div>
      </section>

      <section class="border-base-300 bg-base-100 space-y-5 rounded-2xl border p-4 sm:p-6">
        <div v-if="initialValue?.poster_image_id" class="space-y-2">
          <p class="text-base-content/60 text-sm">
            Сохранённая обложка
          </p>

          <VideosPoster
            :video="initialValue"
            eager
            class="max-w-xl rounded-xl"
          />
        </div>

        <MediaField
          v-model="form.image_id"
          purpose="video"
          :entity-id="initialValue?.id || null"
          :saved-image-id="initialValue?.image_id || null"
          :disabled="saving || uploader.uploading.value"
          @busy="imageBusy = $event"
        />

        <p class="text-base-content/60 text-sm">
          Без ручной обложки используется сохранённый кадр видео.
          При первом сохранении он создаётся автоматически.
        </p>
      </section>

      <section class="border-base-300 bg-base-100 space-y-5 rounded-2xl border p-4 sm:p-6">
        <div>
          <p class="mb-3 font-medium">Теги</p>

          <ContentTagSelector
            v-model="form.tag_ids"
            :tags="tags"
            :loading="loading"
          />
        </div>

        <label class="border-base-300 flex items-start justify-between gap-4 rounded-xl border p-4">
          <span>
            <span class="block font-medium">Pro-контент</span>
            <span class="text-base-content/60 mt-1 block text-sm">
              В общем каталоге требуется Pro-доступ.
            </span>
          </span>

          <input
            v-model="form.pro_content"
            type="checkbox"
            class="toggle toggle-primary"
            :disabled="saving"
          >
        </label>

        <ContentLibraryVisibility
          v-model="form.is_library_hidden"
          :disabled="saving"
        />
      </section>

      <div class="flex justify-end gap-3">
        <button
          type="button"
          class="btn"
          :disabled="busy"
          @click="emit('cancel')"
        >
          Отмена
        </button>

        <button
          type="submit"
          class="btn btn-primary"
          :disabled="busy || !limits"
        >
          <span v-if="saving" class="loading loading-spinner loading-sm" />
          Сохранить видео
        </button>
      </div>
    </template>
  </form>
</template>