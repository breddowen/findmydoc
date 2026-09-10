// ./frontend/app/composables/useFooterAwarePosition.js
export function useFooterAwarePosition() {
  const route = useRoute()

  const footerOverlap = ref(0)

  let mounted = false
  let frame = null
  let resizeObserver = null

  const floatingStyle = computed(() => ({
    right: 'calc(1rem + env(safe-area-inset-right, 0px))',

    bottom: (
      'calc(1rem'
      + ' + env(safe-area-inset-bottom, 0px)'
      + ` + ${footerOverlap.value}px)`
    ),
  }))

  function getFooters() {
    return document.querySelectorAll(
      '[data-floating-footer]',
    )
  }

  function updatePosition() {
    if (!mounted) return

    const viewportHeight = window.innerHeight

    let overlap = 0

    for (const footer of getFooters()) {
      const rect = footer.getBoundingClientRect()

      // Не учитываем скрытые элементы и Footer,
      // который находится вне видимой области.
      if (
        rect.width === 0
        || rect.height === 0
        || rect.bottom <= 0
        || rect.top >= viewportHeight
      ) {
        continue
      }

      overlap = Math.max(
        overlap,
        viewportHeight - rect.top,
      )
    }

    footerOverlap.value = Math.max(
      0,
      Math.ceil(overlap),
    )
  }

  function scheduleUpdate() {
    if (!mounted || frame !== null) return

    frame = window.requestAnimationFrame(() => {
      frame = null
      updatePosition()
    })
  }

  function observeLayout() {
    resizeObserver?.disconnect()

    if (!resizeObserver) return

    // Реагируем на изменение высоты страницы:
    // загрузку контента, раскрытие блоков и т. п.
    resizeObserver.observe(document.documentElement)

    if (document.body) {
      resizeObserver.observe(document.body)
    }

    for (const footer of getFooters()) {
      resizeObserver.observe(footer)
    }
  }

  watch(
    () => route.fullPath,
    async () => {
      await nextTick()

      if (!mounted) return

      observeLayout()
      scheduleUpdate()
    },
    { flush: 'post' },
  )

  onMounted(() => {
    mounted = true

    if ('ResizeObserver' in window) {
      resizeObserver = new ResizeObserver(
        scheduleUpdate,
      )
    }

    observeLayout()
    updatePosition()

    window.addEventListener(
      'scroll',
      scheduleUpdate,
      { passive: true },
    )

    window.addEventListener(
      'resize',
      scheduleUpdate,
    )
  })

  onBeforeUnmount(() => {
    mounted = false

    window.removeEventListener(
      'scroll',
      scheduleUpdate,
    )

    window.removeEventListener(
      'resize',
      scheduleUpdate,
    )

    resizeObserver?.disconnect()

    if (frame !== null) {
      window.cancelAnimationFrame(frame)
    }
  })

  return {
    floatingStyle,
  }
}