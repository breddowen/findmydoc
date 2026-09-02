// ./frontend/app/stores/user.js
export const useUserStore = defineStore(
  'user',
  () => {
    const user = ref(null)
    const loading = ref(false)
    const saving = ref(false)

    const fullName = computed(() => {
      if (!user.value) return ''

      return (
        [
          user.value.last_name,
          user.value.first_name,
          user.value.middle_name,
        ]
          .filter(Boolean)
          .join(' ')
        || user.value.email
        || ''
      )
    })

    const initials = computed(() => {
      if (!user.value) return '?'

      const first = (
        user.value.first_name
        || user.value.email
        || '?'
      ).charAt(0)

      const last = (
        user.value.last_name || ''
      ).charAt(0)

      return `${first}${last}`.toUpperCase()
    })

    const isEmailVerified = computed(() =>
      Boolean(user.value?.is_email_verified),
    )

    async function fetchMe() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        user.value = await $api(
          '/api/v1/users/me',
        )

        return user.value
      } finally {
        loading.value = false
      }
    }

    async function updateProfile(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        user.value = await $api(
          '/api/v1/users/me',
          {
            method: 'PATCH',
            body: payload,
          },
        )

        return user.value
      } finally {
        saving.value = false
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
      saving,

      fullName,
      initials,
      isEmailVerified,

      fetchMe,
      updateProfile,
      resendVerificationEmail,
      clear,
    }
  },
)