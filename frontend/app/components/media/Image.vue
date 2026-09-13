<!-- ./frontend/app/components/media/Image.vue -->
<script setup>
import {
  isMediaId,
  MEDIA_PRESETS,
  mediaEntityPath,
} from '~/utils/media'

const props = defineProps({
  purpose: {
    type: String,
    required: true,
  },
  entityId: {
    type: String,
    default: null,
  },
  imageId: {
    type: String,
    default: null,
  },
  temporary: {
    type: Boolean,
    default: false,
  },
  programId: {
    type: String,
    default: null,
  },
  programStageId: {
    type: String,
    default: null,
  },
  alt: {
    type: String,
    default: '',
  },
  eager: {
    type: Boolean,
    default: false,
  },
  fit: {
    type: String,
    default: 'cover',
    validator: value => ['cover', 'contain'].includes(value),
  },
})

const container = ref(null)
const visible = ref(false)

let observer = null

const request = computed(() => {
  if (
    !MEDIA_PRESETS[props.purpose]
    || !isMediaId(props.imageId)
  ) {
    return null
  }

  if (props.temporary) {
    return {
      path: `/api/v1/media/uploads/${props.imageId}/preview`,
      query: {},
    }
  }

  if (!isMediaId(props.entityId)) {
    return null
  }

  return {
    path: `${mediaEntityPath(
      props.purpose,
      props.entityId,
    )}/file`,
    query: {
      image_id: props.imageId,
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
    (entries) => {
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
    class="overflow-hidden bg-base-200"
  >
    <img
      v-if="src"
      :src="src"
      :alt="alt"
      class="block h-full w-full"
      :class="fit === 'contain' ? 'object-contain' : 'object-cover'"
      decoding="async"
    >

    <div
      v-else
      class="text-base-content/30 flex h-full min-h-12 w-full items-center justify-center"
      aria-hidden="true"
    >
      <span
        v-if="loading"
        class="loading loading-spinner loading-sm"
      />

      <Icon
        v-else
        name="lucide:image"
        class="size-7"
      />
    </div>
  </div>
</template>