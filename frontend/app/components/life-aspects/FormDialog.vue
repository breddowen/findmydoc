<!-- frontend\app\components\life-aspects\FormDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  aspect: {
    type: Object,
    default: null,
  },
  defaultOrder: {
    type: Number,
    default: 10,
  },
  saving: {
    type: Boolean,
    default: false,
  },
  errorMessage: {
    type: String,
    default: '',
  },
})

const emit = defineEmits(['save'])

const form = reactive({
  name: '',
  description: '',
  order_index: 10,
})

const canSave = computed(() =>
  Boolean(form.name.trim())
  && Number.isInteger(form.order_index)
  && form.order_index >= 0
  && form.order_index <= 100000,
)

watch(
  () => model.value,
  (open) => {
    if (!open) return

    form.name = props.aspect?.name || ''
    form.description = props.aspect?.description || ''
    form.order_index =
      props.aspect?.order_index ?? props.defaultOrder
  },
  { immediate: true },
)

function submit() {
  if (props.saving || !canSave.value) return

  emit('save', {
    name: form.name.trim(),
    description: form.description.trim() || null,
    order_index: form.order_index,
  })
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    :title="aspect ? 'Изменить сферу жизни' : 'Новая сфера жизни'"
    max-width-class="max-w-3xl"
    :close-on-backdrop="!saving"
    :show-close-button="!saving"
  >
    <form
      id="life-aspect-form"
      class="space-y-5"
      @submit.prevent="submit"
    >
      <div
        v-if="errorMessage"
        class="alert alert-error"
        role="alert"
      >
        {{ errorMessage }}
      </div>

      <label class="block">
        <span class="mb-2 block text-sm font-medium">
          Название
        </span>

        <input
          v-model="form.name"
          type="text"
          class="input w-full"
          placeholder="Например, Сон и восстановление"
          required
          maxlength="100"
          :disabled="saving"
        >
      </label>

      <label class="block">
        <span class="mb-2 block text-sm font-medium">
          Порядок отображения
        </span>

        <input
          v-model.number="form.order_index"
          type="number"
          class="input w-full sm:max-w-48"
          min="0"
          max="100000"
          step="1"
          required
          :disabled="saving"
        >

        <span class="text-base-content/60 mt-2 block text-xs">
          Меньшее число — выше в списке.
          Удобно использовать 10, 20, 30…
        </span>
      </label>

      <div>
        <p class="mb-2 text-sm font-medium">
          Описание
        </p>

        <ContentRichTextEditor
          v-model="form.description"
          placeholder="Расскажите, с чем помогают программы этой сферы"
          min-height="12rem"
          :disabled="saving"
        />
      </div>
    </form>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn"
          :disabled="saving"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="submit"
          form="life-aspect-form"
          class="btn btn-primary"
          :disabled="saving || !canSave"
        >
          <span
            v-if="saving"
            class="loading loading-spinner loading-sm"
          />
          Сохранить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>