<!-- ./frontend/app/components/questionnaires/QuestionItem.vue -->
<script setup>
const model = defineModel({
  type: Object,
  required: true,
})

defineProps({
  index: {
    type: Number,
    required: true,
  },
  total: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits([
  'remove',
  'move-up',
  'move-down',
])

const questionTypes = [
  {
    value: 'text',
    title: 'Текст',
  },
  {
    value: 'number',
    title: 'Число',
  },
  {
    value: 'boolean',
    title: 'Да / Нет',
  },
  {
    value: 'scale',
    title: 'Шкала',
  },
  {
    value: 'single_choice',
    title: 'Один вариант',
  },
  {
    value: 'multiple_choice',
    title: 'Несколько вариантов',
  },
]

const hasOptions = computed(() =>
  [
    'single_choice',
    'multiple_choice',
  ].includes(model.value.question_type),
)

const isScale = computed(
  () => model.value.question_type === 'scale',
)

function handleTypeChange() {
  if (!hasOptions.value) {
    model.value.options = []
  }

  if (isScale.value) {
    model.value.scale_min ??= 0
    model.value.scale_max ??= 10
  } else {
    model.value.scale_min = null
    model.value.scale_max = null
    model.value.scale_min_label = null
    model.value.scale_max_label = null
  }
}

function addOption() {
  model.value.options.push({
    client_id: crypto.randomUUID(),
    text: '',
    order_index: model.value.options.length,
  })
}

function removeOption(optionIndex) {
  model.value.options.splice(optionIndex, 1)

  model.value.options.forEach((option, index) => {
    option.order_index = index
  })
}

watch(
  () => model.value.question_type,
  handleTypeChange,
)
</script>

<template>
  <article
    class="bg-base-100 border-base-300 rounded-2xl border"
  >
    <header
      class="border-base-300 flex items-center gap-2 border-b px-4 py-3"
    >
      <div
        class="bg-primary text-primary-content flex size-8 shrink-0 items-center justify-center rounded-full text-sm font-bold"
      >
        {{ index + 1 }}
      </div>

      <span class="min-w-0 flex-1 font-medium">
        Вопрос
      </span>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm"
        :disabled="index === 0"
        title="Переместить вверх"
        @click="emit('move-up')"
      >
        <Icon
          name="lucide:arrow-up"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm"
        :disabled="index === total - 1"
        title="Переместить вниз"
        @click="emit('move-down')"
      >
        <Icon
          name="lucide:arrow-down"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm text-error"
        title="Удалить вопрос"
        @click="emit('remove')"
      >
        <Icon
          name="lucide:trash-2"
          class="size-4"
        />
      </button>
    </header>

    <div class="space-y-5 p-4 sm:p-5">
      <div class="grid gap-4 md:grid-cols-[1fr_15rem]">
        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Текст вопроса
            </span>
          </span>

          <textarea
            v-model="model.text"
            class="textarea textarea-bordered min-h-24 w-full"
            placeholder="Введите вопрос"
          />
        </label>

        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Тип ответа
            </span>
          </span>

          <select
            v-model="model.question_type"
            class="select select-bordered w-full"
          >
            <option
              v-for="type in questionTypes"
              :key="type.value"
              :value="type.value"
            >
              {{ type.title }}
            </option>
          </select>
        </label>
      </div>

      <label class="label cursor-pointer justify-start gap-3">
        <input
          v-model="model.is_required"
          type="checkbox"
          class="checkbox checkbox-primary"
        >

        <span class="label-text">
          Обязательный вопрос
        </span>
      </label>

      <div
        v-if="isScale"
        class="bg-base-200 grid gap-4 rounded-2xl p-4 sm:grid-cols-2"
      >
        <label class="form-control block">
          <span class="label-text mb-2">
            Минимум
          </span>

          <input
            v-model.number="model.scale_min"
            type="number"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Максимум
          </span>

          <input
            v-model.number="model.scale_max"
            type="number"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Подпись минимума
          </span>

          <input
            v-model="model.scale_min_label"
            type="text"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Подпись максимума
          </span>

          <input
            v-model="model.scale_max_label"
            type="text"
            class="input input-bordered w-full"
          >
        </label>
      </div>

      <div v-if="hasOptions">
        <div class="mb-3 flex items-center justify-between">
          <span class="font-medium">
            Варианты ответа
          </span>

          <button
            type="button"
            class="btn btn-sm btn-outline"
            @click="addOption"
          >
            <Icon
              name="lucide:plus"
              class="size-4"
            />
            Добавить
          </button>
        </div>

        <div class="space-y-2">
          <div
            v-for="(option, optionIndex) in model.options"
            :key="option.client_id"
            class="flex items-center gap-2"
          >
            <span
              class="text-base-content/50 w-6 shrink-0 text-center text-sm"
            >
              {{ optionIndex + 1 }}
            </span>

            <input
              v-model="option.text"
              type="text"
              class="input input-bordered min-w-0 flex-1"
              placeholder="Вариант ответа"
            >

            <button
              type="button"
              class="btn btn-circle btn-ghost btn-sm text-error"
              aria-label="Удалить вариант"
              @click="removeOption(optionIndex)"
            >
              <Icon
                name="lucide:x"
                class="size-4"
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  </article>
</template>