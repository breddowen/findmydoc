<!-- ./frontend/app/components/articles/FinishButton.vue -->
<script setup>
defineProps({
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['close'])
</script>

<template>
  <button
    type="button"
    class="btn btn-primary btn-lg w-full sm:w-auto"
    :disabled="disabled"
    @click="emit('close')"
  >
    <span
      v-if="disabled"
      class="loading loading-spinner loading-sm"
    />

    <Icon
      v-else
      name="lucide:check"
      class="size-5"
    />

    Завершить
  </button>
</template>