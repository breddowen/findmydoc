<!-- ./frontend/app/pages/content/articles/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useArticlesStore()

const errorMessage = ref('')

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

async function toggleVisibility(article) {
  errorMessage.value = ''

  try {
    await store.setVisibility(
      article.id,
      !article.is_hidden,
    )

    await store.fetchArticles()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость'
  }
}

onMounted(store.fetchArticles)
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Статьи
        </h1>

        <p class="text-base-content/60 mt-1">
          Материалы для пациентов.
        </p>
      </div>

      <NuxtLink
        v-if="canManage"
        to="/content/articles/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая статья
      </NuxtLink>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-if="store.loading"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <div
      v-else-if="store.articles.length"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <article
        v-for="article in store.articles"
        :key="article.id"
        class="card bg-base-100 border-base-300 border"
        :class="{
          'opacity-60': article.is_hidden,
        }"
      >
        <div class="card-body">
          <div class="flex flex-wrap gap-2">
            <span
              v-if="article.pro_content"
              class="badge badge-secondary"
            >
              Pro
            </span>

            <span
              v-if="article.is_hidden"
              class="badge badge-warning"
            >
              Скрыта
            </span>
          </div>

          <h2 class="card-title">
            {{ article.title }}
          </h2>

          <div class="flex flex-wrap gap-1">
            <span
              v-for="tag in article.tags"
              :key="tag.id"
              class="badge badge-outline badge-sm"
            >
              {{ tag.name }}
            </span>
          </div>

          <div class="card-actions mt-4">
            <NuxtLink
              :to="`/content/articles/${article.id}`"
              class="btn btn-sm"
            >
              Открыть
            </NuxtLink>

            <NuxtLink
              v-if="canManage"
              :to="`/content/articles/${article.id}/edit`"
              class="btn btn-sm btn-outline"
            >
              Редактировать
            </NuxtLink>

            <button
              v-if="canManage"
              type="button"
              class="btn btn-sm btn-ghost"
              @click="toggleVisibility(article)"
            >
              {{
                article.is_hidden
                  ? 'Показать'
                  : 'Скрыть'
              }}
            </button>
          </div>
        </div>
      </article>
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:file-text"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Статей пока нет
      </p>
    </div>
  </div>
</template>