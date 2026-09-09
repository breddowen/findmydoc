<!-- ./frontend/app/components/life-aspects/TagLinks.vue -->
<script setup>
import { VueDraggable } from 'vue-draggable-plus'

const props = defineProps({
  aspect: {
    type: Object,
    required: true,
  },
  tags: {
    type: Array,
    default: () => [],
  },
  saving: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['add', 'remove'])

const search = ref('')
const searchId = useId()

const sourceDraft = ref([])
const assignedDraft = ref([])

const dragging = ref(false)
const dragContext = ref(null)
const pendingAction = ref(false)

const { matches: reduceMotion } = useBreakpoint(
  '(prefers-reduced-motion: reduce)',
)

const controlsDisabled = computed(() =>
  props.saving
  || pendingAction.value
  || dragging.value,
)

const groupName = computed(() =>
  `life-aspect-tags-${props.aspect.id}`,
)

const sourceGroup = computed(() => ({
  name: groupName.value,
  pull: 'clone',
  put: false,
}))

const targetGroup = computed(() => ({
  name: groupName.value,
  pull: false,
  put: [groupName.value],
}))

const assignedTags = computed(() =>
  [...(props.aspect.tags || [])].sort(
    (left, right) =>
      left.name.localeCompare(right.name, 'ru'),
  ),
)

const availableTags = computed(() => {
  const assignedIds = new Set(
    assignedTags.value.map(tag => tag.id),
  )

  const query = search.value
    .trim()
    .toLocaleLowerCase('ru')

  return props.tags
    .filter(tag =>
      !tag.is_hidden
      && !assignedIds.has(tag.id)
      && (
        !query
        || tag.name
          .toLocaleLowerCase('ru')
          .includes(query)
      ),
    )
    .sort(
      (left, right) =>
        left.name.localeCompare(right.name, 'ru'),
    )
})

// Sortable работает только с локальными массивами.
// Данные store меняются после успешного ответа API.
function resetDrafts() {
  sourceDraft.value = availableTags.value.map(
    tag => ({ ...tag }),
  )

  assignedDraft.value = assignedTags.value.map(
    tag => ({ ...tag }),
  )
}

watch(
  [
    assignedTags,
    availableTags,
  ],
  resetDrafts,
  {
    immediate: true,
    deep: true,
  },
)

watch(
  () => props.aspect.id,
  () => {
    search.value = ''
    dragContext.value = null
    dragging.value = false
  },
)

// Копируем объект для интерфейса,
// но сохраняем настоящий ID тега из backend.
function cloneTag(tag) {
  return { ...tag }
}

function canAddTag(tagId) {
  const tag = props.tags.find(
    item => item.id === tagId,
  )

  return Boolean(
    tag
    && !tag.is_hidden
    && !assignedTags.value.some(
      item => item.id === tagId,
    ),
  )
}

function requestAction(action, tagId) {
  if (props.saving || pendingAction.value) return

  if (action === 'add' && !canAddTag(tagId)) {
    return
  }

  if (
    action === 'remove'
    && !assignedTags.value.some(
      item => item.id === tagId,
    )
  ) {
    return
  }

  // Блокируем повторное действие сразу,
  // не дожидаясь обновления props.saving.
  pendingAction.value = true

  emit(action, tagId)

  void nextTick(() => {
    // Убираем временные изменения Sortable.
    // Новый тег появится в данных после ответа backend.
    resetDrafts()
    pendingAction.value = false
  })
}

function handleDragStart(event) {
  dragging.value = true

  dragContext.value = {
    aspectId: props.aspect.id,
    tagId: event.item?.dataset.tagId || null,
  }
}

function handleDrop(event) {
  const tagId = event.item?.dataset.tagId
  const context = dragContext.value

  const validContext = (
    context
    && context.aspectId === props.aspect.id
    && context.tagId === tagId
  )

  if (validContext && tagId) {
    requestAction('add', tagId)
  }

  // В том числе очищаем невалидный или отменённый drop.
  void nextTick(resetDrafts)
}

function handleDragEnd() {
  dragging.value = false
  dragContext.value = null

  void nextTick(resetDrafts)
}
</script>

<template>
  <div class="space-y-4">
    <div
      class="text-base-content/60 flex items-start gap-2 text-sm"
    >
      <Icon
        name="lucide:mouse-pointer-2"
        class="mt-0.5 size-4 shrink-0"
      />

      <p>
        Перетащите тег за ручку в блок «Теги сферы»
        или нажмите плюс. Один тег можно добавить
        в несколько сфер.
      </p>
    </div>

    <p
      v-if="saving"
      class="text-primary flex items-center gap-2 text-sm"
      role="status"
    >
      <span class="loading loading-spinner loading-xs" />
      Сохраняем изменения…
    </p>

    <div class="grid gap-5 xl:grid-cols-2">
      <section class="min-w-0 space-y-3">
        <h3 class="font-semibold">
          Теги сферы · {{ assignedTags.length }}
        </h3>

        <p class="text-base-content/60 text-sm">
          Для попадания программы в сферу достаточно
          хотя бы одного общего тега.
        </p>

        <p
          v-if="!assignedTags.length"
          class="sr-only"
        >
          В сфере пока нет тегов.
          Их можно добавить кнопками из списка доступных.
        </p>

        <VueDraggable
          v-model="assignedDraft"
          :group="targetGroup"
          :sort="false"
          :disabled="saving || pendingAction"
          :animation="reduceMotion ? 0 : 150"
          draggable=".life-aspect-tag-item"
          ghost-class="life-aspect-drag-ghost"
          class="life-aspect-drop-zone min-h-28 space-y-2 rounded-2xl border-2 border-dashed p-3 transition-colors"
          :class="[
            dragging
              ? 'border-primary bg-primary/5'
              : 'border-base-300',
            {
              'life-aspect-drop-zone--empty':
                !assignedDraft.length,
            },
          ]"
          data-empty-text="Перетащите тег сюда или добавьте кнопкой «+»"
          role="list"
          aria-label="Теги выбранной сферы"
          :aria-busy="saving"
          @add="handleDrop"
        >
          <LifeAspectsTag
            v-for="tag in assignedDraft"
            :key="tag.id"
            :tag="tag"
            action="remove"
            :disabled="controlsDisabled"
            @action="requestAction('remove', $event)"
          />
        </VueDraggable>

        <p class="text-base-content/50 text-xs">
          Крестик убирает только связь со сферой.
          Сам тег остаётся в справочнике.
        </p>
      </section>

      <section class="min-w-0 space-y-3">
        <h3 class="font-semibold">
          Доступные теги · {{ availableTags.length }}
        </h3>

        <label :for="searchId" class="sr-only">
          Поиск доступных тегов
        </label>

        <input
          :id="searchId"
          v-model="search"
          type="search"
          class="input w-full"
          placeholder="Найти тег"
          :disabled="dragging || saving"
        >

        <p
          v-if="!availableTags.length"
          class="text-base-content/60 py-3 text-sm"
        >
          {{
            search.trim()
              ? 'По вашему запросу ничего не найдено.'
              : 'Нет доступных тегов для добавления.'
          }}
        </p>

        <VueDraggable
          v-model="sourceDraft"
          :group="sourceGroup"
          :clone="cloneTag"
          :sort="false"
          :disabled="saving || pendingAction"
          :animation="reduceMotion ? 0 : 150"
          :force-fallback="true"
          :fallback-on-body="true"
          :fallback-tolerance="5"
          :delay="150"
          :delay-on-touch-only="true"
          handle=".life-aspect-tag-handle"
          draggable=".life-aspect-tag-item"
          ghost-class="life-aspect-drag-ghost"
          fallback-class="life-aspect-drag-fallback"
          class="max-h-96 space-y-2 overflow-y-auto overscroll-contain"
          role="list"
          aria-label="Доступные для добавления теги"
          @start="handleDragStart"
          @end="handleDragEnd"
        >
          <LifeAspectsTag
            v-for="tag in sourceDraft"
            :key="tag.id"
            :tag="tag"
            action="add"
            draggable
            :disabled="controlsDisabled"
            @action="requestAction('add', $event)"
          />
        </VueDraggable>

        <p class="text-base-content/50 text-xs">
          На телефоне ненадолго удерживайте ручку
          перед перетаскиванием.
          Скрытые теги недоступны для добавления.
        </p>
      </section>
    </div>
  </div>
</template>

<style scoped>
.life-aspect-drop-zone--empty::before {
  content: attr(data-empty-text);
  display: block;
  padding: 1rem 0.5rem;
  color: var(--color-base-content);
  font-size: 0.875rem;
  line-height: 1.5;
  text-align: center;
  opacity: 0.55;
  pointer-events: none;
}

.life-aspect-drag-ghost {
  opacity: 0.3;
}

.life-aspect-drag-fallback {
  box-shadow: 0 12px 32px rgb(0 0 0 / 18%);
}

@media (prefers-reduced-motion: reduce) {
  .life-aspect-drop-zone {
    transition: none;
  }
}
</style>