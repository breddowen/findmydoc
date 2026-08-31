<!-- ./frontend/app/pages/settings/directories.vue -->
<script setup>
definePageMeta({
  middleware: ['user-manager'],
})

const directories = useDirectoriesStore()

const activeTab = ref('specialities')
const errorMessage = ref('')

onMounted(async () => {
  try {
    await directories.fetchAll()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить справочники'
  }
})
</script>

<template>
  <div class="mx-auto max-w-6xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Справочники
      </h1>

      <p class="text-base-content/60 mt-1">
        Управление специальностями и тегами.
      </p>
    </header>

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
      v-if="directories.loading"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <template v-else>
      <div role="tablist" class="tabs tabs-box">
        <button
          type="button"
          role="tab"
          class="tab"
          :class="{
            'tab-active':
              activeTab === 'specialities',
          }"
          @click="activeTab = 'specialities'"
        >
          Специальности
        </button>

        <button
          type="button"
          role="tab"
          class="tab"
          :class="{
            'tab-active': activeTab === 'tags',
          }"
          @click="activeTab = 'tags'"
        >
          Теги
        </button>
      </div>

      <DirectoriesSpecialities
        v-if="activeTab === 'specialities'"
      />

      <DirectoriesTags v-else />
    </template>
  </div>
</template>