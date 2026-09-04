<!-- ./frontend/app/pages/content/articles/[id]/index.vue -->
<script setup>
const route = useRoute()

const auth = useAuthStore()
const store = useArticlesStore()

const article = ref(null)
const interactionId = ref(null)

const loading = ref(true)
const errorMessage = ref('')

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

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

async function registerPatientOpen() {
  if (!isPatient.value) return

  interactionId.value =
    window.crypto.randomUUID()

  try {
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
    // Ошибка аналитики не должна запрещать
    // пациенту читать доступную статью.
    console.warn(
      'Не удалось зарегистрировать открытие статьи',
      error,
    )

    // Без успешно зарегистрированного открытия
    // не создаём связанное событие ARTICLE_READ.
    interactionId.value = null
  }
}

onMounted(async () => {
  try {
    article.value = await store.fetchArticle(
      route.params.id,
    )

    await registerPatientOpen()
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
    :interaction-id="interactionId"
  />
</template>