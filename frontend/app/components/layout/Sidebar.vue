<!-- ./frontend/app/components/layout/Sidebar.vue -->
<script setup>
const ui = useUiStore()
const route = useRoute()

const {
  isStaff,
  navigationGroups,
} = useAppNavigation()

function isLinkActive(link) {
  if (!link?.to) return false

  if (route.path === link.to) {
    return true
  }

  if (link.exact) {
    return false
  }

  return (
    link.to !== '/dashboard'
    && route.path.startsWith(`${link.to}/`)
  )
}

function handleNavigation() {
  if (
    import.meta.client
    && window.innerWidth < 1024
  ) {
    ui.closeSidebar()
  }
}

watch(
  () => isStaff.value,
  (value) => {
    if (!value) {
      // Закрываем только временный мобильный drawer.
      // Desktop-предпочтение пользователя сохраняется.
      ui.closeMobileSidebar()
    }
  },
)
</script>

<template>
  <div
    class="min-h-dvh"
    :class="{
      'drawer lg:drawer-open': isStaff,
    }"
  >
    <input
      v-if="isStaff"
      id="staff-sidebar-drawer"
      v-model="ui.sidebarOpen"
      type="checkbox"
      class="drawer-toggle"
    >

    <div
      class="min-w-0"
      :class="{
        'drawer-content': isStaff,
      }"
    >
      <slot />
    </div>

    <div
      v-if="isStaff"
      class="drawer-side z-50 is-drawer-close:overflow-visible"
    >
      <label
        for="staff-sidebar-drawer"
        aria-label="Закрыть меню"
        class="drawer-overlay"
      />

      <aside
        class="bg-base-100 border-base-300 flex min-h-full flex-col border-r transition-[width] duration-200 is-drawer-close:w-16 is-drawer-open:w-72"
      >
        <div
          class="border-base-300 flex h-16 shrink-0 items-center justify-center border-b px-2 transition-[height] duration-200 is-drawer-open:h-24"
        >
          <LayoutLogo
            to="/dashboard"
            variant="sidebar"
            class="hover:bg-base-200 w-full overflow-hidden rounded-box px-2 py-1.5 transition-colors"
            @click="handleNavigation"
          />
        </div>

        <nav
          class="min-h-0 flex-1 overflow-y-auto overflow-x-hidden p-2"
          aria-label="Навигация сотрудников"
        >
          <ul class="menu w-full gap-1 p-0">
            <template
              v-for="group in navigationGroups"
              :key="group.key"
            >
              <li
                class="menu-title mt-4 px-3 first:mt-1 is-drawer-close:hidden"
              >
                <span>{{ group.label }}</span>
              </li>

              <li
                v-for="link in group.links"
                :key="link.to"
              >
                <NuxtLink
                  :to="link.to"
                  class="is-drawer-close:tooltip is-drawer-close:tooltip-right"
                  :class="{
                    'menu-active': isLinkActive(link),
                  }"
                  :data-tip="link.label"
                  :aria-current="
                    isLinkActive(link)
                      ? 'page'
                      : undefined
                  "
                  @click="handleNavigation"
                >
                  <Icon
                    :name="link.icon"
                    class="size-5 shrink-0"
                  />

                  <span
                    class="whitespace-nowrap is-drawer-close:hidden"
                  >
                    {{ link.label }}
                  </span>
                </NuxtLink>
              </li>
            </template>
          </ul>
        </nav>

        <div
          class="border-base-300 shrink-0 border-t p-2"
        >
          <button
            type="button"
            class="btn btn-ghost w-full justify-start overflow-hidden px-3"
            :aria-label="
              ui.sidebarOpen
                ? 'Свернуть боковое меню'
                : 'Развернуть боковое меню'
            "
            @click="ui.toggleSidebar"
          >
            <Icon
              :name="
                ui.sidebarOpen
                  ? 'lucide:panel-left-close'
                  : 'lucide:panel-left-open'
              "
              class="size-5 shrink-0"
            />

            <span
              class="ml-2 whitespace-nowrap is-drawer-close:hidden"
            >
              Свернуть меню
            </span>
          </button>
        </div>
      </aside>
    </div>
  </div>
</template>