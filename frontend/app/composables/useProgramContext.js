// ./frontend/app/composables/useProgramContext.js
export function useProgramContext() {
  const route = useRoute()
  const auth = useAuthStore()

  function queryString(value) {
    return typeof value === 'string' && value
      ? value
      : null
  }

  const isProgramPage = computed(() =>
    Boolean(route.params.id)
    && /^\/programs\/[^/]+\/?$/.test(route.path),
  )

  const isArticlePage = computed(() =>
    /^\/content\/articles\/[^/]+\/?$/.test(route.path)
    && Boolean(route.params.id),
  )

  const isQuestionnairePage = computed(() =>
    /^\/questionnaires\/[^/]+\/?$/.test(route.path)
    && Boolean(route.params.id),
  )

  const isMaterialPage = computed(() =>
    isArticlePage.value || isQuestionnairePage.value,
  )

  const programId = computed(() => {
    if (isProgramPage.value) {
      return String(route.params.id)
    }

    if (!isMaterialPage.value) return null

    return queryString(route.query.program_id)
      || queryString(route.query.program)
  })

  const stageId = computed(() =>
    queryString(route.query.program_stage_id)
    || queryString(route.query.stage),
  )

  const usesProgramLayout = computed(() =>
    auth.isAuthenticated
    && auth.activeRole === 'patient'
    && Boolean(programId.value),
  )

  return {
    programId,
    stageId,
    isProgramPage,
    isArticlePage,
    isQuestionnairePage,
    isMaterialPage,
    usesProgramLayout,
  }
}