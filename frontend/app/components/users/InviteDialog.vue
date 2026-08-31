<!-- ./frontend/app/components/users/InviteDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const emit = defineEmits([
  'created',
])

function handleCreated(invitation) {
  model.value = false
  emit('created', invitation)
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Добавить пользователя"
    max-width-class="max-w-xl"
  >
    <UsersInviteForm
      @created="handleCreated"
      @cancel="model = false"
    />
  </UiResponsiveDialog>
</template>