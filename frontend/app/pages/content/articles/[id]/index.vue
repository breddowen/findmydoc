<!-- ./frontend/app/pages/content/articles/[id]/index.vue -->
<script setup>
definePageMeta({
  // При смене программы или статьи создаём
  // отдельный экземпляр страницы и взаимодействия.
  key: route => route.fullPath,
})

const route = useRoute()

const auth = useAuthStore()
const store = useArticlesStore()

const article = ref(null)
const interactionId = ref(null)

const loading = ref(true)
const errorMessage = ref('')

let disposed = false

function stringQuery(value) {
  return typeof value === 'string' && value
    ? value
    : null
}

const programId = computed(() =>
  stringQuery(route.query.program_id)
  || stringQuery(route.query.program),
)

const programStageId = computed(() =>
  stringQuery(route.query.program_stage_id)
  || stringQuery(route.query.stage),
)

const assignmentId = computed(() =>
  stringQuery(route.query.assignment_id),
)

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
  if (programId.value) return 'program'

  const source = stringQuery(route.query.source)

  return allowedSources.has(source)
    ? source
    : 'direct'
}

async function registerPatientOpen() {
  if (!isPatient.value) return

  const currentInteractionId =
    window.crypto.randomUUID()

  try {
    await store.registerOpen(
      route.params.id,
      {
        interaction_id: currentInteractionId,
        source: getOpenSource(),
        program_id: programId.value,
        program_stage_id: programStageId.value,
        assignment_id: assignmentId.value,
      },
    )

    if (!disposed) {
      interactionId.value = currentInteractionId
    }
  } catch {
    // Отсутствие аналитики не мешает чтению.
    interactionId.value = null
  }
}

onMounted(async () => {
  try {
    const response = await store.fetchArticle(
      route.params.id,
      {
        programId: programId.value,
        programStageId: programStageId.value,
      },
    )

    if (disposed) return

    article.value = response

    await registerPatientOpen()
  } catch (error) {
    if (disposed) return

    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось загрузить статью'
  } finally {
    if (!disposed) {
      loading.value = false
    }
  }
})

onBeforeUnmount(() => {
  disposed = true
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
    role="alert"
  >
    {{ errorMessage }}
  </div>

  <ArticlesReader
    v-else-if="article"
    :article="article"
    :interaction-id="interactionId"
    :program-id="programId"
    :program-stage-id="programStageId"
  />
</template>