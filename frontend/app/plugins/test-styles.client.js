// ./frontend/app/plugins/test-styles.client.js
export default defineNuxtPlugin(() => {
  const auth = useAuthStore()
  const styles = useTestStylesStore()

  let element = document.getElementById('test-styles-overrides')

  watch(
    () => [auth.accessToken, auth.activeRole],
    ([token, role]) => {
      styles.setContext(token, role)
    },
    {
      immediate: true,
      flush: 'sync',
    },
  )

  watch(
    () => styles.appliedCss,
    (css) => {
      if (!css) {
        element?.remove()
        element = null
        return
      }

      if (!element) {
        element = document.createElement('style')
        element.id = 'test-styles-overrides'
        document.head.appendChild(element)
      }

      element.textContent = css
    },
    {
      immediate: true,
      flush: 'sync',
    },
  )
})