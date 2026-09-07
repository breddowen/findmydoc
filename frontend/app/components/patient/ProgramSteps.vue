<!-- ./frontend/app/components/patient/ProgramSteps.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const stages = computed(() =>
  [...(props.program.stages || [])]
    .sort((left, right) => left.order_index - right.order_index)
    .map(stage => ({
      ...stage,
      items: [...(stage.items || [])]
        .filter(item => !item.is_hidden)
        .sort((left, right) => left.order_index - right.order_index),
    }))
    .filter(stage => stage.items.length),
)

const itemsCount = computed(() =>
  stages.value.reduce(
    (total, stage) => total + stage.items.length,
    0,
  ),
)

function itemIcon(item) {
  if (item.is_completed) return 'lucide:circle-check'

  const icons = {
    article: 'lucide:file-text',
    questionnaire: 'lucide:clipboard-list',
    consultation: 'lucide:stethoscope',
  }

  return icons[item.item_type] || 'lucide:circle'
}
</script>

<template>
  <details
    v-if="itemsCount"
    class="border-base-300 mt-3 border-t pt-3"
  >
    <summary
      class="text-base-content/70 cursor-pointer text-sm marker:text-base-content/40"
    >
      Что входит в программу
      <span class="text-base-content/50">
        · {{ itemsCount }}
      </span>
    </summary>

    <div class="mt-3 space-y-4">
      <section
        v-for="stage in stages"
        :key="stage.id"
      >
        <h3 class="text-base-content/60 mb-2 text-xs font-medium">
          {{ stage.title }}
        </h3>

        <ul class="space-y-2">
          <li
            v-for="item in stage.items"
            :key="item.id"
            class="flex items-start gap-2 text-sm"
          >
            <Icon
              :name="itemIcon(item)"
              class="mt-0.5 size-4 shrink-0"
              :class="
                item.is_completed
                  ? 'text-success'
                  : 'text-base-content/50'
              "
            />

            <span class="min-w-0 flex-1">
              {{ item.title }}
            </span>

            <Icon
              v-if="!item.can_access"
              name="lucide:lock-keyhole"
              class="text-base-content/40 mt-0.5 size-3.5 shrink-0"
              aria-label="Доступ ограничен"
            />
          </li>
        </ul>
      </section>
    </div>
  </details>
</template>