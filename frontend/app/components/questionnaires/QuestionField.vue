<!-- ./frontend/app/components/questionnaires/QuestionField.vue -->
<script setup>
const model = defineModel()

const props = defineProps({
  question: {
    type: Object,
    required: true,
  },
})

function toggleMultiple(optionId) {
  const current = Array.isArray(model.value)
    ? model.value
    : []

  if (current.includes(optionId)) {
    model.value = current.filter(
      (item) => item !== optionId,
    )
  } else {
    model.value = [
      ...current,
      optionId,
    ]
  }
}
</script>

<template>
  <textarea
    v-if="question.question_type === 'text'"
    v-model="model"
    class="textarea textarea-bordered min-h-28 w-full"
    placeholder="Введите ответ"
  />

  <input
    v-else-if="question.question_type === 'number'"
    v-model.number="model"
    type="number"
    class="input input-bordered w-full"
  >

  <div
    v-else-if="question.question_type === 'boolean'"
    class="grid grid-cols-2 gap-3"
  >
    <button
      type="button"
      class="btn"
      :class="{
        'btn-primary': model === true,
        'btn-outline': model !== true,
      }"
      @click="model = true"
    >
      Да
    </button>

    <button
      type="button"
      class="btn"
      :class="{
        'btn-primary': model === false,
        'btn-outline': model !== false,
      }"
      @click="model = false"
    >
      Нет
    </button>
  </div>

  <div
    v-else-if="question.question_type === 'scale'"
    class="space-y-4"
  >
    <input
      v-model.number="model"
      type="range"
      class="range range-primary"
      :min="question.scale_min"
      :max="question.scale_max"
      step="1"
    >

    <div class="flex justify-between text-xs">
      <span>
        {{ question.scale_min_label || question.scale_min }}
      </span>

      <strong class="text-primary text-base">
        {{ model ?? '—' }}
      </strong>

      <span>
        {{ question.scale_max_label || question.scale_max }}
      </span>
    </div>
  </div>

  <div
    v-else-if="
      question.question_type === 'single_choice'
    "
    class="space-y-2"
  >
    <label
      v-for="option in question.options"
      :key="option.id"
      class="border-base-300 flex cursor-pointer items-center gap-3 rounded-xl border p-3"
      :class="{
        'border-primary bg-primary/5':
          model === option.id,
      }"
    >
      <input
        v-model="model"
        type="radio"
        :value="option.id"
        class="radio radio-primary"
      >

      <span>{{ option.text }}</span>
    </label>
  </div>

  <div
    v-else-if="
      question.question_type === 'multiple_choice'
    "
    class="space-y-2"
  >
    <label
      v-for="option in question.options"
      :key="option.id"
      class="border-base-300 flex cursor-pointer items-center gap-3 rounded-xl border p-3"
      :class="{
        'border-primary bg-primary/5':
          Array.isArray(model)
          && model.includes(option.id),
      }"
    >
      <input
        type="checkbox"
        class="checkbox checkbox-primary"
        :checked="
          Array.isArray(model)
          && model.includes(option.id)
        "
        @change="toggleMultiple(option.id)"
      >

      <span>{{ option.text }}</span>
    </label>
  </div>
</template>