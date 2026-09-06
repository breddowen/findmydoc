<!-- ./frontend/app/components/programs/configurator/HomeSettings.vue -->
<script setup>
const isStart = defineModel('isStart', {
  type: Boolean,
  default: false,
})

const priority = defineModel('priority', {
  type: Number,
  default: 0,
})
</script>

<template>
  <section
    class="border-base-300 space-y-5 rounded-2xl border p-5"
  >
    <div>
      <h2 class="font-semibold">
        Отображение на главной пациента
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Подбор по тегам сохраняется. Приоритет определяет
        порядок среди подходящих программ.
      </p>
    </div>

    <label class="flex cursor-pointer items-start gap-3">
      <input
        v-model="isStart"
        type="checkbox"
        class="toggle toggle-primary mt-1"
      >

      <span>
        <span class="block font-medium">
          Стартовый маршрут
        </span>

        <span class="text-base-content/60 mt-1 block text-sm">
          Бесплатное знакомство: статьи и опросники,
          без платной услуги и консультаций.
        </span>
      </span>
    </label>

    <label class="block">
      <span class="mb-2 block text-sm font-medium">
        Приоритет на главной
      </span>

      <input
        v-model.number="priority"
        type="number"
        min="0"
        max="1000"
        step="1"
        required
        class="input input-bordered w-full max-w-xs"
      >

      <span class="text-base-content/60 mt-2 block text-xs">
        От 0 до 1000. Чем больше значение, тем выше программа.
      </span>
    </label>
  </section>
</template>