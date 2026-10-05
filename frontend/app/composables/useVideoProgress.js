// ./frontend/app/composables/useVideoProgress.js

import { mediaErrorText } from '~/utils/media'

export function useVideoProgress({
  video,
  programId,
  programStageId,
}) {
  const { $api } = useNuxtApp()
  const auth = useAuthStore()
  const route = useRoute()
  const journey = useProgramJourneyStore()

  const mounted = ref(false)
  const maxPercent = ref(0)
  const completed = ref(false)
  const completing = ref(false)
  const errorMessage = ref('')

  const enabled = computed(() =>
    auth.activeRole === 'patient'
    && Boolean(toValue(video)?.id),
  )

  let context = null
  let timer = null
  let disposed = false

  function isCurrent(ctx) {
    return !disposed && context === ctx
  }

  function showError(ctx, error) {
    if (!isCurrent(ctx)) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось сохранить прогресс. Просмотр можно продолжить.',
    )
  }

  function apply(ctx, response) {
    if (!isCurrent(ctx)) return

    maxPercent.value = Math.max(
      maxPercent.value,
      Number(response.max_progress_percent) || 0,
    )

    completed.value = completed.value
      || Boolean(response.completed_at)

    errorMessage.value = ''

    if (
      response.completed_at
      && ctx.programId
      && !ctx.journeySynced
    ) {
      ctx.journeySynced = true

      void journey.load(ctx.programId).catch(() => {
        if (isCurrent(ctx)) ctx.journeySynced = false
      })
    }
  }

  async function ensureOpen(ctx) {
    if (ctx.ready) return
    if (ctx.openPromise) return await ctx.openPromise

    const operation = $api(
      `/api/v1/videos/${ctx.videoId}/open`,
      {
        method: 'POST',
        retry: 0,
        body: {
          interaction_id: ctx.interactionId,
          source: ctx.source,
          program_id: ctx.programId,
          program_stage_id: ctx.stageId,
        },
      },
    ).then(response => {
      if (!isCurrent(ctx)) return

      ctx.ready = true
      apply(ctx, response.progress)
    })

    ctx.openPromise = operation

    try {
      await operation
    } finally {
      if (ctx.openPromise === operation) {
        ctx.openPromise = null
      }
    }
  }

  async function ensureStarted(ctx) {
    if (ctx.started) return
    if (ctx.startPromise) return await ctx.startPromise

    const operation = (async () => {
      await ensureOpen(ctx)

      if (!isCurrent(ctx) || !ctx.ready) return

      const response = await $api(
        `/api/v1/videos/${ctx.videoId}/progress`,
        {
          method: 'PUT',
          retry: 0,
          body: {
            interaction_id: ctx.interactionId,
            action: 'started',
          },
        },
      )

      if (!isCurrent(ctx)) return

      ctx.started = true
      apply(ctx, response)
    })()

    ctx.startPromise = operation

    try {
      await operation
    } finally {
      if (ctx.startPromise === operation) {
        ctx.startPromise = null
      }
    }
  }

  async function flushContext(ctx) {
    if (!ctx || !isCurrent(ctx) || !ctx.played) return false
    if (ctx.flushPromise) return await ctx.flushPromise
    if (!ctx.dirty) return true

    const operation = (async () => {
      try {
        await ensureStarted(ctx)

        if (!isCurrent(ctx) || !ctx.started) return false

        const percent = ctx.latestPercent
        ctx.dirty = false

        const response = await $api(
          `/api/v1/videos/${ctx.videoId}/progress`,
          {
            method: 'PUT',
            retry: 0,
            body: {
              interaction_id: ctx.interactionId,
              action: 'progress',
              progress_percent: percent,
            },
          },
        )

        if (!isCurrent(ctx)) return false

        if (percent >= 90) {
          ctx.autoReported = true
        }

        apply(ctx, response)
        return true
      } catch (error) {
        if (isCurrent(ctx)) ctx.dirty = true
        showError(ctx, error)
        return false
      }
    })()

    ctx.flushPromise = operation

    try {
      return await operation
    } finally {
      if (ctx.flushPromise === operation) {
        ctx.flushPromise = null
      }
    }
  }

  function started() {
    const ctx = context
    if (!ctx) return

    ctx.played = true

    void ensureStarted(ctx).catch(error => {
      showError(ctx, error)
    })
  }

  function report(value) {
    const ctx = context

    if (!ctx || !ctx.played) return

    const percent = Math.min(
      100,
      Math.max(0, Number(value) || 0),
    )

    // Максимум текущего открытия. Перемотка назад
    // не должна терять уже достигнутую позицию.
    if (percent > ctx.latestPercent) {
      ctx.latestPercent = percent
      ctx.dirty = true
    }

    maxPercent.value = Math.max(
      maxPercent.value,
      percent,
    )

    if (percent >= 90 && !ctx.autoReported) {
      void flushContext(ctx)
    }
  }

  function flush() {
    return flushContext(context)
  }

  function ended() {
    report(100)
    void flush()
  }

  async function complete() {
    const ctx = context

    if (!ctx || completing.value) return false

    completing.value = true

    try {
      await ensureOpen(ctx)

      if (!isCurrent(ctx) || !ctx.ready) return false

      // Дожидаемся уже отправленного обновления.
      if (ctx.flushPromise) {
        await ctx.flushPromise
      }

      if (ctx.played && ctx.dirty) {
        await flushContext(ctx)
      }

      if (!isCurrent(ctx)) return false

      const response = await $api(
        `/api/v1/videos/${ctx.videoId}/progress`,
        {
          method: 'PUT',
          retry: 0,
          body: {
            interaction_id: ctx.interactionId,
            action: 'complete',
          },
        },
      )

      if (!isCurrent(ctx)) return false

      ctx.autoReported = true
      apply(ctx, response)

      return true
    } catch (error) {
      showError(ctx, error)
      return false
    } finally {
      if (isCurrent(ctx)) completing.value = false
    }
  }

  function reset() {
    context = null

    maxPercent.value = 0
    completed.value = false
    completing.value = false
    errorMessage.value = ''

    if (!mounted.value || !enabled.value) return

    const currentProgramId = toValue(programId) || null
    const requestedSource = route.query.source

    const ctx = {
      videoId: toValue(video).id,
      interactionId: crypto.randomUUID(),
      programId: currentProgramId,
      stageId: toValue(programStageId) || null,
      source: currentProgramId
        ? 'program'
        : requestedSource === 'library'
          ? 'library'
          : 'direct',

      ready: false,
      started: false,
      played: false,
      dirty: false,
      latestPercent: 0,
      autoReported: false,
      journeySynced: false,

      openPromise: null,
      startPromise: null,
      flushPromise: null,
    }

    context = ctx

    void ensureOpen(ctx).catch(error => {
      showError(ctx, error)
    })
  }

  function onVisibilityChange() {
    if (document.hidden) {
      void flush()
    }
  }

  watch(
    [
      mounted,
      () => toValue(video)?.id,
      () => toValue(programId),
      () => toValue(programStageId),
      () => auth.accessToken,
      () => auth.activeRole,
    ],
    reset,
  )

  onMounted(() => {
    mounted.value = true

    timer = window.setInterval(() => {
      void flush()
    }, 15000)

    document.addEventListener(
      'visibilitychange',
      onVisibilityChange,
    )
  })

  onBeforeUnmount(() => {
    const ctx = context

    // Последняя небольшая отправка — best effort.
    // Закрытие браузера не гарантирует доставку запроса.
    if (
      ctx?.ready
      && ctx.started
      && ctx.dirty
      && auth.accessToken
    ) {
      void $api(`/api/v1/videos/${ctx.videoId}/progress`, {
        method: 'PUT',
        retry: 0,
        keepalive: true,
        body: {
          interaction_id: ctx.interactionId,
          action: 'progress',
          progress_percent: ctx.latestPercent,
        },
      }).catch(() => {})
    }

    disposed = true
    context = null

    window.clearInterval(timer)

    document.removeEventListener(
      'visibilitychange',
      onVisibilityChange,
    )
  })

  return {
    enabled,
    maxPercent,
    completed,
    completing,
    errorMessage,

    started,
    report,
    flush,
    ended,
    complete,
  }
}