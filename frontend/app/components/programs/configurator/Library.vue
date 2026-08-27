<!-- ./frontend/app/components/programs/configurator/Library.vue -->
<script setup>
import { VueDraggable } from 'vue-draggable-plus'

const props = defineProps({
  articles: {
    type: Array,
    default: () => [],
  },
  questionnaires: {
    type: Array,
    default: () => [],
  },
  specialities: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
  draggable: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits([
  'add',
])

const activeTab = ref('article')
const search = ref('')

const tabs = [
  {
    value: 'article',
    title: 'Статьи',
    icon: 'lucide:file-text',
  },
  {
    value: 'questionnaire',
    title: 'Опросники',
    icon: 'lucide:clipboard-list',
  },
  {
    value: 'consultation',
    title: 'Консультации',
    icon: 'lucide:stethoscope',
  },
]

const sourceItems = computed(() => {
  if (activeTab.value === 'article') {
    return props.articles
      .filter((item) => !item.is_hidden)
      .map((item) => ({
        source_id: item.id,
        item_type: 'article',
        title: item.title,
        description: null,
        pro_content: item.pro_content,
        article_id: item.id,
        questionnaire_id: null,
        speciality_id: null,
        consultation_title: null,
        consultation_description: null,
      }))
  }

  if (activeTab.value === 'questionnaire') {
    return props.questionnaires
      .filter((item) => !item.is_hidden)
      .map((item) => ({
        source_id: item.id,
        item_type: 'questionnaire',
        title: item.title,
        description: item.description,
        pro_content: item.pro_content,
        article_id: null,
        questionnaire_id: item.id,
        speciality_id: null,
        consultation_title: null,
        consultation_description: null,
      }))
  }

  return props.specialities.map((item) => ({
    source_id: item.id,
    item_type: 'consultation',
    title:
      item.consultation_name
      || `Консультация: ${item.name}`,
    description: item.consultation_description,
    pro_content: false,
    article_id: null,
    questionnaire_id: null,
    speciality_id: item.id,
    speciality_name: item.name,
    consultation_title:
      item.consultation_name
      || `Консультация: ${item.name}`,
    consultation_description:
      item.consultation_description || '',
  }))
})

const filteredItems = computed(() => {
  const value = search.value
    .trim()
    .toLocaleLowerCase('ru-RU')

  if (!value) return sourceItems.value

  return sourceItems.value.filter((item) =>
    item.title
      .toLocaleLowerCase('ru-RU')
      .includes(value)
    || item.description
      ?.toLocaleLowerCase('ru-RU')
      .includes(value),
  )
})

function cloneItem(item) {
  return {
    ...structuredClone(item),
    client_id: crypto.randomUUID(),
    order_index: 0,
  }
}

function addItem(item) {
  emit('add', cloneItem(item))
}
</script>

<template>
  <div class="space-y-4">
    <div
      role="tablist"
      class="tabs tabs-box w-full"
    >
      <button
        v-for="tab in tabs"
        :key="tab.value"
        type="button"
        role="tab"
        class="tab min-w-0 flex-1 gap-1 px-2"
        :class="{
          'tab-active':
            activeTab === tab.value,
        }"
        :title="tab.title"
        @click="activeTab = tab.value"
      >
        <Icon
          :name="tab.icon"
          class="size-4"
        />

        <span class="hidden 2xl:inline">
          {{ tab.title }}
        </span>
      </button>
    </div>

    <label
      class="input input-bordered input-sm flex w-full items-center gap-2"
    >
      <Icon
        name="lucide:search"
        class="text-base-content/50 size-4"
      />

      <input
        v-model="search"
        type="search"
        class="min-w-0 grow"
        placeholder="Поиск"
      >
    </label>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="5"
    />

    <VueDraggable
      v-else-if="draggable"
      :model-value="filteredItems"
      :group="{
        name: 'program-content',
        pull: 'clone',
        put: false,
      }"
      :sort="false"
      :clone="cloneItem"
      class="space-y-2"
    >
      <button
        v-for="item in filteredItems"
        :key="`${item.item_type}-${item.source_id}`"
        type="button"
        class="border-base-300 hover:border-primary bg-base-100 flex w-full cursor-grab items-start gap-3 rounded-2xl border p-3 text-left active:cursor-grabbing"
        @click="addItem(item)"
      >
        <Icon
          name="lucide:grip-vertical"
          class="text-base-content/40 mt-1 size-4 shrink-0"
        />

        <div class="min-w-0 flex-1">
          <p class="text-sm font-medium">
            {{ item.title }}
          </p>

          <span
            v-if="item.pro_content"
            class="badge badge-secondary badge-xs mt-1"
          >
            Pro
          </span>
        </div>

        <Icon
          name="lucide:plus"
          class="text-primary mt-1 size-4 shrink-0"
        />
      </button>
    </VueDraggable>

    <div
      v-else
      class="space-y-2"
    >
      <button
        v-for="item in filteredItems"
        :key="`${item.item_type}-${item.source_id}`"
        type="button"
        class="border-base-300 hover:border-primary flex w-full items-center gap-3 rounded-2xl border p-3 text-left"
        @click="addItem(item)"
      >
        <div class="min-w-0 flex-1">
          <p class="font-medium">
            {{ item.title }}
          </p>

          <p
            v-if="item.description"
            class="text-base-content/50 mt-1 line-clamp-2 text-xs"
          >
            {{ item.description }}
          </p>
        </div>

        <Icon
          name="lucide:plus"
          class="text-primary size-5 shrink-0"
        />
      </button>
    </div>

    <p
      v-if="!loading && !filteredItems.length"
      class="text-base-content/50 py-8 text-center text-sm"
    >
      Ничего не найдено
    </p>
  </div>
</template>