// ./frontend/app/stores/auth.js
export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref(null)
  const activeRole = ref(null)

  const roleSelectionToken = ref(null)
  const availableRoles = ref([])

  const loading = ref(false)
  const initialized = ref(false)

  const isAuthenticated = computed(
    () => Boolean(accessToken.value),
  )

  const needsRoleSelection = computed(
    () =>
      Boolean(roleSelectionToken.value)
      && availableRoles.value.length > 0,
  )

  function persistAuth() {
    if (!import.meta.client) return

    if (accessToken.value) {
      localStorage.setItem(
        'mentalme_access_token',
        accessToken.value,
      )
    } else {
      localStorage.removeItem('mentalme_access_token')
    }

    if (activeRole.value) {
      localStorage.setItem(
        'mentalme_active_role',
        activeRole.value,
      )
    } else {
      localStorage.removeItem('mentalme_active_role')
    }
  }

  function initFromStorage() {
    if (!import.meta.client || initialized.value) return

    accessToken.value = localStorage.getItem(
      'mentalme_access_token',
    )

    activeRole.value = localStorage.getItem(
      'mentalme_active_role',
    )

    initialized.value = true
  }

  function clearRoleSelection() {
    roleSelectionToken.value = null
    availableRoles.value = []
  }

  function processLoginResponse(response) {
    if (response.status === 'authenticated') {
      accessToken.value = response.access_token
      activeRole.value = response.active_role

      clearRoleSelection()
      persistAuth()

      return {
        authenticated: true,
        needsRoleSelection: false,
      }
    }

    roleSelectionToken.value =
      response.role_selection_token

    availableRoles.value = response.roles || []

    return {
      authenticated: false,
      needsRoleSelection: true,
    }
  }

  async function login(email, password) {
    const { $api } = useNuxtApp()

    loading.value = true

    try {
      const response = await $api('/api/v1/auth/login', {
        method: 'POST',
        body: {
          email,
          password,
        },
      })

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  async function selectRole(role) {
    const { $api } = useNuxtApp()

    if (!roleSelectionToken.value) {
      throw new Error('Отсутствует токен выбора роли')
    }

    loading.value = true

    try {
      const response = await $api(
        '/api/v1/auth/select-role',
        {
          method: 'POST',
          body: {
            role_selection_token:
              roleSelectionToken.value,
            role,
          },
        },
      )

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  async function loginWithPasskey() {
    const { $api } = useNuxtApp()
    const { authenticateWithPasskey } = useWebAuthn()

    loading.value = true

    try {
      const optionsResponse = await $api(
        '/api/v1/auth/passkeys/authentication/options',
        {
          method: 'POST',
        },
      )

      const credential = await authenticateWithPasskey(
        optionsResponse.options,
      )

      const response = await $api(
        '/api/v1/auth/passkeys/authentication/verify',
        {
          method: 'POST',
          body: {
            challenge_id: optionsResponse.challenge_id,
            credential,
          },
        },
      )

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  function logout() {
    accessToken.value = null
    activeRole.value = null

    clearRoleSelection()
    persistAuth()

    const notificationsStore = useNotificationsStore()
    notificationsStore.disconnect()

    const userStore = useUserStore()
    userStore.clear()

    return navigateTo('/login')
  }

  return {
    accessToken,
    activeRole,
    roleSelectionToken,
    availableRoles,
    loading,
    initialized,

    isAuthenticated,
    needsRoleSelection,

    initFromStorage,
    login,
    loginWithPasskey,
    selectRole,
    logout,
    clearRoleSelection,
  }
})