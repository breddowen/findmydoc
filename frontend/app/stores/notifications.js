// ./frontend/app/stores/notifications.js
export const useNotificationsStore = defineStore(
  'notifications',
  () => {
    const items = ref([])
    const unreadCount = ref(0)

    const page = ref(1)
    const totalItems = ref(0)
    const totalPages = ref(1)

    const loading = ref(false)
    const connected = ref(false)

    let socket = null
    let reconnectTimer = null
    let pingTimer = null
    let manuallyDisconnected = false
    let assignmentRefreshTimer = null

    let notificationRefreshTimer = null
    let notificationSessionVersion = 0

    const seenNotificationIds = new Set()

    async function fetchNotifications(requestedPage = 1) {
    const { $api } = useNuxtApp()
    const version = notificationSessionVersion

    loading.value = true

    try {
      const response = await $api(
        '/api/v1/notifications',
        {
          query: {
            page: requestedPage,
            page_size: 10,
          },
        },
      )

      if (version !== notificationSessionVersion) {
        return response
      }

      items.value = response.items
      unreadCount.value = response.unread_count
      page.value = response.page
      totalItems.value = response.total_items
      totalPages.value = response.total_pages

      return response
    } finally {
      if (version === notificationSessionVersion) {
        loading.value = false
      }
    }
  }

  async function fetchUnreadCount() {
    const { $api } = useNuxtApp()
    const version = notificationSessionVersion

    const response = await $api(
      '/api/v1/notifications/unread-count',
    )

    if (version === notificationSessionVersion) {
      unreadCount.value = response.unread_count
    }
  }

  function scheduleNotificationsRefresh() {
    window.clearTimeout(notificationRefreshTimer)

    notificationRefreshTimer = window.setTimeout(() => {
      void fetchNotifications(page.value).catch(() => {
        // Уведомление уже сохранено на backend.
        // Не ломаем интерфейс при временной ошибке сети.
      })
    }, 200)
  }
  async function markAsRead(notification) {
        if (notification.is_read) return
  
        const { $api } = useNuxtApp()
  
        const response = await $api(
          `/api/v1/notifications/${notification.id}/read`,
          {
            method: 'PATCH',
          },
        )
  
        const item = items.value.find(
          (current) => current.id === notification.id,
        )
  
        if (item) {
          item.is_read = true
          item.read_at = response.read_at
        }
  
        unreadCount.value = Math.max(
          unreadCount.value - 1,
          0,
        )
      }

    async function markAllAsRead() {
      const { $api } = useNuxtApp()

      await $api(
        '/api/v1/notifications/read-all',
        {
          method: 'PATCH',
        },
      )

      for (const item of items.value) {
        item.is_read = true
      }

      unreadCount.value = 0
    }

    function showBrowserNotification(notification) {
      if (!import.meta.client) return

      if (
        !notification.channels?.includes('browser')
        || !('Notification' in window)
        || Notification.permission !== 'granted'
      ) {
        return
      }

      try {
        const browserNotification = new Notification(
          notification.title,
          {
            body: notification.message,
            tag: notification.id,
            icon: '/favicon.ico',
          },
        )

        browserNotification.onclick = () => {
          window.focus()

          const actionUrl = notification.action_url

          if (
            typeof actionUrl === 'string'
            && actionUrl.startsWith('/')
            && !actionUrl.startsWith('//')
          ) {
            void navigateTo(actionUrl)
          }

          browserNotification.close()
        }
      } catch {
        // Некоторые мобильные браузеры не поддерживают
        // создание Notification без Service Worker.
        // Колокольчик при этом должен продолжать работать.
      }
    }

    function handleSocketMessage(event) {
      let data

      try {
        data = JSON.parse(event.data)
      } catch {
        return
      }

      if (data.type === 'authenticated') {
        connected.value = true
        scheduleNotificationsRefresh()
        return
      }

      if (
        data.type !== 'notification'
        || !data.notification?.id
      ) {
        return
      }

      const notification = data.notification

      if (seenNotificationIds.has(notification.id)) {
        return
      }

      seenNotificationIds.add(notification.id)

      if (seenNotificationIds.size > 1000) {
        const oldestId = seenNotificationIds.values().next().value
        seenNotificationIds.delete(oldestId)
      }

      if (
        [
          'article_assigned',
          'questionnaire_assigned',
        ].includes(notification.notification_type)
      ) {
        scheduleAssignmentsRefresh()
      }

      if (notification.channels?.includes('in_app')) {
        // Счётчики берём с backend, не увеличиваем вслепую:
        // уведомление могло уже попасть в HTTP-ответ.
        scheduleNotificationsRefresh()
      }

      showBrowserNotification(notification)
    }

    function connect() {
      if (!import.meta.client) return

      const token = localStorage.getItem(
        'mentalme_access_token',
      )

      if (!token || socket) return

      manuallyDisconnected = false
      window.clearTimeout(reconnectTimer)

      const config = useRuntimeConfig()

      const websocketUrl = new URL(
        config.public.apiBase,
        window.location.origin,
      )

      websocketUrl.protocol =
        websocketUrl.protocol === 'https:' ? 'wss:' : 'ws:'

      websocketUrl.pathname =
        websocketUrl.pathname.replace(/\/$/, '')
        + '/api/v1/notifications/ws'

      websocketUrl.search = ''
      websocketUrl.hash = ''

      const currentSocket = new WebSocket(
        websocketUrl.toString(),
      )

      socket = currentSocket

      currentSocket.addEventListener('open', () => {
        if (socket !== currentSocket) return

        currentSocket.send(
          JSON.stringify({
            type: 'authenticate',
            token,
          }),
        )

        window.clearInterval(pingTimer)

        pingTimer = window.setInterval(() => {
          if (
            socket === currentSocket
            && currentSocket.readyState === WebSocket.OPEN
          ) {
            currentSocket.send(
              JSON.stringify({ type: 'ping' }),
            )
          }
        }, 30000)
      })

      currentSocket.addEventListener('message', (event) => {
        if (socket === currentSocket) {
          handleSocketMessage(event)
        }
      })

      currentSocket.addEventListener('close', () => {
        if (socket !== currentSocket) return

        connected.value = false
        socket = null

        window.clearInterval(pingTimer)

        if (!manuallyDisconnected) {
          reconnectTimer = window.setTimeout(connect, 3000)
        }
      })
    }

    function disconnect() {
      if (!import.meta.client) return

      manuallyDisconnected = true
      notificationSessionVersion += 1

      window.clearTimeout(reconnectTimer)
      window.clearInterval(pingTimer)
      window.clearTimeout(assignmentRefreshTimer)
      window.clearTimeout(notificationRefreshTimer)

      const previousSocket = socket
      socket = null

      previousSocket?.close()

      connected.value = false
      loading.value = false

      items.value = []
      unreadCount.value = 0
      page.value = 1
      totalItems.value = 0
      totalPages.value = 1

      seenNotificationIds.clear()
    }

    async function requestBrowserPermission() {
      if (
        !import.meta.client
        || !window.isSecureContext
        || !('Notification' in window)
      ) {
        return 'unsupported'
      }

      return await Notification.requestPermission()
    }

    function scheduleAssignmentsRefresh() {
        const auth = useAuthStore()

        if (auth.activeRole !== 'patient') {
            return
        }

        window.clearTimeout(assignmentRefreshTimer)

        assignmentRefreshTimer = window.setTimeout(
            async () => {
            try {
                const assignmentsStore =
                useAssignmentsStore()

                await assignmentsStore.fetchMyAssignments()
            } catch {
                // Ошибка фонового обновления не должна
                // прерывать обработку уведомлений.
            }
            },
            150,
        )
        }

    return {
      items,
      unreadCount,
      page,
      totalItems,
      totalPages,
      loading,
      connected,

      fetchNotifications,
      fetchUnreadCount,
      markAsRead,
      markAllAsRead,

      connect,
      disconnect,
      requestBrowserPermission,
    }
  },
)