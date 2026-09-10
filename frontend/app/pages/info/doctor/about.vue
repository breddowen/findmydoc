<!-- ./frontend/app/pages/info/doctor/about.vue -->
<script setup>
definePageMeta({
  middleware: ['doctor-only'],
})

useHead({
  title: 'О приложении для врача — MentalConnect',
})

const info = useInfoStore()
</script>

<template>
  <InfoArticle :entry="info.doctorAbout" />
</template>