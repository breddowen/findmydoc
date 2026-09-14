<!-- ./frontend/app/components/patient/home/LifeAspects.vue -->
<script setup>
defineProps({
  aspects: {
    type: Array,
    default: () => [],
  },
  title: {
    type: String,
    default: 'Что Вы хотите улучшить?',
  },
  description: {
    type: String,
    default:
      'Выберите сферу жизни и познакомьтесь с подходящими программами.',
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
        {{ title }}
      </h2>

      <p
        v-if="description"
        class="text-base-content/60 mt-1 text-sm"
      >
        {{ description }}
      </p>
    </header>

    <details
      v-for="aspect in aspects"
      :key="aspect.id"
      class="collapse collapse-plus border-base-300 bg-base-100 border"
    >
      <summary
        class="collapse-title relative overflow-hidden pr-12"
        :class="{
          'min-h-32 text-white sm:min-h-40': aspect.image_id,
        }"
      >
        <template v-if="aspect.image_id">
          <MediaImage
            purpose="life_aspect"
            :entity-id="aspect.id"
            :image-id="aspect.image_id"
            class="absolute inset-0 h-full w-full"
            alt=""
          />

          <div
            class="pointer-events-none absolute inset-0 bg-black/60"
            aria-hidden="true"
          />
        </template>

        <span class="relative z-10 block font-semibold wrap-anywhere">
          {{ aspect.name }}
        </span>

        <span
          class="relative z-10 mt-1 block text-xs"
          :class="
            aspect.image_id
              ? 'text-white/80'
              : 'text-base-content/60'
          "
        >
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