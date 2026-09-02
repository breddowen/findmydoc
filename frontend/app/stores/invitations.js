// ./frontend/app/stores/invitations.js
export const useInvitationsStore = defineStore(
  'invitations',
  () => {
    const preparingPatient = ref(false)
    const sendingEmail = ref(false)

    async function preparePatient(payload) {
      const { $api } = useNuxtApp()

      preparingPatient.value = true

      try {
        return await $api(
          '/api/v1/invitations/patients/prepare',
          {
            method: 'POST',
            body: payload,
          },
        )
      } finally {
        preparingPatient.value = false
      }
    }

    async function sendPatientInvitation(
      invitationId,
    ) {
      const { $api } = useNuxtApp()

      sendingEmail.value = true

      try {
        return await $api(
          `/api/v1/invitations/patients/${invitationId}/send`,
          {
            method: 'POST',
          },
        )
      } finally {
        sendingEmail.value = false
      }
    }

    return {
      preparingPatient,
      sendingEmail,

      preparePatient,
      sendPatientInvitation,
    }
  },
)