// ./frontend/app/stores/programs.js
export const useProgramsStore = defineStore(
  'programs',
  () => {
    const programs = ref([])
    const currentProgram = ref(null)

    const patientAccessPrograms = ref([])

    const loading = ref(false)
    const saving = ref(false)

    const patientProgressPrograms = ref([])

    async function fetchProgramsForStaff() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/manage',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramsForPatient() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/patient',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForStaff(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/manage/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForPatient(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/patient/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function createProgram(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          '/api/v1/programs/manage',
          {
            method: 'POST',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function updateProgram(
      programId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          `/api/v1/programs/manage/${programId}`,
          {
            method: 'PUT',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function setVisibility(
      programId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/manage/${programId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function startProgram(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/start`,
        {
          method: 'POST',
        },
      )
    }

    async function requestPurchase(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/request-purchase`,
        {
          method: 'POST',
        },
      )
    }

    async function fetchPatientProgramAccess(
      patientId,
    ) {
      const { $api } = useNuxtApp()

      patientAccessPrograms.value = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access`,
      )

      return patientAccessPrograms.value
    }

    async function setPatientProgramAccess(
      patientId,
      programId,
      isActive,
    ) {
      const { $api } = useNuxtApp()

      const response = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access/${programId}`,
        {
          method: 'PATCH',
          body: {
            is_active: isActive,
          },
        },
      )

      const item = patientAccessPrograms.value.find(
        (program) =>
          program.program_id === programId,
      )

      if (item) {
        Object.assign(item, response)
      }

      return response
    }

    async function fetchPatientProgramProgress(
        patientId,
        ) {
        const { $api } = useNuxtApp()

        patientProgressPrograms.value = await $api(
            `/api/v1/programs/manage/patient/${patientId}/progress`,
        )

        return patientProgressPrograms.value
        }

    return {
      programs,
      currentProgram,
      patientAccessPrograms,

      loading,
      saving,

      fetchProgramsForStaff,
      fetchProgramsForPatient,
      fetchProgramForStaff,
      fetchProgramForPatient,

      createProgram,
      updateProgram,
      setVisibility,

      startProgram,
      requestPurchase,

      fetchPatientProgramAccess,
      setPatientProgramAccess,

      patientProgressPrograms,
      fetchPatientProgramProgress,
    }
  },
)