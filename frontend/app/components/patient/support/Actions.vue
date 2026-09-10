<!-- ./frontend/app/components/patient/support/Actions.vue -->
<script setup>
defineProps({
  footer: {
    type: Boolean,
    default: false,
  },
})

const support = usePatientSupportStore()
</script>

<template>
  <div
    class="grid gap-2"
    :class="footer ? 'sm:grid-cols-3' : 'grid-cols-1'"
  >
    <button
      type="button"
      class="btn btn-outline h-auto min-h-12 justify-start whitespace-normal py-3 text-left"
      :class="{ 'sm:justify-center': footer }"
      @click="support.open('assistant')"
    >
      <Icon name="lucide:phone" class="size-5 shrink-0" />
      Связаться с ассистентом
    </button>

    <button
      type="button"
      class="btn btn-outline h-auto min-h-12 justify-start whitespace-normal py-3 text-left"
      :class="{ 'sm:justify-center': footer }"
      @click="support.open('doctors')"
    >
      <Icon name="lucide:stethoscope" class="size-5 shrink-0" />
      Записаться к врачу
    </button>

    <NuxtLink
      to="/programs"
      class="btn btn-outline h-auto min-h-12 justify-start whitespace-normal py-3 text-left"
      :class="{ 'sm:justify-center': footer }"
      @click="support.close"
    >
      <Icon name="lucide:route" class="size-5 shrink-0" />
      Индивидуальные программы
    </NuxtLink>
  </div>
</template>