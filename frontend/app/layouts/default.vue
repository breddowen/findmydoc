<!-- ./frontend/app/layouts/default.vue -->
<script setup>
</script>

<template>
  <LayoutSidebar>
    <div
      class="bg-base-200 flex min-h-dvh min-w-0 flex-col"
    >
      <LayoutEmailVerificationBanner />
      <LayoutNavbar />

      <main
        class="mx-auto w-full max-w-7xl flex-1 px-4 py-6 sm:py-8"
      >
        <slot />
      </main>

      <LayoutFooter />
    </div>
  </LayoutSidebar>
</template>