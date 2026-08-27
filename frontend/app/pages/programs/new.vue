<!-- ./frontend/app/pages/programs/new.vue -->
<script setup>
definePageMeta({
  middleware: [
    'program-manager',
  ],
})
</script>

<template>
  <ProgramsConfiguratorEditor />
</template>