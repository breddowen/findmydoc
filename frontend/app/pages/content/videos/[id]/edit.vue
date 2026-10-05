<!-- ./frontend/app/pages/content/videos/[id]/edit.vue -->
<script setup>
definePageMeta({
  middleware: 'video-manager',
  key: route => route.fullPath,
})

const route = useRoute()
</script>

<template>
  <VideosEditor :video-id="String(route.params.id)" />
</template>