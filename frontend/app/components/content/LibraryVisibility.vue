<!-- ./frontend/app/components/content/LibraryVisibility.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

defineProps({
  disabled: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <label
    class="border-base-300 flex cursor-pointer items-start justify-between gap-4 rounded-2xl border p-4"
  >
    <span class="min-w-0">
      <span class="block font-medium">
        Не показывать в общем каталоге
      </span>

      <span class="text-base-content/60 mt-1 block text-sm">
        Материал останется доступен внутри программ,
        по назначениям и прямой ссылке — с учётом прав доступа.
      </span>
    </span>

    <input
      v-model="model"
      type="checkbox"
      class="toggle toggle-primary shrink-0"
      :disabled="disabled"
    >
  </label>
</template>