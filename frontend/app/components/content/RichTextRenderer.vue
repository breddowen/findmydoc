<!-- ./frontend/app/components/content/RichTextRenderer.vue -->
<script setup>
const props = defineProps({
  content: {
    type: String,
    default: '',
  },
})

const sanitizedContent = ref('')

let DOMPurify = null

async function sanitize() {
  if (!import.meta.client) return

  if (!DOMPurify) {
    const module = await import('dompurify')
    DOMPurify = module.default
  }

  sanitizedContent.value = DOMPurify.sanitize(
    props.content || '',
    {
      USE_PROFILES: {
        html: true,
      },
      ADD_ATTR: [
        'target',
        'rel',
      ],
    },
  )
}

watch(
  () => props.content,
  sanitize,
  {
    immediate: true,
  },
)

onMounted(sanitize)
</script>

<template>
  <article
    class="rich-text-content"
    v-html="sanitizedContent"
  />
</template>

<style>
.rich-text-content {
  line-height: 1.75;
  overflow-wrap: anywhere;
}

.rich-text-content p {
  margin: 0.875rem 0;
}

.rich-text-content h2 {
  margin: 2rem 0 0.875rem;
  font-size: 1.75rem;
  font-weight: 700;
  line-height: 1.25;
}

.rich-text-content h3 {
  margin: 1.5rem 0 0.75rem;
  font-size: 1.4rem;
  font-weight: 700;
  line-height: 1.3;
}

.rich-text-content h4 {
  margin: 1.25rem 0 0.625rem;
  font-size: 1.15rem;
  font-weight: 600;
}

.rich-text-content ul {
  margin: 1rem 0;
  list-style: disc;
  padding-left: 1.5rem;
}

.rich-text-content ol {
  margin: 1rem 0;
  list-style: decimal;
  padding-left: 1.5rem;
}

.rich-text-content li {
  margin: 0.375rem 0;
}

.rich-text-content blockquote {
  margin: 1.25rem 0;
  border-left: 0.25rem solid var(--color-primary);
  border-radius: 0 0.75rem 0.75rem 0;
  background: var(--color-base-200);
  padding: 0.75rem 1rem;
}

.rich-text-content pre {
  margin: 1rem 0;
  overflow-x: auto;
  border-radius: 0.75rem;
  background: var(--color-base-300);
  padding: 1rem;
}

.rich-text-content code {
  border-radius: 0.25rem;
  background: var(--color-base-300);
  padding: 0.125rem 0.375rem;
}

.rich-text-content pre code {
  padding: 0;
  background: transparent;
}

.rich-text-content a {
  color: var(--color-primary);
  text-decoration: underline;
}

.rich-text-content hr {
  margin: 2rem 0;
  border-color: var(--color-base-300);
}
</style>