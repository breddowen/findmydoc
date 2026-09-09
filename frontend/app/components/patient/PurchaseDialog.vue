<!-- ./frontend/app/components/patient/PurchaseDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  program: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits(['requested'])

const store = usePatientHomeStore()

const requesting = ref(false)
const errorMessage = ref('')

watch(
  () => [model.value, props.program?.id],
  () => {
    errorMessage.value = ''
  },
)

async function sendRequest() {
  const programId = props.program?.id

  if (!programId || requesting.value) return

  requesting.value = true
  errorMessage.value = ''

  try {
    const response = await store.requestPurchase(programId)

    emit('requested', {
      programId,
      response,
    })

    if (props.program?.id === programId) {
      model.value = false
    }
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось отправить запрос. Попробуйте ещё раз.'
  } finally {
    requesting.value = false
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Обсудить сопровождение"
    max-width-class="max-w-md"
    :close-on-backdrop="!requesting"
    :show-close-button="!requesting"
  >
    <div class="space-y-4">
      <p class="font-medium">
        {{ program?.title }}
      </p>

      <p class="text-base-content/70 text-sm">
        Ассистент поможет разобраться в составе программы,
        стоимости консультаций и порядке записи.
      </p>

      <p class="text-base-content/70 text-sm">
        Материалы без отметки Pro можно проходить бесплатно.
        Для Pro-материалов нужен индивидуальный доступ
        к программе сопровождения.
      </p>

      <p class="text-base-content/60 text-sm">
        Нажимая «Прошу связаться со мной», Вы разрешаете
        ассистенту клиники связаться с Вами по поводу программы.
      </p>

      <p class="text-base-content/50 text-xs">
        Запрос не обязывает покупать программу.
        Оплата в приложении не производится.
        Это не канал срочной медицинской помощи.
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
        role="alert"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn btn-ghost"
          :disabled="requesting"
          @click="model = false"
        >
          Пока не нужно
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="requesting || !program"
          @click="sendRequest"
        >
          <span
            v-if="requesting"
            class="loading loading-spinner loading-sm"
          />
          Прошу связаться со мной
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>