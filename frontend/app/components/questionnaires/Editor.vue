<!-- ./frontend/app/components/questionnaires/Editor.vue -->
<script setup>
const route = useRoute()
const { $api } = useNuxtApp()
const store = useQuestionnairesStore()

const saving = ref(false)
const loading = ref(false)
const loadingTags = ref(false)

const tags = ref([])

const importOpen = ref(false)
const errorMessage = ref('')

const form = reactive(createEmptyForm())

function createEmptyQuestion() {
  return {
    client_id: crypto.randomUUID(),
    question_type: 'text',
    text: '',
    is_required: true,
    order_index: 0,

    scale_min: null,
    scale_max: null,
    scale_min_label: null,
    scale_max_label: null,

    options: [],
  }
}

function createEmptyForm() {
  return {
    title: '',
    description: '',
    pro_content: true,
    tag_ids: [],
    copied_from_id: null,
    questions: [
      createEmptyQuestion(),
    ],
  }
}

function applyForm(data) {
  form.title = data.title || ''
  form.description = data.description || ''
  form.pro_content = data.pro_content !== false
  form.tag_ids = data.tag_ids || []
  form.copied_from_id =
    data.copied_from_id || null

  form.questions = (data.questions || []).map(
    (question, questionIndex) => ({
      client_id:
        question.client_id
        || crypto.randomUUID(),

      question_type: question.question_type,
      text: question.text || '',
      is_required:
        question.is_required !== false,
      order_index: questionIndex,

      scale_min: question.scale_min ?? null,
      scale_max: question.scale_max ?? null,
      scale_min_label:
        question.scale_min_label ?? null,
      scale_max_label:
        question.scale_max_label ?? null,

      options: (question.options || []).map(
        (option, optionIndex) => ({
          client_id:
            option.client_id
            || crypto.randomUUID(),
          text: option.text || '',
          order_index: optionIndex,
        }),
      ),
    }),
  )

  if (!form.questions.length) {
    form.questions = [
      createEmptyQuestion(),
    ]
  }
}

async function loadTags() {
  loadingTags.value = true

  try {
    tags.value = await $api('/api/v1/tags')
  } finally {
    loadingTags.value = false
  }
}

async function loadCopySource() {
  const sourceId = route.query.copy

  if (typeof sourceId !== 'string') return

  loading.value = true

  try {
    const source =
      await store.fetchQuestionnaire(sourceId)

    applyForm({
      title: `${source.title} — копия`,
      description: source.description,
      pro_content: source.pro_content,
      tag_ids: source.tags.map((tag) => tag.id),
      copied_from_id: source.id,
      questions: source.questions,
    })
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить исходный опросник'
  } finally {
    loading.value = false
  }
}

function addQuestion() {
  const question = createEmptyQuestion()
  question.order_index = form.questions.length

  form.questions.push(question)
}

function removeQuestion(index) {
  if (form.questions.length === 1) {
    errorMessage.value =
      'Опросник должен содержать хотя бы один вопрос'
    return
  }

  form.questions.splice(index, 1)
  reindexQuestions()
}

function moveQuestion(index, direction) {
  const targetIndex = index + direction

  if (
    targetIndex < 0
    || targetIndex >= form.questions.length
  ) {
    return
  }

  const temporary = form.questions[index]
  form.questions[index] = form.questions[targetIndex]
  form.questions[targetIndex] = temporary

  reindexQuestions()
}

function reindexQuestions() {
  form.questions.forEach((question, index) => {
    question.order_index = index

    question.options.forEach((option, optionIndex) => {
      option.order_index = optionIndex
    })
  })
}

function validateForm() {
  if (!form.title.trim()) {
    return 'Введите название опросника'
  }

  if (!form.questions.length) {
    return 'Добавьте хотя бы один вопрос'
  }

  for (
    let index = 0;
    index < form.questions.length;
    index += 1
  ) {
    const question = form.questions[index]

    if (!question.text.trim()) {
      return `Введите текст вопроса №${index + 1}`
    }

    if (
      [
        'single_choice',
        'multiple_choice',
      ].includes(question.question_type)
    ) {
      if (question.options.length < 2) {
        return (
          `У вопроса №${index + 1} должно быть `
          + 'не менее двух вариантов'
        )
      }

      if (
        question.options.some(
          (option) => !option.text.trim(),
        )
      ) {
        return (
          `Заполните варианты ответа `
          + `в вопросе №${index + 1}`
        )
      }
    }

    if (
      question.question_type === 'scale'
      && question.scale_max <= question.scale_min
    ) {
      return (
        `В вопросе №${index + 1} максимум `
        + 'должен быть больше минимума'
      )
    }
  }

  return null
}

function buildPayload() {
  reindexQuestions()

  return {
    title: form.title.trim(),
    description:
      form.description.trim() || null,
    pro_content: form.pro_content,
    tag_ids: form.tag_ids,
    copied_from_id: form.copied_from_id,

    questions: form.questions.map(
      (question, questionIndex) => ({
        question_type: question.question_type,
        text: question.text.trim(),
        is_required: question.is_required,
        order_index: questionIndex,

        scale_min:
          question.question_type === 'scale'
            ? question.scale_min
            : null,

        scale_max:
          question.question_type === 'scale'
            ? question.scale_max
            : null,

        scale_min_label:
          question.question_type === 'scale'
            ? question.scale_min_label || null
            : null,

        scale_max_label:
          question.question_type === 'scale'
            ? question.scale_max_label || null
            : null,

        options: [
          'single_choice',
          'multiple_choice',
        ].includes(question.question_type)
          ? question.options.map(
              (option, optionIndex) => ({
                text: option.text.trim(),
                order_index: optionIndex,
              }),
            )
          : [],
      }),
    ),
  }
}

async function save() {
  errorMessage.value = validateForm() || ''

  if (errorMessage.value) return

  saving.value = true

  try {
    const questionnaire =
      await store.createQuestionnaire(
        buildPayload(),
      )

    await navigateTo('/content/questionnaires')
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось создать опросник'
  } finally {
    saving.value = false
  }
}

function handleImport(data) {
  applyForm(data)
  errorMessage.value = ''
}

function downloadJson() {
  const payload = buildPayload()

  const blob = new Blob(
    [
      JSON.stringify(payload, null, 2),
    ],
    {
      type: 'application/json',
    },
  )

  const url = URL.createObjectURL(blob)
  const anchor = document.createElement('a')

  anchor.href = url
  anchor.download = 'questionnaire.json'
  anchor.click()

  URL.revokeObjectURL(url)
}

onMounted(async () => {
  await Promise.all([
    loadTags(),
    loadCopySource(),
  ])
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Новый опросник
        </h1>

        <p class="text-base-content/60 mt-1">
          После сохранения опросник нельзя редактировать.
        </p>
      </div>

      <div class="flex flex-col gap-2 sm:flex-row">
        <button
          type="button"
          class="btn btn-outline"
          @click="downloadJson"
        >
          <Icon
            name="lucide:download"
            class="size-4"
          />
          Скачать JSON
        </button>

        <button
          type="button"
          class="btn btn-outline"
          @click="importOpen = true"
        >
          <Icon
            name="lucide:upload"
            class="size-4"
          />
          Загрузить JSON
        </button>
      </div>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <div
      v-if="loading"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <template v-else>
      <section
        class="bg-base-100 border-base-300 space-y-5 rounded-2xl border p-4 sm:p-6"
      >
        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Название
          </span>

          <input
            v-model="form.title"
            type="text"
            maxlength="300"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Описание
          </span>

          <textarea
            v-model="form.description"
            class="textarea textarea-bordered min-h-28 w-full"
          />
        </label>

        <div>
          <p class="mb-3 font-medium">
            Теги
          </p>

          <ContentTagSelector
            v-model="form.tag_ids"
            :tags="tags"
            :loading="loadingTags"
          />
        </div>

        <label
          class="border-base-300 flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4"
        >
          <span>
            <span class="block font-medium">
              Профессиональный контент
            </span>

            <span
              class="text-base-content/60 text-sm"
            >
              Требует доступа Pro.
            </span>
          </span>

          <input
            v-model="form.pro_content"
            type="checkbox"
            class="toggle toggle-primary"
          >
        </label>
      </section>

      <section class="space-y-4">
        <QuestionnairesQuestionItem
          v-for="(question, index) in form.questions"
          :key="question.client_id"
          v-model="form.questions[index]"
          :index="index"
          :total="form.questions.length"
          @remove="removeQuestion(index)"
          @move-up="moveQuestion(index, -1)"
          @move-down="moveQuestion(index, 1)"
        />

        <button
          type="button"
          class="btn btn-outline w-full"
          @click="addQuestion"
        >
          <Icon
            name="lucide:plus"
            class="size-5"
          />
          Добавить вопрос
        </button>
      </section>

      <div
        class="flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
      >
        <NuxtLink
          to="/content/questionnaires"
          class="btn"
        >
          Отмена
        </NuxtLink>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="saving"
          @click="save"
        >
          <span
            v-if="saving"
            class="loading loading-spinner loading-sm"
          />

          Создать опросник
        </button>
      </div>
    </template>
  </div>

  <QuestionnairesJsonImporter
    v-model="importOpen"
    @import="handleImport"
  />
</template>