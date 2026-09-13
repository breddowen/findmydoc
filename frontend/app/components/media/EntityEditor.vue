<!-- ./frontend/app/components/media/EntityEditor.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

const props = defineProps({
  purpose: {
    type: String,
    required: true,
  },
  entityId: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    default: '',
  },
})

const emit = defineEmits([
  'saved',
  'busy',
])

const api = useMediaApi()
const auth = useAuthStore()

const mounted = ref(false)
const loaded = ref(false)
const loading = ref(false)
const saving = ref(false)
const fieldBusy = ref(false)

const currentImageId = ref(null)
const selectedImageId = ref(null)

const errorMessage = ref('')
const message = ref('')
const fieldVersion = ref(0)

let generation = 0
let controller = null

const changed = computed(
  () => selectedImageId.value !== currentImageId.value,
)

const busy = computed(
  () => loading.value || saving.value || fieldBusy.value,
)

watch(
  busy,
  value => emit('busy', value),
  { immediate: true },
)

async function load() {
  const version = ++generation

  controller?.abort()
  controller = new AbortController()

  loading.value = true
  saving.value = false
  loaded.value = false
  fieldBusy.value = false
  errorMessage.value = ''
  message.value = ''

  try {
    const response = await api.getEntityImage(
      props.purpose,
      props.entityId,
      { signal: controller.signal },
    )

    if (version !== generation) return

    currentImageId.value = response.image_id
    selectedImageId.value = response.image_id
    fieldVersion.value += 1
    loaded.value = true
  } catch (error) {
    if (version !== generation) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось загрузить сведения об изображении',
    )
  } finally {
    if (version === generation) {
      loading.value = false
    }
  }
}

async function save() {
  if (!loaded.value || busy.value || !changed.value) return

  const version = generation

  controller = new AbortController()
  saving.value = true
  errorMessage.value = ''
  message.value = ''

  try {
    const response = await api.updateEntityImage(
      props.purpose,
      props.entityId,
      {
        imageId: selectedImageId.value,
        expectedImageId: currentImageId.value,
        signal: controller.signal,
      },
    )

    if (version !== generation) return

    currentImageId.value = response.image_id
    selectedImageId.value = response.image_id

    message.value = response.image_id
      ? 'Изображение сохранено'
      : 'Изображение удалено'

    emit('saved', response)
  } catch (error) {
    if (version !== generation) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось подтвердить сохранение. Обновите данные.',
    )
  } finally {
    if (version === generation) {
      saving.value = false
    }
  }
}

function reset() {
  if (busy.value) return

  selectedImageId.value = currentImageId.value
  fieldVersion.value += 1
  errorMessage.value = ''
  message.value = ''
}

watch(
  [
    mounted,
    () => props.purpose,
    () => props.entityId,
    () => auth.accessToken,
    () => auth.activeRole,
  ],
  () => {
    if (!mounted.value) return

    if (!auth.accessToken) {
      generation += 1
      controller?.abort()
      loaded.value = false
      loading.value = false
      saving.value = false
      fieldBusy.value = false
      return
    }

    void load()
  },
)

onMounted(() => {
  mounted.value = true
})

onBeforeUnmount(() => {
  generation += 1
  controller?.abort()
})
</script>

<template>
  <section class="border-base-300 bg-base-100 space-y-4 rounded-2xl border p-4">
    <div
      v-if="loading"
      class="flex justify-center py-8"
    >
      <span class="loading loading-spinner loading-md" />
    </div>

    <MediaField
      v-if="loaded"
      :key="fieldVersion"
      v-model="selectedImageId"
      :purpose="purpose"
      :entity-id="entityId"
      :saved-image-id="currentImageId"
      :label="label"
      :disabled="saving"
      @busy="fieldBusy = $event"
    />

    <p class="text-base-content/60 text-xs">
      Изображение сохраняется отдельно от остальных данных.
    </p>

    <div
      v-if="errorMessage"
      class="alert alert-error text-sm"
      role="alert"
    >
      {{ errorMessage }}
    </div>

    <p
      v-if="message"
      class="text-success text-sm"
      role="status"
    >
      {{ message }}
    </p>

    <div class="flex flex-wrap justify-end gap-2">
      <button
        type="button"
        class="btn btn-ghost btn-sm"
        :disabled="busy"
        @click="load"
      >
        Обновить данные
      </button>

      <button
        v-if="loaded && changed"
        type="button"
        class="btn btn-sm"
        :disabled="busy"
        @click="reset"
      >
        Отменить изменение
      </button>

      <button
        v-if="loaded"
        type="button"
        class="btn btn-primary btn-sm"
        :disabled="busy || !changed"
        @click="save"
      >
        <span
          v-if="saving"
          class="loading loading-spinner loading-xs"
        />

        Сохранить изображение
      </button>
    </div>
  </section>
</template>