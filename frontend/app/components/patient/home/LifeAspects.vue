<!-- ./frontend/app/components/patient/home/LifeAspects.vue -->
<script setup>
defineProps({
  aspects: {
    type: Array,
    default: () => [],
  },
})

const emit = defineEmits(['request-purchase'])
</script>

<template>
  <section
    v-if="aspects.length"
    class="space-y-3"
    aria-labelledby="patient-life-aspects-title"
  >
    <header>
      <h2
        id="patient-life-aspects-title"
        class="text-xl font-bold sm:text-2xl"
      >
        Что Вы хотите улучшить?
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Выберите сферу жизни и познакомьтесь
        с подходящими программами.
      </p>
    </header>

    <details
      v-for="aspect in aspects"
      :key="aspect.id"
      class="collapse collapse-plus border-base-300 bg-base-100 border"
    >
      <summary class="collapse-title pr-12">
        <span class="block font-semibold wrap-anywhere">
          {{ aspect.name }}
        </span>

        <span class="text-base-content/60 mt-1 block text-xs">
          Программ: {{ aspect.programs.length }}
        </span>
      </summary>

      <div class="collapse-content">
        <ContentRichTextRenderer
          v-if="aspect.description"
          :content="aspect.description"
          class="mb-4"
        />

        <div class="grid items-stretch gap-3 md:grid-cols-2">
          <PatientProgramCard
            v-for="program in aspect.programs"
            :key="program.id"
            :program="program"
            :show-steps="false"
            @request-purchase="
              emit('request-purchase', $event)
            "
          />
        </div>
      </div>
    </details>
  </section>
</template>