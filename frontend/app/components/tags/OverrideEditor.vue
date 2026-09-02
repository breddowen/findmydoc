<!-- ./frontend/app/components/tags/OverrideEditor.vue -->
<script setup>
const props = defineProps({
  tags: {
    type: Array,
    default: () => [],
  },
  effectiveTags: {
    type: Array,
    default: () => [],
  },
  overrides: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
  saving: {
    type: Boolean,
    default: false,
  },
  defaultLabel: {
    type: String,
    default: 'Автоматически',
  },
})

const emit = defineEmits([
  'set',
  'reset',
])

const search = ref('')
const errorMessage = ref('')

const effectiveIds = computed(
  () => new Set(
    props.effectiveTags.map(tag => tag.id),
  ),
)

const overrideByTagId = computed(
  () => new Map(
    props.overrides.map(
      override => [
        override.tag.id,
        override,
      ],
    ),
  ),
)

const filteredTags = computed(() => {
  const query = search.value
    .trim()
    .toLocaleLowerCase('ru')

  return props.tags
    .filter(tag => !tag.is_system)
    .filter((tag) => {
      if (!query) return true

      return (
        tag.name
          .toLocaleLowerCase('ru')
          .includes(query)
        || (
          tag.description || ''
        )
          .toLocaleLowerCase('ru')
          .includes(query)
      )
    })
    .sort(
      (first, second) =>
        first.name.localeCompare(
          second.name,
          'ru',
        ),
    )
})

function getMode(tagId) {
  return (
    overrideByTagId.value
      .get(tagId)
      ?.action
    || 'default'
  )
}

function isEffective(tagId) {
  return effectiveIds.value.has(tagId)
}

async function changeMode(tag, event) {
  const mode = event.target.value
  errorMessage.value = ''

  try {
    if (mode === 'default') {
      if (overrideByTagId.value.has(tag.id)) {
        await emit('reset', tag)
      }

      return
    }

    await emit('set', {
      tag,
      action: mode,
    })
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить настройку тега'
  }
}
</script>

<template>
  <div class="space-y-4">
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
        class="min-w-0 grow"
        placeholder="Найти тег"
      >
    </label>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="5"
    />

    <div
      v-else-if="filteredTags.length"
      class="space-y-3"
    >
      <article
        v-for="tag in filteredTags"
        :key="tag.id"
        class="border-base-300 flex flex-col gap-4 rounded-2xl border p-4 sm:flex-row sm:items-center"
      >
        <div class="min-w-0 flex-1">
          <div class="flex flex-wrap items-center gap-2">
            <p class="font-medium">
              {{ tag.name }}
            </p>

            <span
              v-if="isEffective(tag.id)"
              class="badge badge-success badge-sm"
            >
              Активен
            </span>

            <span
              v-if="
                getMode(tag.id) === 'add'
              "
              class="badge badge-info badge-sm"
            >
              Добавлен вручную
            </span>

            <span
              v-if="
                getMode(tag.id) === 'remove'
              "
              class="badge badge-error badge-sm"
            >
              Исключён вручную
            </span>
          </div>

          <p
            v-if="tag.description"
            class="text-base-content/60 mt-1 text-sm"
          >
            {{ tag.description }}
          </p>
        </div>

        <select
          :value="getMode(tag.id)"
          class="select select-bordered w-full sm:w-56"
          :disabled="saving"
          @change="changeMode(tag, $event)"
        >
          <option value="default">
            {{ defaultLabel }}
          </option>

          <option value="add">
            Добавить
          </option>

          <option value="remove">
            Исключить
          </option>
        </select>
      </article>
    </div>

    <div
      v-else
      class="border-base-300 rounded-2xl border border-dashed p-8 text-center"
    >
      Теги не найдены
    </div>
  </div>
</template>