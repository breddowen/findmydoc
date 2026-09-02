<!-- ./frontend/app/components/services/DeleteDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  service: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits([
  'deleted',
])

const store = useServicesStore()
const errorMessage = ref('')

async function confirm() {
  if (!props.service) return

  errorMessage.value = ''

  try {
    const deletedId = props.service.id

    await store.deleteService(deletedId)

    model.value = false
    emit('deleted', deletedId)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось удалить услугу'
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Удалить услугу"
    max-width-class="max-w-md"
  >
    <div
      v-if="errorMessage"
      class="alert alert-error mb-4"
    >
      {{ errorMessage }}
    </div>

    <p>
      Удалить услугу без возможности восстановления?
    </p>

    <p class="mt-3 font-semibold">
      {{ service?.code }} — {{ service?.title }}
    </p>

    <p class="text-base-content/60 mt-3 text-sm">
      Если услуга используется программой, backend
      запретит удаление. В таком случае её следует
      скрыть.
    </p>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-error"
          :disabled="store.deleting"
          @click="confirm"
        >
          <span
            v-if="store.deleting"
            class="loading loading-spinner loading-sm"
          />

          Удалить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>