<!-- ./frontend/app/pages/content/questionnaires/index.vue -->
<script setup>
const store = useQuestionnairesStore()

const errorMessage = ref('')

async function toggleVisibility(questionnaire) {
  errorMessage.value = ''

  try {
    await store.setVisibility(
      questionnaire.id,
      !questionnaire.is_hidden,
    )

    await store.fetchQuestionnaires()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость'
  }
}

function copyQuestionnaire(questionnaireId) {
  return navigateTo({
    path: '/content/questionnaires/new',
    query: {
      copy: questionnaireId,
    },
  })
}

onMounted(store.fetchQuestionnaires)
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Опросники
        </h1>

        <p class="text-base-content/60 mt-1">
          Опубликованные опросники неизменяемы.
        </p>
      </div>

      <NuxtLink
        to="/content/questionnaires/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новый опросник
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
      v-else-if="store.questionnaires.length"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <article
        v-for="questionnaire in store.questionnaires"
        :key="questionnaire.id"
        class="card bg-base-100 border-base-300 border"
        :class="{
          'opacity-60': questionnaire.is_hidden,
        }"
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
              v-if="questionnaire.is_hidden"
              class="badge badge-warning"
            >
              Скрыт
            </span>
          </div>

          <h2 class="card-title">
            {{ questionnaire.title }}
          </h2>

          <p class="text-base-content/60 line-clamp-3 text-sm">
            {{ questionnaire.description }}
          </p>

          <p class="text-sm">
            Вопросов:
            <strong>
              {{ questionnaire.questions_count }}
            </strong>
          </p>

          <div class="card-actions mt-4">
            <button
              type="button"
              class="btn btn-sm btn-primary"
              @click="copyQuestionnaire(questionnaire.id)"
            >
              <Icon
                name="lucide:copy"
                class="size-4"
              />
              Копировать
            </button>

            <button
              type="button"
              class="btn btn-sm btn-ghost"
              @click="toggleVisibility(questionnaire)"
            >
              {{
                questionnaire.is_hidden
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
        name="lucide:clipboard-list"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Опросников пока нет
      </p>
    </div>
  </div>
</template>