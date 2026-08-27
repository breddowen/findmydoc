// ./frontend/app/stores/patients.js
export const usePatientsStore = defineStore(
  'patients',
  () => {
    const patients = ref([])
    const currentPatient = ref(null)

    const page = ref(1)
    const pageSize = ref(10)
    const totalItems = ref(0)
    const totalPages = ref(1)

    const loading = ref(false)

    async function fetchPatients({
      requestedPage = 1,
      requestedPageSize = 10,
      search = '',
    } = {}) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        const response = await $api(
          '/api/v1/patients',
          {
            query: {
              page: requestedPage,
              page_size: requestedPageSize,
              search: search || undefined,
            },
          },
        )

        patients.value = response.items
        page.value = response.page
        pageSize.value = response.page_size
        totalItems.value = response.total_items
        totalPages.value = response.total_pages

        return response
      } finally {
        loading.value = false
      }
    }

    async function fetchPatient(patientId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentPatient.value = await $api(
          `/api/v1/patients/${patientId}`,
        )

        return currentPatient.value
      } finally {
        loading.value = false
      }
    }

    async function setPatientPro(
      patientId,
      proEnabled,
    ) {
      const { $api } = useNuxtApp()

      const response = await $api(
        `/api/v1/patients/${patientId}/pro`,
        {
          method: 'PATCH',
          body: {
            pro_enabled: proEnabled,
          },
        },
      )

      if (
        currentPatient.value?.patient_id
        === patientId
      ) {
        currentPatient.value.pro_enabled =
          response.pro_enabled
      }

      return response
    }

    return {
      patients,
      currentPatient,
      page,
      pageSize,
      totalItems,
      totalPages,
      loading,

      fetchPatients,
      fetchPatient,
      setPatientPro,
    }
  },
)