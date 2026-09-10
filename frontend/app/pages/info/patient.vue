<!-- ./frontend/app/pages/info/patient.vue -->
<script setup>
useHead({
  title: 'Как помогает приложение — MentalConnect',
})

const info = useInfoStore()
</script>

<template>
  <InfoArticle :entry="info.patientAbout" />
</template>