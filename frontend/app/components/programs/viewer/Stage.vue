<!-- ./frontend/app/components/programs/viewer/Stage.vue -->
<script setup>
const props = defineProps({
  stage: {
    type: Object,
    required: true,
  },
  programId: {
    type: String,
    required: true,
  },
  patientId: {
    type: String,
    default: null,
  },
  isPatient: {
    type: Boolean,
    default: false,
  },
  purchaseLabel: {
    type: String,
    default: 'Купить программу',
  },
})

const emit = defineEmits([
  'purchase',
])

const statusMeta = {
  upcoming: {
    title: 'Ещё не открыт',
    class: 'badge-neutral',
    icon: 'lucide:clock',
  },
  available: {
    title: 'Доступен',
    class: 'badge-info',
    icon: 'lucide:play',
  },
  in_progress: {
    title: 'В процессе',
    class: 'badge-warning',
    icon: 'lucide:loader-circle',
  },
  completed: {
    title: 'Выполнен',
    class: 'badge-success',
    icon: 'lucide:circle-check',
  },
  overdue: {
    title: 'Есть невыполненные задания',
    class: 'badge-error',
    icon: 'lucide:triangle-alert',
  },
}

function getItemLink(item) {
  if (item.item_type === 'article') {
    return {
      path: `/content/articles/${item.content_id}`,
      query: {
        program: props.programId,
        stage: props.stage.id,
      },
    }
  }

  if (
    item.item_type === 'questionnaire'
    && props.isPatient
  ) {
    return {
      path: `/questionnaires/${item.content_id}`,
      query: {
        program: props.programId,
        stage: props.stage.id,
      },
    }
  }

  if (
    item.item_type === 'questionnaire'
    && props.patientId
    && item.submission_id
  ) {
    return (
      `/patients/${props.patientId}`
      + `/questionnaires/${item.submission_id}`
    )
  }

  return null
}
function canOpenItem(item) {
  if (item.item_type === 'consultation') {
    return false
  }

  if (props.isPatient) {
    return item.can_access
  }

  if (item.item_type === 'article') {
    return true
  }

  return Boolean(
    props.patientId
    && item.submission_id
  )
}

function getActionText(item) {
  if (props.isPatient) {
    return item.is_completed
      ? 'Открыть снова'
      : 'Выполнить'
  }

  if (item.item_type === 'article') {
    return 'Открыть статью'
  }

  if (item.submission_id) {
    return item.is_completed
      ? 'Посмотреть результат'
      : 'Посмотреть ответы'
  }

  return ''
}
</script>

<template>
  <section
    class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
  >
    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between"
    >
      <div>
        <p class="text-primary text-sm font-medium">
          День {{ stage.day_from }}–{{ stage.day_to }}
        </p>

        <h2 class="mt-1 text-2xl font-bold">
          {{ stage.title }}
        </h2>

        <p
          v-if="stage.description"
          class="text-base-content/70 mt-3"
        >
          {{ stage.description }}
        </p>
      </div>

      <span
        class="badge gap-1"
        :class="
          statusMeta[stage.status]?.class
        "
      >
        <Icon
          :name="
            statusMeta[stage.status]?.icon
            || 'lucide:circle'
          "
          class="size-3"
        />

        {{
          statusMeta[stage.status]?.title
          || stage.status
        }}
      </span>
    </div>

    <div
      v-if="isPatient"
      class="mt-5"
    >
      <div class="mb-2 flex justify-between text-sm">
        <span>Выполнение этапа</span>
        <strong>{{ stage.progress_percent }}%</strong>
      </div>

      <progress
        class="progress progress-primary w-full"
        :value="stage.progress_percent"
        max="100"
      />
    </div>

    <div
      v-if="stage.doctor_description"
      class="border-info/30 bg-info/10 mt-5 rounded-2xl border p-4"
    >
      <div class="flex gap-3">
        <Icon
          name="lucide:stethoscope"
          class="text-info size-5 shrink-0"
        />

        <div>
          <p class="font-semibold">
            Инструкция для врача
          </p>

          <p class="mt-1 text-sm">
            {{ stage.doctor_description }}
          </p>
        </div>
      </div>
    </div>

    <div class="relative mt-8 space-y-4">
      <div
        class="bg-base-300 absolute bottom-5 left-5 top-5 w-0.5"
      />

      <article
        v-for="(item, index) in stage.items"
        :key="item.id"
        class="relative flex gap-4"
      >
        <div
          class="z-10 flex size-10 shrink-0 items-center justify-center rounded-full border-4 border-base-100"
          :class="{
            'bg-success text-success-content':
              item.is_completed,
            'bg-primary text-primary-content':
              !item.is_completed
              && item.can_access
              && item.item_type !== 'consultation',
            'bg-base-300':
              !item.can_access,
            'bg-accent text-accent-content':
              item.item_type === 'consultation',
          }"
        >
          <Icon
            v-if="item.is_completed"
            name="lucide:check"
            class="size-4"
          />

          <Icon
            v-else-if="item.item_type === 'article'"
            name="lucide:file-text"
            class="size-4"
          />

          <Icon
            v-else-if="
              item.item_type === 'questionnaire'
            "
            name="lucide:clipboard-list"
            class="size-4"
          />

          <Icon
            v-else
            name="lucide:stethoscope"
            class="size-4"
          />
        </div>

        <div
          class="border-base-300 min-w-0 flex-1 rounded-2xl border p-4"
          :class="{
            'border-success/40 bg-success/5':
              item.is_completed,
            'border-accent/40 bg-accent/5':
              item.item_type === 'consultation',
          }"
        >
          <div
            class="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between"
          >
            <div>
              <p class="text-base-content/50 text-xs">
                Шаг {{ index + 1 }}
              </p>

              <h3 class="mt-1 font-semibold">
                {{ item.title }}
              </h3>

              <p
                v-if="item.description"
                class="text-base-content/60 mt-2 text-sm"
              >
                {{ item.description }}
              </p>
            </div>

            <span
              v-if="item.pro_content"
              class="badge badge-secondary shrink-0"
            >
              Pro
            </span>
          </div>

          <div
                v-if="
                    item.item_type !== 'consultation'
                "
                class="mt-4"
                >
                <!-- Пациент -->
                <template v-if="isPatient">
                    <NuxtLink
                    v-if="item.can_access"
                    :to="getItemLink(item)"
                    class="btn btn-primary btn-sm"
                    >
                    {{ getActionText(item) }}
                    </NuxtLink>

                    <button
                    v-else
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="emit('purchase')"
                    >
                    <Icon
                        name="lucide:shopping-cart"
                        class="size-4"
                    />

                    {{ purchaseLabel }}
                    </button>
                </template>

                <!-- Врач, ассистент или суперпользователь -->
                <template v-else>
                    <NuxtLink
                    v-if="canOpenItem(item)"
                    :to="getItemLink(item)"
                    class="btn btn-outline btn-sm"
                    >
                    <Icon
                        :name="
                        item.item_type === 'article'
                            ? 'lucide:external-link'
                            : 'lucide:clipboard-check'
                        "
                        class="size-4"
                    />

                    {{ getActionText(item) }}
                    </NuxtLink>

                    <span
                    v-else-if="
                        item.item_type === 'questionnaire'
                    "
                    class="badge badge-ghost"
                    >
                    Пациент не начинал
                    </span>
                </template>
                </div>

          <div
            v-else
            class="mt-4 flex items-center gap-2 text-sm"
          >
            <Icon
              name="lucide:calendar-clock"
              class="text-accent size-4"
            />

            Консультация запланирована после выполнения
            предыдущих заданий этапа.
          </div>
        </div>
      </article>
    </div>
  </section>
</template>