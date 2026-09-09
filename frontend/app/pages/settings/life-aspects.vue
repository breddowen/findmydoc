<!-- frontend\app\pages\settings\life-aspects.vue -->

<script setup>
import AspectFormDialog from '~/components/life-aspects/FormDialog.vue'
import AspectTagLinks from '~/components/life-aspects/TagLinks.vue'

definePageMeta({
  middleware: ['life-aspect-manager'],
})

const store = useLifeAspectsStore()

const loaded = ref(false)
const showHidden = ref(false)
const selectedId = ref(null)

const dialogOpen = ref(false)
const editingAspect = ref(null)

const pageError = ref('')
const dialogError = ref('')
const message = ref('')

const visibleAspects = computed(() =>
  store.orderedAspects.filter(
    aspect => showHidden.value || !aspect.is_hidden,
  ),
)

const selectedAspect = computed(() =>
  visibleAspects.value.find(
    aspect => aspect.id === selectedId.value,
  ) || null,
)

const nextOrder = computed(() =>
  Math.min(
    100000,
    Math.max(
      0,
      ...store.aspects.map(aspect => aspect.order_index),
    ) + 10,
  ),
)

watch(
  visibleAspects,
  (items) => {
    if (!items.some(item => item.id === selectedId.value)) {
      selectedId.value = items[0]?.id || null
    }
  },
  { immediate: true },
)

function errorText(error, fallback) {
  return typeof error?.data?.detail === 'string'
    ? error.data.detail
    : fallback
}

async function load() {
  pageError.value = ''
  loaded.value = false

  try {
    await store.load()
    loaded.value = true
  } catch (error) {
    pageError.value = errorText(
      error,
      'Не удалось загрузить сферы жизни',
    )
  }
}

function openCreate() {
  editingAspect.value = null
  dialogError.value = ''
  message.value = ''
  dialogOpen.value = true
}

function openEdit() {
  if (!selectedAspect.value) return

  editingAspect.value = selectedAspect.value
  dialogError.value = ''
  message.value = ''
  dialogOpen.value = true
}

async function saveAspect(payload) {
  if (store.saving) return

  dialogError.value = ''
  pageError.value = ''

  try {
    const aspect = await store.saveAspect(
      payload,
      editingAspect.value?.id,
    )

    selectedId.value = aspect.id
    dialogOpen.value = false
    message.value = 'Сфера жизни сохранена'
  } catch (error) {
    dialogError.value = errorText(
      error,
      'Не удалось сохранить сферу жизни',
    )
  }
}

async function toggleHidden() {
  const aspect = selectedAspect.value

  if (!aspect || store.saving) return

  const nextIsHidden = !aspect.is_hidden

  pageError.value = ''
  message.value = ''

  try {
    await store.saveAspect(
      { is_hidden: nextIsHidden },
      aspect.id,
    )

    message.value = nextIsHidden
      ? 'Сфера скрыта. Её можно найти через «Показать скрытые».'
      : 'Сфера восстановлена'
  } catch (error) {
    pageError.value = errorText(
      error,
      'Не удалось изменить видимость сферы',
    )
  }
}

async function changeTag(action, tagId) {
  const aspectId = selectedAspect.value?.id

  if (!aspectId || store.saving) return

  pageError.value = ''
  message.value = ''

  try {
    await store[action](aspectId, tagId)

    message.value = action === 'addTag'
      ? 'Тег добавлен в сферу'
      : 'Тег убран из сферы'
  } catch (error) {
    pageError.value = errorText(
      error,
      'Не удалось изменить теги сферы',
    )
  }
}

onMounted(load)

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="mx-auto max-w-6xl space-y-5">
    <header class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Сферы жизни
        </h1>

        <p class="text-base-content/60 mt-2 max-w-2xl text-sm">
          Объединяйте теги в понятные направления:
          сон, питание, стресс и другие сферы.
          Изменения сохраняются отдельно для каждой операции.
        </p>
      </div>

      <button
        type="button"
        class="btn btn-primary shrink-0"
        :disabled="!loaded || store.loading || store.saving"
        @click="openCreate"
      >
        <Icon name="lucide:plus" class="size-4" />
        Новая сфера
      </button>
    </header>

    <div
      v-if="pageError"
      class="alert alert-error"
      role="alert"
    >
      {{ pageError }}
    </div>

    <div
      v-if="message"
      class="alert alert-success"
      role="status"
    >
      {{ message }}
    </div>

    <UiContentSkeleton
      v-if="store.loading"
      variant="card"
      :count="2"
    />

    <div
      v-else-if="!loaded"
      class="border-base-300 bg-base-100 rounded-2xl border p-5"
    >
      <button
        type="button"
        class="btn btn-primary btn-sm"
        @click="load"
      >
        Загрузить сферы жизни
      </button>
    </div>

    <template v-else>
      <label class="flex w-fit cursor-pointer items-center gap-3 text-sm">
        <input
          v-model="showHidden"
          type="checkbox"
          class="toggle toggle-sm"
          :disabled="store.saving"
        >
        Показать скрытые
      </label>

      <div class="grid items-start gap-5 lg:grid-cols-[17rem_minmax(0,1fr)]">
        <aside
          class="border-base-300 bg-base-100 min-w-0 rounded-2xl border p-3"
          aria-label="Выбор сферы жизни"
        >
          <p
            v-if="!visibleAspects.length"
            class="text-base-content/60 p-3 text-sm"
          >
            {{
              store.aspects.length
                ? 'Все сферы скрыты. Включите их отображение.'
                : 'Пока нет сфер жизни. Создайте первую.'
            }}
          </p>

          <ul v-else class="space-y-2">
            <li
              v-for="aspect in visibleAspects"
              :key="aspect.id"
            >
              <button
                type="button"
                class="w-full rounded-xl border p-3 text-left transition"
                :class="
                  selectedId === aspect.id
                    ? 'border-primary bg-primary/10'
                    : 'border-transparent hover:bg-base-200'
                "
                :aria-pressed="selectedId === aspect.id"
                :disabled="store.saving"
                @click="selectedId = aspect.id"
              >
                <span class="block font-medium wrap-anywhere">
                  {{ aspect.name }}
                </span>

                <span class="text-base-content/60 mt-1 block text-xs">
                  Порядок: {{ aspect.order_index }}
                  · Тегов: {{ aspect.tags.length }}
                </span>

                <span
                  v-if="aspect.is_hidden"
                  class="badge badge-warning badge-sm mt-2"
                >
                  Скрыта
                </span>
              </button>
            </li>
          </ul>
        </aside>

        <section
          v-if="selectedAspect"
          class="border-base-300 bg-base-100 min-w-0 space-y-5 rounded-2xl border p-4 sm:p-5"
        >
          <header class="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
            <div class="min-w-0">
              <h2 class="text-xl font-bold wrap-anywhere">
                {{ selectedAspect.name }}
              </h2>

              <p
                v-if="selectedAspect.is_hidden"
                class="text-warning mt-1 text-sm"
              >
                Сфера скрыта от пациентов
              </p>
            </div>

            <div class="flex shrink-0 flex-wrap gap-2">
              <button
                type="button"
                class="btn btn-outline btn-sm"
                :disabled="store.saving"
                @click="openEdit"
              >
                <Icon name="lucide:pencil" class="size-4" />
                Изменить
              </button>

              <button
                type="button"
                class="btn btn-ghost btn-sm"
                :disabled="store.saving"
                @click="toggleHidden"
              >
                {{
                  selectedAspect.is_hidden
                    ? 'Восстановить'
                    : 'Скрыть'
                }}
              </button>
            </div>
          </header>

          <ContentRichTextRenderer
            v-if="selectedAspect.description"
            :content="selectedAspect.description"
          />

          <p v-else class="text-base-content/50 text-sm">
            Описание пока не добавлено.
          </p>

          <div class="border-base-300 border-t pt-5">
            <AspectTagLinks
              :aspect="selectedAspect"
              :tags="store.tags"
              :saving="store.saving"
              @add="changeTag('addTag', $event)"
              @remove="changeTag('removeTag', $event)"
            />
          </div>
        </section>

        <section
          v-else
          class="border-base-300 rounded-2xl border border-dashed p-6"
        >
          <p class="text-base-content/60 text-sm">
            Создайте или выберите сферу, чтобы настроить
            её описание и связанные теги.
          </p>
        </section>
      </div>
    </template>

    <AspectFormDialog
      v-model="dialogOpen"
      :aspect="editingAspect"
      :default-order="nextOrder"
      :saving="store.saving"
      :error-message="dialogError"
      @save="saveAspect"
    />
  </div>
</template>