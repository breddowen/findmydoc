<!-- ./frontend/app/layouts/program.vue -->
<script setup>
const route = useRoute()
const context = useProgramContext()
const store = useProgramJourneyStore()

watch(
  () => route.fullPath,
  () => {
    if (context.programId.value) {
      void store.load(context.programId.value).catch(() => {})
    }
  },
  { immediate: true },
)

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="bg-base-200 flex min-h-dvh min-w-0 flex-col">
    <ProgramsJourneyNavbar />

    <main
      class="mx-auto w-full max-w-7xl flex-1 px-4 py-5 sm:py-7"
    >
      <slot />
    </main>

    <footer 
    data-floating-footer
    class="border-base-300 mt-6 border-t px-4 py-5">
      <div class="mx-auto w-full max-w-7xl">
        <PatientSupportActions footer />
      </div>
    </footer>
  </div>
</template>