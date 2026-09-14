<!-- ./frontend/app/components/programs/ConsultationsDialog.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  programId: {
    type: String,
    default: null,
  },
})

const emit = defineEmits(['saved'])

const { $api } = useNuxtApp()

const programTitle = ref('')
const stages = ref([])
const specialities = ref([])

const selectedStageId = ref('')
const draft = ref([])

const loaded = ref(false)
const loading = ref(false)
const saving = ref(false)

const errorMessage = ref('')
const message = ref('')

let generation = 0
let controller = null

const busy = computed(
  () => loading.value || saving.value,
)

const selectedStage = computed(
  () => stages.value.find(
    stage => stage.id === selectedStageId.value,
  ) || null,
)

function buildItems(items) {
  return items.map((item) => {
    if (item.item_type !== 'consultation') {
      return {
        id: item.id,
        item_type: item.item_type,
      }
    }

    return {
      id: item.id || null,
      item_type: 'consultation',
      speciality_id: item.speciality_id || null,
      consultation_title:
        item.consultation_title?.trim() || null,
      consultation_description:
        item.consultation_description?.trim() || null,
    }
  })
}

const dirty = computed(() => {
  if (!selectedStage.value) return false

  return JSON.stringify(buildItems(draft.value))
    !== JSON.stringify(
      buildItems(selectedStage.value.items),
    )
})

function resetDraft() {
  draft.value = (selectedStage.value?.items || []).map(
    item => ({
      ...item,
      client_id: item.id,
      consultation_title: item.consultation_title || '',
      consultation_description:
        item.consultation_description || '',
    }),
  )
}

function changeStage() {
  errorMessage.value = ''
  message.value = ''
  resetDraft()
}

function cancelChanges() {
  if (busy.value) return

  resetDraft()
  errorMessage.value = ''
  message.value = ''
}

async function load() {
  if (!props.programId) return

  const version = ++generation
  const programId = props.programId

  controller?.abort()
  controller = new AbortController()

  loading.value = true
  loaded.value = false
  errorMessage.value = ''
  message.value = ''

  try {
    const [program, specialityItems] = await Promise.all([
      $api(
        `/api/v1/programs/manage/${programId}/consultations`,
        {
          signal: controller.signal,
          retry: 0,
        },
      ),
      $api('/api/v1/specialities', {
        signal: controller.signal,
        retry: 0,
      }),
    ])

    if (version !== generation) return

    programTitle.value = program.title
    stages.value = program.stages
    specialities.value = specialityItems

    if (
      !stages.value.some(
        stage => stage.id === selectedStageId.value,
      )
    ) {
      selectedStageId.value = stages.value[0]?.id || ''
    }

    resetDraft()
    loaded.value = true
  } catch (error) {
    if (version !== generation) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось загрузить консультации программы',
    )
  } finally {
    if (version === generation) {
      loading.value = false
    }
  }
}

async function reload() {
  if (busy.value) return

  if (
    dirty.value
    && !window.confirm(
      'Отменить несохранённые изменения и загрузить актуальные данные?',
    )
  ) {
    return
  }

  await load()
}

async function save() {
  if (
    busy.value
    || !selectedStage.value
    || !dirty.value
  ) {
    return
  }

  const items = buildItems(draft.value)

  if (
    items.some(
      item =>
        item.item_type === 'consultation'
        && !item.speciality_id,
    )
  ) {
    errorMessage.value =
      'Выберите специальность для каждой консультации'
    return
  }

  const programId = props.programId
  const stageId = selectedStage.value.id
  const version = generation

  saving.value = true
  errorMessage.value = ''
  message.value = ''

  controller = new AbortController()

  try {
    const response = await $api(
      `/api/v1/programs/manage/${programId}/stages/${stageId}/consultations`,
      {
        method: 'PUT',
        body: {
          expected_revision: selectedStage.value.revision,
          items,
        },
        signal: controller.signal,
        retry: 0,
      },
    )

    if (version !== generation) return

    const index = stages.value.findIndex(
      stage => stage.id === response.id,
    )

    if (index !== -1) {
      stages.value[index] = response
    }

    resetDraft()

    message.value =
      'Консультации этапа сохранены. Изменения общие для всех пациентов.'

    emit('saved', {
      program_id: programId,
      stage_id: stageId,
    })
  } catch (error) {
    if (version !== generation) return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось подтвердить сохранение. Обновите данные.',
    )
  } finally {
    if (version === generation) {
      saving.value = false
    }
  }
}

function requestClose() {
  if (busy.value) return

  if (
    dirty.value
    && !window.confirm('Закрыть без сохранения изменений?')
  ) {
    return
  }

  model.value = false
}

watch(
  [
    () => model.value,
    () => props.programId,
  ],
  ([open]) => {
    if (open && props.programId) {
      stages.value = []
      draft.value = []
      selectedStageId.value = ''
      void load()
      return
    }

    generation += 1
    controller?.abort()

    loading.value = false
    saving.value = false
    loaded.value = false

    stages.value = []
    draft.value = []
  },
)

onBeforeUnmount(() => {
  generation += 1
  controller?.abort()
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Консультации программы"
    max-width-class="max-w-3xl"
    :persistent="busy || dirty"
    :close-on-backdrop="!busy && !dirty"
    :show-close-button="!busy && !dirty"
  >
    <div class="space-y-5">
      <div>
        <h3
          v-if="programTitle"
          class="font-semibold"
        >
          {{ programTitle }}
        </h3>

        <p class="text-base-content/60 mt-2 text-sm">
          Можно менять только консультации.
          Статьи, опросники и результаты пациентов сохраняются.
          Изменения будут видны всем пациентам программы.
        </p>
      </div>

      <div
        v-if="loading"
        class="flex justify-center py-10"
      >
        <span class="loading loading-spinner loading-lg" />
      </div>

      <div
        v-if="errorMessage"
        class="alert alert-error text-sm"
        role="alert"
      >
        {{ errorMessage }}
      </div>

      <div
        v-if="message"
        class="alert alert-success text-sm"
        role="status"
      >
        {{ message }}
      </div>

      <template v-if="loaded">
        <label
          v-if="stages.length"
          class="block"
        >
          <span class="mb-2 block text-sm font-medium">
            Этап программы
          </span>

          <select
            v-model="selectedStageId"
            class="select w-full"
            :disabled="busy || dirty"
            @change="changeStage"
          >
            <option
              v-for="stage in stages"
              :key="stage.id"
              :value="stage.id"
            >
              {{ stage.title }}
            </option>
          </select>

          <span
            v-if="dirty"
            class="text-base-content/60 mt-2 block text-xs"
          >
            Сохраните или отмените изменения перед выбором другого этапа.
          </span>
        </label>

        <ProgramsConsultationsItems
          v-if="selectedStage"
          v-model="draft"
          :specialities="specialities"
          :disabled="busy"
        />

        <p
          v-else
          class="text-base-content/60 text-sm"
        >
          В программе нет этапов.
        </p>
      </template>
    </div>

    <template #footer>
      <div class="flex flex-wrap justify-between gap-2">
        <button
          type="button"
          class="btn btn-ghost btn-sm"
          :disabled="busy"
          @click="reload"
        >
          Обновить данные
        </button>

        <div class="flex flex-wrap gap-2">
          <button
            v-if="dirty"
            type="button"
            class="btn btn-sm"
            :disabled="busy"
            @click="cancelChanges"
          >
            Отменить изменения
          </button>

          <button
            type="button"
            class="btn btn-sm"
            :disabled="busy"
            @click="requestClose"
          >
            Закрыть
          </button>

          <button
            type="button"
            class="btn btn-primary btn-sm"
            :disabled="busy || !dirty || !selectedStage"
            @click="save"
          >
            <span
              v-if="saving"
              class="loading loading-spinner loading-xs"
            />
            Сохранить этап
          </button>
        </div>
      </div>
    </template>
  </UiResponsiveDialog>
</template>