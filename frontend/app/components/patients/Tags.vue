<!-- ./frontend/app/components/patients/Tags.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useTagAccessStore()
const errorMessage = ref('')

async function load() {
  errorMessage.value = ''

  try {
    await store.fetchPatientState(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить теги пациента'
  }
}

async function setOverride({ tag, action }) {
  errorMessage.value = ''

  try {
    await store.setPatientOverride(
      props.patientId,
      tag.id,
      action,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить тег пациента'
  }
}

async function resetOverride(tag) {
  errorMessage.value = ''

  try {
    await store.resetPatientOverride(
      props.patientId,
      tag.id,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сбросить настройку тега'
  }
}

watch(
  () => props.patientId,
  load,
  {
    immediate: true,
  },
)
</script>

<template>
  <section
    class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
  >
    <div>
      <h2 class="text-xl font-bold">
        Теги пациента
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Пациент наследует теги активных врачей.
        Индивидуальные настройки имеют более высокий
        приоритет.
      </p>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-4"
    >
      {{ errorMessage }}
    </div>

    <div class="mt-5">
      <TagsOverrideEditor
        :tags="store.tags"
        :effective-tags="
          store.patientEffectiveTags
        "
        :overrides="store.patientOverrides"
        :loading="store.loadingPatient"
        :saving="store.saving"
        default-label="Наследовать от врачей"
        @set="setOverride"
        @reset="resetOverride"
      />
    </div>
  </section>
</template>