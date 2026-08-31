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

const canManageUsers = computed(() =>
  isClientReady.value
  && [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole)
)

const canConfigurePrograms = computed(() =>
  isClientReady.value
  && [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole)
)

const navigationGroups = computed(() => {
  if (!isClientReady.value) {
    return []
  }

  const mainLinks = [
    {
      to: '/dashboard',
      label: 'Главная',
      icon: 'lucide:layout-dashboard',
      description: 'Обзор и последние действия',
    },
  ]

  if (isStaff.value) {
    mainLinks.push({
      to: '/patients',
      label: 'Пациенты',
      icon: 'lucide:users',
      description: 'Список и карточки пациентов',
    })
  }

  if (canManageUsers.value) {
    mainLinks.push({
      to: '/users',
      label: 'Пользователи',
      icon: 'lucide:user-cog',
      description: 'Аккаунты и приглашения',
    })
  }

  const contentLinks = [
    {
      to: '/content/articles',
      label: 'Статьи',
      icon: 'lucide:file-text',
      description: 'Материалы для пользователей',
    },
    {
      to: '/programs',
      label: 'Программы',
      icon: 'lucide:route',
      description: 'Программы сопровождения',
    },
  ]

  if (isPatient.value) {
    contentLinks.push({
      to: '/questionnaires',
      label: 'Опросники',
      icon: 'lucide:clipboard-list',
      description: 'Назначенные опросники',
    })
  }

  if (canManageContent.value) {
    contentLinks.push({
      to: '/content/questionnaires',
      label: 'Опросники',
      icon: 'lucide:clipboard-list',
      description: 'Редактор опросников',
    })
  }

  const groups = [
    {
      key: 'main',
      label: 'Работа',
      icon: 'lucide:briefcase',
      links: mainLinks,
    },
    {
      key: 'content',
      label: 'Контент',
      icon: 'lucide:files',
      links: contentLinks,
    },
  ]

  if (canConfigurePrograms.value) {
    groups.push({
      key: 'management',
      label: 'Управление',
      icon: 'lucide:settings-2',
      links: [
        {
          to: '/programs/new',
          label: 'Конфигуратор',
          icon: 'lucide:workflow',
          description: 'Создание программ',
        },
        {
          to: '/settings/directories',
          label: 'Справочники',
          icon: 'lucide:library',
          description: 'Специальности и теги',
        },
      ],
    })
  }

  groups.push({
    key: 'settings',
    label: 'Настройки',
    icon: 'lucide:settings',
    links: [
      {
        to: '/settings/security',
        label: 'Безопасность',
        icon: 'lucide:shield-check',
        description: 'Пароль и passkey',
      },
    ],
  })

  return groups
})
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
      class="mx-auto grid min-h-16 w-full max-w-7xl grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-2 px-3 sm:px-4"
    >
      <!-- Левая часть -->
      <div class="flex min-w-0 items-center">
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
          class="btn btn-ghost shrink-0 px-2 text-lg font-bold"
        >
          MentalMe
        </NuxtLink>
      </div>

      <!-- Центральная часть -->
      <div
        class="hidden min-w-0 items-center justify-center px-2 lg:flex"
      >
        <UiMegaMenu
          :groups="navigationGroups"
          size-class="megamenu-sm"
        />
      </div>

      <!-- Правая часть -->
      <div
        class="flex shrink-0 items-center justify-end gap-1"
      >
        <NotificationsCenter />

        <LayoutThemeToggle />

        <div class="dropdown dropdown-end">
          <button
            type="button"
            tabindex="0"
            class="btn btn-ghost gap-2 px-2"
          >
            <div class="avatar avatar-placeholder">
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

        <li v-if="canManageUsers">
          <NuxtLink
            to="/users"
            @click="closeMobileMenu"
          >
            <Icon
              name="lucide:user-cog"
              class="size-5"
            />
            Пользователи
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