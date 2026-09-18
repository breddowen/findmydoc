// ./frontend/app/middleware/test-styles.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (
    !auth.isAuthenticated
    || auth.activeRole !== 'superuser'
  ) {
    return navigateTo('/dashboard')
  }
})