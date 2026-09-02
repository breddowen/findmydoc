<!-- ./frontend/app/components/programs/configurator/ServiceSelect.vue -->
<script setup>
const model = defineModel({
  type: String,
  default: null,
})

const props = defineProps({
  services: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()

const selectValue = computed({
  get() {
    return model.value || ''
  },
  set(value) {
    model.value = value || null
  },
})

const availableServices = computed(() =>
  props.services.filter(
    service =>
      !service.is_hidden
      || service.id === model.value,
  ),
)

const selectedService = computed(() =>
  props.services.find(
    service => service.id === model.value,
  ) || null,
)
</script>

<template>
  <div
    class="border-base-300 rounded-2xl border p-4 sm:col-span-2"
  >
    <div
      class="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between"
    >
      <div>
        <p class="font-medium">
          Медицинская услуга
        </p>

        <p class="text-base-content/50 mt-1 text-xs">
          Цена и скидка управляются в отдельном
          каталоге услуг.
        </p>
      </div>

      <NuxtLink
        to="/services"
        class="btn btn-ghost btn-sm"
      >
        <Icon
          name="lucide:external-link"
          class="size-4"
        />
        Каталог услуг
      </NuxtLink>
    </div>

    <select
      v-model="selectValue"
      class="select select-bordered mt-4 w-full"
      :disabled="loading"
    >
      <option value="">
        Без услуги
      </option>

      <option
        v-for="service in availableServices"
        :key="service.id"
        :value="service.id"
      >
        {{ service.code }} — {{ service.title }}
        {{ service.is_hidden ? ' (скрыта)' : '' }}
      </option>
    </select>

    <div
      v-if="selectedService"
      class="bg-base-200 mt-4 rounded-xl p-4"
    >
      <div
        class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"
      >
        <div>
          <div class="flex flex-wrap items-center gap-2">
            <span
              class="badge badge-neutral font-mono"
            >
              {{ selectedService.code }}
            </span>

            <span
              v-if="selectedService.is_hidden"
              class="badge badge-warning"
            >
              Скрыта
            </span>

            <span
              v-if="hasDiscount(selectedService)"
              class="badge badge-error"
            >
              −{{ selectedService.discount_percent }}%
            </span>
          </div>

          <p class="mt-2 font-medium">
            {{ selectedService.title }}
          </p>

          <p
            v-if="selectedService.description"
            class="text-base-content/60 mt-1 text-sm"
          >
            {{ selectedService.description }}
          </p>
        </div>

        <div class="shrink-0 sm:text-right">
          <p class="text-primary text-lg font-bold">
            {{ formatFinalPrice(selectedService) }}
          </p>

          <p
            v-if="hasDiscount(selectedService)"
            class="text-base-content/40 text-sm line-through"
          >
            {{ formatOriginalPrice(selectedService) }}
          </p>
        </div>
      </div>
    </div>

    <div
      v-else
      class="alert alert-info mt-4"
    >
      <Icon
        name="lucide:gift"
        class="size-5"
      />
      <span>
        Программа будет отображаться как бесплатная.
        Обычный контент останется доступным, а
        Pro-контент потребует ручного открытия доступа.
      </span>
    </div>
  </div>
</template>