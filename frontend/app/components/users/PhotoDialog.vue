<!-- ./frontend/app/components/users/PhotoDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

defineProps({
  user: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits(['saved'])

const busy = ref(false)

watch(model, (open) => {
  if (!open) {
    busy.value = false
  }
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Фотография врача"
    max-width-class="max-w-2xl"
    :persistent="busy"
    :close-on-backdrop="!busy"
    :show-close-button="!busy"
  >
    <template v-if="model && user">
      <p class="mb-4 font-medium">
        {{ user.full_name || user.email }}
      </p>

      <MediaEntityEditor
        :key="user.id"
        purpose="doctor"
        :entity-id="user.id"
        @busy="busy = $event"
        @saved="emit('saved', $event)"
      />
    </template>
  </UiResponsiveDialog>
</template>