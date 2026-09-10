<!-- ./frontend/app/components/layout/PatientActions.vue -->
<script setup>
const emit = defineEmits(['menu'])
</script>

<template>
  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm shrink-0"
    aria-label="Открыть меню"
    @click="emit('menu')"
  >
    <Icon name="lucide:menu" class="size-5" />
  </button>
</template>