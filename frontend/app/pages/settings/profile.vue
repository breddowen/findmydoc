<!-- ./frontend/app/pages/settings/profile.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()

const message = ref('')
const errorMessage = ref('')

const form = reactive({
  last_name: '',
  first_name: '',
  middle_name: '',
  gender: '',
  dob: '',
})
const { isClientReady } = useClientReady()
const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient',
)

function fillForm() {
  const user = userStore.user

  if (!user) return

  Object.assign(form, {
    last_name: user.last_name || '',
    first_name: user.first_name || '',
    middle_name: user.middle_name || '',
    gender: user.gender || '',
    dob: user.patient_profile?.dob || '',
  })
}

async function load() {
  errorMessage.value = ''

  try {
    if (!userStore.user) {
      await userStore.fetchMe()
    }

    fillForm()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить личные данные'
  }
}

async function save() {
  errorMessage.value = ''
  message.value = ''

  const payload = {
    last_name:
      form.last_name.trim() || null,
    first_name:
      form.first_name.trim() || null,
    middle_name:
      form.middle_name.trim() || null,
    gender: form.gender || null,
  }

  if (isPatient.value) {
    payload.dob = form.dob || null
  }

  try {
    await userStore.updateProfile(payload)

    fillForm()
    message.value = 'Личные данные сохранены'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить личные данные'
  }
}

onMounted(load)
</script>

<template>
  <div class="mx-auto max-w-3xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Личные данные
      </h1>

      <p class="text-base-content/60 mt-1">
        Имя и основные данные вашего аккаунта.
      </p>
    </header>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <UiContentSkeleton
      v-if="userStore.loading"
      variant="card"
      :count="1"
    />

    <form
      v-else
      class="card bg-base-100 border-base-300 border"
      @submit.prevent="save"
    >
      <div class="card-body gap-5 p-5 sm:p-6">
        <label class="form-control block">
          <span class="label-text mb-2">
            Email
          </span>

          <input
            :value="userStore.user?.email"
            type="email"
            readonly
            class="input input-bordered bg-base-200 w-full"
          >

          <span
            class="text-base-content/50 mt-1 text-xs"
          >
            Изменение email пока не предусмотрено.
          </span>
        </label>

        <div class="grid gap-4 sm:grid-cols-2">
          <label class="form-control block">
            <span class="label-text mb-2">
              Фамилия
            </span>

            <input
              v-model="form.last_name"
              type="text"
              maxlength="100"
              autocomplete="family-name"
              class="input input-bordered w-full"
            >
          </label>

          <label class="form-control block">
            <span class="label-text mb-2">
              Имя
            </span>

            <input
              v-model="form.first_name"
              type="text"
              maxlength="100"
              autocomplete="given-name"
              class="input input-bordered w-full"
            >
          </label>

          <label class="form-control block">
            <span class="label-text mb-2">
              Отчество
            </span>

            <input
              v-model="form.middle_name"
              type="text"
              maxlength="100"
              class="input input-bordered w-full"
            >
          </label>

          <label class="form-control block">
            <span class="label-text mb-2">
              Пол
            </span>

            <select
              v-model="form.gender"
              class="select select-bordered w-full"
            >
              <option value="">
                Не указан
              </option>
              <option value="male">
                Мужской
              </option>
              <option value="female">
                Женский
              </option>
              <option value="other">
                Другой
              </option>
              <option value="not_specified">
                Не хочу указывать
              </option>
            </select>
          </label>

          <label
            v-if="isPatient"
            class="form-control block"
          >
            <span class="label-text mb-2">
              Дата рождения
            </span>

            <input
              v-model="form.dob"
              type="date"
              :max="
                new Date()
                  .toISOString()
                  .slice(0, 10)
              "
              class="input input-bordered w-full"
            >
          </label>
        </div>

        <div
          class="card-actions border-base-300 justify-end border-t pt-5"
        >
          <button
            type="submit"
            class="btn btn-primary"
            :disabled="userStore.saving"
          >
            <span
              v-if="userStore.saving"
              class="loading loading-spinner loading-sm"
            />

            <Icon
              v-else
              name="lucide:save"
              class="size-4"
            />

            Сохранить
          </button>
        </div>
      </div>
    </form>
  </div>
</template>