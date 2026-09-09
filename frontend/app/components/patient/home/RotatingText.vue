<script setup>
const phrases = [
  'Налаживаем питание',
  'Улучшаем сон',
  'Снижаем стресс',
  'Формируем полезные привычки',
  'Поддерживаем активность',
  'Находим эмоциональный баланс',
]

const paused = ref(false)
</script>

<template>
  <div class="rotating-text">
    <!--
      Для скринридера оставляем статичный текст.
      Анимация не должна постоянно озвучиваться.
    -->
    <p class="sr-only">
      Направления работы:
      {{ phrases.join(', ') }}.
    </p>

    <div
      class="flex min-w-0 items-center justify-center gap-1 sm:gap-2"
    >
      <span
        class="text-rotate rotating-text__animation text-primary font-semibold"
        :class="{
          'rotating-text__animation--paused': paused,
        }"
        aria-hidden="true"
      >
        <span class="justify-items-center">
          <span
            v-for="phrase in phrases"
            :key="phrase"
          >
            {{ phrase }}
          </span>
        </span>
      </span>

      <span
        class="rotating-text__static text-primary font-semibold"
        aria-hidden="true"
      >
        {{ phrases[0] }}
      </span>

      <!-- <button
        type="button"
        class="rotating-text__toggle btn btn-circle btn-ghost btn-xs shrink-0"
        :aria-label="
          paused
            ? 'Продолжить смену фраз'
            : 'Приостановить смену фраз'
        "
        :title="
          paused
            ? 'Продолжить смену фраз'
            : 'Приостановить смену фраз'
        "
        @click="paused = !paused"
      >
        <Icon
          :name="
            paused
              ? 'lucide:play'
              : 'lucide:pause'
          "
          class="size-3.5"
        />
      </button> -->
    </div>
  </div>
</template>

<style scoped>
.rotating-text {
  min-width: 0;
}

.rotating-text__animation,
.rotating-text__static {
  font-size: clamp(0.8125rem, 3.5vw, 1.75rem);
  line-height: 2;
}

.rotating-text__animation {
  max-width: 100%;
}

.rotating-text__animation--paused,
.rotating-text__animation--paused * {
  animation-play-state: paused !important;
}

.rotating-text__static {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .rotating-text__animation,
  .rotating-text__toggle {
    display: none;
  }

  .rotating-text__animation,
  .rotating-text__animation * {
    animation: none !important;
  }

  .rotating-text__static {
    display: inline;
  }
}
</style>