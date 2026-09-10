// ./frontend/app/composables/useProgramJourney.js
export function useProgramJourney() {
  const route = useRoute()
  const context = useProgramContext()
  const store = useProgramJourneyStore()

  const program = computed(() => store.program)

  const stages = computed(() =>
    program.value?.stages || [],
  )

  const started = computed(() =>
    Boolean(program.value?.enrollment),
  )

  function isStageCompleted(stage) {
    return started.value
      && Number(stage?.progress_percent) >= 100
  }

  const selectedIndex = computed(() => {
    const requestedIndex = stages.value.findIndex(
      stage => stage.id === context.stageId.value,
    )

    if (requestedIndex >= 0) return requestedIndex

    const unfinishedIndex = stages.value.findIndex(
      stage => !isStageCompleted(stage),
    )

    return unfinishedIndex >= 0 ? unfinishedIndex : 0
  })

  const selectedStage = computed(() =>
    stages.value[selectedIndex.value] || null,
  )

  const nextStage = computed(() =>
    stages.value[selectedIndex.value + 1] || null,
  )

  const stageProgress = computed(() => {
    if (!started.value) return 0

    const value = Number(
      selectedStage.value?.progress_percent,
    ) || 0

    return Math.min(100, Math.max(0, value))
  })

  const completedStageCount = computed(() =>
    stages.value.filter(isStageCompleted).length,
  )

  async function selectStage(stageId) {
    if (
      !program.value
      || !stages.value.some(stage => stage.id === stageId)
    ) {
      return
    }

    const query = context.isProgramPage.value
      ? { ...route.query }
      : {}

    delete query.program_stage_id
    query.stage = stageId

    return await navigateTo(
      {
        path: `/programs/${program.value.id}`,
        query,
      },
      {
        replace: context.isProgramPage.value,
      },
    )
  }

  return {
    program,
    stages,
    started,
    selectedIndex,
    selectedStage,
    nextStage,
    stageProgress,
    completedStageCount,

    isStageCompleted,
    selectStage,
  }
}