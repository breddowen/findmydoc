<!-- ./frontend/app/components/patient/support/ConsultationButton.vue -->
<script setup>
defineProps({
  disabled: {
    type: Boolean,
    default: false,
  },
})

const support = usePatientSupportStore()
</script>

<template>
  <button
    type="button"
    class="btn btn-primary w-full sm:w-auto"
    :disabled="disabled"
    @click="support.open('actions')"
  >
    <Icon
      name="lucide:calendar-plus"
      class="size-5"
    />

    Записаться на консультацию
  </button>
</template>