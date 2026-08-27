<!-- ./frontend/app/components/patients/ProAccess.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
  enabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'updated',
])

const store = usePatientsStore()

const confirmOpen = ref(false)
const updating = ref(false)

async function confirm() {
  updating.value = true

  try {
    const response = await store.setPatientPro(
      props.patientId,
      !props.enabled,
    )

    emit('updated', response.pro_enabled)
    confirmOpen.value = false
  } finally {
    updating.value = false
  }
}
</script>

<template>
  <label
    class="border-base-300 flex cursor-pointer items-center gap-4 rounded-2xl border p-4"
  >
    <span>
      <span class="block font-medium">
        Общий доступ Pro
      </span>

      <span class="text-base-content/50 block text-xs">
        Отдельные Pro-статьи и опросники
      </span>
    </span>

    <input
      type="checkbox"
      class="toggle toggle-secondary"
      :checked="enabled"
      @change.prevent="confirmOpen = true"
    >
  </label>

  <UiResponsiveDialog
    v-model="confirmOpen"
    :title="
      enabled
        ? 'Отключить общий Pro'
        : 'Включить общий Pro'
    "
    max-width-class="max-w-md"
  >
    <p>
      {{
        enabled
          ? 'Пациент потеряет общий доступ к отдельному Pro-контенту. Доступы внутри приобретённых программ сохранятся.'
          : 'Пациент получит доступ к отдельным Pro-статьям и опросникам вне программ.'
      }}
    </p>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          :disabled="updating"
          @click="confirmOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn"
          :class="enabled ? 'btn-error' : 'btn-secondary'"
          :disabled="updating"
          @click="confirm"
        >
          <span
            v-if="updating"
            class="loading loading-spinner loading-sm"
          />

          Подтвердить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>