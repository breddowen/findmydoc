// ./frontend/app/stores/users.js
export const useUsersStore = defineStore('users', () => {
  const users = ref([])
  const invitations = ref([])

  const usersPage = reactive({
    page: 1,
    pageSize: 20,
    totalItems: 0,
    totalPages: 1,
  })

  const invitationsPage = reactive({
    page: 1,
    pageSize: 20,
    totalItems: 0,
    totalPages: 1,
  })

  const usersFilters = reactive({
    search: '',
    role: '',
  })

  const invitationsFilters = reactive({
    invitationType: '',
    status: '',
  })

  const loadingUsers = ref(false)
  const loadingInvitations = ref(false)
  const creatingInvitation = ref(false)

  async function fetchUsers(options = {}) {
    const { $api } = useNuxtApp()

    if (options.page !== undefined) {
      usersPage.page = options.page
    }

    if (options.pageSize !== undefined) {
      usersPage.pageSize = options.pageSize
    }

    if (options.search !== undefined) {
      usersFilters.search = options.search
    }

    if (options.role !== undefined) {
      usersFilters.role = options.role
    }

    loadingUsers.value = true

    try {
      const response = await $api('/api/v1/users', {
        query: {
          page: usersPage.page,
          page_size: usersPage.pageSize,
          search:
            usersFilters.search.trim()
            || undefined,
          role:
            usersFilters.role
            || undefined,
        },
      })

      users.value = response.items

      usersPage.page = response.page
      usersPage.pageSize = response.page_size
      usersPage.totalItems = response.total_items
      usersPage.totalPages = response.total_pages

      return response
    } finally {
      loadingUsers.value = false
    }
  }

  async function fetchInvitations(options = {}) {
    const { $api } = useNuxtApp()

    if (options.page !== undefined) {
      invitationsPage.page = options.page
    }

    if (options.pageSize !== undefined) {
      invitationsPage.pageSize = options.pageSize
    }

    if (options.invitationType !== undefined) {
      invitationsFilters.invitationType =
        options.invitationType
    }

    if (options.status !== undefined) {
      invitationsFilters.status = options.status
    }

    loadingInvitations.value = true

    try {
      const response = await $api(
        '/api/v1/invitations/admin',
        {
          query: {
            page: invitationsPage.page,
            page_size: invitationsPage.pageSize,
            invitation_type:
              invitationsFilters.invitationType
              || undefined,
            status:
              invitationsFilters.status
              || undefined,
          },
        },
      )

      invitations.value = response.items

      invitationsPage.page = response.page
      invitationsPage.pageSize = response.page_size
      invitationsPage.totalItems =
        response.total_items
      invitationsPage.totalPages =
        response.total_pages

      return response
    } finally {
      loadingInvitations.value = false
    }
  }

  async function createInvitation(payload) {
    const { $api } = useNuxtApp()

    creatingInvitation.value = true

    try {
      const response = await $api(
        '/api/v1/invitations/admin',
        {
          method: 'POST',
          body: payload,
        },
      )

      await fetchInvitations({
        page: 1,
      })

      return response
    } finally {
      creatingInvitation.value = false
    }
  }

  async function sendInvitation(invitationId) {
    const { $api } = useNuxtApp()

    const response = await $api(
      `/api/v1/invitations/admin/${invitationId}/send`,
      {
        method: 'POST',
      },
    )

    await fetchInvitations()

    return response
  }

  async function revokeInvitation(invitationId) {
    const { $api } = useNuxtApp()

    const response = await $api(
      `/api/v1/invitations/${invitationId}/revoke`,
      {
        method: 'POST',
      },
    )

    await fetchInvitations()

    return response
  }

  async function setUserBlocked(userId, isBlocked) {
    const { $api } = useNuxtApp()

    const updatedUser = await $api(
      `/api/v1/users/${userId}/block`,
      {
        method: 'PATCH',
        body: {
          is_blocked: isBlocked,
        },
      },
    )

    const index = users.value.findIndex(
      item => item.id === userId,
    )

    if (index !== -1) {
      users.value[index] = updatedUser
    }

    return updatedUser
  }

  async function deleteUser(userId) {
    const { $api } = useNuxtApp()

    await $api(`/api/v1/users/${userId}`, {
      method: 'DELETE',
    })

    await fetchUsers()
  }

  function clear() {
    users.value = []
    invitations.value = []

    usersPage.page = 1
    usersPage.totalItems = 0
    usersPage.totalPages = 1

    invitationsPage.page = 1
    invitationsPage.totalItems = 0
    invitationsPage.totalPages = 1

    usersFilters.search = ''
    usersFilters.role = ''

    invitationsFilters.invitationType = ''
    invitationsFilters.status = ''
  }

  return {
    users,
    invitations,

    usersPage,
    invitationsPage,

    usersFilters,
    invitationsFilters,

    loadingUsers,
    loadingInvitations,
    creatingInvitation,

    fetchUsers,
    fetchInvitations,
    createInvitation,
    sendInvitation,
    revokeInvitation,
    setUserBlocked,
    deleteUser,
    clear,
  }
})