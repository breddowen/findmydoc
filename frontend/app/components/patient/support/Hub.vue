<!-- ./frontend/app/components/patient/support/Hub.vue -->
<script setup>
const route = useRoute()
const support = usePatientSupportStore()
const emc = useEmcAppStore()

const demoMessage = ref('')

function panelModel(name) {
  return computed({
    get: () => support.panel === name,
    set: value => {
      if (!value && support.panel === name) {
        support.close()
      }
    },
  })
}

const actionsOpen = panelModel('actions')
const assistantOpen = panelModel('assistant')
const doctorsOpen = panelModel('doctors')

function selectDemoAppointment() {
  demoMessage.value =
    'Демонстрационный режим: запись пока недоступна. '
    + 'Реальная заявка не создавалась.'
}

watch(
  () => support.panel,
  panel => {
    if (panel === 'doctors') {
      demoMessage.value = ''
      emc.refreshDemoDays()
    }
  },
  { immediate: true },
)

watch(
  () => route.fullPath,
  () => support.close(),
)

onBeforeUnmount(() => {
  support.close()
})
</script>

<template>
  <!--
    При смене действия предыдущий диалог размонтируется:
    вложенных окон и двух одновременных backdrop нет.
  -->
  <UiResponsiveDialog
    v-if="support.panel === 'actions'"
    v-model="actionsOpen"
    title="Чем мы можем помочь?"
    max-width-class="max-w-md"
  >
    <PatientSupportActions />

    <!-- <p class="text-base-content/50 mt-4 text-xs">
      Это не канал срочной медицинской помощи.
    </p> -->
  </UiResponsiveDialog>

  <PatientContactDialog
    v-else-if="support.panel === 'assistant'"
    v-model="assistantOpen"
  />

  <UiResponsiveDialog
    v-else-if="support.panel === 'doctors'"
    v-model="doctorsOpen"
    title="Записаться к врачу"
    max-width-class="max-w-3xl"
  >
    <p class="text-base-content/60 mb-4 text-sm">
      Демонстрационные специалисты и даты.
      Реальное расписание появится после интеграции
      с личным кабинетом EMC.
    </p>

    <div class="grid gap-4 sm:grid-cols-2">
      <TestPsychiatristCard
        v-for="doctor in emc.doctors"
        :key="doctor.id"
        :doctor="doctor"
        :days="emc.nearestDays"
        @select="selectDemoAppointment"
      />
    </div>

    <div
      v-if="demoMessage"
      class="alert alert-info mt-4"
      role="status"
    >
      <Icon name="lucide:info" class="size-5" />
      <span>{{ demoMessage }}</span>
    </div>
  </UiResponsiveDialog>
</template>