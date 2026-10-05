// ./frontend/app/stores/video-playback.js

export const useVideoPlaybackStore = defineStore(
  'video-playback',
  () => {
    const auth = useAuthStore()

    const expiresAt = ref(0)

    let generation = 0
    let pending = null
    let controller = null

    function invalidate() {
      generation += 1
      controller?.abort()
      controller = null
      pending = null
      expiresAt.value = 0
    }

    async function ensureSession(force = false) {
      if (!import.meta.client || !auth.accessToken) {
        throw new Error('Требуется авторизация')
      }

      if (pending) return await pending

      if (
        !force
        && expiresAt.value > Date.now() + 60000
      ) {
        return
      }

      const { $api } = useNuxtApp()
      const currentGeneration = generation

      controller = new AbortController()

      const operation = $api('/api/v1/videos/media-session', {
        method: 'POST',
        credentials: 'include',
        signal: controller.signal,
        retry: 0,
        timeout: 15000,
      }).then(response => {
        if (currentGeneration !== generation) {
          const error = new Error('Авторизация изменилась')
          error.name = 'AbortError'
          throw error
        }

        expiresAt.value = Date.parse(response.expires_at)
      })

      pending = operation

      try {
        await operation
      } finally {
        if (pending === operation) {
          pending = null
          controller = null
        }
      }
    }

    watch(
      [() => auth.accessToken, () => auth.activeRole],
      invalidate,
    )

    return {
      expiresAt,
      ensureSession,
      invalidate,
    }
  },
)