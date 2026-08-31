<!-- ./frontend/app/components/auth/PasswordForm.vue -->
<script setup>
const auth = useAuthStore()
const { $api } = useNuxtApp()

const submitting = ref(false)
const errorMessage = ref('')

const form = reactive({
  current_password: '',
  new_password: '',
  new_password_confirmation: '',
})

const passwordsMatch = computed(
  () =>
    !form.new_password_confirmation
    || form.new_password
      === form.new_password_confirmation,
)

const canSubmit = computed(
  () =>
    form.current_password.length > 0
    && form.new_password.length >= 8
    && form.new_password.length <= 128
    && form.new_password
      === form.new_password_confirmation
    && !submitting.value,
)

async function submit() {
  if (!canSubmit.value) return

  submitting.value = true
  errorMessage.value = ''

  try {
    await $api('/api/v1/auth/change-password', {
      method: 'POST',
      body: {
        current_password: form.current_password,
        new_password: form.new_password,
        new_password_confirmation:
          form.new_password_confirmation,
      },
    })

    await auth.logout()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить пароль'
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <section
    class="card bg-base-100 border-base-300 border"
  >
    <div class="card-body p-5 sm:p-6">
      <div>
        <h2 class="card-title">
          <Icon
            name="lucide:key-round"
            class="size-6"
          />
          Пароль
        </h2>

        <p class="text-base-content/60 mt-2 text-sm">
          После изменения пароля потребуется войти
          в аккаунт повторно.
        </p>
      </div>

      <div
        v-if="errorMessage"
        class="alert alert-error mt-4"
      >
        <Icon
          name="lucide:circle-alert"
          class="size-5"
        />
        <span>{{ errorMessage }}</span>
      </div>

      <form
        class="mt-5 space-y-4"
        @submit.prevent="submit"
      >
        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Текущий пароль
            </span>
          </span>

          <input
            v-model="form.current_password"
            type="password"
            required
            maxlength="128"
            autocomplete="current-password"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Новый пароль
            </span>
          </span>

          <input
            v-model="form.new_password"
            type="password"
            required
            minlength="8"
            maxlength="128"
            autocomplete="new-password"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Подтверждение нового пароля
            </span>
          </span>

          <input
            v-model="form.new_password_confirmation"
            type="password"
            required
            minlength="8"
            maxlength="128"
            autocomplete="new-password"
            class="input input-bordered w-full"
            :class="{
              'input-error': !passwordsMatch,
            }"
          >

          <span
            v-if="!passwordsMatch"
            class="text-error mt-1 text-xs"
          >
            Пароли не совпадают
          </span>
        </label>

        <button
          type="submit"
          class="btn btn-primary"
          :disabled="!canSubmit"
        >
          <span
            v-if="submitting"
            class="loading loading-spinner loading-sm"
          />

          Изменить пароль
        </button>
      </form>
    </div>
  </section>
</template>