<!-- ./frontend/app/pages/verify-email.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
})

const route = useRoute()
const { $api } = useNuxtApp()

const loading = ref(true)
const success = ref(false)
const errorMessage = ref('')

onMounted(async () => {
  try {
    await $api(
      '/api/v1/auth/email-verification/confirm',
      {
        method: 'POST',
        body: {
          token: route.query.token,
        },
      },
    )

    success.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось подтвердить email'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div
    class="card bg-base-100 border-base-300 border shadow-xl"
  >
    <div class="card-body p-6 text-center sm:p-8">
      <span
        v-if="loading"
        class="loading loading-spinner loading-lg text-primary mx-auto"
      />

      <template v-else-if="success">
        <Icon
          name="lucide:badge-check"
          class="text-success mx-auto size-14"
        />

        <h1 class="mt-4 text-2xl font-bold">
          Email подтверждён
        </h1>
      </template>

      <template v-else>
        <Icon
          name="lucide:circle-alert"
          class="text-error mx-auto size-14"
        />

        <h1 class="mt-4 text-2xl font-bold">
          Не удалось подтвердить email
        </h1>

        <p class="text-base-content/60 mt-2">
          {{ errorMessage }}
        </p>
      </template>

      <NuxtLink
        to="/login"
        class="btn btn-primary mt-6"
      >
        Перейти ко входу
      </NuxtLink>
    </div>
  </div>
</template>