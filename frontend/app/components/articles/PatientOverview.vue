<!-- ./frontend/app/components/articles/PatientOverview.vue -->
<script setup>
const store = useArticlesStore()

const articles = ref([])
const loading = ref(true)
const errorMessage = ref('')

function canReadArticle(article) {
  return article.can_access !== false
}

function articleAuraClass(article) {
  if (!article.pro_content) {
    return ''
  }

  return canReadArticle(article)
    ? 'aura aura-rainbow'
    : 'aura aura-silver'
}

onMounted(async () => {
  try {
    const response = await store.fetchArticles()

    articles.value = response.slice(0, 6)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить статьи'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="space-y-4">
    <div
      class="flex items-center justify-between gap-4"
    >
      <div>
        <h2 class="text-xl font-bold sm:text-2xl">
          Рекомендуемые статьи
        </h2>

        <p class="text-base-content/60 text-sm">
          Материалы подобраны по вашим тегам.
        </p>
      </div>

      <NuxtLink
        to="/content/articles"
        class="btn btn-ghost btn-sm"
      >
        Все статьи
      </NuxtLink>
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-else-if="articles.length"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="article in articles"
        :key="article.id"
        :class="[
          articleAuraClass(article),
          'h-full',
        ]"
      >
        <!-- Доступная статья -->
        <NuxtLink
          v-if="canReadArticle(article)"
          :to="`/content/articles/${article.id}`"
          class="card bg-base-100 border-base-300 hover:border-primary h-full border transition"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                v-if="article.pro_content"
                class="badge badge-secondary badge-sm"
              >
                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-primary btn-sm"
              >
                Читать
              </span>
            </div>
          </div>
        </NuxtLink>

        <!-- Заблокированная Pro-статья -->
        <div
          v-else
          class="card bg-base-100 h-full"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                class="badge badge-secondary badge-sm gap-1"
              >
                <Icon
                  name="lucide:sparkles"
                  class="size-3"
                />

                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <p
              class="text-base-content/60 text-sm"
            >
              Статья доступна пользователям Pro.
            </p>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-disabled btn-sm gap-1"
              >
                <Icon
                  name="lucide:lock"
                  class="size-4"
                />

                Только Pro
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p
      v-else
      class="text-base-content/50"
    >
      Подходящих статей пока нет.
    </p>
  </section>
</template>