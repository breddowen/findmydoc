<!-- ./frontend/app/components/layout/PatientActions.vue -->
<script setup>
const emit = defineEmits(['menu'])

const contactOpen = ref(false)
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

  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm text-primary bg-primary/10 shrink-0"
    aria-label="Заказать звонок ассистента"
    title="Связаться с ассистентом"
    @click="contactOpen = true"
  >
    <Icon name="lucide:phone" class="size-4" />
  </button>

  <PatientContactDialog v-model="contactOpen" />
</template>