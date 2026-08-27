<!-- ./frontend/app/components/layout/EmailVerificationBanner.vue -->
<script setup>
const userStore = useUserStore()

const loading = ref(false)
const message = ref('')
const errorMessage = ref('')

async function resend() {
  loading.value = true
  message.value = ''
  errorMessage.value = ''

  try {
    const response =
      await userStore.resendVerificationEmail()

    message.value = response.message
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сформировать ссылку'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div
    v-if="
      userStore.user
      && !userStore.isEmailVerified
    "
    class="bg-warning text-warning-content"
  >
    <div
      class="mx-auto flex max-w-7xl flex-col gap-3 px-4 py-3 sm:flex-row sm:items-center sm:justify-between"
    >
      <div class="flex items-start gap-3">
        <Icon
          name="lucide:mail-warning"
          class="mt-0.5 size-5 shrink-0"
        />

        <div>
          <p class="font-semibold">
            Подтвердите email
          </p>

          <p class="text-sm opacity-80">
            Мы отправили ссылку на
            {{ userStore.user.email }}.
          </p>

          <p
            v-if="message"
            class="mt-1 text-sm font-medium"
          >
            {{ message }}
          </p>

          <p
            v-if="errorMessage"
            class="mt-1 text-sm font-medium"
          >
            {{ errorMessage }}
          </p>
        </div>
      </div>

      <button
        type="button"
        class="btn btn-sm"
        :disabled="loading"
        @click="resend"
      >
        <span
          v-if="loading"
          class="loading loading-spinner loading-xs"
        />

        Отправить повторно
      </button>
    </div>
  </div>
</template>