<!-- ./frontend/app/app.vue -->
<script setup>
const route = useRoute()
const ui = useUiStore()
const auth = useAuthStore()
const userStore = useUserStore()
const notificationsStore = useNotificationsStore()

const context = useProgramContext()

const initialized = ref(false)

const layoutName = computed(() => {
  if (context.usesProgramLayout.value) {
    return 'program'
  }

  return route.meta.layout ?? 'default'
})

const isPatient = computed(() =>
  initialized.value
  && auth.isAuthenticated
  && auth.activeRole === 'patient',
)

const authPaths = new Set([
  '/login',
  '/forgot-password',
  '/reset-password',
  '/verify-email',
])

const showSupportFab = computed(() =>
  isPatient.value
  && !context.usesProgramLayout.value
  && !context.isArticlePage.value
  && !context.isQuestionnairePage.value
  && layoutName.value !== 'auth'
  && !authPaths.has(route.path.replace(/\/$/, ''))
  && !route.path.startsWith('/register'),
)

onMounted(async () => {
  ui.initTheme()
  ui.initSidebar()
  auth.initFromStorage()

  initialized.value = true

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
  <NuxtLoadingIndicator color="var(--color-primary)" />

  <!--
    Компонент NuxtLayout существует всегда.
    Пока авторизация не инициализирована,
    name=false отключает только оболочку layout.
  -->
  <NuxtLayout
    :name="initialized ? layoutName : false"
  >
    <!--
      NuxtPage тоже существует всегда.
      Откладываем только монтирование самой страницы,
      чтобы она не отправляла запросы до загрузки роли.
    -->
    <NuxtPage v-slot="{ Component }">
      <component
        :is="Component"
        v-if="initialized && Component"
      />
    </NuxtPage>
  </NuxtLayout>

  <div
    v-if="!initialized"
    class="bg-base-200 flex min-h-dvh items-center justify-center"
    role="status"
    aria-label="Загрузка приложения"
  >
    <span
      class="loading loading-spinner text-primary loading-md"
    />
  </div>

  <PatientSupportHub v-if="isPatient" />

  <PatientSupportFab v-if="showSupportFab" />
</template>