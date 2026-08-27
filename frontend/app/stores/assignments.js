// ./frontend/app/stores/assignments.js
export const useAssignmentsStore = defineStore(
  'assignments',
  () => {
    const assignments = ref([])
    const patientAssignments = ref([])

    const loading = ref(false)
    const patientAssignmentsLoading = ref(false)
    const creating = ref(false)

    async function fetchMyAssignments() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        assignments.value = await $api(
          '/api/v1/assignments/me',
        )

        return assignments.value
      } finally {
        loading.value = false
      }
    }

    async function fetchPatientAssignments(
      patientId,
      {
        includeCompleted = true,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      patientAssignmentsLoading.value = true

      try {
        patientAssignments.value = await $api(
          `/api/v1/assignments/patient/${patientId}`,
          {
            query: {
              include_completed: includeCompleted,
            },
          },
        )

        return patientAssignments.value
      } finally {
        patientAssignmentsLoading.value = false
      }
    }

    async function createAssignment(payload) {
      const { $api } = useNuxtApp()

      creating.value = true

      try {
        const assignment = await $api(
          '/api/v1/assignments',
          {
            method: 'POST',
            body: payload,
          },
        )

        patientAssignments.value = [
          assignment,
          ...patientAssignments.value.filter(
            (item) => item.id !== assignment.id,
          ),
        ]

        return assignment
      } finally {
        creating.value = false
      }
    }

    function clearPatientAssignments() {
      patientAssignments.value = []
    }

    return {
      assignments,
      patientAssignments,

      loading,
      patientAssignmentsLoading,
      creating,

      fetchMyAssignments,
      fetchPatientAssignments,
      createAssignment,
      clearPatientAssignments,
    }
  },
)