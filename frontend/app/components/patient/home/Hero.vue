<script setup>
import RotatingText from './RotatingText.vue'
</script>

<template>
  <section
    class="hero patient-home-hero border-base-300 bg-base-100 overflow-hidden rounded-3xl border"
    aria-labelledby="patient-home-hero-title"
  >
    <div
      class="hero-content w-full min-w-0 px-4 py-6 text-center sm:px-8 sm:py-8"
    >
      <div class="w-full min-w-0 max-w-2xl">
        <h1
          id="patient-home-hero-title"
          class="text-balance text-2xl font-bold leading-tight sm:text-3xl lg:text-4xl"
        >
          Помогаем улучшить
          <span class="text-primary">
            Вашу жизнь
          </span>
        </h1>

        <RotatingText class="mt-3 sm:mt-4" />

        <p
          class="text-base-content/65 mx-auto mt-3 max-w-lg text-pretty text-sm leading-relaxed sm:text-base"
        >
          Программы для самостоятельной работы
          и поддержки специалистов.<br>
          Шаг за шагом
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.patient-home-hero {
  min-height: 0;
  background-image: linear-gradient(
    135deg,
    color-mix(
      in oklab,
      var(--color-primary) 7%,
      transparent
    ),
    transparent 65%
  );
}
</style>