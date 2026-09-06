<!-- ./frontend/app/components/patient/Home.vue -->
<script setup>
const store = usePatientHomeStore()

onMounted(() => {
  store.load()
})

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-7">
    <UiContentSkeleton
      v-if="store.loading"
      variant="card"
      :count="2"
    />

    <section
      v-else-if="store.errorMessage"
      class="border-base-300 bg-base-100 rounded-3xl border p-6"
    >
      <p role="alert">
        {{ store.errorMessage }}
      </p>

      <button
        type="button"
        class="btn btn-primary mt-4"
        @click="store.load"
      >
        Попробовать ещё раз
      </button>
    </section>

    <template v-else>
      <PatientNextStep
        v-if="store.primaryProgram"
        :key="store.primaryProgram.id"
        :program="store.primaryProgram"
      />

      <section
        v-else
        class="border-base-300 bg-base-100 rounded-3xl border p-5 sm:p-8"
      >
        <h1 class="text-2xl font-bold">
          {{
            store.hasCompletedStart
              ? 'Первый маршрут пройден'
              : 'Здравствуйте'
          }}
        </h1>

        <p class="text-base-content/70 mt-3">
          {{
            store.hasCompletedStart
              ? 'Можно вернуться к материалам или обсудить дальнейшую поддержку со специалистом.'
              : 'Здесь можно познакомиться с материалами клиники и доступными программами.'
          }}
        </p>

        <NuxtLink
          to="/programs"
          class="btn btn-primary mt-5"
        >
          {{
            store.hasCompletedStart
              ? 'Посмотреть дальнейшие варианты'
              : 'Посмотреть программы'
          }}
        </NuxtLink>
      </section>

      <PatientJourney
        v-if="store.primaryProgram?.is_start"
        :program="store.primaryProgram"
      />

      <AssignmentsPatientList />

      <details
        v-if="store.otherActivePrograms.length"
        class="border-base-300 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer font-medium">
          Другие начатые программы
        </summary>

        <div class="mt-4 space-y-3">
          <NuxtLink
            v-for="program in store.otherActivePrograms"
            :key="program.id"
            :to="`/programs/${program.id}`"
            class="border-base-300 block rounded-xl border p-4"
          >
            <span class="font-medium">
              {{ program.title }}
            </span>

            <span class="text-base-content/60 mt-1 block text-sm">
              Продолжить программу
            </span>
          </NuxtLink>
        </div>
      </details>

      <PatientSupport />

      <details
        v-if="store.completedPrograms.length"
        class="border-base-300 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer font-medium">
          Пройденные материалы программ
        </summary>

        <div class="mt-4 space-y-3">
          <NuxtLink
            v-for="program in store.completedPrograms"
            :key="program.id"
            :to="`/programs/${program.id}`"
            class="link link-primary block"
          >
            {{ program.title }}
          </NuxtLink>
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
  </div>
</template>