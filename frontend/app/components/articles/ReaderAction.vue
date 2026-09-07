<!-- ./frontend/app/components/articles/ReaderAction.vue -->
<script setup>
const props = defineProps({
  target: {
    type: Object,
    default: null,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['close'])

const atBoundary = ref(true)
const scrolling = ref(false)

const showClose = computed(() =>
  atBoundary.value && !scrolling.value,
)

let frame = null
let scrollTimer = null
let resizeObserver = null
let mounted = false

const EDGE_DISTANCE = 48

function getBounds() {
  const element = props.target

  if (!element) return null

  const rect = element.getBoundingClientRect()
  const scrollY = window.scrollY
  const viewportHeight = window.innerHeight

  const maxScroll = Math.max(
    document.documentElement.scrollHeight - viewportHeight,
    0,
  )

  const articleTop = rect.top + scrollY
  const articleBottom = rect.bottom + scrollY

  const start = Math.min(
    maxScroll,
    Math.max(0, articleTop - 16),
  )

  const end = Math.min(
    maxScroll,
    Math.max(start, articleBottom - viewportHeight),
  )

  return {
    start,
    end,
    shortArticle: rect.height <= viewportHeight,
  }
}

function updateBoundary() {
  const bounds = getBounds()

  if (!bounds) {
    atBoundary.value = true
    return
  }

  atBoundary.value =
    bounds.shortArticle
    || window.scrollY <= bounds.start + EDGE_DISTANCE
    || window.scrollY >= bounds.end - EDGE_DISTANCE
}

function scheduleUpdate() {
  if (frame !== null) return

  frame = window.requestAnimationFrame(() => {
    frame = null
    updateBoundary()
  })
}

function handleScroll() {
  scrolling.value = true

  window.clearTimeout(scrollTimer)
  scheduleUpdate()

  scrollTimer = window.setTimeout(() => {
    scrolling.value = false
    updateBoundary()
  }, 180)
}

function scrollToStart() {
  const bounds = getBounds()

  if (!bounds) return

  const reduceMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)',
  ).matches

  window.scrollTo({
    top: bounds.start,
    behavior: reduceMotion ? 'instant' : 'smooth',
  })
}

function handleClick() {
  if (props.disabled) return

  if (showClose.value) {
    emit('close')
  } else {
    scrollToStart()
  }
}

function observeTarget() {
  resizeObserver?.disconnect()

  if (!mounted || !props.target) return

  resizeObserver = new ResizeObserver(scheduleUpdate)
  resizeObserver.observe(props.target)
  resizeObserver.observe(document.documentElement)

  scheduleUpdate()
}

watch(
  () => props.target,
  observeTarget,
  { flush: 'post' },
)

onMounted(() => {
  mounted = true
  observeTarget()
  updateBoundary()

  window.addEventListener('scroll', handleScroll, {
    passive: true,
  })
  window.addEventListener('resize', scheduleUpdate)
})

onBeforeUnmount(() => {
  mounted = false

  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', scheduleUpdate)

  window.clearTimeout(scrollTimer)
  resizeObserver?.disconnect()

  if (frame !== null) {
    window.cancelAnimationFrame(frame)
  }
})
</script>

<template>
  <div
    class="fixed z-[60]"
    style="
      right: calc(1rem + env(safe-area-inset-right, 0px));
      bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
    "
  >
    <button
      type="button"
      class="btn btn-circle btn-lg border-base-300 bg-base-200 text-base-content hover:bg-base-300 shadow-lg"
      :disabled="disabled"
      :aria-label="showClose ? 'Закрыть статью' : 'В начало статьи'"
      :title="showClose ? 'Закрыть статью' : 'В начало статьи'"
      @click="handleClick"
    >
      <span
        v-if="disabled"
        class="loading loading-spinner loading-sm"
      />

      <Icon
        v-else
        :name="showClose ? 'lucide:x' : 'lucide:arrow-up'"
        class="size-6"
      />
    </button>
  </div>
</template>