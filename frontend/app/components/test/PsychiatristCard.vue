<!-- ./frontend/app/components/test/PsychiatristCard.vue -->
<script setup>
defineProps({
  doctor: {
    type: Object,
    required: true,
  },
  days: {
    type: Array,
    default: () => [],
  },
})

const emit = defineEmits(['select'])
</script>

<template>
  <article class="border-base-300 overflow-hidden rounded-2xl border">
    <div
      class="from-primary/15 to-base-200 relative flex h-36 items-center justify-center bg-gradient-to-br"
      aria-hidden="true"
    >
      <div
        class="bg-base-100 text-primary flex size-20 items-center justify-center rounded-full shadow-sm"
      >
        <Icon name="lucide:user-round" class="size-10" />
      </div>

      <span class="badge badge-ghost absolute right-3 top-3">
        Демо
      </span>
    </div>

    <div class="space-y-4 p-4">
      <div>
        <p class="text-primary text-xs font-semibold">
          {{ doctor.speciality }}
        </p>

        <h3 class="mt-1 text-lg font-bold">
          {{ doctor.fullName }}
        </h3>

        <p class="mt-3 text-sm font-medium">
          {{ doctor.clinic }}
        </p>

        <p class="text-base-content/65 mt-1 flex items-center gap-1 text-sm">
          <Icon name="lucide:map-pin" class="size-4 shrink-0" />
          {{ doctor.address }}
        </p>
      </div>

      <div>
        <p class="mb-2 text-sm font-medium">
          Ближайшие дни
        </p>

        <div class="grid grid-cols-2 gap-2">
          <button
            v-for="day in days"
            :key="day.id"
            type="button"
            class="btn btn-outline h-auto min-h-12 flex-col gap-0.5 px-2 py-2"
            @click="emit('select', { doctor, day })"
          >
            <span class="text-xs">{{ day.label }}</span>
            <span class="text-[11px] font-normal">
              {{ day.dateLabel }}
            </span>
          </button>
        </div>
      </div>

      <button
        type="button"
        class="btn btn-primary w-full"
        @click="emit('select', { doctor, day: null })"
      >
        Записаться
      </button>
    </div>
  </article>
</template>