// ./frontend/app/stores/videos.js

export const useVideosStore = defineStore('videos', () => {
  const auth = useAuthStore()

  const videos = ref([])
  const loading = ref(false)
  const saving = ref(false)
  const notice = ref(null)

  let listVersion = 0
  let listController = null

  async function fetchVideos() {
    const { $api } = useNuxtApp()

    const version = ++listVersion

    listController?.abort()
    listController = new AbortController()

    loading.value = true

    const path = auth.activeRole === 'patient'
      ? '/api/v1/videos'
      : '/api/v1/videos/manage'

    try {
      const result = []
      const limit = 100
      let offset = 0

      // Загружаются только небольшие JSON-метаданные.
      // Видео и обложки здесь не скачиваются.
      while (true) {
        const page = await $api(path, {
          query: { offset, limit },
          signal: listController.signal,
          retry: 0,
        })

        if (version !== listVersion) return

        result.push(...page)

        if (page.length < limit) break

        offset += page.length
      }

      videos.value = result
      return result
    } finally {
      if (version === listVersion) {
        loading.value = false
      }
    }
  }

  async function fetchVideo(
    id,
    {
      manage = false,
      programId = null,
      programStageId = null,
      signal,
    } = {},
  ) {
    const { $api } = useNuxtApp()

    return await $api(
      manage
        ? `/api/v1/videos/manage/${id}`
        : `/api/v1/videos/${id}`,
      {
        query: manage
          ? undefined
          : {
              program_id: programId || undefined,
              program_stage_id: programStageId || undefined,
            },
        signal,
        retry: 0,
      },
    )
  }

  async function mutate(path, method, body) {
    if (saving.value) {
      throw new Error('Дождитесь завершения сохранения')
    }

    const { $api } = useNuxtApp()

    saving.value = true

    try {
      const result = await $api(path, {
        method,
        body,
        retry: 0,
        timeout: 60000,
      })

      notice.value = result.poster_warning
        ? {
            videoId: result.id,
            message: result.poster_warning,
          }
        : null

      return result
    } finally {
      saving.value = false
    }
  }

  function createVideo(payload) {
    return mutate(
      '/api/v1/videos/manage',
      'POST',
      payload,
    )
  }

  function updateVideo(id, payload) {
    return mutate(
      `/api/v1/videos/manage/${id}`,
      'PUT',
      payload,
    )
  }

  function setVisibility(video, isHidden) {
    return mutate(
      `/api/v1/videos/manage/${video.id}/visibility`,
      'PATCH',
      {
        is_hidden: isHidden,
        expected_version: video.version,
      },
    )
  }

  async function fetchUsage(videoId, { signal } = {}) {
    const { $api } = useNuxtApp()

    return await $api(
      `/api/v1/videos/manage/${videoId}/usage`,
      {
        signal,
        cache: 'no-store',
        retry: 0,
      },
    )
  }

  async function deleteVideo(videoId, payload) {
    const response = await mutate(
      `/api/v1/videos/manage/${videoId}`,
      'DELETE',
      payload,
    )

    videos.value = videos.value.filter(
      video => video.id !== videoId,
    )

    if (notice.value?.videoId === videoId) {
      notice.value = null
    }

    return response
  }

  watch(
    [() => auth.accessToken, () => auth.activeRole],
    () => {
      listVersion += 1
      listController?.abort()

      videos.value = []
      loading.value = false
      notice.value = null
    },
  )

  return {
    videos,
    loading,
    saving,
    notice,

    fetchVideos,
    fetchVideo,
    createVideo,
    updateVideo,
    setVisibility,

    fetchUsage,
    deleteVideo,
  }
})