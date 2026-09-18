<!-- ./frontend/app/pages/settings/test-styles.vue -->
<script setup>
definePageMeta({
  middleware: ['test-styles'],
})

useHead({
  title: 'Студия оформления — MentalConnect',
})
</script>

<template>
  <TestStylesEditor />
</template>