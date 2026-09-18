<!-- ./frontend/app/components/test-styles/Preview.vue -->
<script setup>
import { buildPreviewStyle } from '~/utils/test-styles'

const props = defineProps({
  settings: {
    type: Object,
    required: true,
  },
  theme: {
    type: String,
    default: 'light',
  },
})

const previewStyle = computed(() =>
  buildPreviewStyle(props.settings, props.theme),
)
</script>

<template>
  <section
    :data-theme="theme"
    :style="previewStyle"
    class="bg-base-200 text-base-content border-base-300 overflow-hidden rounded-box border"
    aria-label="Предпросмотр оформления"
  >
    <div class="bg-base-100 border-base-300 border-b p-5">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <strong style="font-size: 1.15em">
          MentalConnect
        </strong>

        <span class="badge badge-primary">
          Предпросмотр
        </span>
      </div>
    </div>

    <div class="space-y-5 p-5">
      <div class="card bg-base-100 border-base-300 border">
        <div class="card-body gap-4">
          <span class="text-primary font-semibold">
            Программа сопровождения
          </span>

          <h3 class="font-bold" style="font-size: 1.4em">
            Забота о себе каждый день
          </h3>

          <p>
            Здесь можно оценить фон, текст, основные цвета
            и оформление элементов интерфейса.
          </p>

          <p class="text-base-content/60">
            Дополнительный текст и второстепенная информация.
          </p>

          <div class="flex flex-wrap gap-2">
            <button type="button" class="btn btn-primary">
              Продолжить
            </button>

            <button type="button" class="btn btn-secondary">
              Подробнее
            </button>

            <button type="button" class="btn btn-outline">
              Отмена
            </button>
          </div>
        </div>
      </div>

      <div class="bg-base-100 border-base-300 space-y-4 rounded-box border p-4">
        <label class="block">
          <span class="mb-2 block">Имя</span>

          <input
            class="input w-full"
            value="Демонстрационный пример"
            readonly
            aria-label="Пример поля ввода"
          >
        </label>

        <div class="flex items-center gap-3">
          <input
            type="checkbox"
            class="checkbox checkbox-primary"
            checked
            aria-label="Пример флажка"
          >

          <span>Получать уведомления</span>
        </div>

        <div class="flex flex-wrap gap-2">
          <span class="badge badge-accent">Акцент</span>
          <span class="badge badge-neutral">Нейтральный</span>
          <span class="badge badge-info">Информация</span>
          <span class="badge badge-success">Успех</span>
          <span class="badge badge-warning">Внимание</span>
          <span class="badge badge-error">Ошибка</span>
        </div>
      </div>

      <div class="alert alert-success">
        <Icon name="lucide:check-circle" class="size-5 shrink-0" />
        <span>Пример успешного действия</span>
      </div>
    </div>
  </section>
</template>