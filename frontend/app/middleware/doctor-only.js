// ./frontend/app/middleware/doctor-only.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (auth.activeRole !== 'doctor') {
    return navigateTo('/dashboard')
  }
})