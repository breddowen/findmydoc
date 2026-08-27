<!-- ./frontend/app/components/assignments/ContentPicker.vue -->
<script setup>
const model = defineModel({
  type: String,
  default: null,
})

const props = defineProps({
  items: {
    type: Array,
    default: () => [],
  },
  assignedContentIds: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
  contentType: {
    type: String,
    required: true,
    validator: (value) =>
      [
        'article',
        'questionnaire',
      ].includes(value),
  },
})

const search = ref('')
const page = ref(1)
const pageSize = 10

const assignedIdsSet = computed(
  () => new Set(props.assignedContentIds),
)

const preparedItems = computed(() =>
  props.items.map((item) => ({
    ...item,
    content_type: props.contentType,
  })),
)

const filteredItems = computed(() => {
  const normalizedSearch = search.value
    .trim()
    .toLocaleLowerCase('ru-RU')

  if (!normalizedSearch) {
    return preparedItems.value
  }

  return preparedItems.value.filter((item) => {
    const titleMatches = item.title
      ?.toLocaleLowerCase('ru-RU')
      .includes(normalizedSearch)

    const descriptionMatches = item.description
      ?.toLocaleLowerCase('ru-RU')
      .includes(normalizedSearch)

    const tagMatches = item.tags?.some((tag) =>
      tag.name
        .toLocaleLowerCase('ru-RU')
        .includes(normalizedSearch),
    )

    return (
      titleMatches
      || descriptionMatches
      || tagMatches
    )
  })
})

const paginatedItems = computed(() => {
  const start = (page.value - 1) * pageSize

  return filteredItems.value.slice(
    start,
    start + pageSize,
  )
})

function isAssigned(itemId) {
  return assignedIdsSet.value.has(itemId)
}

function select(item) {
  model.value = item.id
}

watch(search, () => {
  page.value = 1
})

watch(
  () => props.contentType,
  () => {
    search.value = ''
    page.value = 1
  },
)
</script>

<template>
  <div class="space-y-4">
    <label
      class="input input-bordered flex w-full items-center gap-2"
    >
      <Icon
        name="lucide:search"
        class="text-base-content/50 size-4"
      />

      <input
        v-model="search"
        type="search"
        class="min-w-0 grow"
        :placeholder="
          contentType === 'article'
            ? 'Найти статью'
            : 'Найти опросник'
        "
      >
    </label>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="5"
    />

    <div
      v-else-if="paginatedItems.length"
      class="space-y-2"
    >
      <AssignmentsPickerItem
        v-for="item in paginatedItems"
        :key="item.id"
        :item="item"
        :selected="model === item.id"
        :assigned="isAssigned(item.id)"
        @select="select"
      />
    </div>

    <div
      v-else
      class="border-base-300 rounded-2xl border border-dashed p-8 text-center"
    >
      <Icon
        :name="
          contentType === 'article'
            ? 'lucide:file-search'
            : 'lucide:clipboard-x'
        "
        class="text-base-content/30 mx-auto size-10"
      />

      <p class="mt-3 font-medium">
        {{
          search
            ? 'Ничего не найдено'
            : contentType === 'article'
              ? 'Статей пока нет'
              : 'Опросников пока нет'
        }}
      </p>
    </div>

    <UiPagination
      v-model="page"
      :total-items="filteredItems.length"
      :page-size="pageSize"
    />
  </div>
</template>