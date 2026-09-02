// ./frontend/app/stores/tag-access.js
export const useTagAccessStore = defineStore(
  'tag-access',
  () => {
    const tags = ref([])

    const doctorEffectiveTags = ref([])
    const doctorOverrides = ref([])

    const patientEffectiveTags = ref([])
    const patientOverrides = ref([])

    const loadingDoctor = ref(false)
    const loadingPatient = ref(false)
    const saving = ref(false)

    async function fetchTags() {
      const { $api } = useNuxtApp()

      tags.value = await $api(
        '/api/v1/tags',
      )

      return tags.value
    }

    async function fetchDoctorState() {
      const { $api } = useNuxtApp()

      loadingDoctor.value = true

      try {
        const [
          catalog,
          effective,
          overrides,
        ] = await Promise.all([
          $api('/api/v1/tags'),
          $api('/api/v1/tags/me/effective'),
          $api(
            '/api/v1/tags/doctors/me/overrides',
          ),
        ])

        tags.value = catalog
        doctorEffectiveTags.value =
          effective.tags || []
        doctorOverrides.value = overrides

        return {
          effective: effective.tags || [],
          overrides,
        }
      } finally {
        loadingDoctor.value = false
      }
    }

    async function setDoctorOverride(
      tagId,
      action,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          '/api/v1/tags/doctors/me/overrides',
          {
            method: 'PUT',
            body: {
              tag_id: tagId,
              action,
            },
          },
        )

        await fetchDoctorState()
      } finally {
        saving.value = false
      }
    }

    async function resetDoctorOverride(tagId) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/doctors/me/overrides/${tagId}`,
          {
            method: 'DELETE',
          },
        )

        await fetchDoctorState()
      } finally {
        saving.value = false
      }
    }

    async function fetchPatientState(patientId) {
      const { $api } = useNuxtApp()

      loadingPatient.value = true

      try {
        const [
          catalog,
          effective,
          overrides,
        ] = await Promise.all([
          $api('/api/v1/tags'),
          $api(
            `/api/v1/tags/patients/${patientId}/effective`,
          ),
          $api(
            `/api/v1/tags/patients/${patientId}/overrides`,
          ),
        ])

        tags.value = catalog
        patientEffectiveTags.value =
          effective.tags || []
        patientOverrides.value = overrides

        return {
          effective: effective.tags || [],
          overrides,
        }
      } finally {
        loadingPatient.value = false
      }
    }

    async function setPatientOverride(
      patientId,
      tagId,
      action,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/patients/${patientId}/overrides`,
          {
            method: 'PUT',
            body: {
              tag_id: tagId,
              action,
            },
          },
        )

        await fetchPatientState(patientId)
      } finally {
        saving.value = false
      }
    }

    async function resetPatientOverride(
      patientId,
      tagId,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/patients/${patientId}/overrides/${tagId}`,
          {
            method: 'DELETE',
          },
        )

        await fetchPatientState(patientId)
      } finally {
        saving.value = false
      }
    }

    return {
      tags,

      doctorEffectiveTags,
      doctorOverrides,

      patientEffectiveTags,
      patientOverrides,

      loadingDoctor,
      loadingPatient,
      saving,

      fetchTags,
      fetchDoctorState,
      setDoctorOverride,
      resetDoctorOverride,

      fetchPatientState,
      setPatientOverride,
      resetPatientOverride,
    }
  },
)