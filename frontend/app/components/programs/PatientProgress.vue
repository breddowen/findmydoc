<!-- ./frontend/app/components/programs/PatientProgress.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const loading = ref(true)
const errorMessage = ref('')

const selectedProgramIndex = ref(0)
const selectedStageIndexes = reactive({})

const selectedProgram = computed(
  () =>
    store.patientProgressPrograms[
      selectedProgramIndex.value
    ],
)

function getSelectedStage(program) {
  const index =
    selectedStageIndexes[program.id] || 0

  return program.stages[index]
}

function statusName(program) {
  if (!program.enrollment) {
    if (program.purchase_requested) {
      return 'Запрошена пациентом'
    }

    return 'Доступ открыт, не начата'
  }

  if (
    program.enrollment.status === 'completed'
  ) {
    return 'Завершена'
  }

  return 'В процессе'
}

onMounted(async () => {
  try {
    await store.fetchPatientProgramProgress(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы пациента'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="2"
  />

  <div
    v-else-if="errorMessage"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="store.patientProgressPrograms.length"
    class="space-y-5"
  >
    <div class="overflow-x-auto pb-1">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(program, index) in store.patientProgressPrograms"
          :key="program.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedProgramIndex === index,
          }"
          @click="selectedProgramIndex = index"
        >
          <Icon
            name="lucide:route"
            class="size-4"
          />
          {{ program.title }}
        </button>
      </div>
    </div>

    <template v-if="selectedProgram">
      <header
        class="bg-base-100 border-base-300 rounded-2xl border p-5"
      >
        <div
          class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"
        >
          <div>
            <h2 class="text-xl font-bold">
              {{ selectedProgram.title }}
            </h2>

            <p class="text-base-content/60 text-sm">
              {{ statusName(selectedProgram) }}
            </p>
          </div>

          <span
            class="badge"
            :class="{
              'badge-warning':
                selectedProgram.purchase_requested,
              'badge-success':
                selectedProgram.enrollment?.status
                  === 'completed',
              'badge-primary':
                selectedProgram.enrollment?.status
                  === 'active',
            }"
          >
            {{ selectedProgram.progress_percent }}%
          </span>
        </div>

        <progress
          class="progress progress-primary mt-4 w-full"
          :value="selectedProgram.progress_percent"
          max="100"
        />
      </header>

      <div class="overflow-x-auto pb-1">
        <div class="join">
          <button
            v-for="(stage, index) in selectedProgram.stages"
            :key="stage.id"
            type="button"
            class="btn join-item btn-sm"
            :class="{
              'btn-primary':
                (selectedStageIndexes[
                  selectedProgram.id
                ] || 0) === index,
            }"
            @click="
              selectedStageIndexes[
                selectedProgram.id
              ] = index
            "
          >
            <Icon
              :name="
                stage.status === 'completed'
                  ? 'lucide:circle-check'
                  : stage.status === 'overdue'
                    ? 'lucide:triangle-alert'
                    : 'lucide:circle'
              "
              class="size-4"
            />

            Этап {{ index + 1 }}
          </button>
        </div>
      </div>

      <ProgramsViewerStage
        v-if="getSelectedStage(selectedProgram)"
        :stage="getSelectedStage(selectedProgram)"
        :program-id="selectedProgram.id"
        :patient-id="patientId"
        :is-patient="false"
        />
    </template>
  </div>

  <div
    v-else
    class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:route-off"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Пациент пока не начал и не приобретал программы
    </p>
  </div>
</template>