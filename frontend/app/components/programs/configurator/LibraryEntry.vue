<!-- ./frontend/app/components/programs/configurator/LibraryEntry.vue -->
<script setup>
defineProps({
  item: {
    type: Object,
    required: true,
  },
  draggable: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['add'])
</script>

<template>
  <button
    type="button"
    class="border-base-300 hover:border-primary bg-base-100 flex w-full items-start gap-3 rounded-xl border p-3 text-left transition-colors"
    :class="{
      'cursor-grab active:cursor-grabbing': draggable,
    }"
    :aria-label="`Добавить: ${item.title}`"
    @click="emit('add', item)"
  >
    <Icon
      v-if="draggable"
      name="lucide:grip-vertical"
      class="text-base-content/40 mt-0.5 size-4 shrink-0"
    />

    <div class="min-w-0 flex-1">
      <p class="text-sm font-medium">
        {{ item.title }}
      </p>

      <p
        v-if="item.description"
        class="text-base-content/60 mt-1 line-clamp-2 text-xs"
      >
        {{ item.description }}
      </p>

      <div
        v-if="item.pro_content || item.is_library_hidden"
        class="mt-2 flex flex-wrap gap-1"
      >
        <span
          v-if="item.pro_content"
          class="badge badge-secondary badge-xs"
        >
          Pro
        </span>

        <span
          v-if="item.is_library_hidden"
          class="badge badge-outline badge-xs"
        >
          Вне каталога
        </span>
      </div>
    </div>

    <Icon
      name="lucide:plus"
      class="text-primary mt-0.5 size-4 shrink-0"
    />
  </button>
</template>