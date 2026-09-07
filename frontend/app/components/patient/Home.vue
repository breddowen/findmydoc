<!-- ./frontend/app/components/patient/Home.vue -->
<script setup>
const store = usePatientHomeStore()

const purchaseDialogOpen = ref(false)
const selectedProgram = ref(null)

function openPurchaseDialog(program) {
  selectedProgram.value = program
  purchaseDialogOpen.value = true
}

onMounted(() => {
  void store.load()
})

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-5">
    <header>
      <h1 class="text-xl font-bold sm:text-2xl">
        Ваши программы
      </h1>

      <p class="text-base-content/60 mt-1 text-sm">
        Выберите подходящий маршрут и проходите его в своём темпе.
      </p>
    </header>

    <UiContentSkeleton
      v-if="store.loading"
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
        v-if="store.homePrograms.length"
        class="space-y-3"
        aria-label="Доступные программы"
      >
        <PatientProgramCard
          v-for="program in store.homePrograms"
          :key="program.id"
          :program="program"
          @request-purchase="openPurchaseDialog"
        />
      </section>

      <section
        v-else
        class="border-base-300 bg-base-100 rounded-2xl border p-5"
      >
        <p class="font-medium">
          {{
            store.completedPrograms.length
              ? 'Доступные программы пройдены'
              : 'Пока нет доступных программ'
          }}
        </p>

        <p class="text-base-content/60 mt-2 text-sm">
          Можно вернуться к материалам или посмотреть общий каталог.
        </p>

        <NuxtLink
          to="/programs"
          class="btn btn-outline btn-sm mt-3"
        >
          Каталог программ
        </NuxtLink>
      </section>

      <AssignmentsPatientList />

      <details
        v-if="store.completedPrograms.length"
        class="border-base-300 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer text-sm font-medium">
          Пройденные программы
          · {{ store.completedPrograms.length }}
        </summary>

        <div class="mt-4 space-y-3">
          <PatientProgramCard
            v-for="program in store.completedPrograms"
            :key="program.id"
            :program="program"
            @request-purchase="openPurchaseDialog"
          />
        </div>
      </details>

      <nav
        class="text-base-content/70 flex flex-wrap gap-x-5 gap-y-3 text-sm"
        aria-label="Материалы и программы"
      >
        <NuxtLink
          to="/content/articles"
          class="link"
        >
          Все статьи
        </NuxtLink>

        <NuxtLink
          to="/questionnaires"
          class="link"
        >
          Опросники
        </NuxtLink>

        <NuxtLink
          to="/programs"
          class="link"
        >
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