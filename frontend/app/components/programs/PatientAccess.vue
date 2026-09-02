<!-- ./frontend/app/components/programs/PatientAccess.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const confirmOpen = ref(false)
const selectedProgram = ref(null)

const errorMessage = ref('')

function requestToggle(program) {
  selectedProgram.value = program
  confirmOpen.value = true
}

async function confirmToggle() {
  if (!selectedProgram.value) return

  try {
    await store.setPatientProgramAccess(
      props.patientId,
      selectedProgram.value.program_id,
      !selectedProgram.value.is_active,
    )

    confirmOpen.value = false
    selectedProgram.value = null
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить доступ'
  }
}

const sortedPrograms = computed(() =>
  [...store.patientAccessPrograms].sort(
    (first, second) => {
      if (
        first.purchase_requested
        !== second.purchase_requested
      ) {
        return first.purchase_requested
          ? -1
          : 1
      }

      return first.title.localeCompare(
        second.title,
        'ru',
      )
    },
  ),
)

onMounted(async () => {
  try {
    await store.fetchPatientProgramAccess(
      props.patientId,
    )
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
  <section
    class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
  >
    <div>
      <h2 class="text-xl font-bold">
        Доступ к программам
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Включение открывает Pro-контент только внутри
        выбранной программы.
      </p>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-4"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="3"
    />

    <div
      v-else
      class="mt-5 space-y-3"
    >
      <div
        v-for="program in sortedPrograms"
        :key="program.program_id"
        class="border-base-300 flex flex-col gap-4 rounded-2xl border p-4 sm:flex-row sm:items-center"
        :class="{
          'border-warning bg-warning/5 ring-warning/10 ring-4':
            program.purchase_requested,
        }"
      >
        <div class="min-w-0 flex-1">
          <div class="flex flex-wrap items-center gap-2">
            <p class="font-medium">
              {{ program.title }}
            </p>

            <span
              v-if="program.purchase_requested"
              class="badge badge-warning badge-sm gap-1"
            >
              <Icon
                name="lucide:shopping-cart"
                class="size-3"
              />
              Пациент запросил доступ
            </span>

            <span
              v-if="program.is_hidden"
              class="badge badge-ghost badge-sm"
            >
              Скрыта
            </span>
          </div>

          <div
            class="text-base-content/60 mt-2 flex flex-wrap items-center gap-2 text-sm"
          >
            <span
              v-if="program.service?.code"
              class="font-mono"
            >
              {{ program.service.code }}
            </span>

            <strong>
              {{ formatFinalPrice(program) }}
            </strong>

            <span
              v-if="hasDiscount(program)"
              class="text-base-content/40 line-through"
            >
              {{ formatOriginalPrice(program) }}
            </span>
          </div>
        </div>

        <label
          class="flex cursor-pointer items-center gap-3"
        >
          <span class="text-sm">
            {{
              program.is_active
                ? 'Доступ открыт'
                : 'Нет доступа'
            }}
          </span>

          <input
            type="checkbox"
            class="toggle toggle-success"
            :checked="program.is_active"
            @change.prevent="requestToggle(program)"
          >
        </label>
      </div>
    </div>
  </section>

  <UiResponsiveDialog
    v-model="confirmOpen"
    :title="
      selectedProgram?.is_active
        ? 'Отключить доступ'
        : 'Открыть доступ'
    "
    max-width-class="max-w-md"
  >
    <p>
      {{
        selectedProgram?.is_active
          ? 'Пациент потеряет доступ к Pro-контенту внутри программы.'
          : 'Пациент получит доступ ко всему Pro-контенту внутри программы.'
      }}
    </p>

    <p class="mt-3 font-semibold">
      {{ selectedProgram?.title }}
    </p>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          @click="confirmOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn"
          :class="
            selectedProgram?.is_active
              ? 'btn-error'
              : 'btn-success'
          "
          @click="confirmToggle"
        >
          Подтвердить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>