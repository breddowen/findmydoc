<!-- ./frontend/app/pages/services/index.vue -->
<script setup>
definePageMeta({
  middleware: [
    'service-manager',
  ],
})

const auth = useAuthStore()
const store = useServicesStore()

const loading = ref(true)
const errorMessage = ref('')

const search = ref('')
const showHidden = ref(false)

const formOpen = ref(false)
const visibilityOpen = ref(false)
const deleteOpen = ref(false)

const selectedService = ref(null)

const canManage = computed(
  () => auth.activeRole === 'superuser',
)

const filteredServices = computed(() => {
  const query = search.value
    .trim()
    .toLocaleLowerCase('ru')

  return store.services.filter((service) => {
    if (!showHidden.value && service.is_hidden) {
      return false
    }

    if (!query) return true

    return (
      service.code
        .toLocaleLowerCase('ru')
        .includes(query)
      || service.title
        .toLocaleLowerCase('ru')
        .includes(query)
      || (
        service.description || ''
      )
        .toLocaleLowerCase('ru')
        .includes(query)
    )
  })
})

function openCreate() {
  selectedService.value = null
  formOpen.value = true
}

function openEdit(service) {
  selectedService.value = service
  formOpen.value = true
}

function openVisibility(service) {
  selectedService.value = service
  visibilityOpen.value = true
}

function openDelete(service) {
  selectedService.value = service
  deleteOpen.value = true
}

onMounted(async () => {
  try {
    // Загружаем скрытые сразу, а отображение
    // регулируем локальным фильтром.
    await store.fetchServices(true)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить услуги'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="mx-auto max-w-6xl space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Услуги
        </h1>

        <p class="text-base-content/60 mt-1">
          Каталог утверждённых медицинским центром
          услуг, цен и скидок.
        </p>
      </div>

      <button
        v-if="canManage"
        type="button"
        class="btn btn-primary"
        @click="openCreate"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая услуга
      </button>
    </header>

    <div
      v-if="!canManage"
      class="alert alert-info"
    >
      <Icon
        name="lucide:info"
        class="size-5"
      />
      <span>
        Медицинский ассистент может просматривать
        услуги. Изменение доступно суперпользователю.
      </span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <section
      class="bg-base-100 border-base-300 grid gap-4 rounded-2xl border p-4 sm:grid-cols-[minmax(0,1fr)_auto] sm:items-center"
    >
      <label
        class="input input-bordered flex items-center gap-2"
      >
        <Icon
          name="lucide:search"
          class="text-base-content/50 size-4"
        />

        <input
          v-model="search"
          type="search"
          class="grow"
          placeholder="Код, название или описание"
        >
      </label>

      <label
        class="label cursor-pointer justify-start gap-3"
      >
        <input
          v-model="showHidden"
          type="checkbox"
          class="toggle toggle-sm"
        >
        <span class="label-text">
          Показать скрытые
        </span>
      </label>
    </section>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="4"
    />

    <ServicesList
      v-else
      :services="filteredServices"
      :can-manage="canManage"
      @edit="openEdit"
      @visibility="openVisibility"
      @delete="openDelete"
    />
  </div>

  <ServicesFormDialog
    v-model="formOpen"
    :service="selectedService"
  />

  <ServicesVisibilityDialog
    v-model="visibilityOpen"
    :service="selectedService"
  />

  <ServicesDeleteDialog
    v-model="deleteOpen"
    :service="selectedService"
  />
</template>