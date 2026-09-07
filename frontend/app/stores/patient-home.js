// ./frontend/app/stores/patient-home.js
export const usePatientHomeStore = defineStore(
  'patient-home',
  () => {
    const { $api } = useNuxtApp()

    const programs = ref([])
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

      try {
        const response = await $api(
          '/api/v1/programs/patient',
        )

        if (currentVersion !== loadVersion) return

        programs.value = response
      } catch (error) {
        if (currentVersion !== loadVersion) return

        errorMessage.value =
          typeof error?.data?.detail === 'string'
            ? error.data.detail
            : 'Не удалось загрузить ваш маршрут'
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

    function clear() {
      loadVersion += 1
      programs.value = []
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

      load,
      startProgram,
      requestPurchase,
      clear,
    }
  },
)