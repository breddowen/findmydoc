<!-- ./frontend/app/components/notifications/Center.vue -->
<script setup>
const store = useNotificationsStore()

const opened = ref(false)
const page = ref(1)

const browserPermission = ref(
  import.meta.client && 'Notification' in window
    ? Notification.permission
    : 'unsupported',
)

function formatDate(value) {
  return new Intl.DateTimeFormat(
    'ru-RU',
    {
      dateStyle: 'short',
      timeStyle: 'short',
    },
  ).format(new Date(value))
}

async function openCenter() {
  opened.value = true
  page.value = 1

  await store.fetchNotifications(1)
}

async function openNotification(notification) {
  await store.markAsRead(notification)
  opened.value = false

  if (notification.action_url) {
    await navigateTo(notification.action_url)
  }
}

async function requestPermission() {
  browserPermission.value =
    await store.requestBrowserPermission()
}

watch(page, () => {
  store.fetchNotifications(page.value)
})

onMounted(async () => {
  await store.fetchUnreadCount()
  store.connect()
})
</script>

<template>
  <button
    type="button"
    class="btn btn-circle btn-ghost"
    aria-label="Уведомления"
    @click="openCenter"
  >
    <div class="indicator">
      <span
        v-if="store.unreadCount"
        class="indicator-item badge badge-secondary badge-sm min-w-5"
      >
        {{
          store.unreadCount > 99
            ? '99+'
            : store.unreadCount
        }}
      </span>

      <Icon
        name="lucide:bell"
        class="size-5"
      />
    </div>
  </button>

  <UiResponsiveDialog
    v-model="opened"
    title="Уведомления"
    max-width-class="max-w-lg"
  >
    <div class="space-y-4">
      <div
        v-if="browserPermission === 'default'"
        class="border-info/30 bg-info/10 rounded-2xl border p-4"
      >
        <p class="text-sm">
          Разрешите системные уведомления браузера,
          чтобы не пропускать новые сообщения.
        </p>

        <button
          type="button"
          class="btn btn-info btn-sm mt-3"
          @click="requestPermission"
        >
          <Icon
            name="lucide:bell-ring"
            class="size-4"
          />
          Разрешить
        </button>
      </div>

      <div class="flex justify-end">
        <button
          v-if="store.unreadCount"
          type="button"
          class="btn btn-ghost btn-sm"
          @click="store.markAllAsRead"
        >
          Прочитать все
        </button>
      </div>

      <UiContentSkeleton
        v-if="store.loading"
        variant="list"
        :count="4"
      />

      <div
        v-else-if="store.items.length"
        class="space-y-2"
      >
        <button
          v-for="notification in store.items"
          :key="notification.id"
          type="button"
          class="border-base-300 hover:border-primary relative w-full rounded-2xl border p-4 text-left transition"
          :class="{
            'bg-primary/5 border-primary/30':
              !notification.is_read,
          }"
          @click="openNotification(notification)"
        >
          <span
            v-if="!notification.is_read"
            class="bg-secondary absolute right-3 top-3 size-2 rounded-full"
          />

          <p class="pr-5 font-semibold">
            {{ notification.title }}
          </p>

          <p class="text-base-content/60 mt-1 text-sm">
            {{ notification.message }}
          </p>

          <p class="text-base-content/40 mt-2 text-xs">
            {{ formatDate(notification.created_at) }}
          </p>
        </button>
      </div>

      <div
        v-else
        class="py-10 text-center"
      >
        <Icon
          name="lucide:bell-off"
          class="text-base-content/30 mx-auto size-12"
        />

        <p class="mt-4">
          Уведомлений пока нет
        </p>
      </div>

      <UiPagination
        v-model="page"
        :total-items="store.totalItems"
        :page-size="10"
      />
    </div>
  </UiResponsiveDialog>
</template>