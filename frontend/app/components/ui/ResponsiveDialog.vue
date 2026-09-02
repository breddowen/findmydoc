<!-- ./frontend/app/components/ui/ResponsiveDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

defineProps({
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

const { isClientReady } = useClientReady()

const { matches: isDesktop } = useBreakpoint(
  '(min-width: 768px)',
)
</script>

<template>
  <!--
    Modal и BottomSheet появляются только после
    завершения hydration. Это предотвращает отличие
    серверного DOM от клиентского.
  -->
  <template v-if="isClientReady">
    <UiModal
      v-if="isDesktop"
      v-model="model"
      :title="title"
      :close-on-backdrop="closeOnBackdrop"
      :show-close-button="showCloseButton"
      :max-width-class="maxWidthClass"
      @close="emit('close')"
      @opened="emit('opened')"
    >
      <template
        v-if="$slots.header"
        #header
      >
        <slot name="header" />
      </template>

      <slot />

      <template
        v-if="$slots.footer"
        #footer
      >
        <slot name="footer" />
      </template>
    </UiModal>

    <UiBottomSheet
      v-else
      v-model="model"
      :title="title"
      :close-on-backdrop="closeOnBackdrop"
      :show-close-button="showCloseButton"
      @close="emit('close')"
      @opened="emit('opened')"
    >
      <template
        v-if="$slots.header"
        #header
      >
        <slot name="header" />
      </template>

      <slot />

      <template
        v-if="$slots.footer"
        #footer
      >
        <slot name="footer" />
      </template>
    </UiBottomSheet>
  </template>
</template>