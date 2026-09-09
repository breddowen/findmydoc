<!-- frontend\app\components\patient\home\Recommendations.vue -->
<script setup>
const props = defineProps({
  programs: {
    type: Array,
    default: () => [],
  },
})

const emit = defineEmits([
  'request-purchase',
])

const { matches: isDesktop } = useBreakpoint(
  '(min-width: 768px)',
)

const { matches: isWide } = useBreakpoint(
  '(min-width: 1280px)',
)

const carousel = ref(null)
const mobileIndex = ref(0)
const page = ref(1)

const pageSize = computed(() =>
  isWide.value ? 3 : 2,
)

const pagePrograms = computed(() => {
  const start = (page.value - 1) * pageSize.value

  return props.programs.slice(
    start,
    start + pageSize.value,
  )
})

function updateMobileIndex() {
  const element = carousel.value

  if (!element || !element.children.length) {
    mobileIndex.value = 0
    return
  }

  // У последней карточки может не хватать места,
  // чтобы её левый край совпал с краем контейнера.
  const remainingScroll =
    element.scrollWidth
    - element.clientWidth
    - element.scrollLeft

  if (remainingScroll <= 2) {
    mobileIndex.value = props.programs.length - 1
    return
  }

  const containerLeft =
    element.getBoundingClientRect().left

  let closestIndex = 0
  let closestDistance = Infinity

  Array.from(element.children).forEach(
    (child, index) => {
      const distance = Math.abs(
        child.getBoundingClientRect().left
        - containerLeft,
      )

      if (distance < closestDistance) {
        closestDistance = distance
        closestIndex = index
      }
    },
  )

  mobileIndex.value = closestIndex
}

function moveMobile(direction) {
  const element = carousel.value

  if (!element || !props.programs.length) return

  const targetIndex = Math.min(
    Math.max(
      mobileIndex.value + direction,
      0,
    ),
    props.programs.length - 1,
  )

  const target = element.children[targetIndex]

  if (!target) return

  const targetLeft =
    element.scrollLeft
    + target.getBoundingClientRect().left
    - element.getBoundingClientRect().left

  const reduceMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)',
  ).matches

  element.scrollTo({
    left: targetLeft,
    behavior: reduceMotion ? 'instant' : 'smooth',
  })
}

// При смене состава или режима отображения
// возвращаемся к началу списка.
watch(
  [
    () => props.programs.map(
      program => program.id,
    ).join(','),
    isDesktop,
    pageSize,
  ],
  async () => {
    page.value = 1
    mobileIndex.value = 0

    await nextTick()

    carousel.value?.scrollTo({
      left: 0,
      behavior: 'instant',
    })
  },
)
</script>

<template>
  <section
    v-if="programs.length"
    class="min-w-0 space-y-3"
    aria-labelledby="patient-recommendations-title"
  >
    <header>
      <h2
        id="patient-recommendations-title"
        class="text-xl font-bold sm:text-2xl"
      >
        Рекомендуемые программы
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Подобраны по направлениям,
        заданным для Вас.
      </p>
    </header>

    <!-- Средние и широкие экраны -->
    <template v-if="isDesktop">
      <div
        class="grid items-stretch gap-4"
        :class="
          isWide
            ? 'grid-cols-3'
            : 'grid-cols-2'
        "
      >
        <PatientProgramCard
          v-for="program in pagePrograms"
          :key="program.id"
          :program="program"
          :show-steps="false"
          class="min-w-0"
          @request-purchase="
            emit('request-purchase', $event)
          "
        />
      </div>

      <UiPagination
        v-model="page"
        :total-items="programs.length"
        :page-size="pageSize"
      />
    </template>

    <!-- Телефоны -->
    <template v-else>
      <div
        ref="carousel"
        class="carousel w-full min-w-0 items-stretch gap-4 rounded-2xl"
        role="region"
        aria-label="Рекомендуемые программы"
        aria-roledescription="карусель"
        @scroll.passive="updateMobileIndex"
      >
        <div
          v-for="(program, index) in programs"
          :key="program.id"
          class="carousel-item min-w-0 snap-start"
          :class="
            programs.length === 1
              ? 'w-full'
              : 'w-[88%]'
          "
          role="group"
          aria-roledescription="слайд"
          :aria-label="
            `${index + 1} из ${programs.length}`
          "
        >
          <PatientProgramCard
            :program="program"
            :show-steps="false"
            class="h-full w-full min-w-0"
            @request-purchase="
              emit('request-purchase', $event)
            "
          />
        </div>
      </div>

      <nav
        v-if="programs.length > 1"
        class="flex items-center justify-center gap-3"
        aria-label="Переключение рекомендуемых программ"
      >
        <button
          type="button"
          class="btn btn-circle btn-sm"
          :disabled="mobileIndex === 0"
          aria-label="Предыдущая программа"
          @click="moveMobile(-1)"
        >
          <Icon
            name="lucide:chevron-left"
            class="size-4"
          />
        </button>

        <span
          class="text-base-content/60 min-w-16 text-center text-sm tabular-nums"
        >
          {{ mobileIndex + 1 }}
          из {{ programs.length }}
        </span>

        <button
          type="button"
          class="btn btn-circle btn-sm"
          :disabled="
            mobileIndex >= programs.length - 1
          "
          aria-label="Следующая программа"
          @click="moveMobile(1)"
        >
          <Icon
            name="lucide:chevron-right"
            class="size-4"
          />
        </button>
      </nav>
    </template>
  </section>
</template>