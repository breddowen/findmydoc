<!-- ./frontend/app/components/media/Field.vue -->
<script setup>
import {
  MEDIA_MAX_BYTES,
  MEDIA_MAX_PIXELS,
  MEDIA_PRESETS,
  mediaErrorText,
  readImageDimensions,
} from '~/utils/media'

const model = defineModel({
  type: String,
  default: null,
})

const props = defineProps({
  purpose: {
    type: String,
    required: true,
    validator: value => Boolean(MEDIA_PRESETS[value]),
  },
  entityId: {
    type: String,
    default: null,
  },
  savedImageId: {
    type: String,
    default: null,
  },
  label: {
    type: String,
    default: '',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['busy'])

const api = useMediaApi()
const auth = useAuthStore()

const input = ref(null)
const sourceUrl = ref(null)
const reading = ref(false)
const uploading = ref(false)
const errorMessage = ref('')

let generation = 0
let uploadController = null

const preset = computed(
  () => MEDIA_PRESETS[props.purpose],
)

const busy = computed(
  () => reading.value
    || uploading.value
    || Boolean(sourceUrl.value),
)

const isTemporary = computed(
  () => Boolean(model.value)
    && (
      model.value !== props.savedImageId
      || !props.entityId
    ),
)

watch(
  busy,
  value => emit('busy', value),
  { immediate: true },
)

function clearEditor() {
  generation += 1

  uploadController?.abort()
  uploadController = null

  if (sourceUrl.value) {
    URL.revokeObjectURL(sourceUrl.value)
  }

  sourceUrl.value = null
  reading.value = false
  uploading.value = false
}

async function selectFile(event) {
  const file = event.target.files?.[0]
  event.target.value = ''

  if (!file || props.disabled || busy.value) return

  errorMessage.value = ''

  const supportedTypes = [
    'image/jpeg',
    'image/png',
    'image/webp',
  ]

  if (
    !supportedTypes.includes(file.type)
    && !(
      !file.type
      && /\.(jpe?g|png|webp)$/i.test(file.name)
    )
  ) {
    errorMessage.value = 'Выберите JPEG, PNG или WebP'
    return
  }

  if (file.size > MEDIA_MAX_BYTES) {
    errorMessage.value = 'Максимальный размер файла — 10 МБ'
    return
  }

  const version = ++generation
  const url = URL.createObjectURL(file)

  reading.value = true
  let accepted = false

  try {
    const dimensions = await readImageDimensions(url)

    if (version !== generation) return

    if (
      dimensions.width * dimensions.height
      > MEDIA_MAX_PIXELS
    ) {
      throw new Error(
        'Слишком большое разрешение: максимум 24 млн пикселей',
      )
    }

    if (!dimensions.width || !dimensions.height) {
      throw new Error('Некорректный размер изображения')
    }

    sourceUrl.value = url
    accepted = true
  } catch (error) {
    if (version === generation) {
      errorMessage.value =
        error?.message || 'Не удалось открыть изображение'
    }
  } finally {
    if (!accepted) {
      URL.revokeObjectURL(url)
    }

    if (version === generation) {
      reading.value = false
    }
  }
}

async function upload(cropped) {
  if (props.disabled || uploading.value) return

  if (cropped.blob.size > MEDIA_MAX_BYTES) {
    errorMessage.value =
      'Подготовленное изображение слишком большое'
    return
  }

  const version = generation
  const purpose = props.purpose

  uploadController = new AbortController()

  uploading.value = true
  errorMessage.value = ''

  try {
    const response = await api.upload(
      purpose,
      cropped,
      {
        signal: uploadController.signal,
      },
    )

    if (version !== generation) return

    model.value = response.id
    clearEditor()
  } catch (error) {
    if (version !== generation) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось загрузить изображение',
    )
  } finally {
    if (version === generation) {
      uploading.value = false
      uploadController = null
    }
  }
}

function remove() {
  if (props.disabled || busy.value) return

  model.value = null
  errorMessage.value = ''
}

watch(
  [
    () => auth.accessToken,
    () => auth.activeRole,
    () => props.purpose,
    () => props.entityId,
  ],
  () => {
    clearEditor()
    errorMessage.value = ''
  },
)

onBeforeUnmount(clearEditor)
</script>

<template>
  <section class="space-y-3">
    <div class="flex flex-wrap items-center justify-between gap-2">
      <p class="font-medium">
        {{ label || preset.label }}
      </p>

      <span class="text-base-content/50 text-xs">
        Необязательно
      </span>
    </div>

    <input
      ref="input"
      type="file"
      accept="image/jpeg,image/png,image/webp"
      class="hidden"
      :disabled="disabled || busy"
      @change="selectFile"
    >

    <ClientOnly>
      <MediaCropper
        v-if="sourceUrl"
        :key="sourceUrl"
        :src="sourceUrl"
        :aspect-ratio="preset.ratio"
        :max-width="preset.width"
        :max-height="preset.height"
        :disabled="disabled || uploading"
        @apply="upload"
        @cancel="clearEditor"
      />
    </ClientOnly>

    <template v-if="!sourceUrl">
      <MediaImage
        v-if="model"
        :purpose="purpose"
        :entity-id="entityId"
        :image-id="model"
        :temporary="isTemporary"
        :alt="label || preset.label"
        eager
        class="w-full rounded-xl"
        :class="purpose === 'doctor' ? 'max-w-56' : 'max-w-2xl'"
        :style="{ aspectRatio: preset.ratio }"
      />

      <div
        v-else
        class="border-base-300 text-base-content/50 flex min-h-28 items-center justify-center rounded-xl border border-dashed p-4 text-sm"
      >
        Изображение не выбрано
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          type="button"
          class="btn btn-outline btn-sm"
          :disabled="disabled || busy"
          @click="input?.click()"
        >
          <span
            v-if="reading"
            class="loading loading-spinner loading-xs"
          />

          <Icon
            v-else
            name="lucide:image-plus"
            class="size-4"
          />

          {{ model ? 'Заменить' : 'Выбрать изображение' }}
        </button>

        <button
          v-if="model"
          type="button"
          class="btn btn-ghost btn-sm text-error"
          :disabled="disabled || busy"
          @click="remove"
        >
          <Icon name="lucide:trash-2" class="size-4" />
          Удалить
        </button>
      </div>
    </template>

    <p
      v-if="errorMessage"
      class="text-error text-sm"
      role="alert"
    >
      {{ errorMessage }}
    </p>

    <p class="text-base-content/50 text-xs">
      JPEG, PNG или WebP, до 10 МБ.
      После сохранения используется WebP.
    </p>
  </section>
</template>