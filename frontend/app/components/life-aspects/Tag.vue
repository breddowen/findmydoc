<!-- ./frontend/app/components/life-aspects/Tag.vue -->
<script setup>
defineProps({
  tag: {
    type: Object,
    required: true,
  },
  action: {
    type: String,
    default: 'add',
  },
  draggable: {
    type: Boolean,
    default: false,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['action'])
</script>

<template>
  <div
    class="life-aspect-tag-item border-base-300 bg-base-100 flex min-w-0 items-center gap-3 rounded-xl border p-3"
    :data-tag-id="tag.id"
    role="listitem"
  >
    <span
      v-if="draggable"
      class="life-aspect-tag-handle text-base-content/40 flex size-9 shrink-0 touch-none items-center justify-center rounded-lg"
      :class="
        disabled
          ? 'cursor-not-allowed opacity-40'
          : 'hover:bg-base-200 cursor-grab active:cursor-grabbing'
      "
      title="Перетащите тег за эту ручку"
      aria-hidden="true"
    >
      <Icon
        name="lucide:grip-vertical"
        class="size-5"
      />
    </span>

    <div class="min-w-0 flex-1">
      <p class="text-sm font-medium wrap-anywhere">
        {{ tag.name }}
      </p>

      <span
        v-if="tag.is_hidden"
        class="badge badge-warning badge-sm mt-1"
      >
        Скрытый тег
      </span>
    </div>

    <button
      type="button"
      class="btn btn-square btn-ghost btn-sm shrink-0"
      :disabled="disabled"
      :aria-label="
        action === 'add'
          ? `Добавить тег «${tag.name}» в сферу`
          : `Убрать тег «${tag.name}» из сферы`
      "
      @click="emit('action', tag.id)"
    >
      <Icon
        :name="
          action === 'add'
            ? 'lucide:plus'
            : 'lucide:x'
        "
        class="size-4"
        :class="{
          'text-primary': action === 'add',
        }"
      />
    </button>
  </div>
</template>