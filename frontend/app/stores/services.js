// ./frontend/app/stores/services.js
export const useServicesStore = defineStore(
  'services',
  () => {
    const services = ref([])

    const loading = ref(false)
    const saving = ref(false)
    const deleting = ref(false)

    function upsertService(service) {
      const index = services.value.findIndex(
        item => item.id === service.id,
      )

      if (index >= 0) {
        services.value[index] = service
      } else {
        services.value.push(service)
      }

      services.value.sort(
        (first, second) =>
          first.code.localeCompare(
            second.code,
            'ru',
          ),
      )
    }

    async function fetchServices(
      includeHidden = false,
    ) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        services.value = await $api(
          '/api/v1/services',
          {
            query: {
              include_hidden: includeHidden,
            },
          },
        )

        return services.value
      } finally {
        loading.value = false
      }
    }

    async function createService(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        const response = await $api(
          '/api/v1/services',
          {
            method: 'POST',
            body: payload,
          },
        )

        upsertService(response)
        return response
      } finally {
        saving.value = false
      }
    }

    async function updateService(
      serviceId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        const response = await $api(
          `/api/v1/services/${serviceId}`,
          {
            method: 'PATCH',
            body: payload,
          },
        )

        upsertService(response)
        return response
      } finally {
        saving.value = false
      }
    }

    async function setVisibility(
      serviceId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        const response = await $api(
          `/api/v1/services/${serviceId}/visibility`,
          {
            method: 'PATCH',
            body: {
              is_hidden: isHidden,
            },
          },
        )

        upsertService(response)
        return response
      } finally {
        saving.value = false
      }
    }

    async function deleteService(serviceId) {
      const { $api } = useNuxtApp()

      deleting.value = true

      try {
        await $api(
          `/api/v1/services/${serviceId}`,
          {
            method: 'DELETE',
          },
        )

        services.value = services.value.filter(
          service => service.id !== serviceId,
        )
      } finally {
        deleting.value = false
      }
    }

    return {
      services,
      loading,
      saving,
      deleting,

      fetchServices,
      createService,
      updateService,
      setVisibility,
      deleteService,
    }
  },
)