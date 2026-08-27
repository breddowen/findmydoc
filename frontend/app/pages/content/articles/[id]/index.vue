<!-- ./frontend/app/pages/content/articles/[id]/index.vue -->
<script setup>
const route = useRoute()
const store = useArticlesStore()

const article = ref(null)
const loading = ref(true)
const errorMessage = ref('')

onMounted(async () => {
  try {
    article.value = await store.fetchArticle(
      route.params.id,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить статью'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="text"
    :count="10"
  />

  <div
    v-else-if="errorMessage"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <ArticlesReader
    v-else-if="article"
    :article="article"
  />
</template>