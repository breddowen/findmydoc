<!-- ./frontend/app/components/layout/Navbar.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()
const ui = useUiStore()

const {
  isStaff,
  activeRoleName,
  navigationGroups,
} = useAppNavigation()

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
      class="mx-auto grid min-h-16 w-full max-w-7xl grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-2 px-3 sm:px-4"
    >
      <div class="flex min-w-0 items-center">
        <button
          v-if="isStaff"
          type="button"
          class="btn btn-circle btn-ghost"
          :aria-label="
            ui.sidebarOpen
              ? 'Свернуть боковое меню'
              : 'Открыть боковое меню'
          "
          @click="ui.toggleSidebar"
        >
          <Icon
            :name="
              ui.sidebarOpen
                ? 'lucide:panel-left-close'
                : 'lucide:menu'
            "
            class="size-5"
          />
        </button>

        <button
          v-else
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
          v-if="!isStaff"
          to="/dashboard"
          class="btn btn-ghost shrink-0 px-2 text-lg font-bold"
        >
          MentalMe
        </NuxtLink>
      </div>

      <div
        v-if="!isStaff"
        class="hidden min-w-0 items-center justify-center px-2 lg:flex"
      >
        <UiMegaMenu
          :groups="navigationGroups"
          size-class="megamenu-sm"
        />
      </div>

      <div
        v-else
        class="text-base-content/60 min-w-0 truncate px-2 text-sm"
      >
        Рабочее пространство
      </div>

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
                {{ activeRoleName }}
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
    v-if="!isStaff"
    v-model="mobileMenuOpen"
    title="Меню"
  >
    <nav>
      <ul class="menu w-full gap-1 p-0 text-base">
        <template
          v-for="group in navigationGroups"
          :key="group.key"
        >
          <li class="menu-title mt-2 first:mt-0">
            <span>{{ group.label }}</span>
          </li>

          <li
            v-for="link in group.links"
            :key="link.to"
          >
            <NuxtLink
              :to="link.to"
              @click="closeMobileMenu"
            >
              <Icon
                :name="link.icon"
                class="size-5"
              />
              {{ link.label }}
            </NuxtLink>
          </li>
        </template>
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