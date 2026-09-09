<!-- ./frontend/app/components/patient/Home.vue -->
<script setup>
import HomeHero from './home/Hero.vue'
import ContinueCard from './home/ContinueCard.vue'
import Recommendations from './home/Recommendations.vue'
import LifeAspects from './home/LifeAspects.vue'

const store = usePatientHomeStore()

const loadStarted = ref(false)

const purchaseDialogOpen = ref(false)
const selectedProgram = ref(null)

const hasProgramsInProgress = computed(() =>
  store.inProgressPrograms.length > 0,
)

function openPurchaseDialog(program) {
  selectedProgram.value = program
  purchaseDialogOpen.value = true
}

onMounted(() => {
  loadStarted.value = true
  void store.load()
})

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-6">
    <UiContentSkeleton
      v-if="!loadStarted || store.loading"
      variant="card"
      :count="3"
    />

    <section
      v-else-if="store.errorMessage"
      class="border-base-300 bg-base-100 rounded-2xl border p-5"
    >
      <p role="alert">
        {{ store.errorMessage }}
      </p>

      <button
        type="button"
        class="btn btn-primary btn-sm mt-4"
        @click="store.load"
      >
        Попробовать ещё раз
      </button>
    </section>

    <template v-else>
      <section
        v-if="hasProgramsInProgress"
        class="space-y-3"
        aria-labelledby="patient-continue-title"
      >
        <header>
          <h1
            id="patient-continue-title"
            class="text-xl font-bold sm:text-2xl"
          >
            Продолжить работу
          </h1>

          <p class="text-base-content/60 mt-1 text-sm">
            Возвращайтесь к программам
            в удобном для Вас темпе.
          </p>
        </header>

        <ContinueCard
          v-for="program in store.inProgressPrograms"
          :key="program.id"
          :program="program"
        />
      </section>

      <HomeHero v-else />

      <Recommendations
        :programs="store.recommendedPrograms"
        @request-purchase="openPurchaseDialog"
      />

      <LifeAspects
        :aspects="store.homeLifeAspects"
        @request-purchase="openPurchaseDialog"
      />

      <section
        v-if="store.unclassifiedPrograms.length"
        class="space-y-3"
        aria-labelledby="patient-other-programs-title"
      >
        <h2
          id="patient-other-programs-title"
          class="text-xl font-bold sm:text-2xl"
        >
          Другие программы
        </h2>

        <div class="grid items-stretch gap-3 md:grid-cols-2">
          <PatientProgramCard
            v-for="program in store.unclassifiedPrograms"
            :key="program.id"
            :program="program"
            :show-steps="false"
            @request-purchase="openPurchaseDialog"
          />
        </div>
      </section>

      <section
        v-if="!store.programs.length"
        class="border-base-300 bg-base-100 rounded-2xl border p-5"
      >
        <h2 class="font-medium">
          Пока нет доступных программ
        </h2>

        <p class="text-base-content/60 mt-2 text-sm">
          Программы появятся здесь после публикации.
        </p>
      </section>

      <AssignmentsPatientList />

      <details
        v-if="store.completedPrograms.length"
        class="border-base-300 bg-base-100 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer text-sm font-medium">
          Пройденные программы
          · {{ store.completedPrograms.length }}
        </summary>

        <div class="mt-4 grid gap-3 md:grid-cols-2">
          <PatientProgramCard
            v-for="program in store.completedPrograms"
            :key="program.id"
            :program="program"
            :show-steps="false"
            @request-purchase="openPurchaseDialog"
          />
        </div>
      </details>

      <nav
        class="text-base-content/70 flex flex-wrap gap-x-5 gap-y-3 text-sm"
        aria-label="Материалы и программы"
      >
        <NuxtLink to="/content/articles" class="link">
          Все статьи
        </NuxtLink>

        <NuxtLink to="/questionnaires" class="link">
          Опросники
        </NuxtLink>

        <NuxtLink to="/programs" class="link">
          Все программы
        </NuxtLink>
      </nav>
    </template>

    <PatientPurchaseDialog
      v-model="purchaseDialogOpen"
      :program="selectedProgram"
    />
  </div>
</template>