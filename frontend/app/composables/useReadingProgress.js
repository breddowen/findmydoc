// ./frontend/app/composables/useReadingProgress.js

const MIN_TRACKABLE_SCROLL_DISTANCE = 240

export function useReadingProgress(target) {
  const progress = ref(0)
  const isTrackable = ref(false)

  let animationFrame = null
  let resizeObserver = null

  function getMetrics() {
    const element = target.value

    if (!element) {
      isTrackable.value = false
      return null
    }

    const rect =
      element.getBoundingClientRect()

    const elementTop =
      rect.top + window.scrollY

    const elementHeight =
      element.offsetHeight

    const maxPageScroll = Math.max(
      document.documentElement.scrollHeight
        - window.innerHeight,
      0,
    )

    const articleEndScroll =
      elementTop
      + elementHeight
      - window.innerHeight

    // Сначала рассчитываем конечную позицию.
    const endPosition = Math.min(
      articleEndScroll,
      maxPageScroll,
    )

    // И только после этого доступную для чтения
    // дистанцию прокрутки.
    const rawReadableHeight =
      endPosition - elementTop

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
      rawReadableHeight,
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

    // До начала статьи прогресс равен нулю.
    if (currentPosition <= 0) {
      progress.value = 0
      return
    }

    // Для слишком короткой статьи допускаем
    // визуальное отображение прогресса, но
    // isTrackable останется false, поэтому
    // ARTICLE_READ зарегистрирован не будет.
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
    if (animationFrame !== null) return

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

    scheduleCalculate()
  }

  onMounted(() => {
    nextTick(() => {
      scheduleCalculate()

      if (target.value) {
        resizeObserver =
          new ResizeObserver(() => {
            scheduleCalculate()
          })

        resizeObserver.observe(
          target.value,
        )
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
    resizeObserver = null

    if (animationFrame !== null) {
      window.cancelAnimationFrame(
        animationFrame,
      )

      animationFrame = null
    }
  })

  return {
    progress: readonly(progress),
    isTrackable: readonly(isTrackable),
    calculate,
    restoreProgress,
  }
}