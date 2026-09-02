<!-- ./frontend/app/pages/patients/index.vue -->
<script setup>
const auth = useAuthStore()
const { isClientReady } = useClientReady()

const titles = {
  doctor: 'Мои пациенты',
  med_assistant: 'Пациенты',
  superuser: 'Пациенты',
}

const title = computed(() => {
  // Сервер и клиент до завершения hydration
  // должны вернуть одинаковый заголовок.
  if (!isClientReady.value) {
    return 'Пациенты'
  }

  return titles[auth.activeRole] || 'Пациенты'
})
</script>

<template>
  <div class="space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        {{ title }}
      </h1>

      <p class="text-base-content/60 mt-1">
        Регистрация, активность и работа с контентом.
      </p>
    </header>

    <PatientsList />
  </div>
</template>