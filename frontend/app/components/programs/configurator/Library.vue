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

const emit = defineEmits(['add'])

const PAGE_SIZE = 5

const activeTab = ref('article')
const search = ref('')
const selectedTagIds = ref([])
const page = ref(1)

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
  if (activeTab.value === 'consultation') {
    return props.specialities
      .filter(item => !item.is_hidden)
      .map(item => {
        const title =
          item.consultation_name
          || `Консультация: ${item.name}`

        return {
          source_id: item.id,
          item_type: 'consultation',
          title,
          description: item.consultation_description,
          pro_content: false,
          is_hidden: false,
          is_library_hidden: false,
          tags: [],
          article_id: null,
          questionnaire_id: null,
          speciality_id: item.id,
          speciality_name: item.name,
          consultation_title: title,
          consultation_description:
            item.consultation_description || '',
        }
      })
  }

  const isArticle = activeTab.value === 'article'
  const source = isArticle
    ? props.articles
    : props.questionnaires

  return source
    // Исключённые из общего каталога материалы
    // здесь намеренно остаются.
    .filter(item => !item.is_hidden)
    .map(item => ({
      source_id: item.id,
      item_type: isArticle ? 'article' : 'questionnaire',
      title: item.title,
      description: isArticle ? null : item.description,
      pro_content: item.pro_content,
      is_hidden: false,
      is_library_hidden: Boolean(item.is_library_hidden),
      tags: item.tags || [],
      article_id: isArticle ? item.id : null,
      questionnaire_id: isArticle ? null : item.id,
      speciality_id: null,
      speciality_name: null,
      consultation_title: null,
      consultation_description: null,
    }))
})

const availableTags = computed(() => {
  const tagsById = new Map()

  // Список тегов не зависит от текущего фильтра:
  // выбранные теги не исчезают после нажатия.
  for (const item of sourceItems.value) {
    for (const tag of item.tags) {
      if (!tagsById.has(tag.id)) {
        tagsById.set(tag.id, {
          id: tag.id,
          name: tag.name,
          count: 0,
        })
      }

      tagsById.get(tag.id).count += 1
    }
  }

  return [...tagsById.values()].sort(
    (left, right) => left.name.localeCompare(
      right.name,
      'ru',
      { sensitivity: 'base' },
    ),
  )
})

const filteredItems = computed(() => {
  const query = search.value.trim().toLocaleLowerCase('ru-RU')
  const selected = new Set(selectedTagIds.value)

  return sourceItems.value.filter(item => {
    const matchesSearch = !query || [
      item.title,
      item.description,
    ].some(value =>
      String(value || '')
        .toLocaleLowerCase('ru-RU')
        .includes(query),
    )

    const matchesTags = !selected.size
      || item.tags.some(tag => selected.has(tag.id))

    return matchesSearch && matchesTags
  })
})

const pageItems = computed(() => {
  const offset = (page.value - 1) * PAGE_SIZE

  return filteredItems.value.slice(
    offset,
    offset + PAGE_SIZE,
  )
})

function toggleTag(tagId) {
  selectedTagIds.value = selectedTagIds.value.includes(tagId)
    ? selectedTagIds.value.filter(id => id !== tagId)
    : [...selectedTagIds.value, tagId]
}

function resetFilters() {
  search.value = ''
  selectedTagIds.value = []
}

function cloneItem(item) {
  // Копируем только поля элемента программы.
  // Не используем structuredClone на Vue Proxy.
  return {
    client_id: crypto.randomUUID(),
    order_index: 0,
    item_type: item.item_type,
    title: item.title,
    description: item.description,
    pro_content: item.pro_content,
    is_hidden: item.is_hidden,
    article_id: item.article_id,
    questionnaire_id: item.questionnaire_id,
    speciality_id: item.speciality_id,
    speciality_name: item.speciality_name,
    consultation_title: item.consultation_title,
    consultation_description: item.consultation_description,
  }
}

function addItem(item) {
  emit('add', cloneItem(item))
}

watch(activeTab, () => {
  resetFilters()
  page.value = 1
})

watch(
  [search, selectedTagIds],
  () => {
    page.value = 1
  },
  { flush: 'sync' },
)

watch(
  () => filteredItems.value.length,
  total => {
    page.value = Math.min(
      page.value,
      Math.max(1, Math.ceil(total / PAGE_SIZE)),
    )
  },
)
</script>

<template>
  <div class="space-y-4">
    <div
      class="bg-base-200 grid grid-cols-3 gap-1 rounded-xl p-1"
      role="group"
      aria-label="Тип материала"
    >
      <button
        v-for="tab in tabs"
        :key="tab.value"
        type="button"
        class="flex min-w-0 flex-col items-center justify-center gap-1 rounded-lg px-1 py-2 text-xs font-medium transition-colors"
        :class="
          activeTab === tab.value
            ? 'bg-base-100 text-primary shadow-sm'
            : 'text-base-content/60 hover:bg-base-100/50'
        "
        :aria-pressed="activeTab === tab.value"
        @click="activeTab = tab.value"
      >
        <Icon
          :name="tab.icon"
          class="size-4"
        />

        {{ tab.title }}
      </button>
    </div>

    <label class="input input-bordered flex w-full items-center gap-2">
      <Icon
        name="lucide:search"
        class="text-base-content/50 size-4 shrink-0"
      />

      <input
        v-model="search"
        type="search"
        class="min-w-0 grow"
        placeholder="Поиск по названию"
        aria-label="Поиск материалов"
      >
    </label>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="PAGE_SIZE"
    />

    <template v-else>
      <p
        class="text-base-content/60 text-xs"
        aria-live="polite"
      >
        Найдено: {{ filteredItems.length }}
      </p>

      <VueDraggable
        v-if="draggable && pageItems.length"
        :model-value="pageItems"
        :group="{
          name: 'program-content',
          pull: 'clone',
          put: false,
        }"
        :sort="false"
        :clone="cloneItem"
        :animation="150"
        class="space-y-2"
      >
        <ProgramsConfiguratorLibraryEntry
          v-for="item in pageItems"
          :key="`${item.item_type}-${item.source_id}`"
          :item="item"
          draggable
          @add="addItem"
        />
      </VueDraggable>

      <div
        v-else-if="pageItems.length"
        class="space-y-2"
      >
        <ProgramsConfiguratorLibraryEntry
          v-for="item in pageItems"
          :key="`${item.item_type}-${item.source_id}`"
          :item="item"
          @add="addItem"
        />
      </div>

      <div
        v-else
        class="border-base-300 rounded-xl border border-dashed p-6 text-center"
      >
        <p class="text-base-content/60 text-sm">
          Ничего не найдено
        </p>

        <button
          v-if="search || selectedTagIds.length"
          type="button"
          class="btn btn-ghost btn-sm mt-2"
          @click="resetFilters"
        >
          Сбросить фильтры
        </button>
      </div>

      <UiPagination
        v-model="page"
        :total-items="filteredItems.length"
        :page-size="PAGE_SIZE"
      />

      <section
        v-if="availableTags.length"
        class="border-base-300 border-t pt-4"
      >
        <div class="mb-3 flex items-center justify-between gap-3">
          <h3 class="text-sm font-medium">
            Теги
          </h3>

          <button
            v-if="selectedTagIds.length"
            type="button"
            class="link text-xs"
            @click="selectedTagIds = []"
          >
            Сбросить
          </button>
        </div>

        <div
          class="flex flex-wrap gap-2"
          role="group"
          aria-label="Фильтр по тегам"
        >
          <button
            v-for="tag in availableTags"
            :key="tag.id"
            type="button"
            class="rounded-full border px-3 py-2 text-xs transition-colors"
            :class="
              selectedTagIds.includes(tag.id)
                ? 'border-primary bg-primary text-primary-content'
                : 'border-base-300 bg-base-200 text-base-content/60 hover:border-primary/50'
            "
            :aria-pressed="selectedTagIds.includes(tag.id)"
            @click="toggleTag(tag.id)"
          >
            {{ tag.name }}
            <span class="ml-1 opacity-70">
              {{ tag.count }}
            </span>
          </button>
        </div>

        <p class="text-base-content/50 mt-3 text-xs">
          При выборе нескольких тегов достаточно совпадения
          хотя бы с одним.
        </p>
      </section>
    </template>
  </div>
</template>