// ./frontend/app/stores/patient-support.js
export const usePatientSupportStore = defineStore(
  'patient-support',
  () => {
    const panel = ref(null)

    const allowedPanels = new Set([
      'actions',
      'assistant',
      'doctors',
    ])

    function open(value = 'actions') {
      if (allowedPanels.has(value)) {
        panel.value = value
      }
    }

    function close() {
      panel.value = null
    }

    return {
      panel,
      open,
      close,
    }
  },
)