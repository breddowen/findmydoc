<!-- ./frontend/app/pages/content/videos/index.vue -->
<script setup>
import { mediaErrorText } from '~/utils/media'

const auth = useAuthStore()
const store = useVideosStore()

const initialized = ref(false)
const search = ref('')
const selectedTags = ref([])
const page = ref(1)
const errorMessage = ref('')

let mounted = false

const canManage = computed(() =>
  ['superuser', 'med_assistant'].includes(auth.activeRole),
)

const availableTags = computed(() => {
  const map = new Map()

  for (const video of store.videos) {
    for (const tag of video.tags || []) {
      map.set(tag.id, tag)
    }
  }

  return [...map.values()].sort(
    (a, b) => a.name.localeCompare(b.name, 'ru'),
  )
})

const filtered = computed(() => {
  const query = search.value.trim().toLocaleLowerCase('ru-RU')

  return store.videos.filter(video => {
    const matchesTitle = !query
      || video.title.toLocaleLowerCase('ru-RU').includes(query)

    const matchesTags = !selectedTags.value.length
      || video.tags.some(tag => selectedTags.value.includes(tag.id))

    return matchesTitle && matchesTags
  })
})

const pageItems = computed(() =>
  filtered.value.slice((page.value - 1) * 9, page.value * 9),
)

function toggleTag(id) {
  selectedTags.value = selectedTags.value.includes(id)
    ? selectedTags.value.filter(value => value !== id)
    : [...selectedTags.value, id]
}

async function load() {
  errorMessage.value = ''

  try {
    await store.fetchVideos()
  } catch (error) {
    if (error?.name === 'AbortError') return

    errorMessage.value = mediaErrorText(
      error,
      'Не удалось загрузить видео',
    )
  } finally {
    initialized.value = true
  }
}

async function toggleVisibility(video) {
  errorMessage.value = ''

  try {
    await store.setVisibility(video, !video.is_hidden)
    await store.fetchVideos()
  } catch (error) {
    errorMessage.value = mediaErrorText(
      error,
      'Не удалось изменить видимость',
    )
  }
}

watch([search, selectedTags], () => {
  page.value = 1
})

watch(
  [() => auth.accessToken, () => auth.activeRole],
  () => {
    if (!mounted) return

    selectedTags.value = []
    page.value = 1
    void load()
  },
)

onMounted(() => {
  mounted = true
  void load()
})

onBeforeUnmount(() => {
  mounted = false
})

const deleteDialogOpen = ref(false)
const deletingVideo = ref(null)
const successMessage = ref('')

function openDelete(video) {
  deletingVideo.value = video
  deleteDialogOpen.value = true
}

async function handleDeleted() {
  successMessage.value = 'Видео удалено'
  deletingVideo.value = null

  await load()
}
</script>

<template>
  <div class="space-y-6">
    <header class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">Видео</h1>
        <p class="text-base-content/60 mt-1">
          Видеоматериалы для пациентов.
        </p>
      </div>

      <ClientOnly>
        <NuxtLink
          v-if="canManage"
          to="/content/videos/new"
          class="btn btn-primary"
        >
          <Icon name="lucide:plus" class="size-4" />
          Добавить видео
        </NuxtLink>
      </ClientOnly>
    </header>

    <div v-if="errorMessage" class="alert alert-error" role="alert">
      {{ errorMessage }}
    </div>

    <input
      v-model="search"
      type="search"
      placeholder="Поиск по названию"
      aria-label="Поиск видео"
      class="input input-bordered w-full"
    >

    <div v-if="availableTags.length" class="flex flex-wrap gap-2">
      <button
        v-for="tag in availableTags"
        :key="tag.id"
        type="button"
        class="badge h-auto px-3 py-2"
        :class="
          selectedTags.includes(tag.id)
            ? 'badge-primary'
            : 'badge-outline'
        "
        :aria-pressed="selectedTags.includes(tag.id)"
        @click="toggleTag(tag.id)"
      >
        {{ tag.name }}
      </button>
    </div>

    <UiContentSkeleton
      v-if="!initialized || store.loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="pageItems.length"
      class="grid items-stretch gap-5 md:grid-cols-2 xl:grid-cols-3"
    >
      <VideosCard
        v-for="video in pageItems"
        :key="video.id"
        :video="video"
        :can-manage="canManage"
        :busy="store.saving"
        @toggle-visibility="toggleVisibility"
        @delete="openDelete"
      />
    </div>

    <div
      v-else
      class="border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon name="lucide:video" class="text-base-content/30 mx-auto size-12" />
      <p class="mt-4">Видео не найдены</p>
    </div>

    <div
      v-if="successMessage"
      class="alert alert-success"
      role="status"
    >
      {{ successMessage }}
    </div>

    <UiPagination
      v-model="page"
      :total-items="filtered.length"
      :page-size="9"
    />

  </div>
  <VideosDeleteDialog
        v-model="deleteDialogOpen"
        :video="deletingVideo"
        @deleted="handleDeleted"
    />
</template>