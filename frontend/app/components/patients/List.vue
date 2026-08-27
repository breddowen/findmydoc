<!-- ./frontend/app/components/patients/List.vue -->
<script setup>
const props = defineProps({
  compact: {
    type: Boolean,
    default: false,
  },
  pageSize: {
    type: Number,
    default: 10,
  },
  showSearch: {
    type: Boolean,
    default: true,
  },
})

const store = usePatientsStore()

const page = ref(1)
const search = ref('')
const errorMessage = ref('')

let searchTimer = null

function formatDate(value) {
  if (!value) return '—'

  return new Intl.DateTimeFormat(
    'ru-RU',
    {
      dateStyle: 'short',
      timeStyle: 'short',
    },
  ).format(new Date(value))
}

async function load() {
  errorMessage.value = ''

  try {
    await store.fetchPatients({
      requestedPage: page.value,
      requestedPageSize: props.pageSize,
      search: search.value,
    })
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить пациентов'
  }
}

watch(page, load)

watch(search, () => {
  window.clearTimeout(searchTimer)

  searchTimer = window.setTimeout(() => {
    page.value = 1
    load()
  }, 350)
})

onMounted(load)

onBeforeUnmount(() => {
  window.clearTimeout(searchTimer)
})
</script>

<template>
  <section class="space-y-4">
    <div
      v-if="showSearch"
      class="flex flex-col gap-3 sm:flex-row"
    >
      <label
        class="input input-bordered flex w-full max-w-xl items-center gap-2"
      >
        <Icon
          name="lucide:search"
          class="text-base-content/50 size-4"
        />

        <input
          v-model.trim="search"
          type="search"
          class="min-w-0 grow"
          placeholder="ФИО, email или номер карты"
        >
      </label>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="store.loading"
      variant="list"
      :count="compact ? 5 : pageSize"
    />

    <template v-else>
      <!-- Mobile -->
      <div class="grid gap-3 lg:hidden">
        <PatientsItem
          v-for="patient in store.patients"
          :key="patient.patient_id"
          :patient="patient"
        />
      </div>

      <!-- Desktop -->
      <div
        class="border-base-300 bg-base-100 hidden overflow-x-auto rounded-2xl border lg:block"
      >
        <table class="table">
          <thead>
            <tr>
              <th>Пациент</th>
              <th>Регистрация</th>
              <th>Последняя активность</th>
              <th>Контакт</th>
              <th>Доступ</th>
              <th />
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="patient in store.patients"
              :key="patient.patient_id"
              class="hover:bg-base-200/60"
            >
              <td>
                <p class="font-medium">
                  {{ patient.fullname }}
                </p>

                <p
                  class="text-base-content/60 text-xs"
                >
                  {{ patient.email }}
                </p>

                <p
                  class="text-base-content/40 text-xs"
                >
                  {{ patient.record_id }}
                </p>
              </td>

              <td>
                <span
                  class="badge"
                  :class="
                    patient.registration_status
                      === 'registered'
                      ? 'badge-success'
                      : 'badge-warning'
                  "
                >
                  {{
                    patient.registration_status
                      === 'registered'
                      ? 'Зарегистрирован'
                      : 'Email не подтверждён'
                  }}
                </span>
              </td>

              <td>
                {{ formatDate(patient.last_activity_at) }}
              </td>

              <td>
                <PatientsContactStatus
                  :allowed="
                    patient.assistant_contact_allowed
                  "
                  :do-not-call="patient.do_not_call"
                  :show-text="false"
                />
              </td>

              <td>
                <span
                  v-if="patient.pro_enabled"
                  class="badge badge-secondary"
                >
                  Pro
                </span>

                <span
                  v-else
                  class="text-base-content/40 text-sm"
                >
                  Обычный
                </span>
              </td>

              <td class="text-right">
                <NuxtLink
                  :to="`/patients/${patient.patient_id}`"
                  class="btn btn-sm btn-primary"
                >
                  Открыть
                </NuxtLink>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div
        v-if="!store.patients.length"
        class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
      >
        <Icon
          name="lucide:users"
          class="text-base-content/30 mx-auto size-12"
        />

        <p class="mt-4 font-medium">
          Пациенты не найдены
        </p>
      </div>

      <UiPagination
        v-if="!compact"
        v-model="page"
        :total-items="store.totalItems"
        :page-size="pageSize"
      />
    </template>
  </section>
</template>