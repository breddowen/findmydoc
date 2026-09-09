<!-- ./frontend/app/components/patient/home/ContinueCard.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const progressValue = computed(() => {
  const value = Number(props.program.progress_percent)

  return Number.isFinite(value)
    ? Math.round(Math.min(Math.max(value, 0), 100))
    : 0
})

const nextStageId = computed(() => {
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

const programLocation = computed(() => ({
  path: `/programs/${props.program.id}`,
  query: nextStageId.value
    ? { stage: nextStageId.value }
    : {},
}))
</script>

<template>
  <article class="border-base-300 bg-base-100 rounded-2xl border p-4">
    <div class="flex min-w-0 flex-col gap-3 sm:flex-row sm:items-center sm:gap-5">
      <div class="min-w-0 flex-1">
        <h2 class="text-base font-semibold leading-snug wrap-anywhere">
          {{ program.title }}
        </h2>

        <div class="mt-2 flex items-center gap-3">
          <progress
            class="progress progress-primary h-1.5 min-w-0 flex-1"
            :value="progressValue"
            max="100"
            :aria-label="`Прогресс программы «${program.title}»`"
          />

          <span class="text-base-content/65 shrink-0 text-xs tabular-nums">
            {{ progressValue }}%
          </span>
        </div>
      </div>

      <NuxtLink
        :to="programLocation"
        class="btn btn-primary btn-sm w-full shrink-0 sm:w-auto"
        :aria-label="`Продолжить программу «${program.title}»`"
      >
        Продолжить программу
        <Icon name="lucide:arrow-right" class="size-4" />
      </NuxtLink>
    </div>
  </article>
</template>