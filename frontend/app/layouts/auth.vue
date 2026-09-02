<!-- ./frontend/app/layouts/auth.vue -->
<script setup>
</script>

<template>
  <div class="bg-base-200 min-h-dvh">
    <div
      class="safe-area-top fixed inset-x-0 top-0 z-20 flex justify-end p-3"
    >
      <LayoutThemeToggle />
    </div>

    <main
      class="flex min-h-dvh items-center justify-center px-4 py-16"
    >
      <div class="w-full max-w-md">
        <div class="mb-7 flex justify-center">
          <LayoutLogo
            to="/login"
            variant="auth"
          />
        </div>

        <slot />
      </div>
    </main>
  </div>
</template>