<!-- ./frontend/app/components/programs/configurator/Stage.vue -->
<script setup>
import { VueDraggable } from 'vue-draggable-plus'

const model = defineModel({
  type: Object,
  required: true,
})

const props = defineProps({
  index: {
    type: Number,
    required: true,
  },
  total: {
    type: Number,
    required: true,
  },
  active: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'remove',
  'activate',
  'open-library',
])

const expanded = ref(true)

function normalizeItems() {
  model.value.items.forEach((item, index) => {
    item.order_index = index
  })
}

function removeItem(index) {
  model.value.items.splice(index, 1)
  normalizeItems()
}
</script>

<template>
  <article
    class="border-base-300 bg-base-100 rounded-3xl border transition"
    :class="{
      'border-primary ring-primary/10 ring-4':
        active,
    }"
    @click="emit('activate')"
  >
    <header
      class="border-base-300 flex items-center gap-2 border-b p-3 sm:p-4"
    >
      <button
        type="button"
        class="stage-drag-handle btn btn-circle btn-ghost btn-sm cursor-grab active:cursor-grabbing"
        aria-label="Перетащить этап"
      >
        <Icon
          name="lucide:grip-vertical"
          class="size-5"
        />
      </button>

      <div
        class="bg-primary text-primary-content flex size-9 shrink-0 items-center justify-center rounded-full font-bold"
      >
        {{ index + 1 }}
      </div>

      <div class="min-w-0 flex-1">
        <p class="truncate font-semibold">
          {{ model.title || `Этап ${index + 1}` }}
        </p>

        <p class="text-base-content/50 text-xs">
          День {{ model.day_from }}–{{ model.day_to }}
          · Элементов: {{ model.items.length }}
        </p>
      </div>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm"
        :aria-label="
          expanded
            ? 'Свернуть этап'
            : 'Развернуть этап'
        "
        @click.stop="expanded = !expanded"
      >
        <Icon
          :name="
            expanded
              ? 'lucide:chevron-up'
              : 'lucide:chevron-down'
          "
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm text-error"
        aria-label="Удалить этап"
        @click.stop="emit('remove')"
      >
        <Icon
          name="lucide:trash-2"
          class="size-4"
        />
      </button>
    </header>

    <div
      v-if="expanded"
      class="space-y-5 p-4 sm:p-5"
    >
      <div class="grid gap-4 md:grid-cols-2">
        <label class="form-control block md:col-span-2">
          <span class="label-text mb-2 font-medium">
            Название этапа
          </span>

          <input
            v-model="model.title"
            type="text"
            class="input input-bordered w-full"
            placeholder="Например, Знакомство с программой"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Первый день
          </span>

          <input
            v-model.number="model.day_from"
            type="number"
            min="0"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Последний день
          </span>

          <input
            v-model.number="model.day_to"
            type="number"
            min="0"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block md:col-span-2">
          <span class="label-text mb-2">
            Описание для пациента
          </span>

          <textarea
            v-model="model.description"
            class="textarea textarea-bordered min-h-24 w-full"
            placeholder="На этом этапе мы научимся..."
          />
        </label>

        <label class="form-control block md:col-span-2">
          <span class="label-text mb-2">
            Инструкция для врача
          </span>

          <textarea
            v-model="model.doctor_description"
            class="textarea textarea-bordered min-h-24 w-full"
            placeholder="Что необходимо обсудить с пациентом..."
          />
        </label>
      </div>

      <div>
        <div
          class="mb-3 flex items-center justify-between"
        >
          <div>
            <h3 class="font-semibold">
              Содержимое этапа
            </h3>

            <p class="text-base-content/50 text-xs">
              Порядок сверху вниз
            </p>
          </div>

          <button
            type="button"
            class="btn btn-outline btn-sm lg:hidden"
            @click.stop="emit('open-library')"
          >
            <Icon
              name="lucide:plus"
              class="size-4"
            />
            Добавить
          </button>
        </div>

        <VueDraggable
          v-model="model.items"
          group="program-content"
          handle=".item-drag-handle"
          :animation="180"
          class="min-h-28 space-y-2 rounded-2xl"
          @add="normalizeItems"
          @update="normalizeItems"
        >
          <ProgramsConfiguratorItem
            v-for="(item, itemIndex) in model.items"
            :key="item.client_id"
            :item="item"
            @remove="removeItem(itemIndex)"
          />
        </VueDraggable>

        <button
          v-if="!model.items.length"
          type="button"
          class="border-base-300 text-base-content/50 flex min-h-28 w-full items-center justify-center rounded-2xl border border-dashed lg:pointer-events-none"
          @click.stop="emit('open-library')"
        >
          <span class="flex flex-col items-center gap-2">
            <Icon
              name="lucide:package-open"
              class="size-8"
            />

            <span class="text-sm">
              Перетащите контент сюда
            </span>
          </span>
        </button>
      </div>
    </div>
  </article>
</template>