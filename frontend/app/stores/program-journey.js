// ./frontend/app/stores/program-journey.js
export const useProgramJourneyStore = defineStore(
  'program-journey',
  () => {
    const { $api } = useNuxtApp()

    const program = ref(null)
    const targetId = ref(null)

    const loading = ref(false)
    const starting = ref(false)
    const errorMessage = ref('')

    let requestVersion = 0
    let generation = 0

    function errorText(error, fallback) {
      return typeof error?.data?.detail === 'string'
        ? error.data.detail
        : fallback
    }

    async function load(programId) {
      if (!programId) return null

      if (targetId.value !== programId) {
        generation += 1
        targetId.value = programId
        program.value = null
        starting.value = false
      }

      const version = ++requestVersion

      // При обновлении той же программы не убираем
      // Navbar и открытый этап со страницы.
      loading.value = !program.value
      errorMessage.value = ''

      try {
        const response = await $api(
          `/api/v1/programs/patient/${programId}`,
        )

        if (version !== requestVersion) return null

        program.value = response
        return response
      } catch (error) {
        if (version === requestVersion) {
          errorMessage.value = errorText(
            error,
            'Не удалось загрузить программу',
          )
        }

        throw error
      } finally {
        if (version === requestVersion) {
          loading.value = false
        }
      }
    }

    async function start() {
      // Проверка обязательно выполняется ДО starting = true.
      if (starting.value || !program.value) return false

      if (program.value.enrollment) return true

      const programId = program.value.id
      const currentGeneration = generation

      starting.value = true
      errorMessage.value = ''

      try {
        await $api(
          `/api/v1/programs/patient/${programId}/start`,
          { method: 'POST' },
        )

        if (
          currentGeneration !== generation
          || targetId.value !== programId
        ) {
          return false
        }

        await load(programId)
        return true
      } catch (error) {
        if (currentGeneration === generation) {
          errorMessage.value = errorText(
            error,
            'Не удалось начать программу',
          )
        }

        return false
      } finally {
        if (currentGeneration === generation) {
          starting.value = false
        }
      }
    }

    function markPurchaseRequested(programId) {
      if (program.value?.id === programId) {
        program.value.purchase_requested = true
      }
    }

    function clear() {
      requestVersion += 1
      generation += 1

      program.value = null
      targetId.value = null
      loading.value = false
      starting.value = false
      errorMessage.value = ''
    }

    return {
      program,
      loading,
      starting,
      errorMessage,

      load,
      start,
      markPurchaseRequested,
      clear,
    }
  },
)