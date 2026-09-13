// ./frontend/app/composables/usePrivateImage.js

import { mediaErrorText } from '~/utils/media'

export function usePrivateImage(
  request,
  enabled,
) {
  const { $api } = useNuxtApp()
  const auth = useAuthStore()

  const src = ref(null)
  const loading = ref(false)
  const errorMessage = ref('')

  watchEffect((onCleanup) => {
    const currentRequest = toValue(request)
    const canLoad = toValue(enabled)

    // Отслеживаем изменение сессии и роли.
    const token = auth.accessToken
    const role = auth.activeRole

    let active = true
    let objectUrl = null

    const controller = new AbortController()

    onCleanup(() => {
      active = false
      controller.abort()

      if (objectUrl) {
        URL.revokeObjectURL(objectUrl)
      }
    })

    src.value = null
    loading.value = false
    errorMessage.value = ''

    if (
      !import.meta.client
      || !canLoad
      || !currentRequest
      || !token
      || !role
    ) {
      return
    }

    loading.value = true

    void $api(currentRequest.path, {
      query: currentRequest.query,
      responseType: 'blob',
      signal: controller.signal,
      cache: 'no-store',
      retry: 0,
    })
      .then((blob) => {
        if (!active) return

        if (
          !(blob instanceof Blob)
          || blob.type.split(';')[0] !== 'image/webp'
        ) {
          throw new Error(
            'Сервер вернул неподдерживаемое изображение',
          )
        }

        objectUrl = URL.createObjectURL(blob)
        src.value = objectUrl
      })
      .catch((error) => {
        if (!active || controller.signal.aborted) return

        errorMessage.value = mediaErrorText(
          error,
          'Изображение недоступно',
        )
      })
      .finally(() => {
        if (active) {
          loading.value = false
        }
      })
  })

  return {
    src,
    loading,
    errorMessage,
  }
}