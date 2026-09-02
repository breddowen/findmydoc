<!-- ./frontend/app/app.vue -->
<script setup>
const ui = useUiStore()
const auth = useAuthStore()
const userStore = useUserStore()
const notificationsStore = useNotificationsStore()

onMounted(async () => {
  ui.initTheme()
  ui.initSidebar()
  auth.initFromStorage()

  if (auth.isAuthenticated && !userStore.user) {
    try {
      await userStore.fetchMe()
      if (auth.isAuthenticated) {
          notificationsStore.connect()
        }
    } catch {
      auth.logout()
    }
  }
})
</script>

<template>
  <NuxtLoadingIndicator color="#570df8" />

  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>