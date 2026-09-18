<!-- ./frontend/app/components/test-styles/ThemeFields.vue -->
<script setup>
import {
  COLOR_FIELDS,
  NUMBER_FIELDS,
} from '~/utils/test-styles'

const model = defineModel({
  type: Object,
  required: true,
})

function updateNumber(field, event) {
  const value = Number(event.target.value)

  model.value[field.key] = (
    `${Number(value.toFixed(4))}${field.unit}`
  )
}
</script>

<template>
  <div class="space-y-8">
    <section>
      <h2 class="text-lg font-semibold">
        Цветовая палитра
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Нажмите на образец, чтобы выбрать цвет.
      </p>

      <div class="mt-4 grid gap-3 sm:grid-cols-2">
        <label
          v-for="field in COLOR_FIELDS"
          :key="field.key"
          class="border-base-300 bg-base-100 flex min-w-0 items-center gap-3 rounded-box border p-3"
        >
          <input
            v-model="model[field.key]"
            type="color"
            class="h-11 w-12 shrink-0 cursor-pointer rounded border-0 bg-transparent p-0"
            :aria-label="field.label"
          >

          <span class="min-w-0">
            <span class="block text-sm font-medium">
              {{ field.label }}
            </span>

            <span class="text-base-content/60 block font-mono text-xs">
              {{ model[field.key] }}
            </span>
          </span>
        </label>
      </div>
    </section>

    <section>
      <h2 class="text-lg font-semibold">
        Геометрия и эффекты
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Влияют на элементы daisyUI. Скругления и отступы,
        явно заданные в отдельных компонентах, не меняются.
      </p>

      <div class="mt-5 space-y-6">
        <label
          v-for="field in NUMBER_FIELDS"
          :key="field.key"
          class="block"
        >
          <span class="mb-3 flex items-center justify-between gap-4 text-sm">
            <span>{{ field.label }}</span>

            <span class="badge badge-outline shrink-0 font-mono">
              {{ model[field.key] }}
            </span>
          </span>

          <input
            type="range"
            class="range range-primary range-sm w-full"
            :min="field.min"
            :max="field.max"
            :step="field.step"
            :value="parseFloat(model[field.key])"
            :aria-label="field.label"
            @input="updateNumber(field, $event)"
          >
        </label>
      </div>
    </section>
  </div>
</template>