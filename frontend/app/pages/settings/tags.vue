<!-- ./frontend/app/pages/settings/tags.vue -->
<script setup>
definePageMeta({
  middleware: [
    'doctor-only',
  ],
})

const store = useTagAccessStore()
const errorMessage = ref('')
const message = ref('')

async function load() {
  errorMessage.value = ''

  try {
    await store.fetchDoctorState()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить теги врача'
  }
}

async function setOverride({ tag, action }) {
  errorMessage.value = ''
  message.value = ''

  try {
    await store.setDoctorOverride(
      tag.id,
      action,
    )

    message.value = 'Настройка тега сохранена'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить тег'
  }
}

async function resetOverride(tag) {
  errorMessage.value = ''
  message.value = ''

  try {
    await store.resetDoctorOverride(tag.id)

    message.value = (
      'Восстановлено значение специальности'
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сбросить настройку'
  }
}

onMounted(load)
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Мои теги
      </h1>

      <p class="text-base-content/60 mt-1">
        Индивидуальная настройка тегов,
        унаследованных от специальности.
      </p>
    </header>

    <div class="alert alert-warning">
      <Icon
        name="lucide:triangle-alert"
        class="size-5"
      />

      <span>
        Изменение ваших тегов повлияет на фильтрацию
        контента у всех прикреплённых пациентов.
      </span>
    </div>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <section
      class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
    >
      <TagsOverrideEditor
        :tags="store.tags"
        :effective-tags="
          store.doctorEffectiveTags
        "
        :overrides="store.doctorOverrides"
        :loading="store.loadingDoctor"
        :saving="store.saving"
        default-label="Настройка специальности"
        @set="setOverride"
        @reset="resetOverride"
      />
    </section>
  </div>
</template>