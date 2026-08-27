// ./frontend/app/stores/user.js
export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const loading = ref(false)

  const fullName = computed(() => {
    if (!user.value) return ''

    const parts = [
      user.value.last_name,
      user.value.first_name,
      user.value.middle_name,
    ].filter(Boolean)

    return parts.join(' ') || user.value.email
  })

  const initials = computed(() => {
    if (!user.value) return '?'

    const firstName = user.value.first_name || ''
    const lastName = user.value.last_name || ''

    const value = `${firstName[0] || ''}${lastName[0] || ''}`

    return value.toUpperCase() || '?'
  })

  const isEmailVerified = computed(
    () => Boolean(user.value?.is_email_verified),
  )

  async function fetchMe() {
    const { $api } = useNuxtApp()

    loading.value = true

    try {
      user.value = await $api('/api/v1/users/me')
      return user.value
    } finally {
      loading.value = false
    }
  }

  async function resendVerificationEmail() {
    const { $api } = useNuxtApp()

    return await $api(
      '/api/v1/auth/email-verification/resend',
      {
        method: 'POST',
      },
    )
  }

  function clear() {
    user.value = null
  }

  return {
    user,
    loading,
    fullName,
    initials,
    isEmailVerified,
    fetchMe,
    resendVerificationEmail,
    clear,
  }
})