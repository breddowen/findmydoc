<!-- ./frontend/app/pages/content/articles/[id]/edit.vue -->
<script setup>
const route = useRoute()
const store = useArticlesStore()

const article = ref(null)
const loading = ref(true)
const saving = ref(false)
const errorMessage = ref('')

async function loadArticle() {
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
}

async function save(payload) {
  saving.value = true
  errorMessage.value = ''

  try {
    await store.updateArticle(
      route.params.id,
      payload,
    )

    await navigateTo(
      `/content/articles/${route.params.id}`,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить статью'
  } finally {
    saving.value = false
  }
}

onMounted(loadArticle)
</script>

<template>
  <div class="mx-auto max-w-5xl space-y-6">
    <h1 class="text-2xl font-bold sm:text-3xl">
      Редактирование статьи
    </h1>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-if="loading"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <ArticlesForm
      v-else-if="article"
      :initial-value="article"
      :saving="saving"
      submit-label="Сохранить изменения"
      @submit="save"
      @cancel="
        navigateTo(
          `/content/articles/${route.params.id}`,
        )
      "
    />
  </div>
</template>