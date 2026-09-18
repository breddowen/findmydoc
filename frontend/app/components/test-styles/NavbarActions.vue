<!-- ./frontend/app/components/test-styles/NavbarActions.vue -->
<script setup>
const styles = useTestStylesStore()
const error = ref('')

const toggleLabel = computed(() =>
  styles.enabled ? 'Сбросить стили' : 'Вернуть стили',
)

const errorOpen = computed({
  get: () => Boolean(error.value),
  set: (value) => {
    if (!value) error.value = ''
  },
})

function toggle() {
  try {
    styles.toggle()
  } catch (cause) {
    error.value = cause.message
  }
}
</script>

<template>
  <div
    v-if="styles.available && styles.hasCustomStyles"
    class="flex shrink-0 items-center gap-1"
  >
    <button
      type="button"
      class="btn btn-ghost btn-sm px-2"
      :title="toggleLabel"
      :aria-label="toggleLabel"
      @click="toggle"
    >
      <Icon
        :name="
          styles.enabled
            ? 'lucide:rotate-ccw'
            : 'lucide:paintbrush'
        "
        class="size-4"
      />

      <span class="hidden xl:inline">
        {{ toggleLabel }}
      </span>
    </button>

    <TestStylesSendButton compact />
  </div>

  <UiResponsiveDialog
    v-model="errorOpen"
    title="Не удалось изменить оформление"
  >
    <p role="alert">{{ error }}</p>
  </UiResponsiveDialog>
</template>