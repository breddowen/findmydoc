// ./frontend/app/composables/useReadingProgress.js

export function useReadingProgress(target) {
  const progress = ref(0)

  let animationFrame = null
  let resizeObserver = null

  function getMetrics() {
    const element = target.value

    if (!element) return null

    const rect = element.getBoundingClientRect()

    const elementTop =
      rect.top + window.scrollY

    const elementHeight =
      element.offsetHeight

    const maxPageScroll = Math.max(
      document.documentElement.scrollHeight
        - window.innerHeight,
      0,
    )

    const articleEndScroll = elementTop + elementHeight - window.innerHeight

    const rawReadableHeight = endPosition - elementTop

    const endPosition = Math.min(
      articleEndScroll,
      maxPageScroll,
    )

    isTrackable.value =
      rawReadableHeight
      >= MIN_TRACKABLE_SCROLL_DISTANCE

    const readableHeight = Math.max(
      rawReadableHeight,
      1,
    )

    return {
      elementTop,
      readableHeight,
      endPosition,
    }
  }

  function calculate() {
    const metrics = getMetrics()

    if (!metrics) return

    const {
      elementTop,
      readableHeight,
      endPosition,
    } = metrics

    const currentPosition =
      window.scrollY - elementTop

    // Важный момент: сначала проверяем начало.
    // Иначе при временно маленькой высоте страницы
    // endPosition может оказаться <= elementTop
    // и мы ошибочно получим 100%.
    if (currentPosition <= 0) {
      progress.value = 0
      return
    }

    if (window.scrollY >= endPosition - 2) {
      progress.value = 100
      return
    }

    progress.value = Math.round(
      Math.min(
        Math.max(
          currentPosition
            / readableHeight
            * 100,
          0,
        ),
        100,
      ),
    )
  }

  function scheduleCalculate() {
    if (animationFrame) return

    animationFrame =
      window.requestAnimationFrame(() => {
        calculate()
        animationFrame = null
      })
  }

  function restoreProgress(percent) {
    if (percent <= 0) return

    const metrics = getMetrics()

    if (!metrics) return

    const {
      elementTop,
      readableHeight,
    } = metrics

    window.scrollTo({
      top:
        elementTop
        + readableHeight
        * Math.min(percent, 100)
        / 100,
      behavior: 'instant',
    })

    // Синхронизируем progress после scrollTo.
    scheduleCalculate()
  }

  onMounted(() => {
    nextTick(() => {
      scheduleCalculate()

      if (target.value) {
        resizeObserver = new ResizeObserver(() => {
          scheduleCalculate()
        })

        resizeObserver.observe(target.value)
      }
    })

    window.addEventListener(
      'scroll',
      scheduleCalculate,
      {
        passive: true,
      },
    )

    window.addEventListener(
      'resize',
      scheduleCalculate,
    )
  })

  onBeforeUnmount(() => {
    window.removeEventListener(
      'scroll',
      scheduleCalculate,
    )

    window.removeEventListener(
      'resize',
      scheduleCalculate,
    )

    resizeObserver?.disconnect()

    if (animationFrame) {
      window.cancelAnimationFrame(
        animationFrame,
      )
    }
  })

  return {
    progress: readonly(progress),
    isTrackable: readonly(isTrackable),
    calculate,
    restoreProgress,
  }
}