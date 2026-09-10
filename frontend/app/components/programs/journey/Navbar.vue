<!-- ./frontend/app/components/programs/journey/Navbar.vue -->
<script setup>
const route = useRoute()
const auth = useAuthStore()
const userStore = useUserStore()
const notifications = useNotificationsStore()
const store = useProgramJourneyStore()

const {
  navigationGroups,
} = useAppNavigation()

const {
  program,
  stages,
  started,
  selectedIndex,
  selectedStage,
  nextStage,
  stageProgress,
  isStageCompleted,
  selectStage,
} = useProgramJourney()

const menuOpen = ref(false)
const stagesOpen = ref(false)

const stageCompleted = computed(() =>
  isStageCompleted(selectedStage.value),
)

async function chooseStage(stageId) {
  stagesOpen.value = false
  await selectStage(stageId)
}

async function startProgram() {
  const successful = await store.start()

  if (successful && selectedStage.value) {
    // В частности, сохраняет выбранный этап в URL.
    // Если начало было из материала, возвращает к этапу.
    await selectStage(selectedStage.value.id)
  }
}

watch(
  () => route.fullPath,
  () => {
    menuOpen.value = false
    stagesOpen.value = false
  },
)

onMounted(() => {
  notifications.connect()

  void notifications.fetchUnreadCount().catch(() => {})
})

onBeforeUnmount(() => {
  notifications.disconnect()
})
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
      class="mx-auto flex h-16 w-full max-w-7xl items-center gap-2 px-3 sm:h-20 sm:px-4"
    >
      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm shrink-0"
        aria-label="Открыть меню"
        @click="menuOpen = true"
      >
        <Icon name="lucide:menu" class="size-5" />
      </button>

      <div class="flex min-w-0 flex-1 items-center gap-2">
        <template v-if="program && !started">
          <button
            type="button"
            class="btn btn-primary btn-sm shrink-0"
            :disabled="store.starting"
            @click="startProgram"
          >
            <span
              v-if="store.starting"
              class="loading loading-spinner loading-xs"
            />
            <Icon
              v-else
              name="lucide:play"
              class="size-4"
            />

            Начать программу
          </button>

          <span class="text-base-content/60 hidden truncate text-sm lg:block">
            {{ program.title }}
          </span>
        </template>

        <template v-else-if="selectedStage">
          <div class="min-w-0 flex-1 py-1 md:max-w-md">
            <div class="stack stack-end w-full">
              <button
                :key="selectedStage.id"
                type="button"
                class="stage-front card border-base-300 h-11 w-full border px-3 text-left sm:h-12"
                :class="
                  stageCompleted
                    ? 'bg-base-200 text-base-content/60'
                    : 'bg-base-100 text-base-content'
                "
                aria-haspopup="dialog"
                :aria-label="
                  `Выбрать этап. Сейчас этап ${selectedIndex + 1}`
                  + ` из ${stages.length}: ${selectedStage.title}`
                "
                @click="stagesOpen = true"
              >
                <span class="flex h-full min-w-0 items-center gap-2">
                  <span class="min-w-0 flex-1">
                    <span class="text-base-content/55 block text-[10px] leading-3">
                      Этап {{ selectedIndex + 1 }} из {{ stages.length }}
                      <span v-if="stageCompleted"> · Выполнен</span>
                    </span>

                    <span class="mt-0.5 block truncate text-sm font-semibold">
                      {{ selectedStage.title }}
                    </span>
                  </span>

                  <Icon
                    :name="
                      stageCompleted
                        ? 'lucide:circle-check'
                        : 'lucide:chevrons-up-down'
                    "
                    class="size-4 shrink-0"
                    :class="stageCompleted ? 'text-success' : 'text-base-content/45'"
                  />
                </span>
              </button>

              <div
                v-for="layer in Math.min(2, stages.length - 1)"
                :key="layer"
                aria-hidden="true"
                class="card border-base-300 bg-base-200 h-11 w-full border sm:h-12"
              />
            </div>
          </div>

          <button
            type="button"
            class="btn btn-circle btn-ghost btn-sm shrink-0"
            :disabled="!nextStage"
            aria-label="Следующий этап"
            title="Следующий этап"
            @click="chooseStage(nextStage.id)"
          >
            <Icon name="lucide:chevron-right" class="size-5" />
          </button>
        </template>

        <span
          v-else-if="store.loading"
          class="loading loading-spinner loading-sm"
          aria-label="Загрузка программы"
        />

        <span v-else class="text-base-content/60 text-sm">
          Программа
        </span>
      </div>

      <div class="flex shrink-0 items-center gap-1">
        <NotificationsCenter />

        <div class="hidden items-center gap-1 md:flex">
          <LayoutThemeToggle />

          <NuxtLink
            to="/settings/profile"
            class="btn btn-circle btn-ghost btn-sm"
            :title="userStore.fullName || 'Личные данные'"
            aria-label="Личные данные"
          >
            <span
              class="bg-primary text-primary-content flex size-8 items-center justify-center rounded-full text-xs"
            >
              {{ userStore.initials }}
            </span>
          </NuxtLink>
        </div>
      </div>
    </div>

    <progress
      v-if="started && selectedStage"
      class="journey-progress absolute inset-x-0 bottom-0 h-[3px] w-full"
      :value="stageProgress"
      max="100"
      :aria-label="`Прогресс этапа ${selectedIndex + 1}`"
    />
  </header>

  <UiResponsiveDialog
    v-model="menuOpen"
    title="Меню"
    max-width-class="max-w-md"
  >
    <NuxtLink
      to="/dashboard"
      class="btn btn-primary btn-outline mb-4 w-full justify-start"
      @click="menuOpen = false"
    >
      <Icon name="lucide:arrow-left" class="size-5" />
      Выйти из программы
    </NuxtLink>

    <div class="border-base-300 mb-4 flex items-center justify-between gap-3 border-b pb-4">
      <div class="min-w-0">
        <p class="truncate font-medium">
          {{ userStore.fullName }}
        </p>
        <p class="text-base-content/60 truncate text-xs">
          {{ userStore.user?.email }}
        </p>
      </div>

      <LayoutThemeToggle />
    </div>

    <nav>
      <ul class="menu w-full gap-1 p-0">
        <template
          v-for="group in navigationGroups"
          :key="group.key"
        >
          <li class="menu-title mt-2">
            {{ group.label }}
          </li>

          <li
            v-for="link in group.links"
            :key="link.to"
          >
            <NuxtLink
              :to="link.to"
              @click="menuOpen = false"
            >
              <Icon :name="link.icon" class="size-5" />
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
        Выйти из аккаунта
      </button>
    </template>
  </UiResponsiveDialog>

  <UiResponsiveDialog
    v-model="stagesOpen"
    title="Этапы программы"
    max-width-class="max-w-lg"
  >
    <div class="space-y-2">
      <button
        v-for="(stage, index) in stages"
        :key="stage.id"
        type="button"
        class="border-base-300 flex w-full items-center gap-3 rounded-2xl border p-3 text-left"
        :class="{
          'bg-primary/5 border-primary/50':
            stage.id === selectedStage?.id,
          'bg-base-200 text-base-content/65':
            isStageCompleted(stage),
        }"
        :aria-current="stage.id === selectedStage?.id ? 'step' : undefined"
        @click="chooseStage(stage.id)"
      >
        <Icon
          :name="
            isStageCompleted(stage)
              ? 'lucide:circle-check'
              : 'lucide:circle'
          "
          class="size-5 shrink-0"
          :class="isStageCompleted(stage) ? 'text-success' : 'text-primary'"
        />

        <span class="min-w-0 flex-1">
          <span class="text-base-content/55 block text-xs">
            Этап {{ index + 1 }}
            <span v-if="isStageCompleted(stage)"> · Выполнен</span>
          </span>

          <span class="mt-1 block font-medium">
            {{ stage.title }}
          </span>
        </span>

        <span class="text-base-content/60 text-xs">
          {{ stage.progress_percent }}%
        </span>
      </button>
    </div>
  </UiResponsiveDialog>
</template>

<style scoped>
.journey-progress {
  display: block;
  appearance: none;
  overflow: hidden;
  border: 0;
  border-radius: 0;
  background: var(--color-base-300);
}

.journey-progress::-webkit-progress-bar {
  background: var(--color-base-300);
}

.journey-progress::-webkit-progress-value {
  background: linear-gradient(
    90deg,
    color-mix(in srgb, var(--color-primary) 30%, var(--color-base-100)),
    var(--color-primary)
  );
  transition: width 250ms ease;
}

.journey-progress::-moz-progress-bar {
  background: linear-gradient(
    90deg,
    color-mix(in srgb, var(--color-primary) 30%, var(--color-base-100)),
    var(--color-primary)
  );
}

.stage-front {
  animation: stage-appear 180ms ease-out;
}

@keyframes stage-appear {
  from {
    opacity: 0.55;
    translate: 0.4rem 0;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .stage-front {
    animation: none;
  }

  .journey-progress::-webkit-progress-value {
    transition: none;
  }
}
</style>