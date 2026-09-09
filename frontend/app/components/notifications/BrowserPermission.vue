<!-- ./frontend/app/components/notifications/BrowserPermission.vue -->
<script setup>
const store = useNotificationsStore()

const permission = ref('checking')
const requesting = ref(false)
const failed = ref(false)

function refreshPermission() {
  if (
    !window.isSecureContext
    || !('Notification' in window)
  ) {
    permission.value = 'unsupported'
    return
  }

  permission.value = Notification.permission
}

const label = computed(() => {
  if (requesting.value) return 'Запрашиваем разрешение…'
  if (failed.value) return 'Повторить включение уведомлений'

  const labels = {
    checking: 'Проверяем уведомления…',
    unsupported: 'Браузерные уведомления недоступны',
    granted: 'Браузерные уведомления включены',
    denied: 'Уведомления запрещены в браузере',
    default: 'Включить браузерные уведомления',
  }

  return labels[permission.value] || labels.default
})

const disabled = computed(() =>
  requesting.value
  || [
    'checking',
    'unsupported',
    'granted',
    'denied',
  ].includes(permission.value),
)

async function enable() {
  if (disabled.value) return

  requesting.value = true
  failed.value = false

  try {
    permission.value =
      await store.requestBrowserPermission()
  } catch {
    failed.value = true
  } finally {
    requesting.value = false
  }
}

onMounted(() => {
  refreshPermission()
  window.addEventListener('focus', refreshPermission)
})

onBeforeUnmount(() => {
  window.removeEventListener('focus', refreshPermission)
})
</script>

<template>
  <button
    type="button"
    :disabled="disabled"
    :title="
      permission === 'denied'
        ? 'Разрешите уведомления в настройках сайта в браузере'
        : label
    "
    @click="enable"
  >
    <Icon
      :name="
        permission === 'granted'
          ? 'lucide:bell-ring'
          : 'lucide:bell'
      "
      class="size-4 shrink-0"
    />

    <span class="text-left text-sm">
      {{ label }}
    </span>
  </button>
</template>