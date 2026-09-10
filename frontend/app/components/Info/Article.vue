<!-- ./frontend/app/components/Info/Article.vue -->
<script setup>
const props = defineProps({
  entry: {
    type: Object,
    required: true,
  },
})

const paragraphs = computed(() =>
  String(props.entry.text || '')
    .trim()
    .split(/\r?\n\s*\r?\n/)
    .filter(Boolean),
)
</script>

<template>
  <article class="mx-auto max-w-3xl space-y-6">
    <header>
      <p class="text-primary text-xs font-semibold uppercase tracking-wide">
        Информация
      </p>

      <h1 class="mt-2 text-2xl font-bold sm:text-3xl">
        {{ entry.title }}
      </h1>

      <p
        v-if="entry.subtitle"
        class="text-base-content/60 mt-2 text-sm sm:text-base"
      >
        {{ entry.subtitle }}
      </p>
    </header>

    <component
      :is="entry.quotation ? 'blockquote' : 'div'"
      class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-8"
      :class="{
        'border-l-primary border-l-4': entry.quotation,
      }"
    >
      <Icon
        v-if="entry.quotation"
        name="lucide:quote"
        class="text-primary/50 mb-4 size-7"
        aria-hidden="true"
      />

      <div class="space-y-4">
        <p
          v-for="(paragraph, index) in paragraphs"
          :key="index"
          class="text-base-content/80 whitespace-pre-line text-base leading-relaxed"
        >
          {{ paragraph }}
        </p>
      </div>
    </component>
  </article>
</template>