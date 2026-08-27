<!-- ./frontend/app/pages/reset-password.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
})

const route = useRoute()
const { $api } = useNuxtApp()

const password = ref('')
const confirmation = ref('')

const loading = ref(false)
const success = ref(false)
const errorMessage = ref('')

async function submit() {
  loading.value = true
  errorMessage.value = ''

  try {
    await $api(
      '/api/v1/auth/password-reset/confirm',
      {
        method: 'POST',
        body: {
          token: route.query.token,
          new_password: password.value,
          new_password_confirmation:
            confirmation.value,
        },
      },
    )

    success.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось восстановить пароль'
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
      <template v-if="success">
        <div class="text-center">
          <Icon
            name="lucide:circle-check-big"
            class="text-success mx-auto size-14"
          />

          <h1 class="mt-4 text-2xl font-bold">
            Пароль изменён
          </h1>

          <NuxtLink
            to="/login"
            class="btn btn-primary mt-6 w-full"
          >
            Перейти ко входу
          </NuxtLink>
        </div>
      </template>

      <template v-else>
        <h1 class="text-2xl font-bold">
          Новый пароль
        </h1>

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
            v-model="password"
            type="password"
            required
            minlength="8"
            autocomplete="new-password"
            class="input input-bordered w-full"
            placeholder="Новый пароль"
          >

          <input
            v-model="confirmation"
            type="password"
            required
            minlength="8"
            autocomplete="new-password"
            class="input input-bordered w-full"
            placeholder="Повторите пароль"
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
            Сохранить пароль
          </button>
        </form>
      </template>
    </div>
  </div>
</template>