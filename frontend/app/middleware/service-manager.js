// ./frontend/app/middleware/service-manager.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (
    ![
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
  ) {
    return navigateTo('/dashboard')
  }
})