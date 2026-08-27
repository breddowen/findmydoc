<!-- ./frontend/app/components/ui/Modal.vue -->
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
  maxWidthClass: {
    type: String,
    default: 'max-w-lg',
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

useBodyScrollLock(opened)

function close() {
  model.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
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
    <Transition name="ui-modal">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 relative flex max-h-[calc(100dvh-2rem)] w-full flex-col overflow-hidden rounded-2xl shadow-2xl"
          :class="maxWidthClass"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-5 py-4"
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

          <div class="min-h-0 flex-1 overflow-y-auto px-5 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-5 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-modal-enter-active,
.ui-modal-leave-active {
  transition: opacity 180ms ease;
}

.ui-modal-enter-active section,
.ui-modal-leave-active section {
  transition:
    transform 180ms ease,
    opacity 180ms ease;
}

.ui-modal-enter-from,
.ui-modal-leave-to {
  opacity: 0;
}

.ui-modal-enter-from section,
.ui-modal-leave-to section {
  opacity: 0;
  transform: scale(0.96) translateY(0.5rem);
}
</style>