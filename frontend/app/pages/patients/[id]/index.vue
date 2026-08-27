<!-- ./frontend/app/pages/patients/[id]/index.vue -->
<script setup>
const route = useRoute()
const auth = useAuthStore()
const store = usePatientsStore()

const patient = computed(
  () => store.currentPatient,
)

const errorMessage = ref('')
const assignmentDialogOpen = ref(false)
const successMessage = ref('')

const activityTab = ref('programs')

const isAdminStaff = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole)
)

function formatDate(value) {
  if (!value) return '—'

  return new Intl.DateTimeFormat(
    'ru-RU',
    {
      dateStyle: 'medium',
      timeStyle: 'short',
    },
  ).format(new Date(value))
}

function handleAssigned(assignment) {
  successMessage.value =
    `Пациенту назначено: ${assignment.title}`

  window.setTimeout(() => {
    successMessage.value = ''
  }, 4000)
}

onMounted(async () => {
  try {
    await store.fetchPatient(route.params.id)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить пациента'
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="store.loading && !patient"
    variant="card"
    :count="3"
  />

  <div
    v-else-if="errorMessage && !patient"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="patient"
    class="space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <div
        class="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between"
      >
        <div>
          <div
            class="flex flex-wrap items-center gap-2"
          >
            <h1 class="text-2xl font-bold sm:text-3xl">
              {{ patient.fullname }}
            </h1>

            <span
              v-if="patient.pro_enabled"
              class="badge badge-secondary"
            >
              Pro
            </span>
          </div>

          <p class="text-base-content/60 mt-2">
            {{ patient.email }}
          </p>

          <p class="text-base-content/50 text-sm">
            Карта: {{ patient.record_id }}
          </p>
        </div>

        <div
          class="flex flex-col gap-3 sm:flex-row sm:items-center"
        >
          <button
            type="button"
            class="btn btn-primary"
            @click="assignmentDialogOpen = true"
          >
            <Icon
              name="lucide:send"
              class="size-4"
            />

            Назначить контент
          </button>

          <PatientsProAccess
            v-if="isAdminStaff"
            :patient-id="patient.patient_id"
            :enabled="patient.pro_enabled"
            @updated="
              patient.pro_enabled = $event
            "
          />
        </div>
      </div>

      <div
        class="border-base-300 mt-6 grid gap-4 border-t pt-5 sm:grid-cols-2 lg:grid-cols-4"
      >
        <div>
          <p class="text-base-content/50 text-xs">
            Регистрация
          </p>

          <p class="mt-1 font-medium">
            {{ formatDate(patient.registered_at) }}
          </p>
        </div>

        <div>
          <p class="text-base-content/50 text-xs">
            Последняя активность
          </p>

          <p class="mt-1 font-medium">
            {{ formatDate(patient.last_activity_at) }}
          </p>
        </div>

        <div>
          <p class="text-base-content/50 text-xs">
            Дата рождения
          </p>

          <p class="mt-1 font-medium">
            {{
              patient.dob
                ? new Date(
                    patient.dob,
                  ).toLocaleDateString('ru-RU')
                : 'Не указана'
            }}
          </p>
        </div>

        <div>
          <p
            class="text-base-content/50 mb-1 text-xs"
          >
            Контакт ассистента
          </p>

          <PatientsContactStatus
            :allowed="
              patient.assistant_contact_allowed
            "
            :do-not-call="patient.do_not_call"
          />
        </div>
      </div>
    </header>

    <div
      v-if="successMessage"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />

      <span>{{ successMessage }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <ProgramsPatientAccess
      v-if="isAdminStaff"
      :patient-id="patient.patient_id"
    />

    <!-- Врачи -->
    <section
      class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
    >
      <h2 class="text-xl font-bold">
        Врачи
      </h2>

      <div
        v-if="patient.doctors.length"
        class="mt-4 grid gap-3 md:grid-cols-2"
      >
        <div
          v-for="doctor in patient.doctors"
          :key="doctor.doctor_id"
          class="border-base-300 flex items-center gap-3 rounded-2xl border p-4"
        >
          <div
            class="bg-primary/10 text-primary flex size-11 shrink-0 items-center justify-center rounded-xl"
          >
            <Icon
              name="lucide:stethoscope"
              class="size-5"
            />
          </div>

          <div class="min-w-0">
            <p class="truncate font-medium">
              {{ doctor.fullname }}
            </p>

            <p class="text-base-content/60 text-sm">
              {{ doctor.speciality_name }}
            </p>
          </div>
        </div>
      </div>

      <p
        v-else
        class="text-base-content/50 mt-4"
      >
        Активных врачей нет.
      </p>
    </section>

    <!-- Активность пациента -->
    <section class="space-y-5">
      <div
        role="tablist"
        class="tabs tabs-box w-full sm:w-fit"
      >
        <button
          type="button"
          role="tab"
          class="tab gap-2"
          :class="{
            'tab-active':
              activityTab === 'programs',
          }"
          @click="activityTab = 'programs'"
        >
          <Icon
            name="lucide:route"
            class="size-4"
          />

          Программы
        </button>

        <button
          type="button"
          role="tab"
          class="tab gap-2"
          :class="{
            'tab-active':
              activityTab === 'content',
          }"
          @click="activityTab = 'content'"
        >
          <Icon
            name="lucide:library"
            class="size-4"
          />

          Отдельный контент
        </button>
      </div>

      <!-- Программы -->
      <ProgramsPatientProgress
        v-if="activityTab === 'programs'"
        :patient-id="patient.patient_id"
      />

      <!-- Отдельный контент -->
      <div
        v-else
        class="space-y-6"
      >
        <!-- Статьи -->
        <section
          class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
        >
          <h2 class="text-xl font-bold">
            Статьи
          </h2>

          <div
            v-if="patient.articles.length"
            class="mt-4 space-y-3"
          >
            <div
              v-for="article in patient.articles"
              :key="article.article_id"
              class="border-base-300 rounded-2xl border p-4"
            >
              <div
                class="flex items-center justify-between gap-4"
              >
                <NuxtLink
                  :to="`/content/articles/${article.article_id}`"
                  class="link link-hover font-medium"
                >
                  {{ article.title }}
                </NuxtLink>

                <span
                  v-if="article.completed_at"
                  class="badge badge-success"
                >
                  Прочитана
                </span>
              </div>

              <progress
                class="progress progress-secondary mt-3 w-full"
                :value="
                  article.max_progress_percent
                "
                max="100"
              />

              <p class="mt-1 text-xs">
                {{ article.max_progress_percent }}%
              </p>
            </div>
          </div>

          <p
            v-else
            class="text-base-content/50 mt-4"
          >
            Пациент пока не открывал статьи.
          </p>
        </section>

        <!-- Опросники -->
        <section
          class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
        >
          <h2 class="text-xl font-bold">
            Опросники
          </h2>

          <div
            v-if="patient.questionnaires.length"
            class="mt-4 space-y-3"
          >
            <NuxtLink
              v-for="submission in patient.questionnaires"
              :key="submission.submission_id"
              :to="
                `/patients/${patient.patient_id}`
                + `/questionnaires/${submission.submission_id}`
              "
              class="border-base-300 hover:border-primary block rounded-2xl border p-4 transition"
            >
              <div
                class="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between"
              >
                <div>
                  <p class="font-medium">
                    {{
                      submission.questionnaire_title
                    }}
                  </p>

                  <p
                    class="text-base-content/50 text-xs"
                  >
                    Начат:
                    {{
                      formatDate(
                        submission.started_at,
                      )
                    }}
                  </p>
                </div>

                <span
                  class="badge"
                  :class="
                    submission.status
                      === 'completed'
                      ? 'badge-success'
                      : 'badge-warning'
                  "
                >
                  {{
                    submission.status
                      === 'completed'
                      ? 'Завершён'
                      : 'Не завершён'
                  }}
                </span>
              </div>

              <progress
                class="progress progress-primary mt-3 w-full"
                :value="
                  submission.progress_percent
                "
                max="100"
              />

              <p class="mt-1 text-xs">
                {{
                  submission.answered_questions
                }}
                из
                {{ submission.questions_count }}
              </p>
            </NuxtLink>
          </div>

          <p
            v-else
            class="text-base-content/50 mt-4"
          >
            Пациент пока не проходил опросники.
          </p>
        </section>
      </div>
    </section>

    <AssignmentsCreateDialog
      v-model="assignmentDialogOpen"
      :patient-id="patient.patient_id"
      :patient-name="patient.fullname"
      @assigned="handleAssigned"
    />
  </div>
</template>