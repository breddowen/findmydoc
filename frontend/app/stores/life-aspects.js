// frontend\app\stores\life-aspects.js

export const useLifeAspectsStore = defineStore(
  'life-aspects',
  () => {
    const { $api } = useNuxtApp()

    const aspects = ref([])
    const tags = ref([])

    const loading = ref(false)
    const saving = ref(false)

    let stateVersion = 0

    const orderedAspects = computed(() =>
      [...aspects.value].sort(
        (left, right) =>
          left.order_index - right.order_index
          || left.name.localeCompare(right.name, 'ru')
          || left.id.localeCompare(right.id),
      ),
    )

    function replaceAspect(aspect) {
      const index = aspects.value.findIndex(
        item => item.id === aspect.id,
      )

      if (index === -1) {
        aspects.value.push(aspect)
      } else {
        aspects.value[index] = aspect
      }
    }

    async function load() {
      if (saving.value) {
        throw new Error('Дождитесь окончания сохранения')
      }

      const version = ++stateVersion
      loading.value = true

      try {
        const [aspectItems, tagItems] = await Promise.all([
          $api('/api/v1/life-aspects/manage', {
            query: { include_hidden: true },
          }),
          $api('/api/v1/tags', {
            query: { include_hidden: true },
          }),
        ])

        if (version !== stateVersion) return

        aspects.value = aspectItems
        tags.value = tagItems
      } catch (error) {
        if (version === stateVersion) throw error
      } finally {
        if (version === stateVersion) {
          loading.value = false
        }
      }
    }

    async function mutate(request, applyResult) {
      if (saving.value || loading.value) {
        throw new Error('Дождитесь окончания операции')
      }

      const version = stateVersion
      saving.value = true

      try {
        const result = await request()

        if (version === stateVersion) {
          applyResult(result)
        }

        return result
      } finally {
        if (version === stateVersion) {
          saving.value = false
        }
      }
    }

    async function saveAspect(payload, aspectId = null) {
      return mutate(
        () => $api(
          aspectId
            ? `/api/v1/life-aspects/manage/${aspectId}`
            : '/api/v1/life-aspects/manage',
          {
            method: aspectId ? 'PATCH' : 'POST',
            body: payload,
          },
        ),
        replaceAspect,
      )
    }

    async function addTag(aspectId, tagId) {
      return mutate(
        () => $api(
          `/api/v1/life-aspects/manage/${aspectId}/tags/${tagId}`,
          { method: 'PUT' },
        ),
        replaceAspect,
      )
    }

    async function removeTag(aspectId, tagId) {
      return mutate(
        () => $api(
          `/api/v1/life-aspects/manage/${aspectId}/tags/${tagId}`,
          { method: 'DELETE' },
        ),
        () => {
          const aspect = aspects.value.find(
            item => item.id === aspectId,
          )

          if (aspect) {
            aspect.tags = aspect.tags.filter(
              tag => tag.id !== tagId,
            )
          }
        },
      )
    }

    function clear() {
      stateVersion += 1
      aspects.value = []
      tags.value = []
      loading.value = false
      saving.value = false
    }

    return {
      aspects,
      orderedAspects,
      tags,
      loading,
      saving,

      load,
      saveAspect,
      addTag,
      removeTag,
      clear,
    }
  },
)