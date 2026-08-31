<!-- ./frontend/app/components/directories/Tags.vue -->
<script setup>
const directories = useDirectoriesStore()
const auth = useAuthStore()

const showHidden = ref(false)
const dialogOpen = ref(false)
const editingTag = ref(null)

const errorMessage = ref('')

const form = reactive({
  name: '',
  description: '',
})

const visibleTags = computed(() =>
  directories.tags.filter(
    tag => showHidden.value || !tag.is_hidden,
  ),
)

const isSuperuser = computed(
  () => auth.activeRole === 'superuser',
)

function openCreate() {
  editingTag.value = null
  form.name = ''
  form.description = ''
  errorMessage.value = ''
  dialogOpen.value = true
}

function openEdit(tag) {
  editingTag.value = tag
  form.name = tag.name
  form.description = tag.description || ''
  errorMessage.value = ''
  dialogOpen.value = true
}

async function save() {
  errorMessage.value = ''

  try {
    await directories.saveTag(
      {
        name: form.name.trim(),
        description:
          form.description.trim() || null,
      },
      editingTag.value?.id,
    )

    dialogOpen.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить тег'
  }
}

async function toggleHidden(tag) {
  try {
    await directories.setTagHidden(
      tag.id,
      !tag.is_hidden,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость'
  }
}

async function remove(tag) {
  if (
    !window.confirm(`Удалить тег «${tag.name}»?`)
  ) {
    return
  }

  try {
    await directories.deleteTag(tag.id)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось удалить тег'
  }
}
</script>

<template>
  <section class="space-y-4">
    <div
      class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"
    >
      <label class="label cursor-pointer justify-start gap-3">
        <input
          v-model="showHidden"
          type="checkbox"
          class="toggle toggle-sm"
        >
        <span class="label-text">
          Показать скрытые
        </span>
      </label>

      <button
        type="button"
        class="btn btn-primary"
        @click="openCreate"
      >
        <Icon name="lucide:plus" class="size-4" />
        Добавить тег
      </button>
    </div>

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

    <div
      v-if="!visibleTags.length"
      class="border-base-300 rounded-2xl border border-dashed p-8 text-center"
    >
      Теги не найдены
    </div>

    <div v-else class="grid gap-3 md:grid-cols-2">
      <article
        v-for="tag in visibleTags"
        :key="tag.id"
        class="card bg-base-100 border-base-300 border"
        :class="{
          'opacity-60': tag.is_hidden,
        }"
      >
        <div class="card-body gap-3 p-4">
          <div class="flex items-start gap-3">
            <div class="min-w-0 flex-1">
              <div class="flex flex-wrap gap-2">
                <h3 class="font-semibold">
                  {{ tag.name }}
                </h3>

                <span
                  v-if="tag.is_system"
                  class="badge badge-neutral badge-sm"
                >
                  Системный
                </span>

                <span
                  v-if="tag.is_hidden"
                  class="badge badge-warning badge-sm"
                >
                  Скрыт
                </span>
              </div>

              <p
                class="text-base-content/60 mt-2 text-sm"
              >
                {{ tag.description || 'Без описания' }}
              </p>
            </div>

            <div class="dropdown dropdown-end">
              <button
                type="button"
                tabindex="0"
                class="btn btn-circle btn-ghost btn-sm"
              >
                <Icon
                  name="lucide:ellipsis-vertical"
                  class="size-4"
                />
              </button>

              <ul
                tabindex="0"
                class="menu dropdown-content bg-base-100 border-base-300 z-20 w-52 rounded-box border p-2 shadow-xl"
              >
                <li>
                  <button
                    type="button"
                    @click="openEdit(tag)"
                  >
                    Редактировать
                  </button>
                </li>

                <li v-if="isSuperuser">
                  <button
                    type="button"
                    @click="toggleHidden(tag)"
                  >
                    {{
                      tag.is_hidden
                        ? 'Восстановить'
                        : 'Скрыть'
                    }}
                  </button>
                </li>

                <li
                  v-if="
                    isSuperuser
                    && !tag.is_system
                  "
                >
                  <button
                    type="button"
                    class="text-error"
                    @click="remove(tag)"
                  >
                    Удалить
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>

  <UiResponsiveDialog
    v-model="dialogOpen"
    :title="
      editingTag ? 'Изменить тег' : 'Новый тег'
    "
  >
    <form
      id="tag-directory-form"
      class="space-y-4"
      @submit.prevent="save"
    >
      <div
        v-if="errorMessage"
        class="alert alert-error"
      >
        {{ errorMessage }}
      </div>

      <label class="form-control block">
        <span class="label">
          <span class="label-text">Название</span>
        </span>

        <input
          v-model="form.name"
          type="text"
          required
          maxlength="100"
          class="input input-bordered w-full"
          :disabled="editingTag?.is_system"
        >
      </label>

      <label class="form-control block">
        <span class="label">
          <span class="label-text">Описание</span>
        </span>

        <textarea
          v-model="form.description"
          class="textarea textarea-bordered min-h-28 w-full"
        />
      </label>
    </form>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          @click="dialogOpen = false"
        >
          Отмена
        </button>

        <button
          type="submit"
          form="tag-directory-form"
          class="btn btn-primary"
          :disabled="
            directories.saving || !form.name.trim()
          "
        >
          <span
            v-if="directories.saving"
            class="loading loading-spinner loading-sm"
          />
          Сохранить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>