<!-- ./frontend/app/components/test-styles/SendButton.vue -->
<script setup>
defineProps({
  compact: {
    type: Boolean,
    default: false,
  },
})

const styles = useTestStylesStore()
const { $api } = useNuxtApp()

const open = ref(false)
const sending = ref(false)
const error = ref('')
const success = ref('')

const name = ref('')
const comment = ref('')
const css = ref('')

function openDialog() {
  if (!styles.saved) return

  name.value = styles.saved.name
  comment.value = styles.saved.comment

  // Фиксируем именно сохранённый вариант на момент открытия.
  css.value = styles.exportCss

  error.value = ''
  success.value = ''
  open.value = true
}

async function send() {
  if (sending.value || success.value) return

  sending.value = true
  error.value = ''

  try {
    const response = await $api('/api/v1/test-styles/send', {
      method: 'POST',
      retry: 0,
      body: {
        name: name.value.trim(),
        comment: comment.value.trim(),
        css: css.value,
      },
    })

    success.value = response.message
  } catch (cause) {
    const detail = cause?.data?.detail

    error.value = typeof detail === 'string'
      ? detail
      : 'Не удалось отправить письмо. Попробуйте ещё раз.'
  } finally {
    sending.value = false
  }
}
</script>

<template>
  <button
    type="button"
    class="btn btn-outline btn-sm"
    :class="{ 'btn-square': compact }"
    :disabled="!styles.saved"
    title="Отправить разработчику"
    aria-label="Отправить разработчику"
    @click="openDialog"
  >
    <Icon name="lucide:send" class="size-4" />

    <span v-if="!compact">
      Отправить разработчику
    </span>
  </button>

  <UiResponsiveDialog
    v-model="open"
    title="Отправить оформление"
    :persistent="sending"
  >
    <div class="space-y-5">
      <p class="text-base-content/70 text-sm">
        На maxim-titkov@yandex.ru будет отправлен последний
        сохранённый вариант, даже если сейчас включено
        исходное оформление.
      </p>

      <label class="block">
        <span class="mb-2 block text-sm font-medium">
          Название варианта — необязательно
        </span>

        <input
          v-model="name"
          type="text"
          maxlength="120"
          class="input w-full"
          placeholder="Например: более светлый фон"
          :disabled="sending || Boolean(success)"
        >
      </label>

      <label class="block">
        <span class="mb-2 block text-sm font-medium">
          Комментарий — необязательно
        </span>

        <textarea
          v-model="comment"
          maxlength="3000"
          rows="4"
          class="textarea w-full"
          placeholder="Что важно учесть при обновлении сайта"
          :disabled="sending || Boolean(success)"
        />
      </label>

      <div v-if="error" class="alert alert-error" role="alert">
        <span>{{ error }}</span>
      </div>

      <div v-if="success" class="alert alert-success" role="status">
        <span>{{ success }}</span>
      </div>
    </div>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn btn-ghost"
          :disabled="sending"
          @click="open = false"
        >
          {{ success ? 'Закрыть' : 'Отмена' }}
        </button>

        <button
          v-if="!success"
          type="button"
          class="btn btn-primary"
          :disabled="sending"
          @click="send"
        >
          <span
            v-if="sending"
            class="loading loading-spinner loading-sm"
          />
          Отправить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>