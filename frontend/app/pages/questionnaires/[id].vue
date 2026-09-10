<!-- ./frontend/app/pages/questionnaires/[id].vue -->
<script setup>
definePageMeta({
  key: route => route.fullPath,
})

const route = useRoute()
const store = useQuestionnairesStore()
const context = useProgramContext()

const questionnaireId = String(route.params.id)

// Контекст фиксируется для экземпляра страницы.
// При смене fullPath Nuxt создаёт новый экземпляр.
const programId = context.programId.value
const programStageId = context.stageId.value

const isProgramQuestionnaire = Boolean(
  programId && programStageId,
)

const questionnaire = ref(null)
const submissionId = ref(null)

const answers = reactive({})
const savingQuestions = reactive({})

const loading = ref(true)
const completing = ref(false)
const leaving = ref(false)
const completed = ref(false)

const errorMessage = ref('')

const saveTimers = new Map()
const revisions = new Map()
const savedRevisions = new Map()

let saveQueue = Promise.resolve()
let disposed = false
let submissionCompleted = false

function errorText(error, fallback) {
  return typeof error?.data?.detail === 'string'
    ? error.data.detail
    : fallback
}

function hasAnswer(value) {
  return value !== undefined
    && value !== null
    && value !== ''
}

const answeredCount = computed(() =>
  questionnaire.value?.questions.filter(
    question => hasAnswer(answers[question.id]),
  ).length || 0,
)

const progress = computed(() => {
  const total = questionnaire.value?.questions.length || 0

  return total
    ? Math.round(answeredCount.value / total * 100)
    : 0
})

async function initialize() {
  loading.value = true
  errorMessage.value = ''

  try {
    const response = await store.fetchQuestionnaire(
      questionnaireId,
      {
        programId,
        programStageId,
      },
    )

    if (disposed) return

    questionnaire.value = response

    const allProgress = await store.fetchMyProgress()

    if (disposed) return

    const existing = allProgress.find(
      item =>
        item.questionnaire_id === questionnaireId
        && item.status === 'in_progress'
        && (
          isProgramQuestionnaire
            ? (
                item.program_id === programId
                && item.program_stage_id === programStageId
              )
            : (
                !item.program_id
                && !item.program_stage_id
              )
        ),
    )

    if (existing) {
      const submission = await store.fetchSubmission(
        existing.submission_id,
      )

      if (disposed) return

      submissionId.value = existing.submission_id

      for (const answer of submission.answers || []) {
        answers[answer.question_id] = answer.value
      }
    } else {
      const submission = await store.startQuestionnaire(
        questionnaireId,
        {
          programId,
          programStageId,
        },
      )

      if (disposed) return

      submissionId.value = submission.submission_id
    }
  } catch (error) {
    if (!disposed) {
      errorMessage.value = errorText(
        error,
        'Не удалось открыть опросник',
      )
    }
  } finally {
    if (!disposed) {
      loading.value = false
    }
  }
}

function clearSaveTimers() {
  for (const timer of saveTimers.values()) {
    window.clearTimeout(timer)
  }

  saveTimers.clear()
}

function enqueueSave(questionId) {
  const revision = revisions.get(questionId) || 0

  if (
    !submissionId.value
    || submissionCompleted
    || revision <= (savedRevisions.get(questionId) || 0)
  ) {
    return Promise.resolve()
  }

  const currentSubmissionId = submissionId.value
  const rawValue = answers[questionId]

  // Снимок не должен измениться, пока запрос ждёт очереди.
  const value = rawValue === undefined
    ? null
    : JSON.parse(JSON.stringify(rawValue))

  const operation = saveQueue.then(async () => {
    savingQuestions[questionId] = true

    try {
      await store.saveAnswer(
        currentSubmissionId,
        questionId,
        value,
      )

      savedRevisions.set(questionId, revision)
    } finally {
      savingQuestions[questionId] = false
    }
  })

  // Ошибка конкретного запроса не блокирует всю очередь.
  // Вызывающий код при этом получает отклонённый operation.
  saveQueue = operation.catch(() => {})

  return operation
}

function scheduleAnswerSave(question) {
  if (
    completing.value
    || leaving.value
    || submissionCompleted
    || !submissionId.value
  ) {
    return
  }

  const questionId = question.id

  revisions.set(
    questionId,
    (revisions.get(questionId) || 0) + 1,
  )

  window.clearTimeout(saveTimers.get(questionId))

  const timer = window.setTimeout(() => {
    saveTimers.delete(questionId)

    void enqueueSave(questionId).catch(error => {
      if (!disposed) {
        errorMessage.value = errorText(
          error,
          'Не удалось сохранить ответ. Перед выходом сохранение будет повторено.',
        )
      }
    })
  }, 500)

  saveTimers.set(questionId, timer)
}

async function flushAnswers() {
  clearSaveTimers()

  // Сначала завершаем уже отправленные сохранения.
  await saveQueue

  // Затем сохраняем актуальные версии, включая ответы,
  // debounce которых ещё не успел сработать.
  for (const [questionId, revision] of revisions) {
    if (revision > (savedRevisions.get(questionId) || 0)) {
      await enqueueSave(questionId)
    }
  }
}

async function complete() {
  if (
    completing.value
    || leaving.value
    || !questionnaire.value
    || !submissionId.value
  ) {
    return
  }

  errorMessage.value = ''

  const missingRequired = questionnaire.value.questions.find(
    question =>
      question.is_required
      && !hasAnswer(answers[question.id]),
  )

  if (missingRequired) {
    errorMessage.value =
      `Ответьте на обязательный вопрос: ${missingRequired.text}`

    document
      .getElementById(`question-${missingRequired.id}`)
      ?.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      })

    return
  }

  completing.value = true

  try {
    // После completeSubmission не должны приходить
    // запоздалые запросы автосохранения.
    await flushAnswers()

    const payload = questionnaire.value.questions
      .filter(question => answers[question.id] !== undefined)
      .map(question => ({
        question_id: question.id,
        value: answers[question.id],
      }))

    await store.completeSubmission(
      submissionId.value,
      payload,
    )

    submissionCompleted = true

    if (isProgramQuestionnaire) {
      await navigateTo({
        path: `/programs/${programId}`,
        query: {
          stage: programStageId,
        },
      })

      return
    }

    completed.value = true
  } catch (error) {
    errorMessage.value = errorText(
      error,
      'Не удалось завершить опросник',
    )
  } finally {
    completing.value = false
  }
}

async function persistBeforeNavigation() {
  if (submissionCompleted) return true

  if (completing.value || leaving.value) {
    return false
  }

  if (!submissionId.value) return true

  leaving.value = true

  try {
    await flushAnswers()
    return true
  } catch (error) {
    errorMessage.value = errorText(
      error,
      'Не удалось сохранить ответы. Проверьте соединение и повторите переход.',
    )

    return false
  } finally {
    leaving.value = false
  }
}

onBeforeRouteLeave(persistBeforeNavigation)
onBeforeRouteUpdate(persistBeforeNavigation)

onMounted(initialize)

onBeforeUnmount(() => {
  disposed = true
  clearSaveTimers()
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

      <div class="mt-5">
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
        class="bg-base-100 border-base-300 scroll-mt-24 rounded-2xl border p-4 sm:p-6"
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

        <fieldset :disabled="completing || leaving || !submissionId">
          <QuestionnairesQuestionField
            v-model="answers[question.id]"
            :question="question"
            @update:model-value="scheduleAnswerSave(question)"
          />
        </fieldset>
      </article>
    </section>

    <div
      class="bg-base-100 border-base-300 sticky bottom-3 rounded-2xl border p-3 shadow-xl"
    >
      <button
        type="button"
        class="btn btn-primary w-full"
        :disabled="completing || leaving || !submissionId"
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