<!-- ./frontend/app/components/users/InviteForm.vue -->
<script setup>
const emit = defineEmits([
  'created',
  'cancel',
])

const auth = useAuthStore()
const usersStore = useUsersStore()
const { $api } = useNuxtApp()

const specialities = ref([])
const loadingSpecialities = ref(false)

const errorMessage = ref('')

const form = reactive({
  role: 'patient',
  email: '',
  record_id: '',
  speciality_id: '',
})

const allRoleOptions = [
  {
    value: 'patient',
    label: 'Пациент',
    description: 'Потребуется номер медицинской карты.',
  },
  {
    value: 'doctor',
    label: 'Врач',
    description: 'Потребуется выбрать специальность.',
  },
  {
    value: 'relative',
    label: 'Родственник',
    description: 'Связь с пациентом можно настроить позднее.',
  },
  {
    value: 'med_assistant',
    label: 'Медицинский ассистент',
    description: 'Доступно только суперпользователю.',
  },
  {
    value: 'superuser',
    label: 'Суперпользователь',
    description: 'Получит полный доступ к системе.',
  },
]

const roleOptions = computed(() => {
  if (auth.activeRole === 'superuser') {
    return allRoleOptions
  }

  return allRoleOptions.filter(option =>
    [
      'patient',
      'doctor',
      'relative',
    ].includes(option.value),
  )
})

const selectedRole = computed(() =>
  roleOptions.value.find(
    option => option.value === form.role,
  ),
)

const isPatient = computed(
  () => form.role === 'patient',
)

const isDoctor = computed(
  () => form.role === 'doctor',
)

const normalizedRecordId = computed(() =>
  form.record_id.trim().toUpperCase(),
)

const recordIdValid = computed(() =>
  /^[A-Z]{1,2}[0-9]{6}$/.test(
    normalizedRecordId.value,
  ),
)

const canSubmit = computed(() => {
  if (!form.email.trim()) return false

  if (isPatient.value && !recordIdValid.value) {
    return false
  }

  if (isDoctor.value && !form.speciality_id) {
    return false
  }

  return !usersStore.creatingInvitation
})

function normalizeRecordIdInput(event) {
  const normalized = event.target.value
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, '')
    .slice(0, 8)

  form.record_id = normalized
  event.target.value = normalized
}

async function fetchSpecialities() {
  loadingSpecialities.value = true

  try {
    specialities.value = await $api(
      '/api/v1/specialities',
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить специальности'
  } finally {
    loadingSpecialities.value = false
  }
}

async function submit() {
  if (!canSubmit.value) return

  errorMessage.value = ''

  const payload = {
    role: form.role,
    email: form.email.trim(),
  }

  if (isPatient.value) {
    payload.record_id = normalizedRecordId.value
  }

  if (isDoctor.value) {
    payload.speciality_id = form.speciality_id
  }

  try {
    const response =
      await usersStore.createInvitation(payload)

    emit('created', response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось создать приглашение'
  }
}

watch(
  () => form.role,
  () => {
    errorMessage.value = ''

    if (!isPatient.value) {
      form.record_id = ''
    }

    if (!isDoctor.value) {
      form.speciality_id = ''
    }
  },
)

onMounted(fetchSpecialities)
</script>

<template>
  <form
    class="space-y-5"
    @submit.prevent="submit"
  >
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

    <fieldset class="space-y-2">
      <legend class="mb-2 text-sm font-medium">
        Роль пользователя
      </legend>

      <label
        v-for="option in roleOptions"
        :key="option.value"
        class="border-base-300 hover:border-primary flex cursor-pointer items-start gap-3 rounded-2xl border p-4 transition"
        :class="{
          'border-primary bg-primary/5':
            form.role === option.value,
        }"
      >
        <input
          v-model="form.role"
          type="radio"
          name="role"
          :value="option.value"
          class="radio radio-primary mt-0.5"
        >

        <span class="min-w-0">
          <span class="block font-medium">
            {{ option.label }}
          </span>

          <span
            class="text-base-content/60 mt-1 block text-sm"
          >
            {{ option.description }}
          </span>
        </span>
      </label>
    </fieldset>

    <label class="form-control block">
      <span class="label">
        <span class="label-text font-medium">
          Email
        </span>
      </span>

      <input
        v-model.trim="form.email"
        type="email"
        required
        maxlength="320"
        autocomplete="email"
        class="input input-bordered w-full"
        placeholder="user@example.com"
      >
    </label>

    <label
      v-if="isPatient"
      class="form-control block"
    >
      <span class="label">
        <span class="label-text font-medium">
          Номер медицинской карты
        </span>
      </span>

      <input
        :value="form.record_id"
        type="text"
        required
        maxlength="8"
        autocomplete="off"
        class="input input-bordered w-full font-mono uppercase"
        :class="{
          'input-error':
            form.record_id
            && !recordIdValid,
        }"
        placeholder="A000000"
        @input="normalizeRecordIdInput"
      >

      <span class="label">
        <span
          class="label-text-alt"
          :class="{
            'text-error':
              form.record_id
              && !recordIdValid,
          }"
        >
          Одна или две латинские буквы и шесть цифр.
        </span>
      </span>
    </label>

    <label
      v-if="isDoctor"
      class="form-control block"
    >
      <span class="label">
        <span class="label-text font-medium">
          Специальность
        </span>
      </span>

      <select
        v-model="form.speciality_id"
        required
        class="select select-bordered w-full"
        :disabled="loadingSpecialities"
      >
        <option value="" disabled>
          {{
            loadingSpecialities
              ? 'Загрузка...'
              : 'Выберите специальность'
          }}
        </option>

        <option
          v-for="speciality in specialities"
          :key="speciality.id"
          :value="speciality.id"
        >
          {{ speciality.name }}
        </option>
      </select>
    </label>

    <div
      v-if="selectedRole"
      class="bg-base-200 rounded-2xl p-4 text-sm"
    >
      <div class="flex gap-3">
        <Icon
          name="lucide:info"
          class="text-info mt-0.5 size-5 shrink-0"
        />

        <p class="text-base-content/70">
          Пользователь получит роль
          <strong>{{ selectedRole.label }}</strong>.
          Email и данные приглашения нельзя будет изменить
          при регистрации.
        </p>
      </div>
    </div>

    <div
      class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
    >
      <button
        type="button"
        class="btn"
        :disabled="usersStore.creatingInvitation"
        @click="emit('cancel')"
      >
        Отмена
      </button>

      <button
        type="submit"
        class="btn btn-primary"
        :disabled="!canSubmit"
      >
        <span
          v-if="usersStore.creatingInvitation"
          class="loading loading-spinner loading-sm"
        />

        Создать приглашение
      </button>
    </div>
  </form>
</template>