// ./frontend/app/composables/useBreakpoint.js
export function useBreakpoint(query = '(min-width: 768px)') {
  const matches = ref(false)
  let mediaQuery = null

  function updateMatches(event) {
    matches.value = event.matches
  }

  onMounted(() => {
    mediaQuery = window.matchMedia(query)
    matches.value = mediaQuery.matches

    mediaQuery.addEventListener(
      'change',
      updateMatches,
    )
  })

  onBeforeUnmount(() => {
    mediaQuery?.removeEventListener(
      'change',
      updateMatches,
    )
  })

  return {
    matches,
  }
}