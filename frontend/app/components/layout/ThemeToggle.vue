<!-- ./frontend/app/components/layout/ThemeToggle.vue -->
<script setup>
const ui = useUiStore()
</script>

<template>
  <button
    type="button"
    class="btn btn-circle btn-ghost swap swap-rotate"
    :class="{ 'swap-active': ui.isDark }"
    :aria-label="
      ui.isDark
        ? 'Включить светлую тему'
        : 'Включить тёмную тему'
    "
    @click="ui.toggleTheme"
  >
    <Icon
      name="lucide:sun"
      class="swap-off size-5"
    />

    <Icon
      name="lucide:moon"
      class="swap-on size-5"
    />
  </button>
</template>