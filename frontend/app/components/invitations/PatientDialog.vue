<!-- ./frontend/app/components/invitations/PatientDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const emit = defineEmits([
  'created',
  'attached',
])

const store = useInvitationsStore()

const errorMessage = ref('')
const existingPatient = ref(null)

const form = reactive({
  record_id: '',
  email: '',
  fullname: '',
  dob: '',
  gender: '',
})

const normalizedRecordId = computed(() =>
  form.record_id.trim().toUpperCase(),
)

const recordIdValid = computed(() =>
  /^[A-Z]{1,2}[0-9]{6}$/.test(
    normalizedRecordId.value,
  ),
)

const canSubmit = computed(() =>
  Boolean(
    recordIdValid.value
    && form.email.trim()
    && !store.preparingPatient,
  ),
)

function reset() {
  errorMessage.value = ''
  existingPatient.value = null

  Object.assign(form, {
    record_id: '',
    email: '',
    fullname: '',
    dob: '',
    gender: '',
  })
}

function normalizeRecordIdInput(event) {
  const normalized = event.target.value
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, '')
    .slice(0, 8)

  form.record_id = normalized
  event.target.value = normalized
  existingPatient.value = null
}

function buildPayload(confirmExisting = false) {
  return {
    record_id: normalizedRecordId.value,
    email: form.email.trim(),
    fullname: form.fullname.trim() || null,
    dob: form.dob || null,
    gender: form.gender || null,
    confirm_existing: confirmExisting,
  }
}

function handleResponse(response) {
  if (
    response.status
    === 'confirmation_required'
  ) {
    existingPatient.value = response
    return
  }

  if (response.status === 'patient_attached') {
    model.value = false
    emit('attached', response)
    return
  }

  if (response.status === 'invitation_created') {
    model.value = false
    emit('created', response)
  }
}

async function submit() {
  if (!canSubmit.value) return

  errorMessage.value = ''
  existingPatient.value = null

  try {
    const response = await store.preparePatient(
      buildPayload(false),
    )

    handleResponse(response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось подготовить приглашение'
  }
}

async function attachExisting() {
  if (
    !existingPatient.value
    || !existingPatient.value.email_matches
  ) {
    return
  }

  errorMessage.value = ''

  try {
    const response = await store.preparePatient(
      buildPayload(true),
    )

    handleResponse(response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось прикрепить пациента'
  }
}

function useRegisteredEmail() {
  if (!existingPatient.value) return

  form.email =
    existingPatient.value.registered_email

  // После исправления снова проверяем данные,
  // прежде чем разрешить прикрепление.
  existingPatient.value = null
}

function openExistingPatient() {
  if (!existingPatient.value) return

  const patientId =
    existingPatient.value.patient_id

  model.value = false

  emit('attached', {
    status: 'patient_attached',
    message: 'Пациент уже прикреплён к врачу',
    patient_id: patientId,
    record_id:
      existingPatient.value.record_id,
  })
}

watch(model, (opened) => {
  if (opened) {
    reset()
  }
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Пригласить пациента"
    max-width-class="max-w-xl"
  >
    <form
      id="doctor-patient-invitation-form"
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

      <div
        v-if="existingPatient"
        class="space-y-4"
      >
        <div
          class="alert"
          :class="
            existingPatient.email_matches
              ? 'alert-info'
              : 'alert-warning'
          "
        >
          <Icon
            name="lucide:user-round-check"
            class="size-5"
          />

          <div>
            <p class="font-medium">
              Пациент уже зарегистрирован
            </p>

            <p class="mt-1 text-sm">
              Карта:
              {{ existingPatient.record_id }}
            </p>
          </div>
        </div>

        <div
          class="border-base-300 rounded-2xl border p-4"
        >
          <p class="text-base-content/50 text-xs">
            Email в базе
          </p>

          <p class="mt-1 font-medium">
            {{ existingPatient.registered_email }}
          </p>

          <p
            v-if="!existingPatient.email_matches"
            class="text-warning mt-3 text-sm"
          >
            Введённый email не совпадает с email
            зарегистрированного пациента. Возможно,
            в адресе была допущена опечатка.
          </p>
        </div>

        <button
          v-if="!existingPatient.email_matches"
          type="button"
          class="btn btn-warning w-full"
          @click="useRegisteredEmail"
        >
          <Icon
            name="lucide:mail-check"
            class="size-4"
          />
          Использовать email из базы
        </button>
      </div>

      <template v-else>
        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Номер медицинской карты
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
            placeholder="A123456"
            @input="normalizeRecordIdInput"
          >

          <span
            class="text-base-content/50 mt-1 text-xs"
          >
            Одна или две латинские буквы и шесть цифр.
          </span>
        </label>

        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Email
          </span>

          <input
            v-model.trim="form.email"
            type="email"
            required
            maxlength="320"
            autocomplete="email"
            class="input input-bordered w-full"
            placeholder="patient@example.com"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            ФИО
          </span>

          <input
            v-model="form.fullname"
            type="text"
            maxlength="300"
            class="input input-bordered w-full"
            placeholder="Иванов Иван Иванович"
          >
        </label>

        <div class="grid gap-4 sm:grid-cols-2">
          <label class="form-control block">
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
        </div>
      </template>
    </form>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          :disabled="store.preparingPatient"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          v-if="
            existingPatient?.already_linked
            && existingPatient?.email_matches
          "
          type="button"
          class="btn btn-primary"
          @click="openExistingPatient"
        >
          Открыть пациента
        </button>

        <button
          v-else-if="
            existingPatient?.email_matches
          "
          type="button"
          class="btn btn-success"
          :disabled="store.preparingPatient"
          @click="attachExisting"
        >
          <span
            v-if="store.preparingPatient"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:user-round-check"
            class="size-4"
          />

          Прикрепить пациента
        </button>

        <button
          v-else-if="!existingPatient"
          type="submit"
          form="doctor-patient-invitation-form"
          class="btn btn-primary"
          :disabled="!canSubmit"
        >
          <span
            v-if="store.preparingPatient"
            class="loading loading-spinner loading-sm"
          />

          Проверить и продолжить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>