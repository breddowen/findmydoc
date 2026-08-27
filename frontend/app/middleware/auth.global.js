// ./frontend/app/middleware/auth.global.js
export default defineNuxtRouteMiddleware((to) => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  const publicPaths = [
    '/login',
    '/forgot-password',
    '/reset-password',
    '/verify-email',
    '/register',
  ]

  const isPublicPath = publicPaths.some((path) =>
    to.path.startsWith(path),
  )

  if (isPublicPath) {
    if (
      auth.isAuthenticated
      && to.path === '/login'
    ) {
      return navigateTo('/dashboard')
    }

    return
  }

  if (!auth.isAuthenticated) {
    return navigateTo(
      `/login?redirect=${encodeURIComponent(to.fullPath)}`,
    )
  }
})