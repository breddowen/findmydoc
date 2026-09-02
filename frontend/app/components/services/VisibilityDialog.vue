<!-- ./frontend/app/components/services/VisibilityDialog.vue -->
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
  'updated',
])

const store = useServicesStore()
const errorMessage = ref('')

async function confirm() {
  if (!props.service) return

  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      props.service.id,
      !props.service.is_hidden,
    )

    model.value = false
    emit('updated', response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость услуги'
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    :title="
      service?.is_hidden
        ? 'Восстановить услугу'
        : 'Скрыть услугу'
    "
    max-width-class="max-w-md"
  >
    <div
      v-if="errorMessage"
      class="alert alert-error mb-4"
    >
      {{ errorMessage }}
    </div>

    <p>
      {{
        service?.is_hidden
          ? 'Услугу снова можно будет выбирать при создании программ.'
          : 'Услугу нельзя будет выбирать для новых программ. Существующие связи сохранятся.'
      }}
    </p>

    <p class="mt-3 font-semibold">
      {{ service?.code }} — {{ service?.title }}
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
          class="btn btn-primary"
          :disabled="store.saving"
          @click="confirm"
        >
          <span
            v-if="store.saving"
            class="loading loading-spinner loading-sm"
          />

          Подтвердить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>