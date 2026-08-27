<!-- ./frontend/app/components/layout/Navbar.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()

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

const { isClientReady } = useClientReady()

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

const isStaff = computed(() =>
  isClientReady.value
  && staffRoles.includes(auth.activeRole)
)

const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient'
)

const canManageContent = computed(() =>
  isClientReady.value
  && [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole)
)

const mobileMenuOpen = ref(false)

function closeMobileMenu() {
  mobileMenuOpen.value = false
}
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
      class="navbar mx-auto min-h-16 max-w-7xl px-3 sm:px-4"
    >
      <div class="navbar-start min-w-0">
        <button
          type="button"
          class="btn btn-circle btn-ghost lg:hidden"
          aria-label="Открыть меню"
          @click="mobileMenuOpen = true"
        >
          <Icon
            name="lucide:menu"
            class="size-5"
          />
        </button>

        <NuxtLink
          to="/dashboard"
          class="btn btn-ghost px-2 text-lg font-bold"
        >
          MentalMe
        </NuxtLink>
      </div>

      <nav class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal gap-1 px-1">
          <li>
            <NuxtLink to="/dashboard">
              <Icon
                name="lucide:layout-dashboard"
                class="size-4"
              />
              Главная
            </NuxtLink>
          </li>

          <li v-if="isStaff">
            <NuxtLink to="/patients">
              <Icon
                name="lucide:users"
                class="size-4"
              />
              Пациенты
            </NuxtLink>
          </li>

          <li>
            <NuxtLink to="/content/articles">
              <Icon
                name="lucide:file-text"
                class="size-4"
              />
              Статьи
            </NuxtLink>
          </li>

          <li v-if="isPatient">
            <NuxtLink to="/questionnaires">
              <Icon
                name="lucide:clipboard-list"
                class="size-4"
              />
              Опросники
            </NuxtLink>
          </li>

          <li v-if="canManageContent">
            <NuxtLink to="/content/questionnaires">
              <Icon
                name="lucide:clipboard-list"
                class="size-4"
              />
              Опросники
            </NuxtLink>
          </li>

          <!-- Программы доступны всем ролям -->
          <li>
            <NuxtLink to="/programs">
              <Icon
                name="lucide:route"
                class="size-4"
              />
              Программы
            </NuxtLink>
          </li>

          <!-- Конфигуратор только для ассистента
               и суперпользователя -->
          <li v-if="canManageContent">
            <NuxtLink to="/programs/new">
              <Icon
                name="lucide:workflow"
                class="size-4"
              />
              Конфигуратор
            </NuxtLink>
          </li>

          <li>
            <NuxtLink to="/settings/security">
              <Icon
                name="lucide:shield-check"
                class="size-4"
              />
              Безопасность
            </NuxtLink>
          </li>
        </ul>
      </nav>

      <div class="navbar-end gap-1">
        <NotificationsCenter />

        <LayoutThemeToggle />

        <div class="dropdown dropdown-end">
          <button
            type="button"
            tabindex="0"
            class="btn btn-ghost gap-2 px-2"
          >
            <div
              class="avatar avatar-placeholder"
            >
              <div
                class="bg-primary text-primary-content w-9 rounded-full"
              >
                <span class="text-sm">
                  {{ userStore.initials }}
                </span>
              </div>
            </div>

            <div
              class="hidden max-w-44 text-left sm:block"
            >
              <p class="truncate text-sm font-medium">
                {{ userStore.fullName }}
              </p>

              <p
                class="text-base-content/60 min-h-4 truncate text-xs"
              >
                <span v-if="isClientReady">
                  {{ activeRoleName }}
                </span>
              </p>
            </div>

            <Icon
              name="lucide:chevron-down"
              class="hidden size-4 sm:block"
            />
          </button>

          <ul
            tabindex="0"
            class="menu dropdown-content bg-base-100 border-base-300 z-50 mt-2 w-64 rounded-box border p-2 shadow-xl"
          >
            <li class="menu-title">
              <span class="truncate">
                {{ userStore.user?.email }}
              </span>
            </li>

            <li>
              <NuxtLink to="/settings/security">
                <Icon
                  name="lucide:key-round"
                  class="size-4"
                />
                Passkey и пароль
              </NuxtLink>
            </li>

            <li>
              <button
                type="button"
                class="text-error"
                @click="auth.logout"
              >
                <Icon
                  name="lucide:log-out"
                  class="size-4"
                />
                Выйти
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>

  <UiBottomSheet
    v-model="mobileMenuOpen"
    title="Меню"
  >
    <nav>
      <ul class="menu w-full gap-2 p-0 text-base">
        <li>
          <NuxtLink
            to="/dashboard"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:layout-dashboard"
              class="size-5"
            />
            Главная
          </NuxtLink>
        </li>

        <li v-if="isStaff">
          <NuxtLink
            to="/patients"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:users"
              class="size-5"
            />
            Пациенты
          </NuxtLink>
        </li>

        <li>
          <NuxtLink
            to="/content/articles"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:file-text"
              class="size-5"
            />
            Статьи
          </NuxtLink>
        </li>

        <li v-if="isPatient">
          <NuxtLink
            to="/questionnaires"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:clipboard-list"
              class="size-5"
            />
            Опросники
          </NuxtLink>
        </li>

        <li v-if="canManageContent">
          <NuxtLink
            to="/content/questionnaires"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:clipboard-list"
              class="size-5"
            />
            Опросники
          </NuxtLink>
        </li>

        <li>
          <NuxtLink
            to="/programs"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:route"
              class="size-5"
            />
            Программы
          </NuxtLink>
        </li>

        <li v-if="canManageContent">
          <NuxtLink
            to="/programs/new"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:workflow"
              class="size-5"
            />
            Конфигуратор
          </NuxtLink>
        </li>

        <li>
          <NuxtLink
            to="/settings/security"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:shield-check"
              class="size-5"
            />
            Безопасность
          </NuxtLink>
        </li>
      </ul>
    </nav>

    <template #footer>
      <button
        type="button"
        class="btn btn-error btn-outline w-full"
        @click="auth.logout"
      >
        <Icon
          name="lucide:log-out"
          class="size-4"
        />
        Выйти
      </button>
    </template>
  </UiBottomSheet>
</template>