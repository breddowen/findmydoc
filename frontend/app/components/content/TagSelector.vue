<!-- ./frontend/app/components/content/TagSelector.vue -->
<script setup>
const model = defineModel({
  type: Array,
  default: () => [],
})

defineProps({
  tags: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

function isSelected(tagId) {
  return model.value.includes(tagId)
}

function toggle(tagId) {
  if (isSelected(tagId)) {
    model.value = model.value.filter(
      (currentId) => currentId !== tagId,
    )
  } else {
    model.value = [
      ...model.value,
      tagId,
    ]
  }
}
</script>

<template>
  <div>
    <div
      v-if="loading"
      class="flex items-center gap-2 py-3"
    >
      <span class="loading loading-spinner loading-sm" />
      <span class="text-sm">Загрузка тегов...</span>
    </div>

    <div
      v-else-if="tags.length"
      class="flex flex-wrap gap-2"
    >
      <button
        v-for="tag in tags"
        :key="tag.id"
        type="button"
        class="badge cursor-pointer gap-1.5 px-3 py-3 transition"
        :class="
          isSelected(tag.id)
            ? 'badge-primary'
            : 'badge-outline'
        "
        @click="toggle(tag.id)"
      >
        <Icon
          v-if="isSelected(tag.id)"
          name="lucide:check"
          class="size-3"
        />

        {{ tag.name }}
      </button>
    </div>

    <p
      v-else
      class="text-base-content/50 text-sm"
    >
      Теги ещё не созданы.
    </p>
  </div>
</template>