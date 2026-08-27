<!-- ./frontend/app/components/assignments/CreateDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
  patientName: {
    type: String,
    default: '',
  },
})

const emit = defineEmits([
  'assigned',
])

const { $api } = useNuxtApp()
const assignmentsStore = useAssignmentsStore()

const activeTab = ref('article')
const selectedContentId = ref(null)

const articles = ref([])
const questionnaires = ref([])

const loadingContent = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

const tabs = [
  {
    value: 'article',
    title: 'Статьи',
    icon: 'lucide:file-text',
  },
  {
    value: 'questionnaire',
    title: 'Опросники',
    icon: 'lucide:clipboard-list',
  },
]

const assignedArticleIds = computed(() =>
  assignmentsStore.patientAssignments
    .filter(
      (assignment) =>
        assignment.assignment_type === 'article'
        && assignment.status !== 'cancelled',
    )
    .map((assignment) => assignment.content_id),
)

const assignedQuestionnaireIds = computed(() =>
  assignmentsStore.patientAssignments
    .filter(
      (assignment) =>
        assignment.assignment_type
          === 'questionnaire'
        && assignment.status !== 'cancelled',
    )
    .map((assignment) => assignment.content_id),
)

const selectedItem = computed(() => {
  const source =
    activeTab.value === 'article'
      ? articles.value
      : questionnaires.value

  return source.find(
    (item) => item.id === selectedContentId.value,
  )
})

async function loadData() {
  loadingContent.value = true
  errorMessage.value = ''

  try {
    const [
      articleItems,
      questionnaireItems,
    ] = await Promise.all([
      $api('/api/v1/articles'),
      $api('/api/v1/questionnaires'),
      assignmentsStore.fetchPatientAssignments(
        props.patientId,
      ),
    ])

    articles.value = articleItems
    questionnaires.value = questionnaireItems
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить контент'
  } finally {
    loadingContent.value = false
  }
}

async function assignContent() {
  if (!selectedContentId.value) return

  errorMessage.value = ''
  successMessage.value = ''

  const payload = {
    patient_id: props.patientId,
    assignment_type: activeTab.value,

    article_id:
      activeTab.value === 'article'
        ? selectedContentId.value
        : null,

    questionnaire_id:
      activeTab.value === 'questionnaire'
        ? selectedContentId.value
        : null,
  }

  try {
    const assignment =
      await assignmentsStore.createAssignment(
        payload,
      )

    successMessage.value =
      `Назначено: ${assignment.title}`

    selectedContentId.value = null

    emit('assigned', assignment)

    window.setTimeout(() => {
      model.value = false
    }, 600)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось назначить контент'
  }
}

function resetDialog() {
  activeTab.value = 'article'
  selectedContentId.value = null
  successMessage.value = ''
  errorMessage.value = ''
}

watch(activeTab, () => {
  selectedContentId.value = null
  successMessage.value = ''
  errorMessage.value = ''
})

watch(model, async (opened) => {
  if (!opened) {
    resetDialog()
    return
  }

  await loadData()
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Назначить контент"
    max-width-class="max-w-4xl"
  >
    <div class="space-y-5">
      <div
        v-if="patientName"
        class="bg-base-200 flex items-center gap-3 rounded-2xl p-4"
      >
        <div
          class="bg-primary/10 text-primary flex size-10 shrink-0 items-center justify-center rounded-xl"
        >
          <Icon
            name="lucide:user-round"
            class="size-5"
          />
        </div>

        <div class="min-w-0">
          <p class="text-base-content/50 text-xs">
            Пациент
          </p>

          <p class="truncate font-medium">
            {{ patientName }}
          </p>
        </div>
      </div>

      <div
        role="tablist"
        class="tabs tabs-box w-full"
      >
        <button
          v-for="tab in tabs"
          :key="tab.value"
          type="button"
          role="tab"
          class="tab flex-1 gap-2"
          :class="{
            'tab-active':
              activeTab === tab.value,
          }"
          @click="activeTab = tab.value"
        >
          <Icon
            :name="tab.icon"
            class="size-4"
          />

          {{ tab.title }}

          <span
            class="badge badge-sm"
            :class="{
              'badge-primary':
                activeTab === tab.value,
            }"
          >
            {{
              tab.value === 'article'
                ? articles.length
                : questionnaires.length
            }}
          </span>
        </button>
      </div>

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
        v-if="successMessage"
        class="alert alert-success"
      >
        <Icon
          name="lucide:circle-check"
          class="size-5"
        />
        <span>{{ successMessage }}</span>
      </div>

      <AssignmentsContentPicker
        v-if="activeTab === 'article'"
        v-model="selectedContentId"
        :items="articles"
        :assigned-content-ids="assignedArticleIds"
        :loading="loadingContent"
        content-type="article"
      />

      <AssignmentsContentPicker
        v-else
        v-model="selectedContentId"
        :items="questionnaires"
        :assigned-content-ids="
          assignedQuestionnaireIds
        "
        :loading="loadingContent"
        content-type="questionnaire"
      />
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:items-center sm:justify-between"
      >
        <p
          class="text-base-content/60 min-w-0 truncate text-sm"
        >
          <template v-if="selectedItem">
            Выбрано:
            <strong>
              {{ selectedItem.title }}
            </strong>
          </template>

          <template v-else>
            Выберите материал
          </template>
        </p>

        <div
          class="flex flex-col-reverse gap-2 sm:flex-row"
        >
          <button
            type="button"
            class="btn"
            :disabled="assignmentsStore.creating"
            @click="model = false"
          >
            Отмена
          </button>

          <button
            type="button"
            class="btn btn-primary"
            :disabled="
              !selectedContentId
              || assignmentsStore.creating
            "
            @click="assignContent"
          >
            <span
              v-if="assignmentsStore.creating"
              class="loading loading-spinner loading-sm"
            />

            <Icon
              v-else
              name="lucide:send"
              class="size-4"
            />

            Назначить
          </button>
        </div>
      </div>
    </template>
  </UiResponsiveDialog>
</template>