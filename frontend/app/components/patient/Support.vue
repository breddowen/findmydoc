<!-- ./frontend/app/components/patient/Support.vue -->
<script setup>
const store = usePatientHomeStore()

const selectedProgram = ref(null)
const dialogOpen = ref(false)
const requesting = ref(false)
const errorMessage = ref('')

function openDialog(program) {
  selectedProgram.value = program
  errorMessage.value = ''
  dialogOpen.value = true
}

async function sendRequest() {
  if (!selectedProgram.value || requesting.value) return

  requesting.value = true
  errorMessage.value = ''

  try {
    await store.requestPurchase(
      selectedProgram.value.id,
    )

    dialogOpen.value = false
    selectedProgram.value = null
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось отправить запрос. Попробуйте ещё раз.'
  } finally {
    requesting.value = false
  }
}
</script>

<template>
  <section
    v-if="
      store.supportPrograms.length
      || store.pendingRequests.length
    "
    class="border-base-300 bg-base-100 rounded-3xl border p-5 sm:p-6"
  >
    <h2 class="text-xl font-semibold">
      Поддержка специалиста
    </h2>

    <p class="text-base-content/70 mt-2 text-sm">
      Можно обсудить программу сопровождения с ассистентом
      клиники. Он объяснит состав, стоимость и порядок записи.
    </p>

    <div
      v-if="store.pendingRequests.length"
      class="mt-5 space-y-3"
      aria-live="polite"
    >
      <div
        v-for="program in store.pendingRequests"
        :key="program.id"
        class="bg-success/10 rounded-2xl p-4"
      >
        <p class="font-medium">
          Запрос отправлен
        </p>

        <p class="mt-1 text-sm">
          {{ program.title }}
        </p>

        <p class="text-base-content/70 mt-2 text-sm">
          Ассистент обычно связывается в течение 1–2 дней
          по телефону, указанному в клинике.
        </p>
      </div>
    </div>

    <div class="mt-5 space-y-4">
      <article
        v-for="program in store.supportPrograms"
        :key="program.id"
        class="border-base-300 rounded-2xl border p-4"
      >
        <p class="text-base-content/60 text-xs">
          Платная программа сопровождения
        </p>

        <h3 class="mt-1 font-semibold">
          {{ program.title }}
        </h3>

        <p
          v-if="program.description"
          class="text-base-content/70 mt-2 text-sm"
        >
          {{ program.description }}
        </p>

        <div class="mt-4 flex flex-wrap gap-2">
          <NuxtLink
            :to="`/programs/${program.id}`"
            class="btn btn-outline btn-sm"
          >
            Состав и стоимость
          </NuxtLink>

          <button
            type="button"
            class="btn btn-ghost btn-sm"
            @click="openDialog(program)"
          >
            Обсудить с ассистентом
          </button>
        </div>
      </article>
    </div>

    <p class="text-base-content/60 mt-4 text-xs">
      Запрос не обязывает покупать программу.
      Это не канал срочной медицинской помощи.
    </p>
  </section>

  <UiResponsiveDialog
    v-model="dialogOpen"
    title="Обсудить программу"
    max-width-class="max-w-md"
  >
    <div class="space-y-4">
      <p class="font-medium">
        {{ selectedProgram?.title }}
      </p>

      <p class="text-base-content/70 text-sm">
        Отправим ассистенту запрос на обсуждение этой программы.
        Он обычно связывается в течение 1–2 дней по телефону,
        указанному в клинике.
      </p>

      <p class="text-base-content/70 text-sm">
        Состав и стоимость согласуются до покупки.
        Оплата в приложении не производится.
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
        role="alert"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn btn-ghost"
          :disabled="requesting"
          @click="dialogOpen = false"
        >
          Пока не нужно
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="requesting"
          @click="sendRequest"
        >
          <span
            v-if="requesting"
            class="loading loading-spinner loading-sm"
          />

          Прошу связаться со мной
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>