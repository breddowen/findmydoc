<!-- ./frontend/app/pages/content/questionnaires/[id].vue -->

<script setup>
const route = useRoute()
const store = useQuestionnairesStore()
const auth = useAuthStore()

const questionnaire = ref(null)
const submissionId = ref(null)

const answers = reactive({})
const savingQuestions = reactive({})

const loading = ref(true)
const completing = ref(false)
const completed = ref(false)

const errorMessage = ref('')

const saveTimers = new Map()

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canManageImage = computed(
  () => ['superuser', 'med_assistant'].includes(auth.activeRole),
)

const answeredCount = computed(() =>
  questionnaire.value?.questions.filter(
    (question) =>
      answers[question.id] !== undefined
      && answers[question.id] !== null
      && answers[question.id] !== '',
  ).length || 0
)

const progress = computed(() => {
  const total =
    questionnaire.value?.questions.length || 0

  return total
    ? Math.round(answeredCount.value / total * 100)
    : 0
})

async function initialize() {
  loading.value = true

  try {
    questionnaire.value =
      await store.fetchQuestionnaire(
        route.params.id,
      )

    if (!isPatient.value) {
      return
    }

    const allProgress =
      await store.fetchMyProgress()

    const existing = allProgress.find(
      (item) =>
        item.questionnaire_id === route.params.id
        && item.status === 'in_progress',
    )

    if (existing) {
      submissionId.value = existing.submission_id

      const submission =
        await store.fetchSubmission(
          existing.submission_id,
        )

      for (const answer of submission.answers) {
        answers[answer.question_id] = answer.value
      }
    } else {
      const submission =
        await store.startQuestionnaire(
          route.params.id,
        )

      submissionId.value = submission.submission_id
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось открыть опросник'
  } finally {
    loading.value = false
  }
}

function scheduleAnswerSave(question) {
  if (!isPatient.value || !submissionId.value) return

  const oldTimer = saveTimers.get(question.id)

  if (oldTimer) {
    window.clearTimeout(oldTimer)
  }

  const timer = window.setTimeout(async () => {
    savingQuestions[question.id] = true

    try {
      await store.saveAnswer(
        submissionId.value,
        question.id,
        answers[question.id],
      )
    } catch (error) {
      errorMessage.value =
        error?.data?.detail
        || 'Не удалось сохранить ответ'
    } finally {
      savingQuestions[question.id] = false
      saveTimers.delete(question.id)
    }
  }, 500)

  saveTimers.set(question.id, timer)
}

async function complete() {
  if (!isPatient.value || !submissionId.value) return

  errorMessage.value = ''

  const missingRequired =
    questionnaire.value.questions.find(
      (question) =>
        question.is_required
        && (
          answers[question.id] === undefined
          || answers[question.id] === null
          || answers[question.id] === ''
        ),
    )

  if (missingRequired) {
    errorMessage.value =
      `Ответьте на обязательный вопрос: ${missingRequired.text}`

    document
      .getElementById(
        `question-${missingRequired.id}`,
      )
      ?.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      })

    return
  }

  completing.value = true

  try {
    const payload = questionnaire.value.questions
      .filter(
        (question) =>
          answers[question.id] !== undefined,
      )
      .map((question) => ({
        question_id: question.id,
        value: answers[question.id],
      }))

    await store.completeSubmission(
      submissionId.value,
      payload,
    )

    completed.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось завершить опросник'
  } finally {
    completing.value = false
  }
}

onMounted(initialize)

onBeforeUnmount(() => {
  for (const timer of saveTimers.values()) {
    window.clearTimeout(timer)
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
    v-else-if="errorMessage && !questionnaire"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="completed"
    class="bg-base-100 border-base-300 mx-auto max-w-2xl rounded-3xl border p-8 text-center"
  >
    <Icon
      name="lucide:circle-check-big"
      class="text-success mx-auto size-16"
    />

    <h1 class="mt-5 text-2xl font-bold">
      Опросник заполнен
    </h1>

    <NuxtLink
      to="/questionnaires"
      class="btn btn-primary mt-6"
    >
      Вернуться к опросникам
    </NuxtLink>
  </div>

  <div
    v-else-if="questionnaire"
    class="mx-auto max-w-3xl space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <h1 class="text-2xl font-bold sm:text-3xl">
        {{ questionnaire.title }}
      </h1>

      <p
        v-if="questionnaire.description"
        class="text-base-content/60 mt-2"
      >
        {{ questionnaire.description }}
      </p>

      <div
        v-if="isPatient"
        class="mt-5"
      >
        <div class="mb-2 flex justify-between text-sm">
          <span>
            Заполнено {{ answeredCount }} из
            {{ questionnaire.questions.length }}
          </span>

          <strong>{{ progress }}%</strong>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="progress"
          max="100"
        />
      </div>
    </header>

    <MediaEntityEditor
      v-if="canManageImage"
      purpose="questionnaire"
      :entity-id="questionnaire.id"
      @saved="questionnaire.image_id = $event.image_id"
    />

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <section class="space-y-4">
      <article
        v-for="(question, index) in questionnaire.questions"
        :id="`question-${question.id}`"
        :key="question.id"
        class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-6"
      >
        <div class="mb-5 flex items-start gap-3">
          <div
            class="bg-primary text-primary-content flex size-8 shrink-0 items-center justify-center rounded-full text-sm font-bold"
          >
            {{ index + 1 }}
          </div>

          <div class="min-w-0 flex-1">
            <h2 class="font-semibold sm:text-lg">
              {{ question.text }}
            </h2>

            <span
              v-if="question.is_required"
              class="text-error text-xs"
            >
              Обязательный вопрос
            </span>
          </div>

          <span
            v-if="savingQuestions[question.id]"
            class="loading loading-spinner loading-xs"
          />
        </div>

        <QuestionnairesQuestionField
          v-if="isPatient"
          v-model="answers[question.id]"
          :question="question"
          @update:model-value="scheduleAnswerSave(question)"
        />

        <div
          v-else
          class="text-base-content/60 text-sm"
        >
          <ul
            v-if="question.options?.length"
            class="list-inside list-disc space-y-1"
          >
            <li
              v-for="option in question.options"
              :key="option.id"
            >
              {{ option.text }}
            </li>
          </ul>

          <p
            v-else-if="question.question_type === 'scale'"
          >
            Шкала:
            {{ question.scale_min }}–{{ question.scale_max }}
          </p>

          <p v-else>
            Тип ответа: {{ question.question_type }}
          </p>
        </div>
      </article>
    </section>

    <div
      v-if="isPatient"
      class="bg-base-100 border-base-300 sticky bottom-3 rounded-2xl border p-3 shadow-xl"
    >
      <button
        type="button"
        class="btn btn-primary w-full"
        :disabled="completing"
        @click="complete"
      >
        <span
          v-if="completing"
          class="loading loading-spinner loading-sm"
        />

        Завершить опросник
      </button>
    </div>
  </div>
</template>