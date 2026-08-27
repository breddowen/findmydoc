<!-- ./frontend/app/components/assignments/PickerItem.vue -->
<script setup>
const props = defineProps({
  item: {
    type: Object,
    required: true,
  },
  selected: {
    type: Boolean,
    default: false,
  },
  assigned: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'select',
])

const disabled = computed(
  () => props.assigned || props.item.is_hidden,
)

function select() {
  if (disabled.value) return

  emit('select', props.item)
}
</script>

<template>
  <button
    type="button"
    class="border-base-300 relative flex w-full items-start gap-3 rounded-2xl border p-4 text-left transition"
    :class="{
      'border-primary bg-primary/5 ring-primary/20 ring-2':
        selected,
      'hover:border-primary':
        !disabled && !selected,
      'cursor-not-allowed opacity-50':
        disabled,
    }"
    :disabled="disabled"
    @click="select"
  >
    <div
      class="mt-0.5 flex size-10 shrink-0 items-center justify-center rounded-xl"
      :class="
        selected
          ? 'bg-primary text-primary-content'
          : 'bg-base-200'
      "
    >
      <Icon
        :name="
          item.content_type === 'article'
            ? 'lucide:file-text'
            : 'lucide:clipboard-list'
        "
        class="size-5"
      />
    </div>

    <div class="min-w-0 flex-1">
      <div class="flex flex-wrap items-center gap-2">
        <p class="font-medium">
          {{ item.title }}
        </p>

        <span
          v-if="item.pro_content"
          class="badge badge-secondary badge-sm"
        >
          Pro
        </span>

        <span
          v-if="assigned"
          class="badge badge-success badge-sm"
        >
          Уже назначено
        </span>

        <span
          v-if="item.is_hidden"
          class="badge badge-warning badge-sm"
        >
          Скрыто
        </span>
      </div>

      <p
        v-if="item.description"
        class="text-base-content/60 mt-1 line-clamp-2 text-sm"
      >
        {{ item.description }}
      </p>

      <div
        v-if="item.tags?.length"
        class="mt-3 flex flex-wrap gap-1"
      >
        <span
          v-for="tag in item.tags.slice(0, 4)"
          :key="tag.id"
          class="badge badge-outline badge-sm"
        >
          {{ tag.name }}
        </span>

        <span
          v-if="item.tags.length > 4"
          class="badge badge-ghost badge-sm"
        >
          +{{ item.tags.length - 4 }}
        </span>
      </div>
    </div>

    <input
      type="radio"
      class="radio radio-primary mt-1 shrink-0"
      :checked="selected"
      :disabled="disabled"
      tabindex="-1"
    >
  </button>
</template>