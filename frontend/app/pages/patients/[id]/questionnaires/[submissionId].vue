<!-- ./frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue -->
<script setup>
const route = useRoute()
const { $api } = useNuxtApp()

const submission = ref(null)
const questionnaire = ref(null)

const loading = ref(true)
const errorMessage = ref('')

function findQuestion(questionId) {
  return questionnaire.value?.questions.find(
    (question) => question.id === questionId,
  )
}

function formatAnswer(answer) {
  const question = findQuestion(answer.question_id)

  if (!question) {
    return String(answer.value ?? '—')
  }

  if (question.question_type === 'boolean') {
    return answer.value ? 'Да' : 'Нет'
  }

  if (
    question.question_type === 'single_choice'
  ) {
    return (
      question.options.find(
        (option) => option.id === answer.value,
      )?.text
      || answer.value
    )
  }

  if (
    question.question_type === 'multiple_choice'
  ) {
    if (!Array.isArray(answer.value)) {
      return '—'
    }

    return answer.value
      .map(
        (optionId) =>
          question.options.find(
            (option) => option.id === optionId,
          )?.text || optionId,
      )
      .join(', ')
  }

  return String(answer.value ?? '—')
}

function getAnswer(questionId) {
  return submission.value?.answers.find(
    (answer) => answer.question_id === questionId,
  )
}

onMounted(async () => {
  try {
    submission.value = await $api(
      `/api/v1/questionnaires/submissions/${route.params.submissionId}`,
    )

    questionnaire.value = await $api(
      `/api/v1/questionnaires/${submission.value.questionnaire_id}`,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить результат'
  } finally {
    loading.value = false
  }
})
</script>

<template>
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
    v-else-if="submission && questionnaire"
    class="mx-auto max-w-4xl space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <NuxtLink
        :to="`/patients/${route.params.id}`"
        class="btn btn-ghost btn-sm mb-4"
      >
        <Icon
          name="lucide:arrow-left"
          class="size-4"
        />
        К пациенту
      </NuxtLink>

      <h1 class="text-2xl font-bold sm:text-3xl">
        {{ questionnaire.title }}
      </h1>

      <div class="mt-4 flex flex-wrap gap-2">
        <span
          class="badge"
          :class="
            submission.status === 'completed'
              ? 'badge-success'
              : 'badge-warning'
          "
        >
          {{
            submission.status === 'completed'
              ? 'Завершён'
              : 'Не завершён'
          }}
        </span>

        <span class="badge badge-outline">
          Ответов: {{ submission.answers.length }}
          из {{ questionnaire.questions.length }}
        </span>
      </div>
    </header>

    <section class="space-y-4">
      <article
        v-for="(question, index) in questionnaire.questions"
        :key="question.id"
        class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-6"
      >
        <div class="flex gap-3">
          <div
            class="bg-primary/10 text-primary flex size-8 shrink-0 items-center justify-center rounded-full text-sm font-bold"
          >
            {{ index + 1 }}
          </div>

          <div class="min-w-0 flex-1">
            <h2 class="font-semibold">
              {{ question.text }}
            </h2>

            <div
              v-if="getAnswer(question.id)"
              class="bg-base-200 mt-4 rounded-xl p-4"
            >
              {{
                formatAnswer(
                  getAnswer(question.id),
                )
              }}
            </div>

            <div
              v-else
              class="border-warning/40 bg-warning/10 mt-4 rounded-xl border p-4 text-sm"
            >
              Ответ не дан
            </div>
          </div>
        </div>
      </article>
    </section>
  </div>
</template>