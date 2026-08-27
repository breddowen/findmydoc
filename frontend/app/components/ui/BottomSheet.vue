<!-- ./frontend/app/components/ui/BottomSheet.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true,
  },
  showCloseButton: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

const translateY = ref(0)
const dragging = ref(false)

let pointerStartY = 0

useBodyScrollLock(opened)

const sheetStyle = computed(() => ({
  transform: translateY.value
    ? `translateY(${translateY.value}px)`
    : undefined,
  transition: dragging.value
    ? 'none'
    : 'transform 180ms ease',
}))

function close() {
  model.value = false
  translateY.value = 0
  dragging.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handlePointerDown(event) {
  dragging.value = true
  pointerStartY = event.clientY

  event.currentTarget.setPointerCapture?.(
    event.pointerId,
  )
}

function handlePointerMove(event) {
  if (!dragging.value) return

  translateY.value = Math.max(
    0,
    event.clientY - pointerStartY,
  )
}

function handlePointerUp() {
  if (!dragging.value) return

  dragging.value = false

  if (translateY.value > 100) {
    close()
    return
  }

  translateY.value = 0
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
    translateY.value = 0
    emit('opened')
  }
})

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'keydown',
    handleKeydown,
  )
})
</script>

<template>
  <Teleport to="body">
    <Transition name="ui-sheet">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-end bg-black/50 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 safe-area-bottom flex max-h-[92dvh] w-full flex-col overflow-hidden rounded-t-3xl shadow-2xl"
          :style="sheetStyle"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <div
            class="flex shrink-0 touch-none justify-center py-3"
            @pointerdown="handlePointerDown"
            @pointermove="handlePointerMove"
            @pointerup="handlePointerUp"
            @pointercancel="handlePointerUp"
          >
            <div
              class="bg-base-300 h-1.5 w-12 rounded-full"
            />
          </div>

          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-4 pb-4"
          >
            <slot name="header">
              <h2 class="min-w-0 flex-1 text-lg font-semibold">
                {{ title }}
              </h2>
            </slot>

            <button
              v-if="showCloseButton"
              type="button"
              class="btn btn-circle btn-ghost btn-sm shrink-0"
              aria-label="Закрыть"
              @click="close"
            >
              <Icon
                name="lucide:x"
                class="size-5"
              />
            </button>
          </header>

          <div class="min-h-0 flex-1 overflow-y-auto px-4 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-4 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-sheet-enter-active,
.ui-sheet-leave-active {
  transition: opacity 220ms ease;
}

.ui-sheet-enter-active section,
.ui-sheet-leave-active section {
  transition: transform 220ms ease;
}

.ui-sheet-enter-from,
.ui-sheet-leave-to {
  opacity: 0;
}

.ui-sheet-enter-from section,
.ui-sheet-leave-to section {
  transform: translateY(100%);
}
</style>