<!-- ./frontend/app/components/articles/Form.vue -->
<script setup>
const props = defineProps({
  initialValue: {
    type: Object,
    default: null,
  },
  saving: {
    type: Boolean,
    default: false,
  },
  submitLabel: {
    type: String,
    default: 'Сохранить статью',
  },
})

const emit = defineEmits([
  'submit',
  'cancel',
])

const { $api } = useNuxtApp()

const tags = ref([])
const loadingTags = ref(false)

const previewOpen = ref(false)
const errorMessage = ref('')

const form = reactive({
  title: '',
  content: '',
  tag_ids: [],
  pro_content: true,
})

function applyInitialValue(value) {
  if (!value) return

  form.title = value.title || ''
  form.content = value.content || ''
  form.tag_ids = (value.tags || []).map(
    (tag) => tag.id,
  )
  form.pro_content = Boolean(value.pro_content)
}

async function loadTags() {
  loadingTags.value = true

  try {
    tags.value = await $api('/api/v1/tags')
  } finally {
    loadingTags.value = false
  }
}

function submit() {
  errorMessage.value = ''

  if (!form.title.trim()) {
    errorMessage.value = 'Введите название статьи'
    return
  }

  if (!form.content.trim() || form.content === '<p></p>') {
    errorMessage.value = 'Введите текст статьи'
    return
  }

  emit('submit', {
    title: form.title.trim(),
    content: form.content,
    tag_ids: form.tag_ids,
    pro_content: form.pro_content,
  })
}

watch(
  () => props.initialValue,
  applyInitialValue,
  {
    immediate: true,
  },
)

onMounted(loadTags)
</script>

<template>
  <form
    class="space-y-6"
    @submit.prevent="submit"
  >
    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <section
      class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-6"
    >
      <div class="space-y-5">
        <label class="form-control block">
          <span class="label">
            <span class="label-text font-medium">
              Название статьи
            </span>
          </span>

          <input
            v-model="form.title"
            type="text"
            maxlength="300"
            required
            class="input input-bordered w-full"
            placeholder="Введите название"
          >
        </label>

        <div>
          <div class="mb-2 flex items-center justify-between">
            <span class="font-medium">
              Текст статьи
            </span>

            <button
              type="button"
              class="btn btn-ghost btn-sm"
              :disabled="!form.content"
              @click="previewOpen = true"
            >
              <Icon
                name="lucide:eye"
                class="size-4"
              />
              Предпросмотр
            </button>
          </div>

          <ContentRichTextEditor
            v-model="form.content"
            placeholder="Введите текст статьи..."
          />
        </div>

        <div>
          <p class="mb-3 font-medium">
            Теги
          </p>

          <ContentTagSelector
            v-model="form.tag_ids"
            :tags="tags"
            :loading="loadingTags"
          />
        </div>

        <label
          class="border-base-300 flex cursor-pointer items-start justify-between gap-4 rounded-2xl border p-4"
        >
          <span>
            <span class="block font-medium">
              Профессиональный контент
            </span>

            <span
              class="text-base-content/60 mt-1 block text-sm"
            >
              Доступен пациенту только после включения
              доступа Pro.
            </span>
          </span>

          <input
            v-model="form.pro_content"
            type="checkbox"
            class="toggle toggle-primary shrink-0"
          >
        </label>
      </div>
    </section>

    <div
      class="flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
    >
      <button
        type="button"
        class="btn"
        :disabled="saving"
        @click="emit('cancel')"
      >
        Отмена
      </button>

      <button
        type="submit"
        class="btn btn-primary"
        :disabled="saving"
      >
        <span
          v-if="saving"
          class="loading loading-spinner loading-sm"
        />

        {{ submitLabel }}
      </button>
    </div>
  </form>

  <UiResponsiveDialog
    v-model="previewOpen"
    title="Предпросмотр статьи"
    max-width-class="max-w-3xl"
  >
    <article>
      <h1 class="mb-6 text-2xl font-bold sm:text-3xl">
        {{ form.title || 'Без названия' }}
      </h1>

      <ContentRichTextRenderer
        :content="form.content"
      />
    </article>
  </UiResponsiveDialog>
</template>