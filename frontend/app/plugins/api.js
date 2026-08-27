// ./frontend/app/plugins/api.js
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()

  const api = $fetch.create({
    baseURL: config.public.apiBase,

    onRequest({ options }) {
      if (!import.meta.client) return

      const accessToken = localStorage.getItem(
        'mentalme_access_token',
      )

      if (!accessToken) return

      const headers = new Headers(options.headers || {})
      headers.set(
        'Authorization',
        `Bearer ${accessToken}`,
      )

      options.headers = headers
    },

    async onResponseError({ response }) {
      if (!import.meta.client) return

      if (response.status !== 401) return

      const hadAccessToken = Boolean(
        localStorage.getItem('mentalme_access_token'),
      )

      if (!hadAccessToken) return

      localStorage.removeItem('mentalme_access_token')
      localStorage.removeItem('mentalme_active_role')

      const publicPaths = [
        '/login',
        '/forgot-password',
        '/reset-password',
        '/verify-email',
        '/register',
      ]

      const isPublicPath = publicPaths.some((path) =>
        window.location.pathname.startsWith(path),
      )

      if (!isPublicPath) {
        window.location.href = '/login?sessionExpired=1'
      }
    },
  })

  return {
    provide: {
      api,
    },
  }
})