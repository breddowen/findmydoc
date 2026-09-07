// ./frontend/app/stores/questionnaires.js
export const useQuestionnairesStore = defineStore(
  'questionnaires',
  () => {
    const questionnaires = ref([])
    const currentQuestionnaire = ref(null)
    const loading = ref(false)

    async function fetchQuestionnaires() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        questionnaires.value = await $api(
          '/api/v1/questionnaires',
        )

        return questionnaires.value
      } finally {
        loading.value = false
      }
    }

    async function fetchQuestionnaire(
      id,
      {
        programId = null,
        programStageId = null,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentQuestionnaire.value = await $api(
          `/api/v1/questionnaires/${id}`,
          {
            query: {
              program_id: programId || undefined,
              program_stage_id:
                programStageId || undefined,
            },
          },
        )

        return currentQuestionnaire.value
      } finally {
        loading.value = false
      }
    }

    async function createQuestionnaire(payload) {
      const { $api } = useNuxtApp()

      return await $api(
        '/api/v1/questionnaires',
        {
          method: 'POST',
          body: payload,
        },
      )
    }

    async function setVisibility(
      questionnaireId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/${questionnaireId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function fetchMyProgress() {
      const { $api } = useNuxtApp()

      return await $api(
        '/api/v1/questionnaires/submissions/mine/progress',
      )
    }

    async function startQuestionnaire(
      questionnaireId,
      {
        programId = null,
        programStageId = null,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/${questionnaireId}/start`,
        {
          method: 'POST',
          query: {
            program_id: programId || undefined,
            program_stage_id:
              programStageId || undefined,
          },
        },
      )
    }

    async function fetchSubmission(submissionId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}`,
      )
    }

    async function saveAnswer(
      submissionId,
      questionId,
      value,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}/answer`,
        {
          method: 'PUT',
          body: {
            question_id: questionId,
            value,
          },
        },
      )
    }

    async function completeSubmission(
      submissionId,
      answers,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}/complete`,
        {
          method: 'POST',
          body: {
            answers,
          },
        },
      )
    }
    async function setLibraryVisibility(
        questionnaireId,
        isLibraryHidden,
      ) {
        const { $api } = useNuxtApp()

        const response = await $api(
          `/api/v1/questionnaires/${questionnaireId}/library-visibility`,
          {
            method: 'PATCH',
            body: {
              is_library_hidden: isLibraryHidden,
            },
          },
        )

        const item = questionnaires.value.find(
          current => current.id === questionnaireId,
        )

        if (item) {
          item.is_library_hidden = response.is_library_hidden
        }

        if (currentQuestionnaire.value?.id === questionnaireId) {
          currentQuestionnaire.value.is_library_hidden =
            response.is_library_hidden
        }

        return response
      }

    return {
      questionnaires,
      currentQuestionnaire,
      loading,

      fetchQuestionnaires,
      fetchQuestionnaire,
      createQuestionnaire,
      setVisibility,
      setLibraryVisibility,

      fetchMyProgress,
      startQuestionnaire,
      fetchSubmission,
      saveAnswer,
      completeSubmission,
    }
  },
)