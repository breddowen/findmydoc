<!-- ./frontend/app/components/ui/Pagination.vue -->
<script setup>
const model = defineModel({
  type: Number,
  default: 1,
})

const props = defineProps({
  totalItems: {
    type: Number,
    default: 0,
  },
  pageSize: {
    type: Number,
    default: 10,
  },
})

const totalPages = computed(() =>
  Math.max(
    1,
    Math.ceil(props.totalItems / props.pageSize),
  ),
)

watch(totalPages, (value) => {
  if (model.value > value) {
    model.value = value
  }
})
</script>

<template>
  <nav
    v-if="totalPages > 1"
    class="flex items-center justify-center gap-2"
    aria-label="Пагинация"
  >
    <button
      type="button"
      class="btn btn-square btn-sm"
      :disabled="model <= 1"
      aria-label="Предыдущая страница"
      @click="model -= 1"
    >
      <Icon
        name="lucide:chevron-left"
        class="size-4"
      />
    </button>

    <span class="px-3 text-sm">
      {{ model }} из {{ totalPages }}
    </span>

    <button
      type="button"
      class="btn btn-square btn-sm"
      :disabled="model >= totalPages"
      aria-label="Следующая страница"
      @click="model += 1"
    >
      <Icon
        name="lucide:chevron-right"
        class="size-4"
      />
    </button>
  </nav>
</template>