<!-- ./frontend/app/pages/programs/[id]/index.vue -->
<script setup>
const route = useRoute()
const auth = useAuthStore()
const store = useProgramsStore()

const selectedStageIndex = ref(0)

const {
  formatOriginalPrice,
  formatFinalPrice,
} = useProgramPrice()

const loading = ref(true)
const starting = ref(false)
const requestingPurchase = ref(false)

const message = ref('')
const errorMessage = ref('')

const program = computed(
  () => store.currentProgram,
)

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

const selectedStage = computed(
  () => program.value?.stages[
    selectedStageIndex.value
  ],
)

async function loadProgram() {
  loading.value = true

  try {
    if (isPatient.value) {
      await store.fetchProgramForPatient(
        route.params.id,
      )

      // Если вернулись из опросника программы,
      // открываем тот же этап.
      const requestedStageId =
        typeof route.query.stage === 'string'
          ? route.query.stage
          : null

      if (requestedStageId) {
        const requestedIndex =
          program.value.stages.findIndex(
            (stage) =>
              stage.id === requestedStageId,
          )

        if (requestedIndex >= 0) {
          selectedStageIndex.value =
            requestedIndex

          return
        }
      }

      // Если конкретный этап не был передан,
      // выбираем текущий активный этап.
      const preferredIndex =
        program.value.stages.findIndex(
          (stage) =>
            [
              'available',
              'in_progress',
              'overdue',
            ].includes(stage.status),
        )

      selectedStageIndex.value =
        preferredIndex >= 0
          ? preferredIndex
          : 0
    } else {
      await store.fetchProgramForStaff(
        route.params.id,
      )
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программу'
  } finally {
    loading.value = false
  }
}

async function startProgram() {
  starting.value = true
  errorMessage.value = ''

  try {
    await store.startProgram(program.value.id)
    message.value = 'Программа начата'

    await loadProgram()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось начать программу'
  } finally {
    starting.value = false
  }
}

async function requestPurchase() {
  if (program.value.purchase_requested) {
    message.value =
      'Запрос уже отправлен медицинскому ассистенту.'
    return
  }

  requestingPurchase.value = true
  errorMessage.value = ''

  try {
    const response = await store.requestPurchase(
      program.value.id,
    )

    program.value.purchase_requested = true
    message.value = response.message
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось отправить запрос'
  } finally {
    requestingPurchase.value = false
  }
}

onMounted(loadProgram)
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="3"
  />

  <div
    v-else-if="errorMessage && !program"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="program"
    class="space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <div
        class="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between"
      >
        <div class="min-w-0 flex-1">
          <div
                class="flex flex-wrap items-center gap-2"
                >
                <span class="text-primary text-2xl font-bold">
                    {{ formatFinalPrice(program) }}
                </span>

                <span
                    v-if="program.discount_percent"
                    class="text-base-content/40 line-through"
                >
                    {{ formatOriginalPrice(program) }}
                </span>

                <span
                    v-if="program.discount_percent"
                    class="badge badge-error font-bold"
                >
                    −{{ program.discount_percent }}%
                </span>

                <span
                    v-if="program.is_popular"
                    class="badge badge-warning gap-1"
                >
                    <Icon
                    name="lucide:flame"
                    class="size-3"
                    />

                    Популярное
                </span>

                <span
                    v-if="program.has_program_access"
                    class="badge badge-success"
                >
                    Полный доступ
                </span>
                </div>

          <h1
            class="mt-3 text-3xl font-bold sm:text-4xl"
          >
            {{ program.title }}
          </h1>

          <p
            v-if="program.description"
            class="text-base-content/70 mt-3 max-w-3xl"
          >
            {{ program.description }}
          </p>

          <div class="mt-4 flex flex-wrap gap-1">
            <span
              v-for="tag in program.tags"
              :key="tag.id"
              class="badge badge-outline"
            >
              {{ tag.name }}
            </span>
          </div>
        </div>

        <div class="flex flex-col gap-2 sm:flex-row">
          <NuxtLink
            v-if="canManage"
            :to="`/programs/${program.id}/edit`"
            class="btn btn-outline"
          >
            <Icon
              name="lucide:pencil"
              class="size-4"
            />
            Редактировать
          </NuxtLink>

          <button
            v-if="
              isPatient
              && !program.enrollment
            "
            type="button"
            class="btn btn-primary"
            :disabled="starting"
            @click="startProgram"
          >
            <span
              v-if="starting"
              class="loading loading-spinner loading-sm"
            />

            Начать программу
          </button>
        </div>
      </div>

      <div
        v-if="isPatient && program.enrollment"
        class="mt-6"
      >
        <div class="mb-2 flex justify-between text-sm">
          <span>
            Общий прогресс
          </span>

          <strong>
            {{ program.progress_percent }}%
          </strong>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="program.progress_percent"
          max="100"
        />

        <p class="text-base-content/50 mt-2 text-xs">
          День программы:
          {{ program.enrollment.elapsed_days }}
        </p>
      </div>
    </header>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div class="overflow-x-auto pb-2">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(stage, index) in program.stages"
          :key="stage.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedStageIndex === index,
          }"
          @click="selectedStageIndex = index"
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
        v-if="selectedStage"
        :stage="selectedStage"
        :program-id="program.id"
        :is-patient="isPatient"
        @purchase="requestPurchase"
        />
  </div>
</template>