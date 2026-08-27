<!-- ./frontend/app/pages/login.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
})

const route = useRoute()
const auth = useAuthStore()

const email = ref('')
const password = ref('')
const showPassword = ref(false)

const errorMessage = ref('')
const roleSelectorOpen = ref(false)

const sessionExpired = computed(
  () => route.query.sessionExpired === '1',
)

async function completeLogin() {
  const redirect =
    typeof route.query.redirect === 'string'
      ? route.query.redirect
      : '/dashboard'

  await navigateTo(redirect)
}

async function submitLogin() {
  errorMessage.value = ''

  try {
    const result = await auth.login(
      email.value,
      password.value,
    )

    if (result.needsRoleSelection) {
      roleSelectorOpen.value = true
      return
    }

    await completeLogin()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось выполнить вход'
  }
}

async function submitPasskeyLogin() {
  errorMessage.value = ''

  try {
    const result = await auth.loginWithPasskey()

    if (result.needsRoleSelection) {
      roleSelectorOpen.value = true
      return
    }

    await completeLogin()
  } catch (error) {
    if (error?.name === 'NotAllowedError') {
      errorMessage.value =
        'Вход с passkey был отменён'
      return
    }

    errorMessage.value =
      error?.data?.detail
      || error?.message
      || 'Не удалось войти с passkey'
  }
}
</script>

<template>
  <div
    class="card bg-base-100 border-base-300 border shadow-xl"
  >
    <div class="card-body p-5 sm:p-8">
      <div>
        <h1 class="text-2xl font-bold">
          Вход
        </h1>

        <p class="text-base-content/60 mt-1 text-sm">
          Войдите в аккаунт MentalMe
        </p>
      </div>

      <div
        v-if="sessionExpired"
        class="alert alert-warning mt-4"
      >
        <Icon
          name="lucide:clock-alert"
          class="size-5"
        />
        <span>
          Сессия завершена. Выполните вход повторно.
        </span>
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
        @submit.prevent="submitLogin"
      >
        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Email
            </span>
          </span>

          <label
            class="input input-bordered flex w-full items-center gap-2"
          >
            <Icon
              name="lucide:mail"
              class="text-base-content/50 size-4"
            />

            <input
              v-model.trim="email"
              type="email"
              required
              autocomplete="username webauthn"
              placeholder="name@example.com"
              class="min-w-0 grow"
            >
          </label>
        </label>

        <label class="form-control block">
          <span class="label">
            <span class="label-text">
              Пароль
            </span>

            <NuxtLink
              to="/forgot-password"
              class="link link-primary text-sm"
            >
              Забыли пароль?
            </NuxtLink>
          </span>

          <label
            class="input input-bordered flex w-full items-center gap-2"
          >
            <Icon
              name="lucide:lock-keyhole"
              class="text-base-content/50 size-4"
            />

            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              required
              autocomplete="current-password"
              placeholder="Введите пароль"
              class="min-w-0 grow"
            >

            <button
              type="button"
              class="btn btn-circle btn-ghost btn-xs"
              :aria-label="
                showPassword
                  ? 'Скрыть пароль'
                  : 'Показать пароль'
              "
              @click="showPassword = !showPassword"
            >
              <Icon
                :name="
                  showPassword
                    ? 'lucide:eye-off'
                    : 'lucide:eye'
                "
                class="size-4"
              />
            </button>
          </label>
        </label>

        <button
          type="submit"
          class="btn btn-primary w-full"
          :disabled="auth.loading"
        >
          <span
            v-if="auth.loading"
            class="loading loading-spinner loading-sm"
          />

          Войти
        </button>
      </form>

      <div class="divider text-xs">
        ИЛИ
      </div>

      <button
        type="button"
        class="btn btn-outline w-full"
        :disabled="auth.loading"
        @click="submitPasskeyLogin"
      >
        <Icon
          name="lucide:fingerprint"
          class="size-5"
        />
        Войти с passkey
      </button>
    </div>
  </div>

  <AuthRoleSelector
    v-model="roleSelectorOpen"
    @selected="completeLogin"
  />
</template>