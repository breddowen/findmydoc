<!-- ./frontend/app/components/patients/ContactStatus.vue -->
<script setup>
defineProps({
  allowed: {
    type: Boolean,
    default: false,
  },
  doNotCall: {
    type: Boolean,
    default: false,
  },
  showText: {
    type: Boolean,
    default: true,
  },
})
</script>

<template>
  <div
    v-if="allowed && !doNotCall"
    class="text-success flex items-center gap-2"
    title="Пациент разрешил связаться"
  >
    <Icon
      name="lucide:phone-call"
      class="size-5"
    />

    <span
      v-if="showText"
      class="text-sm"
    >
      Контакт разрешён
    </span>
  </div>

  <div
    v-else
    class="text-base-content/40 flex items-center gap-2"
    :class="{
      'text-error': doNotCall,
    }"
    :title="
      doNotCall
        ? 'Пациент просит не звонить'
        : 'Разрешение на контакт не получено'
    "
  >
    <Icon
      name="lucide:phone-off"
      class="size-5"
    />

    <span
      v-if="showText"
      class="text-sm"
    >
      {{
        doNotCall
          ? 'Не звонить'
          : 'Нет разрешения'
      }}
    </span>
  </div>
</template>