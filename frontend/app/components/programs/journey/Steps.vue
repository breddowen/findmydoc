<!-- ./frontend/app/components/programs/journey/Steps.vue -->
<script setup>
const props = defineProps({
  stages: {
    type: Array,
    default: () => [],
  },
  selectedId: {
    type: String,
    default: null,
  },
  started: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['select'])

function isCompleted(stage) {
  return props.started
    && Number(stage.progress_percent) >= 100
}
</script>

<template>
  <nav
    class="overflow-x-auto pb-2"
    aria-label="Этапы программы"
  >
    <ul class="steps steps-horizontal min-w-full">
      <li
        v-for="(stage, index) in stages"
        :key="stage.id"
        class="step min-w-24"
        :class="{
          'step-success': isCompleted(stage),
        }"
        :data-content="isCompleted(stage) ? '✓' : String(index + 1)"
      >
        <button
          type="button"
          class="mx-1 mt-1 rounded-xl px-3 py-2 text-xs transition-colors"
          :class="
            selectedId === stage.id
              ? 'bg-primary/10 text-primary ring-primary/40 font-bold ring-2'
              : 'hover:bg-base-300 text-base-content/65'
          "
          :aria-current="selectedId === stage.id ? 'step' : undefined"
          :aria-label="
            `Этап ${index + 1}: ${stage.title}`
            + (isCompleted(stage) ? ', выполнен' : '')
          "
          :title="stage.title"
          @click="emit('select', stage.id)"
        >
          Этап {{ index + 1 }}

          <span
            v-if="isCompleted(stage)"
            class="mt-0.5 block text-[10px]"
          >
            Выполнен
          </span>
        </button>
      </li>
    </ul>
  </nav>
</template>