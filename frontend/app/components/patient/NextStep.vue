<!-- ./frontend/app/components/patient/NextStep.vue -->
 <!-- DELETE -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const store = usePatientHomeStore()

const opening = ref(false)
const errorMessage = ref('')

const nextStep = computed(() => {
  const stages = props.program.stages || []

  for (const stage of stages) {
    if (
      props.program.enrollment
      && stage.status === 'upcoming'
    ) {
      continue
    }

    const item = (stage.items || []).find(
      current =>
        current.item_type !== 'consultation'
        && !current.is_hidden
        && current.can_access
        && !current.is_completed,
    )

    if (item) {
      return { stage, item }
    }
  }

  return null
})

const progressValue = computed(() => {
  const value = Number(props.program.progress_percent)

  return Number.isFinite(value)
    ? Math.min(Math.max(value, 0), 100)
    : 0
})

const actionText = computed(() => {
  if (!props.program.enrollment) {
    return props.program.is_start
      ? 'Начать с первого шага'
      : 'Открыть мой план'
  }

  return nextStep.value
    ? 'Продолжить'
    : 'Посмотреть план'
})

async function openProgram() {
  if (opening.value) return

  opening.value = true
  errorMessage.value = ''

  try {
    if (!props.program.enrollment) {
      await store.startProgram(props.program.id)
    }

    await navigateTo({
      path: `/programs/${props.program.id}`,
      query: nextStep.value
        ? { stage: nextStep.value.stage.id }
        : {},
    })
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось открыть программу'
  } finally {
    opening.value = false
  }
}
</script>

<template>
  <section
    class="border-primary/20 bg-base-100 rounded-3xl border p-5 shadow-sm sm:p-8"
  >
    <p class="text-primary text-sm font-medium">
      {{
        program.enrollment
          ? 'Ваш следующий шаг'
          : program.is_start
            ? 'Начните с небольшого шага'
            : 'Ваша программа доступна'
      }}
    </p>

    <h1 class="mt-3 text-2xl font-bold sm:text-3xl">
      {{ program.title }}
    </h1>

    <p
      v-if="program.description"
      class="text-base-content/70 mt-3 max-w-2xl"
    >
      {{ program.description }}
    </p>

    <div
      v-if="nextStep"
      class="bg-base-200 mt-6 rounded-2xl p-4"
    >
      <p class="text-base-content/60 text-xs">
        {{
          nextStep.item.item_type === 'article'
            ? 'Материал для чтения'
            : 'Вопросы для размышления'
        }}
      </p>

      <h2 class="mt-1 font-semibold">
        {{ nextStep.item.title }}
      </h2>
    </div>

    <div
      v-if="program.enrollment"
      class="mt-5"
    >
      <div class="mb-2 flex justify-between gap-3 text-xs">
        <span>Прогресс по материалам</span>
        <span>{{ progressValue }}%</span>
      </div>

      <progress
        class="progress progress-primary w-full"
        :value="progressValue"
        max="100"
      />
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-5"
      role="alert"
    >
      {{ errorMessage }}
    </div>

    <button
      type="button"
      class="btn btn-primary mt-6 w-full sm:w-auto"
      :disabled="opening"
      @click="openProgram"
    >
      <span
        v-if="opening"
        class="loading loading-spinner loading-sm"
      />

      {{ actionText }}

      <Icon
        v-if="!opening"
        name="lucide:arrow-right"
        class="size-4"
      />
    </button>

    <p
      v-if="program.is_start"
      class="text-base-content/60 mt-3 text-sm"
    >
      Бесплатно. Можно остановиться и продолжить позже.
    </p>
  </section>
</template>