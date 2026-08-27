<!-- ./frontend/app/pages/programs/[id]/edit.vue -->
<script setup>
definePageMeta({
  middleware: [
    'program-manager',
  ],
})

const route = useRoute()
</script>

<template>
  <ProgramsConfiguratorEditor
    :program-id="route.params.id"
  />
</template>