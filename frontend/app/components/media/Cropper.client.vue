<!-- ./frontend/app/components/media/Cropper.client.vue -->
<script setup>
import { Cropper } from 'vue-advanced-cropper'
import 'vue-advanced-cropper/dist/style.css'

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  aspectRatio: {
    type: Number,
    required: true,
    validator: value => Number.isFinite(value) && value > 0,
  },
  maxWidth: {
    type: Number,
    default: 1600,
  },
  maxHeight: {
    type: Number,
    default: 900,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'apply',
  'cancel',
])

const cropper = ref(null)
const ready = ref(false)
const exporting = ref(false)
const errorMessage = ref('')

let disposed = false

const blocked = computed(
  () => props.disabled || exporting.value,
)

function toPngBlob(canvas) {
  return new Promise((resolve, reject) => {
    canvas.toBlob((blob) => {
      if (blob) {
        resolve(blob)
      } else {
        reject(new Error('Не удалось подготовить изображение'))
      }
    }, 'image/png')
  })
}

async function apply() {
  if (blocked.value || !ready.value) return

  exporting.value = true
  errorMessage.value = ''

  try {
    const result = cropper.value?.getResult()
    const source = result?.canvas

    if (!source?.width || !source?.height) {
      throw new Error('Выберите область изображения')
    }

    // Не увеличиваем маленькие изображения.
    const width = Math.floor(Math.min(
      source.width,
      props.maxWidth,
      source.height * props.aspectRatio,
      props.maxHeight * props.aspectRatio,
    ))

    const height = Math.floor(
      width / props.aspectRatio,
    )

    if (width < 16 || height < 16) {
      throw new Error(
        'Выбранная область слишком маленькая',
      )
    }

    const canvas = document.createElement('canvas')
    canvas.width = width
    canvas.height = height

    const context = canvas.getContext('2d')

    if (!context) {
      throw new Error('Браузер не поддерживает обработку изображения')
    }

    context.imageSmoothingEnabled = true
    context.imageSmoothingQuality = 'high'

    context.drawImage(
      source,
      0,
      0,
      source.width,
      source.height,
      0,
      0,
      width,
      height,
    )

    const blob = await toPngBlob(canvas)

    if (disposed) return

    emit('apply', {
      blob,
      width,
      height,
    })
  } catch (error) {
    if (!disposed) {
      errorMessage.value =
        error?.message || 'Не удалось обрезать изображение'
    }
  } finally {
    if (!disposed) {
      exporting.value = false
    }
  }
}

onBeforeUnmount(() => {
  disposed = true
})
</script>

<template>
  <div class="space-y-3">
    <div
      class="overflow-hidden rounded-xl bg-neutral"
      :class="{ 'pointer-events-none opacity-70': blocked }"
      :aria-busy="blocked"
    >
      <Cropper
        ref="cropper"
        :src="src"
        :stencil-props="{
          aspectRatio,
        }"
        :canvas="{
          maxWidth,
          maxHeight,
        }"
        :check-orientation="true"
        class="h-72 sm:h-96"
        @ready="ready = true"
        @error="
          ready = false;
          errorMessage = 'Не удалось открыть изображение'
        "
      />
    </div>

    <p class="text-base-content/60 text-xs">
      Перемещайте изображение или область обрезки.
      Пропорции зафиксированы.
    </p>

    <p
      v-if="errorMessage"
      class="text-error text-sm"
      role="alert"
    >
      {{ errorMessage }}
    </p>

    <div class="flex flex-wrap justify-end gap-2">
      <button
        type="button"
        class="btn btn-sm"
        :disabled="blocked"
        @click="emit('cancel')"
      >
        Отмена обрезки
      </button>

      <button
        type="button"
        class="btn btn-primary btn-sm"
        :disabled="blocked || !ready"
        @click="apply"
      >
        <span
          v-if="blocked"
          class="loading loading-spinner loading-xs"
        />

        Применить
      </button>
    </div>
  </div>
</template>