<!-- ./frontend/app/components/assignments/PatientList.vue -->
<script setup>
const store = useAssignmentsStore()

const activeAssignments = computed(() =>
  store.assignments.filter(
    (item) =>
      [
        'assigned',
        'in_progress',
      ].includes(item.status),
  ),
)

function getLink(assignment) {
  if (assignment.assignment_type === 'article') {
    return `/content/articles/${assignment.content_id}`
  }

  return `/questionnaires/${assignment.content_id}`
}

onMounted(store.fetchMyAssignments)


</script>

<template>
  <section
    v-if="store.loading || activeAssignments.length"
    class="space-y-4"
  >
    <div>
      <h2 class="text-xl font-bold sm:text-2xl">
        Назначено
      </h2>

      <p class="text-base-content/60 text-sm">
        Материалы, назначенные врачом.
      </p>
    </div>

    <UiContentSkeleton
      v-if="store.loading"
      variant="card"
      :count="2"
    />

    <div
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="assignment in activeAssignments"
        :key="assignment.id"
        class="aura aura-gold h-full"
      >
        <NuxtLink
          :to="getLink(assignment)"
          class="card bg-base-100 h-full"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-2">
              <span
                class="badge badge-warning gap-1"
              >
                <Icon
                  name="lucide:star"
                  class="size-3"
                />
                Назначено
              </span>

              <span
                v-if="assignment.pro_content"
                class="badge badge-secondary"
              >
                Pro
              </span>
            </div>

            <h3 class="card-title">
              {{ assignment.title }}
            </h3>

            <p class="text-base-content/60 text-sm">
              {{
                assignment.assignment_type === 'article'
                  ? 'Статья'
                  : 'Опросник'
              }}
            </p>

            <div class="card-actions mt-auto">
              <span class="btn btn-primary btn-sm">
                {{
                  assignment.status === 'in_progress'
                    ? 'Продолжить'
                    : 'Открыть'
                }}
              </span>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
  </section>
</template>