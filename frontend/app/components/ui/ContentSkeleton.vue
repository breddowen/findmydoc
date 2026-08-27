<!-- ./frontend/app/components/ui/ContentSkeleton.vue -->
<script setup>
defineProps({
  count: {
    type: Number,
    default: 3,
  },
  variant: {
    type: String,
    default: 'card',
    validator: (value) =>
      [
        'card',
        'list',
        'text',
      ].includes(value),
  },
})
</script>

<template>
  <div
    v-if="variant === 'text'"
    class="space-y-3"
  >
    <div
      v-for="index in count"
      :key="index"
      class="skeleton h-4"
      :class="
        index % 3 === 0
          ? 'w-2/3'
          : 'w-full'
      "
    />
  </div>

  <div
    v-else
    class="grid gap-4"
    :class="{
      'md:grid-cols-2 xl:grid-cols-3':
        variant === 'card',
    }"
  >
    <div
      v-for="index in count"
      :key="index"
      class="bg-base-100 border-base-300 rounded-2xl border p-5"
    >
      <template v-if="variant === 'list'">
        <div class="flex items-center gap-4">
          <div
            class="skeleton size-14 shrink-0 rounded-full"
          />

          <div class="flex-1 space-y-3">
            <div class="skeleton h-4 w-1/3" />
            <div class="skeleton h-4 w-2/3" />
          </div>
        </div>
      </template>

      <template v-else>
        <div class="skeleton h-5 w-20" />
        <div class="skeleton mt-5 h-6 w-2/3" />
        <div class="skeleton mt-4 h-4 w-full" />
        <div class="skeleton mt-2 h-4 w-5/6" />
        <div class="skeleton mt-6 h-10 w-28" />
      </template>
    </div>
  </div>
</template>