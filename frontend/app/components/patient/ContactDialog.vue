<!-- ./frontend/app/components/patient/ContactDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const { $api } = useNuxtApp()

const consentDocument = ref(null)
const loading = ref(false)
const saving = ref(false)

const errorMessage = ref('')
const result = ref(null)

let loadVersion = 0

async function loadDocument() {
  const version = ++loadVersion

  loading.value = true
  consentDocument.value = null
  errorMessage.value = ''

  try {
    const documents = await $api(
      '/api/v1/consents/available',
    )

    if (version !== loadVersion) return

    consentDocument.value = documents.find(
      item => item.consent_type === 'assistant_contact',
    ) || null

    if (!consentDocument.value) {
      errorMessage.value =
        'Условия разрешения на контакт сейчас недоступны.'
    }
  } catch (error) {
    if (version !== loadVersion) return

    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось загрузить условия контакта.'
  } finally {
    if (version === loadVersion) {
      loading.value = false
    }
  }
}

watch(
  () => model.value,
  open => {
    if (open) {
      result.value = null
      void loadDocument()
    } else {
      loadVersion += 1
    }
  },
  { immediate: true },
)

async function requestContact() {
  if (
    saving.value
    || loading.value
    || !consentDocument.value
  ) {
    return
  }

  saving.value = true
  errorMessage.value = ''

  try {
    result.value = await $api(
      '/api/v1/consents/contact-request',
      {
        method: 'POST',
        body: {
          accepted: true,
          document_version: consentDocument.value.version,
        },
      },
    )
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось отправить запрос. Попробуйте ещё раз.'
  } finally {
    saving.value = false
  }
}

onBeforeUnmount(() => {
  loadVersion += 1
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Связаться с ассистентом"
    max-width-class="max-w-md"
    :close-on-backdrop="!saving"
    :show-close-button="!saving"
  >
    <div class="space-y-4">
      <template v-if="result">
        <div class="alert alert-success" role="status">
          <Icon name="lucide:circle-check" class="size-5" />
          <span>{{ result.message }}</span>
        </div>
      </template>

      <template v-else>
        <p class="font-medium">
          Ассистент поможет с выбором программы
          и записью к специалистам.
        </p>

        <p class="text-base-content/65 text-sm">
          Оставьте запрос — с Вами свяжутся в рабочее время
          клиники. Дополнительно вводить номер телефона
          здесь не нужно.
        </p>

        <div
          v-if="loading"
          class="flex items-center gap-2 py-3 text-sm"
          role="status"
        >
          <span class="loading loading-spinner loading-sm" />
          Загружаем условия контакта…
        </div>

        <div
          v-else-if="consentDocument"
          class="bg-base-200 rounded-2xl p-4"
        >
          <h3 class="text-sm font-semibold">
            {{ consentDocument.title }}
          </h3>

          <p class="text-base-content/70 mt-2 whitespace-pre-line text-sm">
            {{ consentDocument.description }}
          </p>

          <p class="text-base-content/60 mt-3 text-xs">
            Нажимая «Заказать звонок», Вы разрешаете
            ассистенту клиники связаться с Вами.
          </p>
        </div>

        <p class="text-base-content/50 text-xs">
          Это не канал срочной медицинской помощи.
          При экстренной ситуации обращайтесь
          в экстренные службы.
        </p>
      </template>

      <div
        v-if="errorMessage"
        class="alert alert-error"
        role="alert"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn"
          :disabled="saving"
          @click="model = false"
        >
          {{ result ? 'Готово' : 'Закрыть' }}
        </button>

        <button
          v-if="!result"
          type="button"
          class="btn btn-primary"
          :disabled="saving || loading || !consentDocument"
          @click="requestContact"
        >
          <span
            v-if="saving"
            class="loading loading-spinner loading-sm"
          />
          <Icon
            v-else
            name="lucide:phone"
            class="size-4"
          />
          Заказать звонок
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>