<!-- ./frontend/app/pages/forgot-password.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
})

const { $api } = useNuxtApp()

const email = ref('')
const loading = ref(false)
const message = ref('')
const errorMessage = ref('')

async function submit() {
  loading.value = true
  message.value = ''
  errorMessage.value = ''

  try {
    const response = await $api(
      '/api/v1/auth/password-reset/request',
      {
        method: 'POST',
        body: {
          email: email.value,
        },
      },
    )

    message.value = response.message
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось отправить запрос'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div
    class="card bg-base-100 border-base-300 border shadow-xl"
  >
    <div class="card-body p-5 sm:p-8">
      <h1 class="text-2xl font-bold">
        Восстановление пароля
      </h1>

      <p class="text-base-content/60 text-sm">
        Введите email, указанный в аккаунте.
      </p>

      <div
        v-if="message"
        class="alert alert-success mt-4"
      >
        {{ message }}
      </div>

      <div
        v-if="errorMessage"
        class="alert alert-error mt-4"
      >
        {{ errorMessage }}
      </div>

      <form
        class="mt-5 space-y-4"
        @submit.prevent="submit"
      >
        <input
          v-model.trim="email"
          type="email"
          required
          autocomplete="email"
          class="input input-bordered w-full"
          placeholder="name@example.com"
        >

        <button
          type="submit"
          class="btn btn-primary w-full"
          :disabled="loading"
        >
          <span
            v-if="loading"
            class="loading loading-spinner loading-sm"
          />
          Получить ссылку
        </button>
      </form>

      <NuxtLink
        to="/login"
        class="btn btn-ghost mt-2"
      >
        Вернуться ко входу
      </NuxtLink>
    </div>
  </div>
</template>