<!-- ./frontend/app/pages/content/articles/new.vue -->
<script setup>
const store = useArticlesStore()

const saving = ref(false)
const errorMessage = ref('')

async function save(payload) {
  saving.value = true
  errorMessage.value = ''

  try {
    const article = await store.createArticle(payload)

    await navigateTo(
      `/content/articles/${article.id}`,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось создать статью'
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-5xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Новая статья
      </h1>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <ArticlesForm
      :saving="saving"
      @submit="save"
      @cancel="navigateTo('/content/articles')"
    />
  </div>
</template>