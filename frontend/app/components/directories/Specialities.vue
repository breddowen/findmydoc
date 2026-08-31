<!-- ./frontend/app/components/directories/Specialities.vue -->
<script setup>
const directories = useDirectoriesStore()
const auth = useAuthStore()

const showHidden = ref(false)
const dialogOpen = ref(false)
const tagsDialogOpen = ref(false)

const editingSpeciality = ref(null)
const selectedSpeciality = ref(null)
const selectedTagIds = ref([])

const loadingTags = ref(false)
const errorMessage = ref('')

const form = reactive({
  name: '',
  description: '',
  consultation_name: '',
  consultation_description: '',
})

const visibleSpecialities = computed(() =>
  directories.specialities.filter(
    speciality =>
      showHidden.value || !speciality.is_hidden,
  ),
)

const activeTags = computed(() =>
  directories.tags.filter(tag => !tag.is_hidden),
)

const isSuperuser = computed(
  () => auth.activeRole === 'superuser',
)

function openCreate() {
  editingSpeciality.value = null

  Object.assign(form, {
    name: '',
    description: '',
    consultation_name: '',
    consultation_description: '',
  })

  errorMessage.value = ''
  dialogOpen.value = true
}

function openEdit(speciality) {
  editingSpeciality.value = speciality

  Object.assign(form, {
    name: speciality.name,
    description: speciality.description || '',
    consultation_name:
      speciality.consultation_name || '',
    consultation_description:
      speciality.consultation_description || '',
  })

  errorMessage.value = ''
  dialogOpen.value = true
}

async function save() {
  errorMessage.value = ''

  try {
    await directories.saveSpeciality(
      {
        name: form.name.trim(),
        description:
          form.description.trim() || null,
        consultation_name:
          form.consultation_name.trim() || null,
        consultation_description:
          form.consultation_description.trim()
          || null,
      },
      editingSpeciality.value?.id,
    )

    dialogOpen.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить специальность'
  }
}

async function openTags(speciality) {
  selectedSpeciality.value = speciality
  selectedTagIds.value = []
  loadingTags.value = true
  errorMessage.value = ''
  tagsDialogOpen.value = true

  try {
    const response =
      await directories.fetchSpecialityTags(
        speciality.id,
      )

    selectedTagIds.value = response.tags.map(
      tag => tag.id,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить теги'
  } finally {
    loadingTags.value = false
  }
}

async function toggleTag(tag) {
  if (!selectedSpeciality.value) return

  const selected = selectedTagIds.value.includes(
    tag.id,
  )

  try {
    if (selected) {
      await directories.removeTagFromSpeciality(
        selectedSpeciality.value.id,
        tag.id,
      )

      selectedTagIds.value =
        selectedTagIds.value.filter(
          id => id !== tag.id,
        )
    } else {
      await directories.addTagToSpeciality(
        selectedSpeciality.value.id,
        tag.id,
      )

      selectedTagIds.value.push(tag.id)
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить теги'
  }
}

async function toggleHidden(speciality) {
  try {
    await directories.setSpecialityHidden(
      speciality.id,
      !speciality.is_hidden,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость'
  }
}

async function remove(speciality) {
  if (
    !window.confirm(
      `Удалить специальность «${speciality.name}»?`,
    )
  ) {
    return
  }

  try {
    await directories.deleteSpeciality(
      speciality.id,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось удалить специальность'
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
        Добавить специальность
      </button>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-if="!visibleSpecialities.length"
      class="border-base-300 rounded-2xl border border-dashed p-8 text-center"
    >
      Специальности не найдены
    </div>

    <div v-else class="grid gap-3 md:grid-cols-2">
      <article
        v-for="speciality in visibleSpecialities"
        :key="speciality.id"
        class="card bg-base-100 border-base-300 border"
        :class="{
          'opacity-60': speciality.is_hidden,
        }"
      >
        <div class="card-body p-4">
          <div class="flex items-start gap-3">
            <div class="min-w-0 flex-1">
              <div class="flex flex-wrap gap-2">
                <h3 class="font-semibold">
                  {{ speciality.name }}
                </h3>

                <span
                  v-if="speciality.is_hidden"
                  class="badge badge-warning badge-sm"
                >
                  Скрыта
                </span>
              </div>

              <p
                class="text-base-content/60 mt-2 text-sm"
              >
                {{
                  speciality.description
                  || 'Без описания'
                }}
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
                class="menu dropdown-content bg-base-100 border-base-300 z-20 w-56 rounded-box border p-2 shadow-xl"
              >
                <li>
                  <button
                    type="button"
                    @click="openEdit(speciality)"
                  >
                    Редактировать
                  </button>
                </li>

                <li>
                  <button
                    type="button"
                    @click="openTags(speciality)"
                  >
                    Настроить теги
                  </button>
                </li>

                <li v-if="isSuperuser">
                  <button
                    type="button"
                    @click="toggleHidden(speciality)"
                  >
                    {{
                      speciality.is_hidden
                        ? 'Восстановить'
                        : 'Скрыть'
                    }}
                  </button>
                </li>

                <li v-if="isSuperuser">
                  <button
                    type="button"
                    class="text-error"
                    @click="remove(speciality)"
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
      editingSpeciality
        ? 'Изменить специальность'
        : 'Новая специальность'
    "
    max-width-class="max-w-xl"
  >
    <form
      id="speciality-directory-form"
      class="space-y-4"
      @submit.prevent="save"
    >
      <label class="form-control block">
        <span class="label">
          <span class="label-text">Название</span>
        </span>

        <input
          v-model="form.name"
          type="text"
          required
          maxlength="200"
          class="input input-bordered w-full"
        >
      </label>

      <label class="form-control block">
        <span class="label">
          <span class="label-text">Описание</span>
        </span>

        <textarea
          v-model="form.description"
          class="textarea textarea-bordered w-full"
        />
      </label>

      <label class="form-control block">
        <span class="label">
          <span class="label-text">
            Название консультации
          </span>
        </span>

        <input
          v-model="form.consultation_name"
          type="text"
          maxlength="300"
          class="input input-bordered w-full"
        >
      </label>

      <label class="form-control block">
        <span class="label">
          <span class="label-text">
            Описание консультации
          </span>
        </span>

        <textarea
          v-model="form.consultation_description"
          class="textarea textarea-bordered w-full"
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
          form="speciality-directory-form"
          class="btn btn-primary"
          :disabled="
            directories.saving || !form.name.trim()
          "
        >
          Сохранить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>

  <UiResponsiveDialog
    v-model="tagsDialogOpen"
    :title="`Теги: ${selectedSpeciality?.name || ''}`"
  >
    <div
      v-if="loadingTags"
      class="flex justify-center py-10"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <div v-else class="space-y-2">
      <label
        v-for="tag in activeTags"
        :key="tag.id"
        class="border-base-300 flex cursor-pointer items-center gap-3 rounded-xl border p-3"
      >
        <input
          type="checkbox"
          class="checkbox checkbox-primary"
          :checked="selectedTagIds.includes(tag.id)"
          @change="toggleTag(tag)"
        >

        <span>
          <span class="font-medium">
            {{ tag.name }}
          </span>

          <span
            v-if="tag.description"
            class="text-base-content/50 block text-xs"
          >
            {{ tag.description }}
          </span>
        </span>
      </label>
    </div>

    <template #footer>
      <button
        type="button"
        class="btn btn-primary w-full"
        @click="tagsDialogOpen = false"
      >
        Готово
      </button>
    </template>
  </UiResponsiveDialog>
</template>