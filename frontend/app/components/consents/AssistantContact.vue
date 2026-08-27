<!-- ./frontend/app/components/consents/AssistantContact.vue -->
<script setup>
const { $api } = useNuxtApp()

const dialogOpen = ref(false)

const loading = ref(false)
const saving = ref(false)

const accepted = ref(false)
const doNotCall = ref(false)
const confirmed = ref(false)

const document = ref(null)

const message = ref('')
const errorMessage = ref('')

const contactAllowed = computed(
  () => accepted.value && !doNotCall.value,
)

async function loadData() {
  loading.value = true
  errorMessage.value = ''

  try {
    const [documents, current] = await Promise.all([
      $api('/api/v1/consents/available'),
      $api('/api/v1/consents/me'),
    ])

    document.value = documents.find(
      (item) =>
        item.consent_type === 'assistant_contact',
    ) || null

    const currentConsent = current.consents.find(
      (item) =>
        item.consent_type === 'assistant_contact',
    )

    accepted.value = Boolean(
      currentConsent?.accepted,
    )

    doNotCall.value = Boolean(
      current.contact_preference?.do_not_call,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить настройки контакта'
  } finally {
    loading.value = false
  }
}

function openDialog() {
  confirmed.value = false
  message.value = ''
  errorMessage.value = ''
  dialogOpen.value = true
}

async function allowContact() {
  if (!confirmed.value) return

  saving.value = true
  errorMessage.value = ''

  try {
    await $api('/api/v1/consents/me', {
      method: 'POST',
      body: {
        consent_type: 'assistant_contact',
        accepted: true,
      },
    })

    accepted.value = true
    doNotCall.value = false

    message.value =
      'Запрос принят. Ассистент сможет связаться с вами.'

    dialogOpen.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить согласие'
  } finally {
    saving.value = false
  }
}

async function revokeContact() {
  saving.value = true
  errorMessage.value = ''

  try {
    await $api('/api/v1/consents/me', {
      method: 'POST',
      body: {
        consent_type: 'assistant_contact',
        accepted: false,
      },
    })

    accepted.value = false
    message.value =
      'Разрешение на контакт отозвано.'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить настройку'
  } finally {
    saving.value = false
  }
}

onMounted(loadData)
</script>

<template>
  <section
    class="card bg-base-100 border-base-300 border"
  >
    <div class="card-body p-5 sm:p-6">
      <div
        class="flex flex-col gap-4 sm:flex-row sm:items-start"
      >
        <div
          class="bg-primary/10 text-primary flex size-12 shrink-0 items-center justify-center rounded-2xl"
        >
          <Icon
            name="lucide:phone-call"
            class="size-6"
          />
        </div>

        <div class="min-w-0 flex-1">
          <h2 class="card-title">
            Помощь с записью
          </h2>

          <p class="text-base-content/60 mt-2 text-sm">
            Медицинский ассистент может связаться с вами
            и помочь с записью на консультацию.
          </p>

          <div
            v-if="message"
            class="alert alert-success mt-4 py-3"
          >
            <Icon
              name="lucide:circle-check"
              class="size-5"
            />
            <span>{{ message }}</span>
          </div>

          <div
            v-if="errorMessage"
            class="alert alert-error mt-4 py-3"
          >
            <Icon
              name="lucide:circle-alert"
              class="size-5"
            />
            <span>{{ errorMessage }}</span>
          </div>

          <div class="mt-5">
            <span
              v-if="loading"
              class="loading loading-spinner text-primary"
            />

            <div
              v-else-if="contactAllowed"
              class="flex flex-col gap-3 sm:flex-row sm:items-center"
            >
              <span class="badge badge-success gap-2 py-3">
                <Icon
                  name="lucide:check"
                  class="size-4"
                />
                Контакт разрешён
              </span>

              <button
                type="button"
                class="btn btn-ghost btn-sm"
                :disabled="saving"
                @click="revokeContact"
              >
                Отозвать разрешение
              </button>
            </div>

            <button
              v-else
              type="button"
              class="btn btn-primary w-full sm:w-auto"
              :disabled="loading"
              @click="openDialog"
            >
              <Icon
                name="lucide:phone"
                class="size-4"
              />
              Прошу связаться со мной
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <UiResponsiveDialog
    v-model="dialogOpen"
    title="Разрешить контакт"
    max-width-class="max-w-md"
  >
    <div class="space-y-5">
      <div
        class="bg-base-200 rounded-2xl p-4"
      >
        <h3 class="font-semibold">
          {{
            document?.title
            || 'Связаться со мной'
          }}
        </h3>

        <p class="text-base-content/70 mt-2 text-sm">
          {{
            document?.description
            || 'Я разрешаю медицинскому ассистенту связаться со мной.'
          }}
        </p>
      </div>

      <label
        class="border-base-300 flex cursor-pointer items-start gap-3 rounded-2xl border p-4"
      >
        <input
          v-model="confirmed"
          type="checkbox"
          class="checkbox checkbox-primary mt-0.5"
        >

        <span class="text-sm">
          Я согласен, чтобы медицинский ассистент
          связался со мной по контактным данным,
          указанным в аккаунте.
        </span>
      </label>

      <p class="text-base-content/50 text-xs">
        Вы сможете отозвать разрешение в любое время.
      </p>
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          :disabled="saving"
          @click="dialogOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="saving || !confirmed"
          @click="allowContact"
        >
          <span
            v-if="saving"
            class="loading loading-spinner loading-sm"
          />

          Разрешить контакт
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>