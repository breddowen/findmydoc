<!-- ./frontend/app/components/layout/Footer.vue -->
<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer
    class="bg-neutral text-neutral-content mt-auto px-4 py-3"
  >
    <div
      class="mx-auto flex max-w-7xl flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center text-xs sm:flex-nowrap"
    >
      <Icon
        name="lucide:brain-circuit"
        class="size-5 shrink-0"
      />

      <span>
        Разработка — Максим Титков
      </span>

      <span
        class="hidden opacity-40 sm:inline"
        aria-hidden="true"
      >
        •
      </span>

      <a
        href="mailto:mtitkov@emcmos.ru"
        class="link whitespace-nowrap"
      >
        mtitkov@emcmos.ru
      </a>

      <span
        class="hidden opacity-40 sm:inline"
        aria-hidden="true"
      >
        •
      </span>

      <span class="whitespace-nowrap opacity-70">
        © {{ currentYear }}. Все права защищены.
      </span>
    </div>
  </footer>
</template>