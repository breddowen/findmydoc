<!-- ./frontend/app/components/patient/ProgramCard.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['request-purchase'])

const store = usePatientHomeStore()

const opening = ref(false)
const errorMessage = ref('')

const isPaid = computed(() => Boolean(props.program.service))

const isCompleted = computed(() =>
  props.program.enrollment?.status === 'completed',
)

const isActive = computed(() =>
  props.program.enrollment?.status === 'active',
)

const isOffer = computed(() =>
  isPaid.value
  && !props.program.has_program_access
  && !isCompleted.value,
)

const progressValue = computed(() => {
  const value = Number(props.program.progress_percent)

  return Number.isFinite(value)
    ? Math.round(Math.min(Math.max(value, 0), 100))
    : 0
})

const nextStageId = computed(() => {
  if (!isActive.value) return null

  const stages = [...(props.program.stages || [])].sort(
    (left, right) => left.order_index - right.order_index,
  )

  return stages.find(stage =>
    stage.status !== 'upcoming'
    && (stage.items || []).some(item =>
      item.item_type !== 'consultation'
      && !item.is_hidden
      && item.can_access
      && !item.is_completed,
    ),
  )?.id || null
})

const actionText = computed(() => {
  if (isCompleted.value) return 'Открыть материалы'
  if (isActive.value) return 'Продолжить'
  if (props.program.enrollment) return 'Открыть программу'

  return 'Начать'
})

async function openProgram() {
  if (opening.value) return

  opening.value = true
  errorMessage.value = ''

  try {
    if (
      !props.program.enrollment
      && (!isPaid.value || props.program.has_program_access)
    ) {
      await store.startProgram(props.program.id)
    }

    await navigateTo({
      path: `/programs/${props.program.id}`,
      query: nextStageId.value
        ? { stage: nextStageId.value }
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
  <article
    class="bg-base-100 rounded-2xl border p-4 sm:p-5"
    :class="
      isPaid
        ? 'border-amber-500/70 shadow-[0_0_0_1px_rgba(245,158,11,0.08)]'
        : 'border-base-300'
    "
  >
    <div class="flex flex-wrap items-center gap-2 text-xs">
      <span
        v-if="isPaid"
        class="inline-flex items-center gap-1 rounded-full bg-amber-500/15 px-2 py-1"
      >
        <Icon
          name="lucide:sparkles"
          class="size-3.5 text-amber-600"
        />
        Платная программа
      </span>

      <span
        v-else
        class="text-base-content/60"
      >
        Бесплатно
      </span>

      <span
        v-if="program.is_start"
        class="text-primary"
      >
        Стартовая
      </span>

      <span
        v-if="isCompleted"
        class="text-success"
      >
        Пройдена
      </span>

      <span
        v-else-if="isActive"
        class="text-primary"
      >
        Начата
      </span>

      <span
        v-if="isPaid && program.has_program_access"
        class="text-success"
      >
        Доступ открыт
      </span>
    </div>

    <h2 class="mt-2 text-base font-semibold leading-snug sm:text-lg">
      {{ program.title }}
    </h2>

    <p
      v-if="program.description"
      class="text-base-content/65 mt-1.5 line-clamp-2 text-sm"
    >
      {{ program.description }}
    </p>

    <p
      v-if="isPaid && !program.has_program_access"
      class="text-base-content/70 mt-2 text-xs"
    >
      Стоимость по запросу
    </p>

    <div
      v-if="isActive || isCompleted"
      class="mt-3 flex items-center gap-3"
    >
      <progress
        class="progress progress-primary h-1.5 flex-1"
        :value="progressValue"
        max="100"
        aria-label="Прогресс по материалам"
      />

      <span class="text-base-content/60 shrink-0 text-xs">
        {{ progressValue }}%
      </span>
    </div>

    <p
      v-if="errorMessage"
      class="text-error mt-3 text-sm"
      role="alert"
    >
      {{ errorMessage }}
    </p>

    <div
      v-if="isOffer"
      class="mt-3 flex flex-wrap items-center gap-2"
    >
      <NuxtLink
        :to="`/programs/${program.id}`"
        class="btn btn-outline btn-sm"
      >
        Подробнее
      </NuxtLink>

      <span
        v-if="program.purchase_requested"
        class="text-success inline-flex items-center gap-1 text-xs"
        role="status"
      >
        <Icon
          name="lucide:check"
          class="size-4"
        />
        Запрос отправлен
      </span>

      <button
        v-else
        type="button"
        class="btn btn-ghost btn-sm"
        @click="emit('request-purchase', program)"
      >
        Обсудить с ассистентом
      </button>
    </div>

    <div
      v-else
      class="mt-3"
    >
      <button
        type="button"
        class="btn btn-sm"
        :class="isCompleted ? 'btn-outline' : 'btn-primary'"
        :disabled="opening"
        @click="openProgram"
      >
        <span
          v-if="opening"
          class="loading loading-spinner loading-xs"
        />

        {{ actionText }}

        <Icon
          v-if="!opening"
          name="lucide:arrow-right"
          class="size-4"
        />
      </button>
    </div>

    <PatientProgramSteps :program="program" />
  </article>
</template>