<!-- ./frontend/app/pages/dashboard.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()

const { isClientReady } = useClientReady()

const roleNames = {
  superuser: 'Суперпользователь',
  med_assistant: 'Медицинский ассистент',
  doctor: 'Врач',
  patient: 'Пациент',
  relative: 'Родственник',
}

const staffRoles = [
  'doctor',
  'med_assistant',
  'superuser',
]

const activeRoleName = computed(() => {
  if (!isClientReady.value) {
    return ''
  }

  return (
    roleNames[auth.activeRole]
    || auth.activeRole
    || ''
  )
})

const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient'
)

const isStaff = computed(() =>
  isClientReady.value
  && staffRoles.includes(auth.activeRole)
)

onMounted(async () => {
  if (!userStore.user) {
    await userStore.fetchMe()
  }
})
</script>

<template>
  <div class="space-y-6">
    <!-- Приветствие -->
    <section
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-8"
    >
      <p
        class="text-base-content/60 min-h-5 text-sm"
      >
        <span v-if="isClientReady">
          {{ activeRoleName }}
        </span>
      </p>

      <h1
        class="mt-1 text-xl font-bold sm:text-2xl"
      >
        Здравствуйте,
        {{ userStore.user?.first_name || 'пользователь' }}
      </h1>
    </section>

    <!-- Dashboard пациента -->
    <AssignmentsPatientList
      v-if="isPatient"
    />

    <ArticlesPatientOverview
      v-if="isPatient"
    />

    <ConsentsAssistantContact
      v-if="isPatient"
    />

    <!-- Dashboard сотрудников -->
    <section
      v-if="isStaff"
      class="space-y-4"
    >
      <div
        class="flex items-center justify-between gap-4"
      >
        <h2 class="text-xl font-bold sm:text-2xl">
          Пациенты
        </h2>

        <NuxtLink
          to="/patients"
          class="btn btn-ghost btn-sm"
        >
          Открыть весь список
        </NuxtLink>
      </div>

      <PatientsList
        compact
        :page-size="10"
      />
    </section>

    <!-- Общие настройки -->
    <section
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <NuxtLink
        to="/settings/security"
        class="card bg-base-100 border-base-300 hover:border-primary border transition"
      >
        <div class="card-body">
          <div
            class="bg-primary/10 text-primary flex size-12 items-center justify-center rounded-2xl"
          >
            <Icon
              name="lucide:shield-check"
              class="size-6"
            />
          </div>

          <h2 class="card-title mt-2">
            Безопасность
          </h2>

          <p class="text-base-content/60 text-sm">
            Добавьте passkey или измените пароль.
          </p>
        </div>
      </NuxtLink>

      <div
        class="card bg-base-100 border-base-300 border"
      >
        <div class="card-body">
          <div
            class="bg-secondary/10 text-secondary flex size-12 items-center justify-center rounded-2xl"
          >
            <Icon
              name="lucide:tags"
              class="size-6"
            />
          </div>

          <h2 class="card-title mt-2">
            Активная роль
          </h2>

          <p
            class="text-base-content/60 min-h-5 text-sm"
          >
            <span v-if="isClientReady">
              {{ activeRoleName }}
            </span>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>