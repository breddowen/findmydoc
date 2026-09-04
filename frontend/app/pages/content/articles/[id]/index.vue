<!-- ./frontend/app/pages/content/articles/[id]/index.vue -->
<script setup>
const route = useRoute()
const store = useArticlesStore()

const article = ref(null)
const interactionId = ref(null)

const loading = ref(true)
const errorMessage = ref('')

const allowedSources = new Set([
  'library',
  'program',
  'assignment',
  'direct',
])

function getOpenSource() {
  const source = String(
    route.query.source || 'direct',
  )

  return allowedSources.has(source)
    ? source
    : 'direct'
}

onMounted(async () => {
  try {
    article.value = await store.fetchArticle(
      route.params.id,
    )

    interactionId.value =
      window.crypto.randomUUID()

    await store.registerOpen(
      route.params.id,
      {
        interaction_id: interactionId.value,
        source: getOpenSource(),
        program_id:
          route.query.program_id || null,
        assignment_id:
          route.query.assignment_id || null,
      },
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
    v-else-if="article && interactionId"
    :article="article"
    :interaction-id="interactionId"
  />
</template>