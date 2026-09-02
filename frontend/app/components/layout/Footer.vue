<!-- ./frontend/app/components/layout/Footer.vue -->
<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer
    class="bg-neutral text-neutral-content mt-auto px-4 py-4"
  >
    <div
      class="mx-auto flex w-full max-w-7xl flex-col items-center justify-between gap-4 sm:flex-row"
    >
      <LayoutLogo
        to="/dashboard"
        variant="footer"
      />

      <div
        class="flex flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center text-xs sm:justify-end sm:text-right"
      >
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
          class="link whitespace-nowrap opacity-80 transition-opacity hover:opacity-100"
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
    </div>
  </footer>
</template>