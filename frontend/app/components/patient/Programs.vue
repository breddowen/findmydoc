<!-- ./frontend/app/components/patient/Programs.vue -->
<script setup>
const store = usePatientHomeStore()

const initialized = ref(false)
const message = ref('')

const purchaseDialogOpen = ref(false)
const selectedProgramId = ref(null)

const {
  recommendedPrograms,
  groupedAspects,
  unclassifiedPrograms,
} = usePatientProgramGroups(
  () => store.programs,
  () => store.lifeAspects,
)

const selectedProgram = computed(() =>
  store.programs.find(
    program => program.id === selectedProgramId.value,
  ) || null,
)

async function load() {
  initialized.value = false
  message.value = ''

  try {
    await store.load()
  } finally {
    initialized.value = true
  }
}

function requestPurchase(program) {
  if (program.purchase_requested) {
    message.value =
      'Запрос уже отправлен медицинскому ассистенту.'
    return
  }

  selectedProgramId.value = program.id
  purchaseDialogOpen.value = true
}

function handlePurchaseRequested({ programId, response }) {
  const program = store.programs.find(
    item => item.id === programId,
  )

  if (program) {
    program.purchase_requested = true
  }

  message.value =
    response?.message
    || 'Запрос отправлен медицинскому ассистенту.'
}

onMounted(load)
</script>

<template>
  <div class="space-y-8">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Программы
      </h1>

      <p class="text-base-content/60 mt-2 text-sm sm:text-base">
        Сначала — программы, рекомендованные вам.
        Остальные можно выбрать по сферам жизни.
      </p>
    </header>

    <div
      v-if="message"
      class="alert alert-success"
      role="status"
    >
      <Icon name="lucide:circle-check" class="size-5" />
      <span>{{ message }}</span>
    </div>

    <UiContentSkeleton
      v-if="!initialized || store.loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="store.errorMessage"
      class="alert alert-error"
      role="alert"
    >
      <span>{{ store.errorMessage }}</span>

      <button
        type="button"
        class="btn btn-sm"
        @click="load"
      >
        Повторить
      </button>
    </div>

    <template v-else-if="store.programs.length">
      <section
        v-if="recommendedPrograms.length"
        class="space-y-4"
        aria-labelledby="catalog-recommended-title"
      >
        <header>
          <h2
            id="catalog-recommended-title"
            class="text-xl font-bold sm:text-2xl"
          >
            Рекомендуемые программы
          </h2>

          <p class="text-base-content/60 mt-1 text-sm">
            Подобраны с учётом рекомендаций для вас.
          </p>
        </header>

        <div class="grid items-stretch gap-4 md:grid-cols-2 xl:grid-cols-3">
          <PatientProgramCard
            v-for="program in recommendedPrograms"
            :key="program.id"
            :program="program"
            :show-steps="false"
            @request-purchase="requestPurchase"
          />
        </div>
      </section>

      <PatientHomeLifeAspects
        :aspects="groupedAspects"
        title="Другие программы по сферам жизни"
        description="Выберите направление, которое хотите улучшить."
        @request-purchase="requestPurchase"
      />

      <section
        v-if="unclassifiedPrograms.length"
        class="space-y-4"
        aria-labelledby="catalog-other-title"
      >
        <h2
          id="catalog-other-title"
          class="text-xl font-bold sm:text-2xl"
        >
          Другие программы
        </h2>

        <div class="grid items-stretch gap-4 md:grid-cols-2 xl:grid-cols-3">
          <PatientProgramCard
            v-for="program in unclassifiedPrograms"
            :key="program.id"
            :program="program"
            :show-steps="false"
            @request-purchase="requestPurchase"
          />
        </div>
      </section>
    </template>

    <section
      v-else
      class="border-base-300 bg-base-100 rounded-2xl border border-dashed p-8 text-center"
    >
      <Icon
        name="lucide:route"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Программ пока нет
      </p>
    </section>

    <PatientPurchaseDialog
      v-if="selectedProgram"
      v-model="purchaseDialogOpen"
      :program="selectedProgram"
      @requested="handlePurchaseRequested"
    />
  </div>
</template>