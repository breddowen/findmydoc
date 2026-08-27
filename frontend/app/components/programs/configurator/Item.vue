<!-- ./frontend/app/components/programs/configurator/Item.vue -->
<script setup>
const props = defineProps({
  item: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits([
  'remove',
])

const iconName = computed(() => {
  if (props.item.item_type === 'article') {
    return 'lucide:file-text'
  }

  if (
    props.item.item_type === 'questionnaire'
  ) {
    return 'lucide:clipboard-list'
  }

  return 'lucide:stethoscope'
})

const typeName = computed(() => {
  if (props.item.item_type === 'article') {
    return 'Статья'
  }

  if (
    props.item.item_type === 'questionnaire'
  ) {
    return 'Опросник'
  }

  return 'Консультация'
})
</script>

<template>
  <article
    class="border-base-300 bg-base-100 rounded-2xl border p-3"
  >
    <div class="flex items-start gap-3">
      <button
        type="button"
        class="item-drag-handle btn btn-circle btn-ghost btn-sm cursor-grab active:cursor-grabbing"
        aria-label="Перетащить"
      >
        <Icon
          name="lucide:grip-vertical"
          class="size-4"
        />
      </button>

      <div
        class="flex size-10 shrink-0 items-center justify-center rounded-xl"
        :class="{
          'bg-info/10 text-info':
            item.item_type === 'article',
          'bg-secondary/10 text-secondary':
            item.item_type === 'questionnaire',
          'bg-success/10 text-success':
            item.item_type === 'consultation',
        }"
      >
        <Icon
          :name="iconName"
          class="size-5"
        />
      </div>

      <div class="min-w-0 flex-1">
        <div class="flex flex-wrap items-center gap-2">
          <p class="font-medium">
            {{ item.title }}
          </p>

          <span class="badge badge-outline badge-sm">
            {{ typeName }}
          </span>

          <span
            v-if="item.pro_content"
            class="badge badge-secondary badge-sm"
          >
            Pro
          </span>
        </div>

        <template
          v-if="item.item_type === 'consultation'"
        >
          <label class="form-control mt-4 block">
            <span class="label-text mb-1 text-xs">
              Название консультации
            </span>

            <input
              v-model="item.consultation_title"
              type="text"
              class="input input-bordered input-sm w-full"
            >
          </label>

          <label class="form-control mt-3 block">
            <span class="label-text mb-1 text-xs">
              Зачем нужна консультация на этом этапе
            </span>

            <textarea
              v-model="item.consultation_description"
              class="textarea textarea-bordered min-h-20 w-full text-sm"
              placeholder="Описание для пациента"
            />
          </label>
        </template>

        <p
          v-else-if="item.description"
          class="text-base-content/60 mt-1 line-clamp-2 text-sm"
        >
          {{ item.description }}
        </p>
      </div>

      <button
        type="button"
        class="btn btn-circle btn-ghost btn-sm text-error"
        aria-label="Удалить элемент"
        @click="emit('remove')"
      >
        <Icon
          name="lucide:trash-2"
          class="size-4"
        />
      </button>
    </div>
  </article>
</template>