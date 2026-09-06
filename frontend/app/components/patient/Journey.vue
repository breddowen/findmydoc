<!-- ./frontend/app/components/patient/Journey.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const items = computed(() =>
  (props.program.stages || [])
    .flatMap(stage =>
      (stage.items || []).map(item => ({
        ...item,
        stageId: stage.id,
      })),
    )
    .filter(
      item =>
        item.item_type !== 'consultation'
        && !item.is_hidden,
    ),
)

const previewItems = computed(() =>
  items.value.slice(0, 3),
)
</script>

<template>
  <section
    v-if="previewItems.length"
    class="space-y-3"
  >
    <h2 class="text-lg font-semibold">
      Что входит в маршрут
    </h2>

    <ol class="space-y-3">
      <li
        v-for="(item, index) in previewItems"
        :key="item.id"
        class="flex items-start gap-3"
      >
        <span
          class="flex size-7 shrink-0 items-center justify-center rounded-full text-xs font-semibold"
          :class="
            item.is_completed
              ? 'bg-success/15 text-success'
              : 'bg-base-200 text-base-content/70'
          "
        >
          <Icon
            v-if="item.is_completed"
            name="lucide:check"
            class="size-4"
          />

          <template v-else>
            {{ index + 1 }}
          </template>
        </span>

        <span class="pt-0.5 text-sm">
          {{ item.title }}
        </span>
      </li>
    </ol>

    <NuxtLink
      v-if="items.length > previewItems.length"
      :to="`/programs/${program.id}`"
      class="link link-primary text-sm"
    >
      Посмотреть весь маршрут
    </NuxtLink>
  </section>
</template>