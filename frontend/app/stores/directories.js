// ./frontend/app/stores/directories.js
export const useDirectoriesStore = defineStore(
  'directories',
  () => {
    const tags = ref([])
    const specialities = ref([])

    const loading = ref(false)
    const saving = ref(false)

    async function fetchAll() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        const [
          tagsResponse,
          specialitiesResponse,
        ] = await Promise.all([
          $api('/api/v1/tags', {
            query: {
              include_hidden: true,
            },
          }),
          $api('/api/v1/specialities', {
            query: {
              include_hidden: true,
            },
          }),
        ])

        tags.value = tagsResponse
        specialities.value = specialitiesResponse
      } finally {
        loading.value = false
      }
    }

    async function saveTag(payload, tagId = null) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        const result = await $api(
          tagId
            ? `/api/v1/tags/${tagId}`
            : '/api/v1/tags',
          {
            method: tagId ? 'PATCH' : 'POST',
            body: payload,
          },
        )

        await fetchAll()
        return result
      } finally {
        saving.value = false
      }
    }

    async function setTagHidden(tagId, isHidden) {
      const { $api } = useNuxtApp()

      const result = await $api(
        `/api/v1/tags/${tagId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )

      await fetchAll()
      return result
    }

    async function deleteTag(tagId) {
      const { $api } = useNuxtApp()

      await $api(`/api/v1/tags/${tagId}`, {
        method: 'DELETE',
      })

      await fetchAll()
    }

    async function saveSpeciality(
      payload,
      specialityId = null,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        const result = await $api(
          specialityId
            ? `/api/v1/specialities/${specialityId}`
            : '/api/v1/specialities',
          {
            method: specialityId ? 'PATCH' : 'POST',
            body: payload,
          },
        )

        await fetchAll()
        return result
      } finally {
        saving.value = false
      }
    }

    async function setSpecialityHidden(
      specialityId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      const result = await $api(
        `/api/v1/specialities/${specialityId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )

      await fetchAll()
      return result
    }

    async function deleteSpeciality(specialityId) {
      const { $api } = useNuxtApp()

      await $api(
        `/api/v1/specialities/${specialityId}`,
        {
          method: 'DELETE',
        },
      )

      await fetchAll()
    }

    async function fetchSpecialityTags(
      specialityId,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/tags/specialities/${specialityId}`,
      )
    }

    async function addTagToSpeciality(
      specialityId,
      tagId,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/tags/specialities/${specialityId}/${tagId}`,
        {
          method: 'POST',
        },
      )
    }

    async function removeTagFromSpeciality(
      specialityId,
      tagId,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/tags/specialities/${specialityId}/${tagId}`,
        {
          method: 'DELETE',
        },
      )
    }

    return {
      tags,
      specialities,
      loading,
      saving,

      fetchAll,

      saveTag,
      setTagHidden,
      deleteTag,

      saveSpeciality,
      setSpecialityHidden,
      deleteSpeciality,

      fetchSpecialityTags,
      addTagToSpeciality,
      removeTagFromSpeciality,
    }
  },
)