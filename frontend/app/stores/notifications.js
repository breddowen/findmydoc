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

    async function fetchNotifications(
      requestedPage = 1,
    ) {
      const { $api } = useNuxtApp()

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

        items.value = response.items
        unreadCount.value = response.unread_count
        page.value = response.page
        totalItems.value = response.total_items
        totalPages.value = response.total_pages

        return response
      } finally {
        loading.value = false
      }
    }

    async function fetchUnreadCount() {
      const { $api } = useNuxtApp()

      const response = await $api(
        '/api/v1/notifications/unread-count',
      )

      unreadCount.value = response.unread_count
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
      if (!notification.channels?.includes('browser')) {
        return
      }

      if (
        !('Notification' in window)
        || Notification.permission !== 'granted'
      ) {
        return
      }

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

        if (notification.action_url) {
          navigateTo(notification.action_url)
        }

        browserNotification.close()
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
        return
      }

      if (
        data.type !== 'notification'
        || !data.notification
      ) {
        return
      }

      const notification = data.notification

      if (
            [
                'article_assigned',
                'questionnaire_assigned',
            ].includes(notification.notification_type)
            ) {
            scheduleAssignmentsRefresh()
            }

      if (
        notification.channels?.includes('in_app')
      ) {
        items.value = [
          notification,
          ...items.value.filter(
            (item) => item.id !== notification.id,
          ),
        ].slice(0, 10)

        unreadCount.value += 1
        totalItems.value += 1
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

      const config = useRuntimeConfig()

      const websocketBase =
        config.public.apiBase
          .replace(/^http:/, 'ws:')
          .replace(/^https:/, 'wss:')

      socket = new WebSocket(
        `${websocketBase}/api/v1/notifications/ws`,
      )

      socket.addEventListener('open', () => {
        socket.send(
          JSON.stringify({
            type: 'authenticate',
            token,
          }),
        )

        pingTimer = window.setInterval(() => {
          if (socket?.readyState === WebSocket.OPEN) {
            socket.send(
              JSON.stringify({
                type: 'ping',
              }),
            )
          }
        }, 30000)
      })

      socket.addEventListener(
        'message',
        handleSocketMessage,
      )

      socket.addEventListener('close', () => {
        connected.value = false
        socket = null

        window.clearInterval(pingTimer)

        if (!manuallyDisconnected) {
          reconnectTimer = window.setTimeout(
            connect,
            3000,
          )
        }
      })
    }

    function disconnect() {
      manuallyDisconnected = true

      window.clearTimeout(reconnectTimer)
      window.clearInterval(pingTimer)
      window.clearTimeout(assignmentRefreshTimer)

      socket?.close()
      socket = null

      connected.value = false
    }

    async function requestBrowserPermission() {
      if (!('Notification' in window)) {
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