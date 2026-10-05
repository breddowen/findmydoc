<!-- ./frontend/app/components/videos/Poster.vue -->
<script setup>
const props = defineProps({
  video: {
    type: Object,
    required: true,
  },
  programId: {
    type: String,
    default: null,
  },
  programStageId: {
    type: String,
    default: null,
  },
  eager: {
    type: Boolean,
    default: false,
  },
  alt: {
    type: String,
    default: '',
  },
})

const container = ref(null)
const visible = ref(false)

let observer = null

const posterId = computed(() =>
  props.video.poster_image_id
  || props.video.image_id
  || props.video.automatic_image_id
  || null,
)

const request = computed(() => {
  if (!props.video.id || !posterId.value) {
    return null
  }

  return {
    path: `/api/v1/videos/${props.video.id}/poster`,
    query: {
      image_id: posterId.value,
      program_id: props.programId || undefined,
      program_stage_id: props.programStageId || undefined,
    },
  }
})

const { src, loading } = usePrivateImage(
  request,
  visible,
)

onMounted(() => {
  if (
    props.eager
    || !('IntersectionObserver' in window)
  ) {
    visible.value = true
    return
  }

  observer = new IntersectionObserver(
    entries => {
      if (!entries.some(entry => entry.isIntersecting)) {
        return
      }

      visible.value = true
      observer?.disconnect()
      observer = null
    },
    {
      rootMargin: '300px',
    },
  )

  if (container.value) {
    observer.observe(container.value)
  }
})

onBeforeUnmount(() => {
  observer?.disconnect()
})
</script>

<template>
  <div
    ref="container"
    class="bg-base-200 aspect-video overflow-hidden"
  >
    <img
      v-if="src"
      :src="src"
      :alt="alt || video.title || ''"
      class="block h-full w-full object-cover"
      decoding="async"
    >

    <div
      v-else
      class="text-base-content/30 flex h-full min-h-24 items-center justify-center"
      aria-hidden="true"
    >
      <span
        v-if="loading"
        class="loading loading-spinner loading-sm"
      />

      <Icon
        v-else
        name="lucide:video"
        class="size-10"
      />
    </div>
  </div>
</template>