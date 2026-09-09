<!-- ./frontend/app/components/patient/ProgramCard.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
  showSteps: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits(['request-purchase'])

const store = usePatientHomeStore()

const opening = ref(false)
const errorMessage = ref('')

const isPaid = computed(() =>
  Boolean(props.program.service),
)

const isCompleted = computed(() =>
  props.program.enrollment?.status === 'completed',
)

const isActive = computed(() =>
  props.program.enrollment?.status === 'active',
)

const canRequestPurchase = computed(() =>
  isPaid.value
  && !props.program.has_program_access,
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
      ['article', 'questionnaire'].includes(item.item_type)
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

  return 'Начать программу'
})

async function openProgram() {
  if (opening.value) return

  opening.value = true
  errorMessage.value = ''

  try {
    // Начинать можно и платную программу:
    // бесплатные задания внутри неё доступны без покупки.
    if (!props.program.enrollment) {
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
    class="border-base-300 bg-base-100 flex min-w-0 flex-col rounded-2xl border p-4 sm:p-5"
  >
    <div class="flex flex-wrap items-center gap-2 text-xs">
      <span
        v-if="program.is_recommended && !isCompleted"
        class="badge badge-primary badge-outline badge-sm"
      >
        Рекомендуется
      </span>

      <span class="text-base-content/60">
        {{ isPaid ? 'Со специалистами' : 'Бесплатно' }}
      </span>

      <span v-if="program.is_start" class="text-primary">
        Стартовая
      </span>

      <span v-if="isCompleted" class="text-success">
        Пройдена
      </span>

      <span v-else-if="isActive" class="text-primary">
        Начата
      </span>

      <span
        v-if="isPaid && program.has_program_access"
        class="text-success"
      >
        Pro-материалы открыты
      </span>
    </div>

    <h3 class="mt-2 text-base font-semibold leading-snug wrap-anywhere sm:text-lg">
      {{ program.title }}
    </h3>

    <p
      v-if="program.description"
      class="text-base-content/65 mt-2 line-clamp-3 text-sm"
    >
      {{ program.description }}
    </p>

    <p
      v-if="canRequestPurchase"
      class="text-base-content/60 mt-3 text-xs leading-relaxed"
    >
      Начните с бесплатных материалов.
      Консультации и материалы с отметкой Pro
      доступны после оформления программы сопровождения.
    </p>

    <div
      v-if="isActive || isCompleted"
      class="mt-3 flex items-center gap-3"
    >
      <progress
        class="progress progress-primary h-1.5 min-w-0 flex-1"
        :value="progressValue"
        max="100"
        :aria-label="`Прогресс программы «${program.title}»`"
      />

      <span class="text-base-content/60 shrink-0 text-xs tabular-nums">
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

    <div class="mt-auto space-y-3 pt-4">
      <div class="flex flex-wrap gap-2">
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
        </button>

        <NuxtLink
          v-if="!program.enrollment"
          :to="`/programs/${program.id}`"
          class="btn btn-ghost btn-sm"
        >
          Подробнее
        </NuxtLink>
      </div>

      <template v-if="canRequestPurchase">
        <p
          v-if="program.purchase_requested"
          class="text-success flex items-center gap-1 text-xs"
          role="status"
        >
          <Icon name="lucide:check" class="size-4" />
          Запрос на сопровождение отправлен
        </p>

        <button
          v-else
          type="button"
          class="btn btn-outline btn-sm w-full"
          @click="emit('request-purchase', program)"
        >
          Обсудить сопровождение
        </button>
      </template>
    </div>

    <PatientProgramSteps
      v-if="showSteps"
      :program="program"
    />
  </article>
</template>