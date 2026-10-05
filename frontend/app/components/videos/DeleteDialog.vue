<!-- ./frontend/app/components/videos/DeleteDialog.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  video: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits(['deleted'])

const store = useVideosStore()

const usage = ref(null)
const loading = ref(false)
const acknowledged = ref(false)
const errorMessage = ref('')

let generation = 0
let controller = null
let disposed = false

const canDelete = computed(() =>
  Boolean(usage.value)
  && !loading.value
  && !store.saving
  && (
    usage.value.program_count === 0
    || acknowledged.value
  ),
)

async function loadUsage({ preserveError = false } = {}) {
  if (!props.video?.id) return

  const version = ++generation

  controller?.abort()
  controller = new AbortController()

  loading.value = true
  usage.value = null
  acknowledged.value = false

  if (!preserveError) {
    errorMessage.value = ''
  }

  try {
    const response = await store.fetchUsage(
      props.video.id,
      { signal: controller.signal },
    )

    if (version !== generation || disposed) return

    usage.value = response
  } catch (error) {
    if (version !== generation || disposed) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось проверить использование видео',
    )
  } finally {
    if (version === generation && !disposed) {
      loading.value = false
    }
  }
}

async function confirmDelete() {
  if (!canDelete.value) return

  const snapshot = usage.value
  errorMessage.value = ''

  try {
    const response = await store.deleteVideo(
      snapshot.video_id,
      {
        expected_version: snapshot.version,
        expected_usage_token: snapshot.usage_token,
        confirm: true,
      },
    )

    if (disposed) return

    model.value = false
    emit('deleted', response)
  } catch (error) {
    if (disposed) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось удалить видео',
    )

    const status = error?.status
      || error?.statusCode
      || error?.response?.status

    if (status === 409 && model.value) {
      // Не повторяем удаление автоматически.
      // Пользователь должен подтвердить новый список.
      await loadUsage({ preserveError: true })
    }
  }
}

watch(
  [model, () => props.video?.id],
  ([open]) => {
    if (open && props.video?.id) {
      void loadUsage()
      return
    }

    generation += 1
    controller?.abort()
    loading.value = false
    usage.value = null
    acknowledged.value = false
  },
  { immediate: true },
)

onBeforeUnmount(() => {
  disposed = true
  generation += 1
  controller?.abort()
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Удалить видео?"
    max-width-class="max-w-xl"
    :close-on-backdrop="!store.saving"
    :show-close-button="!store.saving"
  >
    <div class="space-y-5">
      <p class="font-semibold">
        {{ usage?.title || video?.title }}
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error text-sm"
        role="alert"
      >
        {{ errorMessage }}
      </div>

      <div v-if="loading" class="flex justify-center py-8">
        <span class="loading loading-spinner loading-md" />
      </div>

      <template v-else-if="usage">
        <div
          v-if="usage.program_count"
          class="alert alert-warning text-sm"
        >
          Видео используется в программах:
          {{ usage.program_count }}.
          Видеошагов будет удалено: {{ usage.item_count }}.
        </div>

        <ul
          v-if="usage.programs.length"
          class="divide-base-300 border-base-300 divide-y rounded-xl border"
        >
          <li
            v-for="program in usage.programs"
            :key="program.id"
            class="flex items-start justify-between gap-3 p-3"
          >
            <div class="min-w-0">
              <p class="font-medium">{{ program.title }}</p>

              <p class="text-base-content/60 mt-1 text-xs">
                Вхождений видео: {{ program.item_count }}
              </p>
            </div>

            <span
              v-if="program.is_hidden"
              class="badge badge-ghost badge-sm shrink-0"
            >
              Скрыта
            </span>
          </li>
        </ul>

        <div class="text-base-content/70 space-y-2 text-sm">
          <p>
            Карточка видео и её шаги будут удалены.
            Восстановления из интерфейса нет.
          </p>

          <p>
            Этапы, результаты опросников и прогресс других
            материалов сохранятся. Проценты программ
            пересчитаются по оставшимся заданиям.
          </p>

          <p>
            История событий и статус уже завершённых
            программ сохраняются.
          </p>
        </div>

        <label
          v-if="usage.program_count"
          class="border-base-300 flex cursor-pointer items-start gap-3 rounded-xl border p-3"
        >
          <input
            v-model="acknowledged"
            type="checkbox"
            class="checkbox checkbox-error checkbox-sm mt-0.5"
            :disabled="store.saving"
          >

          <span class="text-sm">
            Понимаю, что видео будет удалено
            из перечисленных программ.
          </span>
        </label>
      </template>
    </div>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          :disabled="store.saving"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          v-if="!usage && !loading"
          type="button"
          class="btn btn-outline"
          :disabled="store.saving"
          @click="loadUsage()"
        >
          Повторить проверку
        </button>

        <button
          type="button"
          class="btn btn-error"
          :disabled="!canDelete"
          @click="confirmDelete"
        >
          <span
            v-if="store.saving"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:trash-2"
            class="size-4"
          />

          Удалить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>