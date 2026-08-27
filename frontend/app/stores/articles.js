// ./frontend/app/stores/articles.js
export const useArticlesStore = defineStore(
  'articles',
  () => {
    const articles = ref([])
    const currentArticle = ref(null)
    const loading = ref(false)

    async function fetchArticles() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        articles.value = await $api(
          '/api/v1/articles',
        )

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

    return {
      articles,
      currentArticle,
      loading,

      fetchArticles,
      fetchArticle,
      createArticle,
      updateArticle,
      setVisibility,
      markAsRead,
    }
  },
)