<!-- ./frontend/app/components/videos/Card.vue -->
<script setup>
import { videoDuration } from '~/utils/videos'

const props = defineProps({
  video: { type: Object, required: true },
  canManage: { type: Boolean, default: false },
  busy: { type: Boolean, default: false },
})

const emit = defineEmits([
  'toggle-visibility',
  'delete',
])

const accessible = computed(() =>
  props.video.can_access !== false,
)

const duration = computed(() =>
  props.video.wide_file?.duration_seconds
  || props.video.mobile_file?.duration_seconds
  || 0,
)
</script>

<template>
  <article
    class="card border-base-300 bg-base-100 overflow-hidden border"
    :class="{ 'opacity-60': video.is_hidden }"
  >
    <div class="relative">
      <VideosPoster :video="video" />

      <span class="absolute bottom-3 right-3 rounded-lg bg-black/75 px-2 py-1 text-xs text-white">
        {{ videoDuration(duration) }}
      </span>
    </div>

    <div class="card-body gap-4 p-5">
      <div class="flex flex-wrap gap-1">
        <span v-if="video.pro_content" class="badge badge-secondary badge-sm">
          Pro
        </span>

        <span v-if="video.is_hidden" class="badge badge-warning badge-sm">
          Скрыто
        </span>

        <span v-if="video.is_library_hidden" class="badge badge-outline badge-sm">
          Вне каталога
        </span>
      </div>

      <h2 class="card-title text-lg">{{ video.title }}</h2>

      <div v-if="video.tags?.length" class="flex flex-wrap gap-1">
        <span
          v-for="tag in video.tags"
          :key="tag.id"
          class="badge badge-outline badge-sm"
        >
          {{ tag.name }}
        </span>
      </div>

      <div class="card-actions mt-auto pt-2">
        <NuxtLink
          v-if="accessible"
          :to="{
            path: `/content/videos/${video.id}`,
            query: { source: 'library' },
          }"
          class="btn btn-primary btn-sm"
        >
          <Icon name="lucide:play" class="size-4" />
          Смотреть
        </NuxtLink>

        <span v-else class="text-base-content/60 py-2 text-sm">
          Требуется Pro-доступ
        </span>

        <template v-if="canManage">
          <NuxtLink
            :to="`/content/videos/${video.id}/edit`"
            class="btn btn-outline btn-sm"
          >
            <Icon name="lucide:pencil" class="size-4" />
            Изменить
          </NuxtLink>

          <button
            type="button"
            class="btn btn-ghost btn-sm"
            :disabled="busy"
            @click="emit('toggle-visibility', video)"
          >
            <Icon
              :name="video.is_hidden ? 'lucide:eye' : 'lucide:eye-off'"
              class="size-4"
            />
            {{ video.is_hidden ? 'Показать' : 'Скрыть' }}
          </button>
          <button
            type="button"
            class="btn btn-ghost btn-sm text-error"
            :disabled="busy"
            @click="emit('delete', video)"
          >
            <Icon name="lucide:trash-2" class="size-4" />
            Удалить
          </button>
        </template>
      </div>
    </div>
  </article>
</template>