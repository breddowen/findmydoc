// ./frontend/app/stores/articles.js
export const useArticlesStore = defineStore(
  'articles',
  () => {
    const articles = ref([])
    const currentArticle = ref(null)
    const loading = ref(false)

    const hasMore = ref(true)

    async function fetchArticles({
      reset = false,
      limit = 5,
    } = {}) {
      const { $api } = useNuxtApp()

      if (loading.value) return articles.value

      if (reset) {
        articles.value = []
        hasMore.value = true
      }

      if (!hasMore.value) {
        return articles.value
      }

      loading.value = true

      try {
        const page = await $api(
          '/api/v1/articles',
          {
            query: {
              offset: articles.value.length,
              limit,
            },
          },
        )

        const existingIds = new Set(
          articles.value.map(
            article => article.id,
          ),
        )

        const newItems = page.filter(
          article => !existingIds.has(article.id),
        )

        articles.value.push(...newItems)

        hasMore.value = page.length === limit

        return articles.value
      } finally {
        loading.value = false
      }
    }

    async function fetchArticle(articleId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentArticle.value = await $api(
          `/api/v1/articles/${articleId}`,
        )

        return currentArticle.value
      } finally {
        loading.value = false
      }
    }

    async function createArticle(payload) {
      const { $api } = useNuxtApp()

      return await $api('/api/v1/articles', {
        method: 'POST',
        body: payload,
      })
    }

    async function updateArticle(
      articleId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}`,
        {
          method: 'PATCH',
          body: payload,
        },
      )
    }

    async function setVisibility(
      articleId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function markAsRead(articleId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/read`,
        {
          method: 'POST',
        },
      )
    }

    async function registerOpen(
      articleId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/open`,
        {
          method: 'POST',
          body: payload,
        },
      )
    }

    return {
      articles,
      currentArticle,
      loading,

      hasMore,
      fetchArticles,
      fetchArticle,
      registerOpen,
      createArticle,
      updateArticle,
      setVisibility,
      markAsRead,
    }
  },
)