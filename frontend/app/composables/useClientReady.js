// ./frontend/app/composables/useClientReady.js
export function useClientReady() {
  const isClientReady = ref(false)

  onMounted(() => {
    isClientReady.value = true
  })

  return {
    isClientReady: readonly(isClientReady),
  }
}