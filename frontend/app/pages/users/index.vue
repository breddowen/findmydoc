<!-- ./frontend/app/pages/users/index.vue -->
<script setup>
definePageMeta({
  middleware: ['user-manager'],
})

const usersStore = useUsersStore()

const activeTab = ref('users')

const inviteDialogOpen = ref(false)
const linkDialogOpen = ref(false)

const createdInvitation = ref(null)
const emailSent = ref(false)

const processingInvitationId = ref('')
const errorMessage = ref('')
const message = ref('')

const userRoleFilters = [
  {
    value: '',
    label: 'Все',
    icon: 'lucide:users',
  },
  {
    value: 'patient',
    label: 'Пациенты',
    icon: 'lucide:user',
  },
  {
    value: 'doctor',
    label: 'Врачи',
    icon: 'lucide:stethoscope',
  },
  {
    value: 'relative',
    label: 'Родственники',
    icon: 'lucide:heart-handshake',
  },
  {
    value: 'med_assistant',
    label: 'Ассистенты',
    icon: 'lucide:briefcase-medical',
  },
  {
    value: 'superuser',
    label: 'Суперпользователи',
    icon: 'lucide:shield',
  },
]

const invitationTypeFilters = [
  {
    value: '',
    label: 'Все роли',
  },
  {
    value: 'patient',
    label: 'Пациенты',
  },
  {
    value: 'doctor',
    label: 'Врачи',
  },
  {
    value: 'relative',
    label: 'Родственники',
  },
  {
    value: 'med_assistant',
    label: 'Ассистенты',
  },
  {
    value: 'superuser',
    label: 'Суперпользователи',
  },
]

const invitationStatusFilters = [
  {
    value: '',
    label: 'Все статусы',
  },
  {
    value: 'pending',
    label: 'Активные',
  },
  {
    value: 'accepted',
    label: 'Принятые',
  },
  {
    value: 'expired',
    label: 'Истёкшие',
  },
  {
    value: 'revoked',
    label: 'Отозванные',
  },
]

let searchTimer = null

async function loadData() {
  errorMessage.value = ''

  try {
    await Promise.all([
      usersStore.fetchUsers(),
      usersStore.fetchInvitations(),
    ])
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить данные'
  }
}

function setUserRole(role) {
  usersStore.usersFilters.role = role
  usersStore.usersPage.page = 1

  usersStore.fetchUsers({
    page: 1,
    role,
  })
}

function handleSearchInput() {
  window.clearTimeout(searchTimer)

  searchTimer = window.setTimeout(() => {
    usersStore.fetchUsers({
      page: 1,
      search: usersStore.usersFilters.search,
    })
  }, 350)
}

function changeUsersPage(page) {
  usersStore.fetchUsers({
    page,
  })
}

function changeInvitationsPage(page) {
  usersStore.fetchInvitations({
    page,
  })
}

function applyInvitationFilters() {
  usersStore.fetchInvitations({
    page: 1,
    invitationType:
      usersStore.invitationsFilters.invitationType,
    status:
      usersStore.invitationsFilters.status,
  })
}

function handleCreated(invitation) {
  createdInvitation.value = invitation
  emailSent.value = false
  linkDialogOpen.value = true
}

async function sendCreatedInvitation() {
  if (!createdInvitation.value) return

  processingInvitationId.value =
    createdInvitation.value.invitation_id

  errorMessage.value = ''

  try {
    createdInvitation.value =
      await usersStore.sendInvitation(
        createdInvitation.value.invitation_id,
      )

    emailSent.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось отправить приглашение'

    await usersStore.fetchInvitations()
  } finally {
    processingInvitationId.value = ''
  }
}

async function sendInvitation(invitation) {
  processingInvitationId.value = invitation.id
  errorMessage.value = ''

  try {
    createdInvitation.value =
      await usersStore.sendInvitation(invitation.id)

    emailSent.value = true
    linkDialogOpen.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось отправить приглашение'
  } finally {
    processingInvitationId.value = ''
  }
}

async function revokeInvitation(invitation) {
  if (
    !window.confirm(
      `Отозвать приглашение для ${invitation.email}?`,
    )
  ) {
    return
  }

  processingInvitationId.value = invitation.id
  errorMessage.value = ''

  try {
    await usersStore.revokeInvitation(invitation.id)
    message.value = 'Приглашение отозвано'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось отозвать приглашение'
  } finally {
    processingInvitationId.value = ''
  }
}

async function toggleBlock(user, isBlocked) {
  errorMessage.value = ''

  try {
    await usersStore.setUserBlocked(
      user.id,
      isBlocked,
    )

    message.value = isBlocked
      ? 'Пользователь заблокирован'
      : 'Пользователь разблокирован'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить статус пользователя'
  }
}

async function deleteUser(user) {
  if (
    !window.confirm(
      `Удалить пользователя ${user.email}?`,
    )
  ) {
    return
  }

  errorMessage.value = ''

  try {
    await usersStore.deleteUser(user.id)
    message.value = 'Пользователь удалён'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось удалить пользователя'
  }
}

onMounted(loadData)

onBeforeUnmount(() => {
  window.clearTimeout(searchTimer)
})
</script>

<template>
  <div class="mx-auto max-w-6xl space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Пользователи
        </h1>

        <p class="text-base-content/60 mt-1">
          Аккаунты и приглашения пользователей.
        </p>
      </div>

      <button
        type="button"
        class="btn btn-primary"
        @click="inviteDialogOpen = true"
      >
        <Icon
          name="lucide:user-plus"
          class="size-5"
        />
        Добавить пользователя
      </button>
    </header>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm ml-auto"
        aria-label="Закрыть"
        @click="message = ''"
      >
        <Icon
          name="lucide:x"
          class="size-4"
        />
      </button>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <div role="tablist" class="tabs tabs-box">
      <button
        type="button"
        role="tab"
        class="tab"
        :class="{ 'tab-active': activeTab === 'users' }"
        @click="activeTab = 'users'"
      >
        Пользователи
      </button>

      <button
        type="button"
        role="tab"
        class="tab"
        :class="{
          'tab-active': activeTab === 'invitations',
        }"
        @click="activeTab = 'invitations'"
      >
        Приглашения
      </button>
    </div>

    <section
      v-if="activeTab === 'users'"
      class="space-y-5"
    >
      <div
        class="card bg-base-100 border-base-300 border"
      >
        <div class="card-body gap-4 p-4">
          <label
            class="input input-bordered flex items-center gap-2"
          >
            <Icon
              name="lucide:search"
              class="text-base-content/50 size-4"
            />

            <input
              v-model="usersStore.usersFilters.search"
              type="search"
              class="grow"
              placeholder="Поиск по email"
              @input="handleSearchInput"
            >
          </label>

          <div
            class="flex max-w-full gap-2 overflow-x-auto pb-1"
            aria-label="Фильтр по роли"
          >
            <button
              v-for="filter in userRoleFilters"
              :key="filter.value || 'all'"
              type="button"
              class="btn btn-sm shrink-0"
              :class="{
                'btn-primary':
                  usersStore.usersFilters.role
                  === filter.value,
                'btn-ghost':
                  usersStore.usersFilters.role
                  !== filter.value,
              }"
              @click="setUserRole(filter.value)"
            >
              <Icon
                :name="filter.icon"
                class="size-4"
              />
              {{ filter.label }}
            </button>
          </div>
        </div>
      </div>

      <UsersList
        :users="usersStore.users"
        :loading="usersStore.loadingUsers"
        @toggle-block="toggleBlock"
        @delete="deleteUser"
      />

      <UiPagination
        :model-value="usersStore.usersPage.page"
        :total-items="
          usersStore.usersPage.totalItems
        "
        :page-size="usersStore.usersPage.pageSize"
        @update:model-value="changeUsersPage"
      />
    </section>

    <section
      v-else
      class="space-y-5"
    >
      <div
        class="card bg-base-100 border-base-300 border"
      >
        <div
          class="card-body grid gap-3 p-4 sm:grid-cols-2"
        >
          <select
            v-model="
              usersStore.invitationsFilters
                .invitationType
            "
            class="select select-bordered w-full"
            aria-label="Фильтр по роли приглашения"
            @change="applyInvitationFilters"
          >
            <option
              v-for="filter in invitationTypeFilters"
              :key="filter.value || 'all'"
              :value="filter.value"
            >
              {{ filter.label }}
            </option>
          </select>

          <select
            v-model="
              usersStore.invitationsFilters.status
            "
            class="select select-bordered w-full"
            aria-label="Фильтр по статусу приглашения"
            @change="applyInvitationFilters"
          >
            <option
              v-for="filter in invitationStatusFilters"
              :key="filter.value || 'all'"
              :value="filter.value"
            >
              {{ filter.label }}
            </option>
          </select>
        </div>
      </div>

      <UsersInvitationList
        :invitations="usersStore.invitations"
        :loading="usersStore.loadingInvitations"
        :processing-id="processingInvitationId"
        @send="sendInvitation"
        @revoke="revokeInvitation"
      />

      <UiPagination
        :model-value="
          usersStore.invitationsPage.page
        "
        :total-items="
          usersStore.invitationsPage.totalItems
        "
        :page-size="
          usersStore.invitationsPage.pageSize
        "
        @update:model-value="changeInvitationsPage"
      />
    </section>
  </div>

  <UsersInviteDialog
    v-model="inviteDialogOpen"
    @created="handleCreated"
  />

  <InvitationsLinkDialog
    v-model="linkDialogOpen"
    :url="createdInvitation?.registration_url || ''"
    :email="createdInvitation?.email || ''"
    title="Приглашение создано"
    description="Передайте пользователю ссылку или покажите QR-код."
    can-send-email
    :sending-email="Boolean(processingInvitationId)"
    :email-sent="emailSent"
    @send-email="sendCreatedInvitation"
  />
</template>