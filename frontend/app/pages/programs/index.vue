<!-- ./frontend/app/pages/programs/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useProgramsStore()

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const errorMessage = ref('')

const visibilityDialogOpen = ref(false)
const selectedProgram = ref(null)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

function openHideDialog(program) {
  selectedProgram.value = program
  visibilityDialogOpen.value = true
}

async function showProgram(program) {
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      program.id,
      false,
    )

    Object.assign(program, response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось показать программу'
  }
}

function handleHidden(response) {
  const item = store.programs.find(
    (program) => program.id === response.id,
  )

  if (item) {
    Object.assign(item, response)
  }
}

onMounted(async () => {
  try {
    if (auth.activeRole === 'patient') {
      await store.fetchProgramsForPatient()
    } else {
      await store.fetchProgramsForStaff()
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Программы
        </h1>

        <p class="text-base-content/60 mt-1">
          Пошаговые программы работы с материалами.
        </p>
      </div>

      <NuxtLink
        v-if="canManage"
        to="/programs/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая программа
      </NuxtLink>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="store.programs.length"
      class="grid gap-5 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="program in store.programs"
        :key="program.id"
        :class="[
          program.is_popular
            ? 'aura aura-rainbow'
            : '',
          'h-full',
        ]"
      >
        <article
          class="card bg-base-100 border-base-300 relative h-full overflow-hidden border"
          :class="{
            'opacity-60': program.is_hidden,
          }"
        >
          <div
            v-if="program.is_popular"
            class="bg-warning text-warning-content absolute right-0 top-0 rounded-bl-2xl px-4 py-2 text-xs font-bold shadow"
          >
            <Icon
              name="lucide:flame"
              class="mr-1 inline size-4"
            />
            Популярное
          </div>

          <div class="card-body">
            <div class="flex flex-wrap gap-2 pr-24">
              <span
                v-if="hasDiscount(program)"
                class="badge badge-error gap-1 font-bold"
              >
                <Icon
                  name="lucide:badge-percent"
                  class="size-3"
                />
                −{{ program.service?.discount_percent }}%
              </span>

              <span
                v-if="program.has_program_access"
                class="badge badge-success"
              >
                Полный доступ
              </span>

              <span
                v-if="program.purchase_requested"
                class="badge badge-warning"
              >
                Запрос отправлен
              </span>

              <span
                v-if="program.is_hidden"
                class="badge badge-ghost"
              >
                Скрыта
              </span>
            </div>

            <h2 class="card-title mt-2">
              {{ program.title }}
            </h2>

            <p
              class="text-base-content/60 line-clamp-3 text-sm"
            >
              {{ program.description }}
            </p>

            <div class="mt-2 flex items-end gap-2">
              <span class="text-primary text-xl font-bold">
                {{ formatFinalPrice(program) }}
              </span>

              <span
                v-if="hasDiscount(program)"
                class="text-base-content/40 text-sm line-through"
              >
                {{ formatOriginalPrice(program) }}
              </span>
            </div>

            <div class="mt-2 flex flex-wrap gap-1">
              <span
                v-for="tag in program.tags"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <div class="card-actions mt-auto pt-5">
              <NuxtLink
                :to="`/programs/${program.id}`"
                class="btn btn-primary btn-sm"
              >
                Открыть
              </NuxtLink>

              <NuxtLink
                v-if="canManage"
                :to="`/programs/${program.id}/edit`"
                class="btn btn-outline btn-sm"
              >
                <Icon
                  name="lucide:pencil"
                  class="size-4"
                />
                Изменить
              </NuxtLink>

              <button
                v-if="canManage && !program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="openHideDialog(program)"
              >
                <Icon
                  name="lucide:eye-off"
                  class="size-4"
                />
                Скрыть
              </button>

              <button
                v-if="canManage && program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="showProgram(program)"
              >
                <Icon
                  name="lucide:eye"
                  class="size-4"
                />
                Показать
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:route"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Программ пока нет
      </p>
    </div>
  </div>

  <ProgramsVisibilityDialog
    v-model="visibilityDialogOpen"
    :program="selectedProgram"
    @hidden="handleHidden"
  />
</template>