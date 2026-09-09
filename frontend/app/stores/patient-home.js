// ./frontend/app/stores/patient-home.js
export const usePatientHomeStore = defineStore(
  'patient-home',
  () => {
    const { $api } = useNuxtApp()

    const programs = ref([])
    const lifeAspects = ref([])
    const loading = ref(false)
    const errorMessage = ref('')

    let loadVersion = 0

    function priorityOf(program) {
      return Number(program.home_priority) || 0
    }

    function comparePrograms(left, right) {
      const priorityDifference =
        priorityOf(right) - priorityOf(left)

      if (priorityDifference) {
        return priorityDifference
      }

      const titleDifference = String(left.title || '').localeCompare(
        String(right.title || ''),
        'ru',
        { sensitivity: 'base' },
      )

      return titleDifference
        || String(left.id).localeCompare(String(right.id))
    }

    const orderedPrograms = computed(() =>
      [...programs.value].sort(comparePrograms),
    )

    function homeGroup(program) {
        if (!program.service) {
          return program.is_start ? 0 : 1
        }

        return program.has_program_access ? 2 : 3
      }

      const homePrograms = computed(() =>
        programs.value
          .filter(
            program =>
              program.enrollment?.status !== 'completed',
          )
          .sort(
            (left, right) =>
              homeGroup(left) - homeGroup(right)
              || comparePrograms(left, right),
          ),
      )

    const activePrograms = computed(() =>
      orderedPrograms.value.filter(
        program =>
          program.enrollment?.status === 'active',
      ),
    )

    function hasCompletedTask(program) {
      return (program.stages || []).some(
        stage => (stage.items || []).some(
          item =>
            [
              'article',
              'questionnaire',
            ].includes(item.item_type)
            && item.is_completed === true,
        ),
      )
    }

    // Пациент начал программу и выполнил
    // хотя бы одно задание.
    const inProgressPrograms = computed(() =>
      activePrograms.value.filter(hasCompletedTask),
    )

    // Остальные программы для обычного списка.
    // Уже показанные в блоке продолжения не дублируем.
    const remainingHomePrograms = computed(() => {
      const inProgressIds = new Set(
        inProgressPrograms.value.map(
          program => program.id,
        ),
      )

      return homePrograms.value.filter(
        program => !inProgressIds.has(program.id),
      )
    })

    const recommendedPrograms = computed(() =>
      remainingHomePrograms.value.filter(
        program => program.is_recommended === true,
      ),
    )

    const otherHomePrograms = computed(() =>
      remainingHomePrograms.value.filter(
        program => program.is_recommended !== true,
      ),
    )

    const completedPrograms = computed(() =>
      orderedPrograms.value.filter(
        program =>
          program.enrollment?.status === 'completed',
      ),
    )

    const hasCompletedStart = computed(() =>
      completedPrograms.value.some(
        program => program.is_start,
      ),
    )

    const primaryProgram = computed(() => {
      const activeWithAccess =
        activePrograms.value.find(
          program => program.has_program_access,
        )

      if (activeWithAccess) {
        return activeWithAccess
      }

      if (activePrograms.value.length) {
        return activePrograms.value[0]
      }

      const purchasedNotStarted =
        orderedPrograms.value.find(
          program =>
            program.has_program_access
            && !program.enrollment,
        )

      if (purchasedNotStarted) {
        return purchasedNotStarted
      }

      if (hasCompletedStart.value) {
        return null
      }

      return orderedPrograms.value.find(
        program =>
          program.is_start
          && !program.service
          && !program.enrollment,
      ) || null
    })

    const otherActivePrograms = computed(() =>
      activePrograms.value.filter(
        program =>
          program.id !== primaryProgram.value?.id,
      ),
    )

    const pendingRequests = computed(() =>
      orderedPrograms.value.filter(
        program => program.purchase_requested,
      ),
    )

    const supportPrograms = computed(() =>
      orderedPrograms.value
        .filter(
          program =>
            Boolean(program.service)
            && !program.is_start
            && !program.has_program_access
            && !program.purchase_requested,
        )
        .slice(0, 2),
    )

    async function load() {
      const currentVersion = ++loadVersion

      loading.value = true
      errorMessage.value = ''
      programs.value = []
      lifeAspects.value = []

      try {
        const [
          programResponse,
          aspectResponse,
        ] = await Promise.all([
          $api('/api/v1/programs/patient'),
          $api('/api/v1/life-aspects/patient'),
        ])

        if (currentVersion !== loadVersion) return

        programs.value = programResponse
        lifeAspects.value = aspectResponse
      } catch (error) {
        if (currentVersion !== loadVersion) return

        errorMessage.value =
          typeof error?.data?.detail === 'string'
            ? error.data.detail
            : 'Не удалось загрузить программы и сферы жизни'
      } finally {
        if (currentVersion === loadVersion) {
          loading.value = false
        }
      }
    }

    async function startProgram(programId) {
      return await $api(
        `/api/v1/programs/patient/${programId}/start`,
        {
          method: 'POST',
        },
      )
    }

    async function requestPurchase(programId) {
      const response = await $api(
        `/api/v1/programs/patient/${programId}/request-purchase`,
        {
          method: 'POST',
        },
      )

      const program = programs.value.find(
        item => item.id === programId,
      )

      if (program) {
        program.purchase_requested = true
      }

      return response
    }

    const homeLifeAspects = computed(() => {
      const programsById = new Map(
        programs.value.map(program => [
          program.id,
          program,
        ]),
      )

      const inProgressIds = new Set(
        inProgressPrograms.value.map(
          program => program.id,
        ),
      )

      return lifeAspects.value
        .map(aspect => ({
          ...aspect,

          // Используем полные пациентские данные программы:
          // доступ к материалам, прогресс, участие и услугу.
          programs: aspect.programs
            .map(program => programsById.get(program.id))
            .filter(program =>
              program
              && !inProgressIds.has(program.id),
            )
            .sort(
              (left, right) =>
                Number(Boolean(right.is_recommended))
                  - Number(Boolean(left.is_recommended))
                || comparePrograms(left, right),
            ),
        }))
        .filter(aspect => aspect.programs.length > 0)
    })

    const unclassifiedPrograms = computed(() => {
      const classifiedIds = new Set(
        lifeAspects.value.flatMap(
          aspect => aspect.programs.map(
            program => program.id,
          ),
        ),
      )

      return remainingHomePrograms.value.filter(
        program =>
          !classifiedIds.has(program.id)
          && !program.is_recommended,
      )
    })

    function clear() {
      loadVersion += 1
      programs.value = []
      lifeAspects.value = []
      loading.value = false
      errorMessage.value = ''
    }

    return {
      programs,
      loading,
      errorMessage,

      primaryProgram,
      otherActivePrograms,
      completedPrograms,
      hasCompletedStart,
      pendingRequests,
      supportPrograms,
      homePrograms,

      inProgressPrograms,
      remainingHomePrograms,
      recommendedPrograms,
      otherHomePrograms,

      load,
      startProgram,
      requestPurchase,
      clear,

      lifeAspects,
      homeLifeAspects,
      unclassifiedPrograms,
    }
  },
)