<!-- ./frontend/app/components/programs/VisibilityDialog.vue -->
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

const emit = defineEmits([
  'hidden',
])

const store = useProgramsStore()

const hiding = ref(false)
const errorMessage = ref('')

async function hideProgram() {
  if (!props.program) return

  hiding.value = true
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      props.program.id,
      true,
    )

    emit('hidden', response)
    model.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось скрыть программу'
  } finally {
    hiding.value = false
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Скрыть программу"
    max-width-class="max-w-md"
  >
    <div class="space-y-4">
      <div
        class="bg-warning/10 border-warning/30 rounded-2xl border p-4"
      >
        <div class="flex gap-3">
          <Icon
            name="lucide:eye-off"
            class="text-warning mt-0.5 size-5 shrink-0"
          />

          <div>
            <p class="font-semibold">
              Программа исчезнет из каталога пациентов
            </p>

            <p class="text-base-content/70 mt-1 text-sm">
              Существующие данные прохождения сохранятся.
              Программу можно будет снова показать.
            </p>
          </div>
        </div>
      </div>

      <p>
        Вы действительно хотите скрыть программу:
      </p>

      <p class="font-semibold">
        {{ program?.title }}
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          :disabled="hiding"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-warning"
          :disabled="hiding"
          @click="hideProgram"
        >
          <span
            v-if="hiding"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:eye-off"
            class="size-4"
          />

          Скрыть
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>