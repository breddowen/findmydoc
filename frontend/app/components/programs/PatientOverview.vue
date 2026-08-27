<!-- ./frontend/app/components/programs/PatientOverview.vue -->
<script setup>
const store = useProgramsStore()

const loading = ref(true)
const errorMessage = ref('')

const activePrograms = computed(() =>
  store.programs.filter(
    (program) =>
      program.has_program_access
      || program.enrollment,
  ),
)

function statusText(program) {
  if (
    program.enrollment?.status === 'completed'
  ) {
    return 'Завершена'
  }

  if (program.enrollment) {
    return 'В процессе'
  }

  if (program.has_program_access) {
    return 'Доступна'
  }

  return ''
}

onMounted(async () => {
  try {
    await store.fetchProgramsForPatient()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section
    v-if="
      loading
      || errorMessage
      || activePrograms.length
    "
    class="space-y-4"
  >
    <div class="flex items-center justify-between gap-4">
      <div>
        <h2 class="text-xl font-bold sm:text-2xl">
          Мои программы
        </h2>

        <p class="text-base-content/60 text-sm">
          Приобретённые и начатые программы.
        </p>
      </div>

      <NuxtLink
        to="/programs"
        class="btn btn-ghost btn-sm"
      >
        Все программы
      </NuxtLink>
    </div>

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
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <NuxtLink
        v-for="program in activePrograms"
        :key="program.id"
        :to="`/programs/${program.id}`"
        class="card bg-base-100 border-primary/30 hover:border-primary border transition"
      >
        <div class="card-body">
          <div class="flex flex-wrap gap-2">
            <span
              class="badge"
              :class="
                program.enrollment?.status
                  === 'completed'
                  ? 'badge-success'
                  : 'badge-primary'
              "
            >
              {{ statusText(program) }}
            </span>

            <span
              v-if="program.has_program_access"
              class="badge badge-secondary"
            >
              Полный доступ
            </span>
          </div>

          <h3 class="card-title">
            {{ program.title }}
          </h3>

          <div v-if="program.enrollment">
            <div
              class="mb-1 flex justify-between text-xs"
            >
              <span>Прогресс</span>
              <strong>
                {{ program.progress_percent }}%
              </strong>
            </div>

            <progress
              class="progress progress-primary w-full"
              :value="program.progress_percent"
              max="100"
            />
          </div>

          <div class="card-actions mt-auto">
            <span class="btn btn-primary btn-sm">
              {{
                program.enrollment
                  ? 'Продолжить'
                  : 'Начать'
              }}
            </span>
          </div>
        </div>
      </NuxtLink>
    </div>
  </section>
</template>