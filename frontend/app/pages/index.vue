<script setup>
const route = useRoute()

onMounted(() => {
  void navigateTo(
    {
      path: '/dashboard',
      query: route.query,
      hash: route.hash,
    },
    {
      replace: true,
    },
  )
})
</script>

<template>
  <p
    class="text-base-content/60 py-6 text-center text-sm"
    role="status"
  >
    Открываем главную…
  </p>
</template>