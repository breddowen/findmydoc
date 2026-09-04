<!-- frontend\app\components\articles\Card.vue -->
 <script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  },

  canManage: {
    type: Boolean,
    default: false,
  },

  showAnalytics: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'toggle-visibility',
])

const openedCount = computed(
  () => props.article.opened_count ?? 0,
)

const readCount = computed(
  () => props.article.read_count ?? 0,
)

const readRate = computed(() => {
  const value = Number(
    props.article.read_rate ?? 0,
  )

  return new Intl.NumberFormat(
    'ru-RU',
    {
      minimumFractionDigits: 0,
      maximumFractionDigits: 1,
    },
  ).format(value)
})

const articleRoute = computed(() => ({
  path: `/content/articles/${props.article.id}`,
  query: {
    source: 'library',
  },
}))

function toggleVisibility() {
  emit(
    'toggle-visibility',
    props.article,
  )
}
</script>

<template>
  <article
    class="card bg-base-100 border-base-300 overflow-hidden border"
    :class="{
      'opacity-60': article.is_hidden,
    }"
  >
    <div class="card-body">
      <div class="flex flex-wrap gap-2">
        <span
          v-if="article.pro_content"
          class="badge badge-secondary"
        >
          Pro
        </span>

        <span
          v-if="article.is_hidden"
          class="badge badge-warning"
        >
          Скрыта
        </span>
      </div>

      <h2 class="card-title">
        {{ article.title }}
      </h2>

      <div
        v-if="article.tags?.length"
        class="flex flex-wrap gap-1"
      >
        <span
          v-for="tag in article.tags"
          :key="tag.id"
          class="badge badge-outline badge-sm"
        >
          {{ tag.name }}
        </span>
      </div>

      <div
        v-if="showAnalytics"
        class="text-base-content/60 flex items-center gap-3 text-xs"
        >
        <div
            class="tooltip tooltip-bottom"
            data-tip="Открытия"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:mouse-pointer-click"
                class="text-primary size-3.5"
            />
            <span class="font-medium">
                {{ openedCount }}
            </span>
            </span>
        </div>

        <div
            class="tooltip tooltip-bottom"
            data-tip="Прочтения"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:book-open-check"
                class="text-success size-3.5"
            />
            <span class="font-medium">
                {{ readCount }}
            </span>
            </span>
        </div>

        <div
            class="tooltip tooltip-bottom"
            data-tip="Дочитали"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:percent"
                class="text-secondary size-3.5"
            />
            <span class="font-medium">
                {{ readRate }}%
            </span>
            </span>
        </div>
        </div>

      <div class="card-actions mt-auto pt-4">
        <NuxtLink
          :to="articleRoute"
          class="btn btn-sm"
        >
          <Icon
            name="lucide:book-open"
            class="size-4"
          />

          Открыть
        </NuxtLink>
        <ClientOnly>
             <NuxtLink
                v-if="canManage"
                :to="`/content/articles/${article.id}/edit`"
                class="btn btn-sm btn-outline"
                >
                <Icon
                    name="lucide:pencil"
                    class="size-4"
                />

                Редактировать
                </NuxtLink>
        </ClientOnly>

        <button
          v-if="canManage"
          type="button"
          class="btn btn-sm btn-ghost"
          @click="toggleVisibility"
        >
          <Icon
            :name="
              article.is_hidden
                ? 'lucide:eye'
                : 'lucide:eye-off'
            "
            class="size-4"
          />

          {{
            article.is_hidden
              ? 'Показать'
              : 'Скрыть'
          }}
        </button>
      </div>
    </div>
  </article>
</template>