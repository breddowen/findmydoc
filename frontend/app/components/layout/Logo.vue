<!-- frontend\app\components\layout\Logo.vue -->

<script setup>
const props = defineProps({
  to: {
    type: String,
    default: '/dashboard',
  },

  variant: {
    type: String,
    default: 'navbar',
    validator: value => [
      'navbar',
      'auth',
      'sidebar',
      'footer',
    ].includes(value),
  },

  showTagline: {
    type: Boolean,
    default: true,
  },
})

const isNavbar = computed(
  () => props.variant === 'navbar',
)

const isAuth = computed(
  () => props.variant === 'auth',
)

const isSidebar = computed(
  () => props.variant === 'sidebar',
)

const isFooter = computed(
  () => props.variant === 'footer',
)
</script>

<template>
  <NuxtLink
    :to="to"
    class="group inline-flex min-w-0 shrink-0 flex-col items-center justify-center text-center"
    :class="{
      'text-base-content': !isFooter,
      'text-neutral-content': isFooter,
    }"
    aria-label="MentalConnect — перейти на главную"
  >
    <img
      src="/logo.png"
      alt="MentalConnect"
      class="block shrink-0 object-contain transition-transform duration-200 group-hover:scale-[1.03]"
      :class="{
        'size-9 sm:size-11': isNavbar,
        'size-20 sm:size-24': isAuth,
        'size-9 is-drawer-open:size-12': isSidebar,
        'size-10': isFooter,
      }"
    >

    <span
      v-if="showTagline"
      class="font-medium tracking-wide"
      :class="{
        'text-base-content/70 mt-0.5 hidden max-w-44 whitespace-nowrap text-[10px] leading-tight sm:block':
          isNavbar,

        'text-base-content/70 mt-2 text-sm leading-snug sm:text-base':
          isAuth,

        'text-base-content/70 mt-1.5 hidden max-w-52 whitespace-nowrap text-xs leading-snug is-drawer-open:block':
          isSidebar,

        'text-neutral-content/75 mt-1 max-w-48 text-[11px] leading-snug':
          isFooter,
      }"
    >
      Связь, которая не прерывается
    </span>
  </NuxtLink>
</template>