<!-- ./frontend/app/components/videos/SourceField.vue -->
<script setup>
import {
  videoDuration,
  videoSize,
} from '~/utils/videos'

const props = defineProps({
  file: { type: Object, default: null },
  format: { type: String, default: null },
  previewUrl: { type: String, default: null },
  disabled: { type: Boolean, default: false },
  uploading: { type: Boolean, default: false },
  progress: { type: Number, default: 0 },
  checking: { type: Boolean, default: false },
  canRemove: { type: Boolean, default: true },
})

const emit = defineEmits([
  'select',
  'format',
  'remove',
  'cancel-upload',
])

const input = ref(null)
const dragging = ref(false)
const localError = ref('')

const formats = [
  {
    value: 'wide',
    title: '16:9',
    label: 'Для широкого экрана',
    icon: 'lucide:monitor',
  },
  {
    value: 'mobile',
    title: '9:16',
    label: 'Для телефона',
    icon: 'lucide:smartphone',
  },
]

function choose() {
  if (!props.disabled) {
    input.value?.click()
  }
}

function acceptFiles(files) {
  dragging.value = false
  localError.value = ''

  if (props.disabled) return
  if (!files?.length) return

  if (files.length !== 1) {
    localError.value = 'Выберите один файл'
    return
  }

  emit('select', files[0])
}

function onInput(event) {
  acceptFiles(event.target.files)
  event.target.value = ''
}
</script>

<template>
  <section class="border-base-300 space-y-4 rounded-2xl border p-4">
    <input
      ref="input"
      type="file"
      accept=".mp4,video/mp4"
      class="hidden"
      :disabled="disabled"
      @change="onInput"
    >

    <div class="flex items-center justify-between gap-3">
      <div
        class="bg-base-200 inline-flex gap-1 rounded-xl p-1"
        role="group"
        aria-label="Назначение видео"
      >
        <button
          v-for="item in formats"
          :key="item.value"
          type="button"
          class="flex items-center gap-2 rounded-lg px-3 py-2 text-sm transition-colors"
          :class="
            format === item.value
              ? 'bg-base-100 text-primary shadow-sm'
              : 'text-base-content/60'
          "
          :disabled="disabled"
          :aria-pressed="format === item.value"
          :aria-label="item.label"
          :title="item.label"
          @click="emit('format', item.value)"
        >
          <Icon :name="item.icon" class="size-4" />
          {{ item.title }}
        </button>
      </div>

      <button
        v-if="canRemove"
        type="button"
        class="btn btn-circle btn-ghost btn-sm text-error"
        :disabled="disabled"
        aria-label="Убрать этот вариант"
        @click="emit('remove')"
      >
        <Icon name="lucide:trash-2" class="size-4" />
      </button>
    </div>

    <div
      role="button"
      :tabindex="disabled ? -1 : 0"
      :aria-disabled="disabled"
      class="flex min-h-36 flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed p-5 text-center"
      :class="[
        dragging ? 'border-primary bg-primary/5' : 'border-base-300',
        disabled ? 'opacity-60' : 'cursor-pointer hover:border-primary',
      ]"
      @click="choose"
      @keydown.enter.prevent="choose"
      @keydown.space.prevent="choose"
      @dragover.prevent="dragging = !disabled"
      @dragleave.prevent="dragging = false"
      @drop.prevent="acceptFiles($event.dataTransfer.files)"
    >
      <Icon
        :name="file ? 'lucide:file-video' : 'lucide:upload'"
        class="text-primary size-8"
      />

      <p class="font-medium">
        {{ file ? 'Заменить видео' : 'Перетащите MP4 сюда' }}
      </p>

      <p class="text-base-content/60 text-xs">
        Или нажмите для выбора файла
      </p>

      <p v-if="file" class="text-base-content/60 text-xs">
        {{ file.width }} × {{ file.height }}
        · {{ videoDuration(file.duration_seconds) }}
        · {{ videoSize(file.size_bytes) }}
      </p>
    </div>

    <div v-if="uploading" class="space-y-2" aria-live="polite">
      <progress
        class="progress progress-primary w-full"
        :value="progress"
        max="100"
      />

      <div class="flex items-center justify-between gap-3 text-sm">
        <span>
          {{ checking ? 'Проверяем видео…' : `Загрузка: ${progress}%` }}
        </span>

        <button
          type="button"
          class="btn btn-ghost btn-xs"
          @click="emit('cancel-upload')"
        >
          Отменить
        </button>
      </div>
    </div>

    <video
      v-if="previewUrl && !uploading"
      :src="previewUrl"
      controls
      playsinline
      preload="metadata"
      class="mx-auto max-h-80 w-full rounded-xl bg-black"
    />

    <p v-if="!format" class="text-base-content/50 text-xs">
      Назначение определится после загрузки.
      Его можно выбрать вручную.
    </p>

    <p v-if="localError" class="text-error text-sm" role="alert">
      {{ localError }}
    </p>
  </section>
</template>