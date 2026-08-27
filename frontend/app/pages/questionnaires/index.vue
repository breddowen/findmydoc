<!-- ./frontend/app/pages/questionnaires/index.vue -->
<script setup>
const store = useQuestionnairesStore()

const questionnaires = ref([])
const progressItems = ref([])

const loading = ref(true)
const page = ref(1)
const pageSize = 10

const paginatedItems = computed(() => {
  const start = (page.value - 1) * pageSize

  return questionnaires.value.slice(
    start,
    start + pageSize,
  )
})

function getProgress(questionnaireId) {
  return progressItems.value.find(
    (item) =>
      item.questionnaire_id === questionnaireId,
  )
}

async function load() {
  loading.value = true

  try {
    const [items, progress] = await Promise.all([
      store.fetchQuestionnaires(),
      store.fetchMyProgress(),
    ])

    questionnaires.value = items
    progressItems.value = progress
  } finally {
    loading.value = false
  }
}

onMounted(load)
</script>

<template>
  <div class="space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Опросники
      </h1>

      <p class="text-base-content/60 mt-1">
        Начатые опросники сохраняются автоматически.
      </p>
    </header>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <article
        v-for="questionnaire in paginatedItems"
        :key="questionnaire.id"
        class="card bg-base-100 border-base-300 border"
      >
        <div class="card-body">
          <div class="flex flex-wrap gap-2">
            <span
              v-if="questionnaire.pro_content"
              class="badge badge-secondary"
            >
              Pro
            </span>

            <span
              v-if="
                getProgress(questionnaire.id)?.status
                === 'completed'
              "
              class="badge badge-success"
            >
              Пройден
            </span>

            <span
              v-else-if="getProgress(questionnaire.id)"
              class="badge badge-warning"
            >
              Не завершён
            </span>
          </div>

          <h2 class="card-title">
            {{ questionnaire.title }}
          </h2>

          <p class="text-base-content/60 line-clamp-3 text-sm">
            {{ questionnaire.description }}
          </p>

          <div
            v-if="getProgress(questionnaire.id)"
            class="mt-3"
          >
            <progress
              class="progress progress-primary w-full"
              :value="
                getProgress(questionnaire.id).progress_percent
              "
              max="100"
            />

            <p class="mt-1 text-xs">
              {{
                getProgress(questionnaire.id).progress_percent
              }}%
            </p>
          </div>

          <div class="card-actions mt-4">
            <NuxtLink
              :to="`/questionnaires/${questionnaire.id}`"
              class="btn btn-primary btn-sm"
            >
              {{
                getProgress(questionnaire.id)?.status
                === 'in_progress'
                  ? 'Продолжить'
                  : 'Начать'
              }}
            </NuxtLink>
          </div>
        </div>
      </article>
    </div>

    <UiPagination
      v-model="page"
      :total-items="questionnaires.length"
      :page-size="pageSize"
    />
  </div>
</template>