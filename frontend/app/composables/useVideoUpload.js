// ./frontend/app/composables/useVideoUpload.js

import { videoApiUrl } from '~/utils/videos'

export function useVideoUpload() {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  const uploading = ref(false)
  const progress = ref(0)
  const checking = ref(false)

  let currentRequest = null

  function cancel() {
    currentRequest?.abort()
  }

  async function upload(file) {
    if (uploading.value) {
      throw new Error('Дождитесь окончания текущей загрузки')
    }

    if (!auth.accessToken) {
      throw new Error('Требуется авторизация')
    }

    uploading.value = true
    progress.value = 0
    checking.value = false

    const xhr = new XMLHttpRequest()
    currentRequest = xhr

    try {
      return await new Promise((resolve, reject) => {
        xhr.open(
          'POST',
          videoApiUrl(
            config.public.apiBase,
            '/api/v1/media/video-uploads',
          ),
        )

        xhr.timeout = 16 * 60 * 1000

        xhr.setRequestHeader(
          'Authorization',
          `Bearer ${auth.accessToken}`,
        )
        xhr.setRequestHeader('Content-Type', 'video/mp4')

        xhr.upload.onprogress = event => {
          if (!event.lengthComputable) return

          progress.value = Math.round(
            event.loaded / event.total * 100,
          )

          checking.value = event.loaded >= event.total
        }

        xhr.onload = () => {
          let data = null

          try {
            data = JSON.parse(xhr.responseText)
          } catch {
            // Например, HTML-ошибка reverse proxy.
          }

          if (xhr.status >= 200 && xhr.status < 300 && data) {
            resolve(data)
            return
          }

          const error = new Error(
            typeof data?.detail === 'string'
              ? data.detail
              : `Не удалось загрузить видео: HTTP ${xhr.status}`,
          )

          error.data = data
          error.status = xhr.status

          reject(error)
        }

        xhr.onerror = () => {
          reject(new Error(
            'Ошибка соединения при загрузке видео',
          ))
        }

        xhr.ontimeout = () => {
          reject(new Error(
            'Превышено время загрузки видео',
          ))
        }

        xhr.onabort = () => {
          const error = new Error('Загрузка отменена')
          error.name = 'AbortError'
          reject(error)
        }

        xhr.send(file)
      })
    } finally {
      if (currentRequest === xhr) {
        currentRequest = null
        uploading.value = false
        checking.value = false
      }
    }
  }

  watch(
    [() => auth.accessToken, () => auth.activeRole],
    cancel,
  )

  onScopeDispose(cancel)

  return {
    uploading,
    progress,
    checking,
    upload,
    cancel,
  }
}