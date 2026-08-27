<!-- ./frontend/app/components/questionnaires/JsonImporter.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const emit = defineEmits([
  'import',
])

const jsonText = ref('')
const errorMessage = ref('')

const supportedTypes = new Set([
  'text',
  'number',
  'boolean',
  'scale',
  'single_choice',
  'multiple_choice',
])

function normalizeQuestionnaire(source) {
  const data = source.questionnaire || source

  if (!data || typeof data !== 'object') {
    throw new Error('JSON должен содержать объект')
  }

  if (
    typeof data.title !== 'string'
    || !data.title.trim()
  ) {
    throw new Error('Поле title обязательно')
  }

  if (!Array.isArray(data.questions)) {
    throw new Error(
      'Поле questions должно быть массивом',
    )
  }

  if (data.questions.length === 0) {
    throw new Error(
      'Опросник должен содержать вопросы',
    )
  }

  const questions = data.questions.map(
    (question, questionIndex) => {
      const questionType = String(
        question.question_type
        || question.type
        || '',
      ).toLowerCase()

      if (!supportedTypes.has(questionType)) {
        throw new Error(
          `Неизвестный тип вопроса №${questionIndex + 1}: ${questionType}`,
        )
      }

      const options = Array.isArray(question.options)
        ? question.options.map(
            (option, optionIndex) => ({
              client_id: crypto.randomUUID(),
              text:
                typeof option === 'string'
                  ? option
                  : String(option.text || ''),
              order_index: optionIndex,
            }),
          )
        : []

      return {
        client_id: crypto.randomUUID(),
        question_type: questionType,
        text: String(question.text || ''),
        is_required:
          question.is_required !== false,
        order_index: questionIndex,

        scale_min:
          questionType === 'scale'
            ? Number(question.scale_min ?? 0)
            : null,

        scale_max:
          questionType === 'scale'
            ? Number(question.scale_max ?? 10)
            : null,

        scale_min_label:
          question.scale_min_label ?? null,

        scale_max_label:
          question.scale_max_label ?? null,

        options,
      }
    },
  )

  return {
    title: data.title.trim(),
    description: data.description || '',
    pro_content: data.pro_content !== false,
    tag_ids: Array.isArray(data.tag_ids)
      ? data.tag_ids
      : [],
    copied_from_id: data.copied_from_id || null,
    questions,
  }
}

function importJson() {
  errorMessage.value = ''

  try {
    const parsed = JSON.parse(jsonText.value)
    const normalized = normalizeQuestionnaire(parsed)

    emit('import', normalized)
    model.value = false
    jsonText.value = ''
  } catch (error) {
    errorMessage.value =
      error?.message
      || 'Не удалось прочитать JSON'
  }
}

async function handleFile(event) {
  errorMessage.value = ''

  const file = event.target.files?.[0]

  if (!file) return

  if (
    !file.name.toLowerCase().endsWith('.json')
    && file.type !== 'application/json'
  ) {
    errorMessage.value =
      'Выберите файл в формате JSON'
    return
  }

  try {
    jsonText.value = await file.text()
  } catch {
    errorMessage.value =
      'Не удалось прочитать файл'
  } finally {
    event.target.value = ''
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Импорт опросника из JSON"
    max-width-class="max-w-3xl"
  >
    <div class="space-y-5">
      <div
        class="border-primary/30 bg-primary/5 rounded-2xl border p-4"
      >
        <div class="flex items-start gap-3">
          <Icon
            name="lucide:info"
            class="text-primary mt-0.5 size-5 shrink-0"
          />

          <div class="text-sm">
            <p class="font-medium">
              Можно загрузить JSON-файл или вставить JSON
              вручную.
            </p>

            <p class="text-base-content/60 mt-1">
              После импорта опросник можно проверить
              и отредактировать перед сохранением.
            </p>
          </div>
        </div>
      </div>

      <label class="form-control block">
        <span class="label">
          <span class="label-text font-medium">
            JSON-файл
          </span>
        </span>

        <input
          type="file"
          accept=".json,application/json"
          class="file-input file-input-bordered w-full"
          @change="handleFile"
        >
      </label>

      <div class="divider">
        ИЛИ
      </div>

      <label class="form-control block">
        <span class="label">
          <span class="label-text font-medium">
            JSON
          </span>
        </span>

        <textarea
          v-model="jsonText"
          class="textarea textarea-bordered min-h-72 w-full font-mono text-sm"
          placeholder="{ ... }"
        />
      </label>

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
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="!jsonText.trim()"
          @click="importJson"
        >
          <Icon
            name="lucide:upload"
            class="size-4"
          />
          Импортировать
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>