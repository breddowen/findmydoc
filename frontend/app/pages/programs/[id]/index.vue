<!-- ./frontend/app/pages/programs/[id]/index.vue -->
<script setup>
definePageMeta({
  key: route => String(route.params.id),
})

const auth = useAuthStore()
const context = useProgramContext()
const store = useProgramJourneyStore()

const {
  program,
  stages,
  started,
  selectedStage,
  nextStage,
  completedStageCount,
  isStageCompleted,
  selectStage,
} = useProgramJourney()

const {
  getPurchaseActionLabel,
} = useProgramPrice()

const descriptionExpanded = ref(false)
const purchaseDialogOpen = ref(false)
const message = ref('')

const isPatient = computed(() =>
  auth.activeRole === 'patient',
)

const selectedStageCompleted = computed(() =>
  isStageCompleted(selectedStage.value),
)

const purchaseActionLabel = computed(() =>
  getPurchaseActionLabel(program.value),
)

const taskItems = computed(() =>
  (selectedStage.value?.items || []).filter(
    item => ['article', 'questionnaire'].includes(item.item_type),
  ),
)

const freePartCompleted = computed(() => {
  if (!started.value || selectedStageCompleted.value) {
    return false
  }

  const freeItems = taskItems.value.filter(
    item => !item.pro_content,
  )

  const lockedUnfinishedItems = taskItems.value.filter(
    item =>
      item.pro_content
      && !item.can_access
      && !item.is_completed,
  )

  return freeItems.length > 0
    && freeItems.every(item => item.is_completed)
    && lockedUnfinishedItems.length > 0
})

function requestPurchase() {
  if (!program.value) return

  if (program.value.purchase_requested) {
    message.value = 'Запрос уже отправлен медицинскому ассистенту.'
    return
  }

  purchaseDialogOpen.value = true
}

function handlePurchaseRequested({ programId, response }) {
  store.markPurchaseRequested(programId)

  if (program.value?.id === programId) {
    message.value = response.message
  }
}

function reload() {
  if (context.programId.value) {
    void store.load(context.programId.value).catch(() => {})
  }
}
</script>

<template>
  <ProgramsStaffOverview v-if="!isPatient" />

  <div v-else class="space-y-6">
    <UiContentSkeleton
      v-if="store.loading"
      variant="card"
      :count="2"
    />

    <div
      v-if="store.errorMessage"
      class="alert alert-error"
      role="alert"
    >
      <span>{{ store.errorMessage }}</span>

      <button
        type="button"
        class="btn btn-sm"
        @click="reload"
      >
        Повторить
      </button>
    </div>

    <template v-if="program">
      <header>
        <p class="text-base-content/50 text-xs font-medium uppercase tracking-wide">
          Программа
        </p>

        <h1 class="mt-1 text-xl font-bold sm:text-3xl">
          {{ program.title }}
        </h1>

        <div
          v-if="program.description"
          class="mt-2 flex items-start gap-2"
        >
          <p
            id="program-description"
            class="text-base-content/65 min-w-0 flex-1 text-sm leading-relaxed sm:text-base"
            :class="{
              'line-clamp-1 sm:line-clamp-none': !descriptionExpanded,
            }"
          >
            {{ program.description }}
          </p>

          <button
            type="button"
            class="text-primary shrink-0 py-0.5 text-xs font-medium sm:hidden"
            aria-controls="program-description"
            :aria-expanded="descriptionExpanded"
            @click="descriptionExpanded = !descriptionExpanded"
          >
            {{ descriptionExpanded ? 'Свернуть' : 'Подробнее' }}
          </button>
        </div>

        <template v-if="started">
          <div class="text-base-content/60 mt-5 flex flex-wrap justify-between gap-2 text-xs">
            <span>
              Выполнено этапов:
              {{ completedStageCount }} из {{ stages.length }}
            </span>

            <span>
              Общий прогресс: {{ program.progress_percent }}%
            </span>
          </div>

          <ProgramsJourneySteps
            class="mt-2"
            :stages="stages"
            :selected-id="selectedStage?.id"
            :started="started"
            @select="selectStage"
          />
        </template>
      </header>

      <div
        v-if="message"
        class="alert alert-success"
        role="status"
      >
        <Icon name="lucide:circle-check" class="size-5" />
        <span>{{ message }}</span>
      </div>

      <section
        v-if="!started"
        class="border-base-300 rounded-2xl border border-dashed p-5 sm:p-7"
      >
        <Icon name="lucide:route" class="text-primary size-8" />

        <h2 class="mt-3 text-lg font-semibold">
          Двигайтесь по программе шаг за шагом
        </h2>

        <p class="text-base-content/65 mt-2 max-w-2xl text-sm">
          Нажмите «Начать программу» в верхней панели.
          Затем читайте статьи и заполняйте опросники:
          выполненные этапы будут отмечаться галочкой.
        </p>

        <p
          v-if="program.service"
          class="text-base-content/60 mt-3 text-sm"
        >
          Бесплатные материалы можно проходить без покупки.
          Для материалов Pro нужен индивидуальный доступ.
        </p>
      </section>

      <template v-else-if="selectedStage">
        <ProgramsViewerStage
          :stage="selectedStage"
          :program-id="program.id"
          :is-patient="true"
          guided
          :purchase-label="purchaseActionLabel"
          :purchase-requested="Boolean(program.purchase_requested)"
          @purchase="requestPurchase"
        />

        <section
          class="border-base-300 flex flex-col gap-4 rounded-2xl border p-4 sm:flex-row sm:items-center sm:justify-between"
          :class="{
            'border-success/30 bg-success/5': selectedStageCompleted,
          }"
        >
          <div class="flex items-start gap-3">
            <Icon
              :name="
                selectedStageCompleted
                  ? 'lucide:circle-check'
                  : freePartCompleted
                    ? 'lucide:lock-keyhole'
                    : 'lucide:route'
              "
              class="mt-0.5 size-5 shrink-0"
              :class="selectedStageCompleted ? 'text-success' : 'text-primary'"
            />

            <div>
              <p class="font-semibold">
                {{
                  selectedStageCompleted
                    ? 'Все задания этапа выполнены'
                    : freePartCompleted
                      ? 'Бесплатные материалы этапа выполнены'
                      : 'Проходите программу в своём темпе'
                }}
              </p>

              <p class="text-base-content/65 mt-1 text-sm">
                {{
                  selectedStageCompleted
                    ? nextStage
                      ? 'Можно переходить к следующему этапу.'
                      : 'Это последний этап. Свой путь по программе можно посмотреть выше.'
                    : freePartCompleted
                      ? 'В этапе остаются Pro-материалы. При этом другие этапы можно просматривать.'
                      : 'Вы можете открыть другой этап и вернуться к невыполненным заданиям позже.'
                }}
              </p>
            </div>
          </div>

          <button
            v-if="nextStage"
            type="button"
            class="btn shrink-0"
            :class="selectedStageCompleted ? 'btn-primary' : 'btn-outline'"
            @click="selectStage(nextStage.id)"
          >
            Следующий этап
            <Icon name="lucide:arrow-right" class="size-4" />
          </button>
        </section>
      </template>

      <PatientPurchaseDialog
        v-model="purchaseDialogOpen"
        :program="program"
        @requested="handlePurchaseRequested"
      />
    </template>
  </div>
</template>