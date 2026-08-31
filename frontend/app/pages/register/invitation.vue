<!-- ./frontend/app/pages/register/invitation.vue -->
<script setup>
definePageMeta({
  layout: 'auth',
})

const route = useRoute()
const { $api } = useNuxtApp()

const token = computed(() => {
  const value = route.query.token
  return typeof value === 'string' ? value : ''
})

const preview = ref(null)

const loading = ref(true)
const submitting = ref(false)
const completed = ref(false)

const errorMessage = ref('')
const successMessage = ref('')

const form = reactive({
  password: '',
  password_confirmation: '',
})

const roleNames = {
  superuser: 'Суперпользователь',
  med_assistant: 'Медицинский ассистент',
  doctor: 'Врач',
  patient: 'Пациент',
  relative: 'Родственник',
}

const passwordsMatch = computed(
  () =>
    form.password_confirmation.length === 0
    || form.password
      === form.password_confirmation,
)

const canSubmit = computed(
  () =>
    form.password.length >= 8
    && form.password.length <= 128
    && form.password
      === form.password_confirmation
    && !submitting.value,
)

async function fetchPreview() {
  loading.value = true
  errorMessage.value = ''

  if (!token.value) {
    errorMessage.value =
      'В ссылке отсутствует токен приглашения'
    loading.value = false
    return
  }

  try {
    preview.value = await $api(
      '/api/v1/invitations/preview',
      {
        query: {
          token: token.value,
        },
      },
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Приглашение недействительно или просрочено'
  } finally {
    loading.value = false
  }
}

async function acceptInvitation() {
  if (!canSubmit.value) return

  submitting.value = true
  errorMessage.value = ''

  try {
    const response = await $api(
      '/api/v1/invitations/accept',
      {
        method: 'POST',
        body: {
          token: token.value,
          password: form.password,
          password_confirmation:
            form.password_confirmation,
        },
      },
    )

    completed.value = true
    successMessage.value = response.email_verification_required
      ? (
          'Регистрация завершена. Мы отправили '
          + 'на вашу почту ссылку для подтверждения email.'
        )
      : 'Регистрация успешно завершена.'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось завершить регистрацию'
  } finally {
    submitting.value = false
  }
}

onMounted(fetchPreview)
</script>

<template>
  <section
    class="card bg-base-100 border-base-300 border shadow-xl"
  >
    <div class="card-body p-5 sm:p-7">
      <div
        v-if="loading"
        class="flex justify-center py-12"
      >
        <span
          class="loading loading-spinner loading-lg text-primary"
        />
      </div>

      <template v-else-if="completed">
        <div
          class="bg-success/10 text-success mx-auto flex size-16 items-center justify-center rounded-full"
        >
          <Icon
            name="lucide:circle-check"
            class="size-9"
          />
        </div>

        <h1 class="mt-3 text-center text-2xl font-bold">
          Аккаунт создан
        </h1>

        <div class="alert alert-success mt-4">
          <span>{{ successMessage }}</span>
        </div>

        <NuxtLink
          to="/login"
          class="btn btn-primary mt-3 w-full"
        >
          Перейти ко входу
        </NuxtLink>
      </template>

      <template v-else-if="errorMessage && !preview">
        <div
          class="bg-error/10 text-error mx-auto flex size-16 items-center justify-center rounded-full"
        >
          <Icon
            name="lucide:link-2-off"
            class="size-8"
          />
        </div>

        <h1 class="mt-3 text-center text-2xl font-bold">
          Приглашение недоступно
        </h1>

        <div class="alert alert-error mt-4">
          <span>{{ errorMessage }}</span>
        </div>

        <NuxtLink
          to="/login"
          class="btn mt-3 w-full"
        >
          На страницу входа
        </NuxtLink>
      </template>

      <template v-else>
        <div>
          <h1 class="text-2xl font-bold">
            Регистрация
          </h1>

          <p class="text-base-content/60 mt-1">
            Создайте пароль для входа в MentalMe.
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

        <dl
          v-if="preview"
          class="bg-base-200 mt-5 space-y-3 rounded-2xl p-4 text-sm"
        >
          <div>
            <dt class="text-base-content/60">
              Email
            </dt>
            <dd class="font-medium">
              {{ preview.email }}
            </dd>
          </div>

          <div>
            <dt class="text-base-content/60">
              Роль
            </dt>
            <dd class="font-medium">
              {{
                roleNames[preview.invitation_type]
                || preview.invitation_type
              }}
            </dd>
          </div>

          <div v-if="preview.record_id">
            <dt class="text-base-content/60">
              Номер медицинской карты
            </dt>
            <dd class="font-mono font-medium">
              {{ preview.record_id }}
            </dd>
          </div>

          <div v-if="preview.speciality_name">
            <dt class="text-base-content/60">
              Специальность
            </dt>
            <dd class="font-medium">
              {{ preview.speciality_name }}
            </dd>
          </div>
        </dl>

        <form
          class="mt-5 space-y-4"
          @submit.prevent="acceptInvitation"
        >
          <label class="form-control block">
            <span class="label">
              <span class="label-text font-medium">
                Новый пароль
              </span>
            </span>

            <input
              v-model="form.password"
              type="password"
              required
              minlength="8"
              maxlength="128"
              autocomplete="new-password"
              class="input input-bordered w-full"
              placeholder="Не менее 8 символов"
            >
          </label>

          <label class="form-control block">
            <span class="label">
              <span class="label-text font-medium">
                Подтверждение пароля
              </span>
            </span>

            <input
              v-model="form.password_confirmation"
              type="password"
              required
              minlength="8"
              maxlength="128"
              autocomplete="new-password"
              class="input input-bordered w-full"
              :class="{
                'input-error': !passwordsMatch,
              }"
              placeholder="Повторите пароль"
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
            class="btn btn-primary mt-2 w-full"
            :disabled="!canSubmit"
          >
            <span
              v-if="submitting"
              class="loading loading-spinner loading-sm"
            />

            Завершить регистрацию
          </button>
        </form>
      </template>
    </div>
  </section>
</template>