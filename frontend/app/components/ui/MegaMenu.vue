<!-- ./frontend/app/components/ui/MegaMenu.vue -->
<script setup>
defineOptions({
  inheritAttrs: false,
})

const props = defineProps({
  groups: {
    type: Array,
    default: () => [],
  },
  sizeClass: {
    type: String,
    default: 'megamenu-sm',
  },
  wide: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits([
  'navigate',
])

const route = useRoute()

const componentId = useId().replace(
  /[^a-zA-Z0-9_-]/g,
  '',
)

const openPopoverId = ref('')

function normalizeKey(value) {
  return String(value)
    .replace(/[^a-zA-Z0-9_-]/g, '-')
}

function popoverId(group, index) {
  const key = normalizeKey(group.key || index)

  return `mega-${componentId}-${key}`
}

function isLinkActive(link) {
  if (!link?.to) return false

  if (route.path === link.to) {
    return true
  }

  return (
    link.to !== '/dashboard'
    && route.path.startsWith(`${link.to}/`)
  )
}

function isGroupActive(group) {
  return group.links?.some(isLinkActive) || false
}

function handleToggle(event, id) {
  if (event.newState === 'open') {
    openPopoverId.value = id
    return
  }

  if (openPopoverId.value === id) {
    openPopoverId.value = ''
  }
}

function closePopover(event) {
  const popover = event.currentTarget.closest(
    '[popover]',
  )

  popover?.hidePopover?.()
  openPopoverId.value = ''

  emit('navigate')
}

watch(
  () => route.fullPath,
  () => {
    if (!import.meta.client) return

    document
      .querySelectorAll('[id^="mega-"][popover]')
      .forEach((popover) => {
        if (popover.matches(':popover-open')) {
          popover.hidePopover?.()
        }
      })

    openPopoverId.value = ''
  },
)
</script>

<template>
  <nav
    v-bind="$attrs"
    class="megamenu border-base-300 bg-base-100 border p-1"
    :class="[
      sizeClass,
      {
        'megamenu-wide': wide,
      },
    ]"
    aria-label="Основная навигация"
  >
    <span class="megamenu-active" />

    <template
      v-for="(group, index) in groups"
      :key="group.key || index"
    >
      <button
        type="button"
        :popovertarget="popoverId(group, index)"
        class="gap-2"
        :class="{
          'text-primary': isGroupActive(group),
        }"
        :aria-expanded="
          openPopoverId === popoverId(group, index)
        "
      >
        <Icon
          v-if="group.icon"
          :name="group.icon"
          class="size-4"
        />

        {{ group.label }}

        <Icon
          name="lucide:chevron-down"
          class="size-3.5 transition-transform"
          :class="{
            'rotate-180':
              openPopoverId
              === popoverId(group, index),
          }"
        />
      </button>

      <div
        :id="popoverId(group, index)"
        popover="auto"
        class="bg-base-100 border-base-300 w-80 max-w-[calc(100vw-2rem)] rounded-box border p-2 shadow-xl"
        @toggle="
          handleToggle(
            $event,
            popoverId(group, index),
          )
        "
      >
        <ul class="menu w-full">
          <li
            v-for="link in group.links"
            :key="link.to"
          >
            <NuxtLink
              :to="link.to"
              class="items-start gap-3 py-3"
              :class="{
                'menu-active': isLinkActive(link),
              }"
              :aria-current="
                isLinkActive(link) ? 'page' : undefined
              "
              @click="closePopover"
            >
              <span
                class="bg-base-200 flex size-9 shrink-0 items-center justify-center rounded-xl"
              >
                <Icon
                  :name="link.icon || 'lucide:link'"
                  class="size-4"
                />
              </span>

              <span class="min-w-0">
                <span class="block font-medium">
                  {{ link.label }}
                </span>

                <span
                  v-if="link.description"
                  class="text-base-content/55 mt-0.5 block text-xs font-normal"
                >
                  {{ link.description }}
                </span>
              </span>
            </NuxtLink>
          </li>
        </ul>
      </div>
    </template>
  </nav>
</template>