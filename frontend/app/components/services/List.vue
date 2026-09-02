<!-- ./frontend/app/components/services/List.vue -->
<script setup>
defineProps({
  services: {
    type: Array,
    default: () => [],
  },
  canManage: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'edit',
  'visibility',
  'delete',
])

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()
</script>

<template>
  <div
    v-if="services.length"
    class="grid gap-4 lg:grid-cols-2"
  >
    <article
      v-for="service in services"
      :key="service.id"
      class="card bg-base-100 border-base-300 border"
      :class="{
        'opacity-60': service.is_hidden,
      }"
    >
      <div class="card-body p-5">
        <div class="flex items-start gap-4">
          <div class="min-w-0 flex-1">
            <div class="flex flex-wrap items-center gap-2">
              <span
                class="badge badge-neutral font-mono"
              >
                {{ service.code }}
              </span>

              <span
                v-if="service.is_hidden"
                class="badge badge-warning"
              >
                Скрыта
              </span>

              <span
                v-if="hasDiscount(service)"
                class="badge badge-error"
              >
                −{{ service.discount_percent }}%
              </span>
            </div>

            <h2 class="mt-3 text-lg font-bold">
              {{ service.title }}
            </h2>

            <p
              class="text-base-content/60 mt-2 text-sm"
            >
              {{ service.description || 'Без описания' }}
            </p>

            <div
              class="mt-4 flex flex-wrap items-center gap-2"
            >
              <strong class="text-primary text-xl">
                {{ formatFinalPrice(service) }}
              </strong>

              <span
                v-if="hasDiscount(service)"
                class="text-base-content/40 line-through"
              >
                {{ formatOriginalPrice(service) }}
              </span>
            </div>
          </div>

          <div
            v-if="canManage"
            class="dropdown dropdown-end"
          >
            <button
              type="button"
              tabindex="0"
              class="btn btn-circle btn-ghost btn-sm"
              aria-label="Действия с услугой"
            >
              <Icon
                name="lucide:ellipsis-vertical"
                class="size-4"
              />
            </button>

            <ul
              tabindex="0"
              class="menu dropdown-content bg-base-100 border-base-300 z-20 w-56 rounded-box border p-2 shadow-xl"
            >
              <li>
                <button
                  type="button"
                  @click="emit('edit', service)"
                >
                  <Icon
                    name="lucide:pencil"
                    class="size-4"
                  />
                  Редактировать
                </button>
              </li>

              <li>
                <button
                  type="button"
                  @click="
                    emit('visibility', service)
                  "
                >
                  <Icon
                    :name="
                      service.is_hidden
                        ? 'lucide:eye'
                        : 'lucide:eye-off'
                    "
                    class="size-4"
                  />

                  {{
                    service.is_hidden
                      ? 'Восстановить'
                      : 'Скрыть'
                  }}
                </button>
              </li>

              <li>
                <button
                  type="button"
                  class="text-error"
                  @click="emit('delete', service)"
                >
                  <Icon
                    name="lucide:trash-2"
                    class="size-4"
                  />
                  Удалить
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </article>
  </div>

  <div
    v-else
    class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:package-search"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Услуги не найдены
    </p>
  </div>
</template>