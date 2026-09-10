<!-- ./frontend/app/pages/info/doctor/conversation.vue -->
<script setup>
definePageMeta({
  middleware: ['doctor-only'],
})

useHead({
  title: 'Как рассказать пациенту — MentalConnect',
})

const info = useInfoStore()
</script>

<template>
  <InfoArticle :entry="info.doctorConversation" />
</template>