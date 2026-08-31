<!-- ./frontend/app/components/invitations/LinkDialog.vue -->
<script setup>
import QRCode from 'qrcode'

const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  url: {
    type: String,
    default: '',
  },
  email: {
    type: String,
    default: '',
  },
  title: {
    type: String,
    default: 'Приглашение',
  },
  description: {
    type: String,
    default:
      'Отсканируйте QR-код или скопируйте ссылку.',
  },
  canSendEmail: {
    type: Boolean,
    default: false,
  },
  sendingEmail: {
    type: Boolean,
    default: false,
  },
  emailSent: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'send-email',
])

const qrCodeDataUrl = ref('')
const generatingQr = ref(false)
const copied = ref(false)

async function generateQrCode() {
  if (!props.url) {
    qrCodeDataUrl.value = ''
    return
  }

  generatingQr.value = true

  try {
    qrCodeDataUrl.value = await QRCode.toDataURL(
      props.url,
      {
        width: 320,
        margin: 2,
        errorCorrectionLevel: 'M',
        color: {
          dark: '#111827',
          light: '#ffffff',
        },
      },
    )
  } finally {
    generatingQr.value = false
  }
}

async function copyLink() {
  if (!props.url) return

  try {
    await navigator.clipboard.writeText(props.url)
    copied.value = true

    window.setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch {
    copied.value = false
  }
}

watch(
  () => [model.value, props.url],
  ([opened]) => {
    if (opened) {
      generateQrCode()
    }
  },
  {
    immediate: true,
  },
)
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    :title="title"
    max-width-class="max-w-md"
  >
    <div class="flex flex-col items-center gap-5">
      <p class="text-base-content/70 text-center text-sm">
        {{ description }}
      </p>

      <div
        v-if="email"
        class="badge badge-outline max-w-full gap-2"
      >
        <Icon
          name="lucide:mail"
          class="size-3.5 shrink-0"
        />
        <span class="truncate">{{ email }}</span>
      </div>

      <div
        v-if="emailSent"
        class="alert alert-success w-full"
      >
        <Icon
          name="lucide:circle-check"
          class="size-5"
        />
        <span>Ссылка отправлена на email</span>
      </div>

      <div
        class="bg-white flex size-72 max-w-full items-center justify-center rounded-2xl p-3 shadow-sm"
      >
        <span
          v-if="generatingQr"
          class="loading loading-spinner loading-lg text-primary"
        />

        <img
          v-else-if="qrCodeDataUrl"
          :src="qrCodeDataUrl"
          alt="QR-код приглашения"
          class="h-full w-full object-contain"
        >

        <div
          v-else
          class="text-error flex flex-col items-center gap-2 text-center"
        >
          <Icon
            name="lucide:triangle-alert"
            class="size-8"
          />
          <span class="text-sm">
            Ссылка не сформирована
          </span>
        </div>
      </div>

      <div class="join w-full">
        <input
          :value="url"
          type="text"
          readonly
          class="input input-bordered join-item min-w-0 flex-1"
          aria-label="Ссылка приглашения"
          @focus="$event.target.select()"
        >

        <button
          type="button"
          class="btn btn-primary join-item"
          :disabled="!url"
          @click="copyLink"
        >
          <Icon
            :name="copied ? 'lucide:check' : 'lucide:copy'"
            class="size-4"
          />

          <span class="hidden sm:inline">
            {{ copied ? 'Скопировано' : 'Копировать' }}
          </span>
        </button>
      </div>

      <p
        v-if="canSendEmail"
        class="text-base-content/50 text-center text-xs"
      >
        При отправке будет сформирована новая ссылка.
        Текущая ссылка перестанет действовать.
      </p>
    </div>

    <template #footer>
      <div class="flex flex-col gap-2 sm:flex-row">
        <button
          v-if="canSendEmail"
          type="button"
          class="btn btn-outline flex-1"
          :disabled="sendingEmail"
          @click="emit('send-email')"
        >
          <span
            v-if="sendingEmail"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:send"
            class="size-4"
          />

          {{
            emailSent
              ? 'Отправить повторно'
              : 'Отправить на email'
          }}
        </button>

        <button
          type="button"
          class="btn btn-primary flex-1"
          @click="model = false"
        >
          Готово
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>