<!-- ./frontend/app/components/patient/support/Fab.vue -->
<script setup>
const support = usePatientSupportStore()

const {
  floatingStyle,
} = useFooterAwarePosition()
</script>

<template>
  <button
    type="button"
    class="btn btn-primary btn-circle btn-lg fixed z-40 shadow-xl ring-4 ring-primary/15"
    :style="floatingStyle"
    aria-label="Связь с клиникой"
    title="Связь с клиникой"
    @click="support.open('actions')"
  >
    <Icon
      name="lucide:messages-square"
      class="size-6"
    />
  </button>
</template>