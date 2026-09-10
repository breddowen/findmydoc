У меня такой проект:
```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (29 lines)
backend/alembic/versions/4a9d77a6cc23_initial_schema.py (887 lines)
backend/alembic/versions/6042112705c7_article_analytics_events.py (487 lines)
backend/alembic/versions/6eb4582e2464_add_new_field_to_users.py (33 lines)
backend/alembic/versions/7c21a6d4ef10_admin_invitations_and_hidden_directories.py (170 lines)
backend/alembic/versions/95f734785945_program_home_fields.py (71 lines)
backend/alembic/versions/9f31b8c4d2e7_medical_services.py (454 lines)
backend/alembic/versions/b1e4c7d902af_content_library_visibility.py (40 lines)
backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py (141 lines)
backend/alembic/versions/d3f8a2c6e901_life_aspects.py (157 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (58 lines)
backend/app/core/db.py (129 lines)
backend/app/core/email.py (150 lines)
backend/app/core/security.py (232 lines)
backend/app/core/transactions.py (60 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (113 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/access.py (64 lines)
backend/app/modules/articles/models.py (126 lines)
backend/app/modules/articles/routers.py (918 lines)
backend/app/modules/articles/schemas.py (127 lines)
backend/app/modules/articles/tracking.py (91 lines)
backend/app/modules/articles/utils.py (186 lines)
backend/app/modules/assignments/__init__.py (0 lines)
backend/app/modules/assignments/enums.py (14 lines)
backend/app/modules/assignments/models.py (81 lines)
backend/app/modules/assignments/routers.py (302 lines)
backend/app/modules/assignments/schemas.py (56 lines)
backend/app/modules/assignments/utils.py (106 lines)
backend/app/modules/auth/__init__.py (0 lines)
backend/app/modules/auth/models.py (73 lines)
backend/app/modules/auth/routers.py (753 lines)
backend/app/modules/auth/schemas.py (97 lines)
backend/app/modules/auth/utils.py (148 lines)
backend/app/modules/consents/__init__.py (0 lines)
backend/app/modules/consents/contact_routers.py (187 lines)
backend/app/modules/consents/contact_schemas.py (20 lines)
backend/app/modules/consents/contact_service.py (123 lines)
backend/app/modules/consents/enums.py (15 lines)
backend/app/modules/consents/models.py (83 lines)
backend/app/modules/consents/routers.py (252 lines)
backend/app/modules/consents/schemas.py (38 lines)
backend/app/modules/consents/utils.py (37 lines)
backend/app/modules/content/__init__.py (0 lines)
backend/app/modules/content/utils.py (167 lines)
backend/app/modules/events/__init__.py (0 lines)
backend/app/modules/events/enums.py (34 lines)
backend/app/modules/events/models.py (116 lines)
backend/app/modules/events/routers.py (69 lines)
backend/app/modules/events/schemas.py (32 lines)
backend/app/modules/events/service.py (60 lines)
backend/app/modules/invitations/__init__.py (0 lines)
backend/app/modules/invitations/admin_routers.py (422 lines)
backend/app/modules/invitations/admin_schemas.py (93 lines)
backend/app/modules/invitations/admin_utils.py (224 lines)
backend/app/modules/invitations/enums.py (17 lines)
backend/app/modules/invitations/models.py (127 lines)
backend/app/modules/invitations/routers.py (1277 lines)
backend/app/modules/invitations/schemas.py (152 lines)
backend/app/modules/invitations/utils.py (222 lines)
backend/app/modules/notifications/__init__.py (0 lines)
backend/app/modules/notifications/enums.py (30 lines)
backend/app/modules/notifications/models.py (64 lines)
backend/app/modules/notifications/routers.py (288 lines)
backend/app/modules/notifications/schemas.py (47 lines)
backend/app/modules/notifications/service.py (163 lines)
backend/app/modules/notifications/ToDo.md (1 lines)
backend/app/modules/notifications/transactional.py (91 lines)
backend/app/modules/patients/__init__.py (0 lines)
backend/app/modules/patients/enums.py (7 lines)
backend/app/modules/patients/routers.py (511 lines)
backend/app/modules/patients/schemas.py (138 lines)
backend/app/modules/patients/utils.py (231 lines)
backend/app/modules/programs/__init__.py (0 lines)
backend/app/modules/programs/enums.py (22 lines)
backend/app/modules/programs/models.py (358 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1848 lines)
backend/app/modules/programs/schemas.py (274 lines)
backend/app/modules/programs/utils.py (632 lines)
backend/app/modules/questionnaires/__init__.py (0 lines)
backend/app/modules/questionnaires/enums.py (17 lines)
backend/app/modules/questionnaires/json_q/audit.json (272 lines)
backend/app/modules/questionnaires/models.py (237 lines)
backend/app/modules/questionnaires/Readme.md (61 lines)
backend/app/modules/questionnaires/routers.py (1291 lines)
backend/app/modules/questionnaires/schemas.py (218 lines)
backend/app/modules/questionnaires/utils.py (303 lines)
backend/app/modules/referrals/__init__.py (0 lines)
backend/app/modules/referrals/enums.py (19 lines)
backend/app/modules/referrals/models.py (114 lines)
backend/app/modules/referrals/routers.py (464 lines)
backend/app/modules/referrals/schemas.py (83 lines)
backend/app/modules/referrals/utils.py (42 lines)
backend/app/modules/relationships/__init__.py (0 lines)
backend/app/modules/relationships/routers.py (580 lines)
backend/app/modules/relationships/schemas.py (79 lines)
backend/app/modules/services/__init__.py (0 lines)
backend/app/modules/services/enums.py (8 lines)
backend/app/modules/services/models.py (131 lines)
backend/app/modules/services/routers.py (350 lines)
backend/app/modules/services/schemas.py (159 lines)
backend/app/modules/services/utils.py (118 lines)
backend/app/modules/specialities/__init__.py (0 lines)
backend/app/modules/specialities/routers.py (331 lines)
backend/app/modules/specialities/schemas.py (50 lines)
backend/app/modules/tags/__init__.py (0 lines)
backend/app/modules/tags/enums.py (7 lines)
backend/app/modules/tags/life_aspect_catalog.py (227 lines)
backend/app/modules/tags/life_aspect_patient_routers.py (46 lines)
backend/app/modules/tags/life_aspect_routers.py (360 lines)
backend/app/modules/tags/life_aspect_schemas.py (131 lines)
backend/app/modules/tags/models.py (279 lines)
backend/app/modules/tags/routers.py (957 lines)
backend/app/modules/tags/schemas.py (104 lines)
backend/app/modules/tags/utils.py (246 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (334 lines)
backend/app/modules/users/routers.py (360 lines)
backend/app/modules/users/schemas.py (145 lines)
backend/app/modules/users/utils.py (126 lines)
backend/requirements.txt (47 lines)
backend/seed/check_program_progress.py (140 lines)
backend/seed/create_superuser.py (153 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/repair_program_submission_stage.py (193 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database — копия.db (1254 lines)
backend/test_database.db (1393 lines)
```

*Files: 141*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (209 lines)
frontend/app/components/articles/Form.vue (241 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (486 lines)
frontend/app/components/articles/ReaderAction.vue (196 lines)
frontend/app/components/assignments/ContentPicker.vue (181 lines)
frontend/app/components/assignments/CreateDialog.vue (345 lines)
frontend/app/components/assignments/PatientList.vue (108 lines)
frontend/app/components/assignments/PickerItem.vue (130 lines)
frontend/app/components/auth/PasswordForm.vue (173 lines)
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (294 lines)
frontend/app/components/content/LibraryVisibility.vue (38 lines)
frontend/app/components/content/RichTextEditor.vue (469 lines)
frontend/app/components/content/RichTextRenderer.vue (136 lines)
frontend/app/components/content/TagSelector.vue (80 lines)
frontend/app/components/directories/Specialities.vue (471 lines)
frontend/app/components/directories/Tags.vue (311 lines)
frontend/app/components/invitations/LinkDialog.vue (257 lines)
frontend/app/components/invitations/PatientDialog.vue (435 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (88 lines)
frontend/app/components/layout/Footer.vue (52 lines)
frontend/app/components/layout/Logo.vue (86 lines)
frontend/app/components/layout/Navbar.vue (405 lines)
frontend/app/components/layout/PatientActions.vue (29 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/life-aspects/FormDialog.vue (165 lines)
frontend/app/components/life-aspects/Tag.vue (85 lines)
frontend/app/components/life-aspects/TagLinks.vue (392 lines)
frontend/app/components/notifications/BrowserPermission.vue (96 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patient/ContactDialog.vue (208 lines)
frontend/app/components/patient/Home.vue (179 lines)
frontend/app/components/patient/home/ContinueCard.vue (74 lines)
frontend/app/components/patient/home/Hero.vue (51 lines)
frontend/app/components/patient/home/LifeAspects.vue (69 lines)
frontend/app/components/patient/home/Recommendations.vue (265 lines)
frontend/app/components/patient/home/RotatingText.vue (119 lines)
frontend/app/components/patient/Journey.vue (79 lines)
frontend/app/components/patient/NextStep.vue (184 lines)
frontend/app/components/patient/ProgramCard.vue (233 lines)
frontend/app/components/patient/ProgramSteps.vue (96 lines)
frontend/app/components/patient/PurchaseDialog.vue (129 lines)
frontend/app/components/patient/Support.vue (186 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (111 lines)
frontend/app/components/patients/List.vue (257 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/patients/Tags.vue (105 lines)
frontend/app/components/programs/configurator/Editor.vue (738 lines)
frontend/app/components/programs/configurator/HomeSettings.vue (68 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (395 lines)
frontend/app/components/programs/configurator/LibraryEntry.vue (70 lines)
frontend/app/components/programs/configurator/ServiceSelect.vue (170 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (411 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (537 lines)
frontend/app/components/questionnaires/JsonImporter.vue (265 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/services/DeleteDialog.vue (95 lines)
frontend/app/components/services/FormDialog.vue (463 lines)
frontend/app/components/services/List.vue (181 lines)
frontend/app/components/services/VisibilityDialog.vue (98 lines)
frontend/app/components/tags/OverrideEditor.vue (231 lines)
frontend/app/components/ui/BottomSheet.vue (203 lines)
frontend/app/components/ui/ContentSkeleton.vue (73 lines)
frontend/app/components/ui/MegaMenu.vue (205 lines)
frontend/app/components/ui/Modal.vue (150 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (99 lines)
frontend/app/components/users/InvitationList.vue (231 lines)
frontend/app/components/users/InviteDialog.vue (29 lines)
frontend/app/components/users/InviteForm.vue (367 lines)
frontend/app/components/users/List.vue (182 lines)
```
*Files: 81*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (146 lines)
frontend/app/pages/content/articles/index.vue (186 lines)
frontend/app/pages/content/articles/new.vue (49 lines)
frontend/app/pages/content/questionnaires/[id].vue (319 lines)
frontend/app/pages/content/questionnaires/index.vue (166 lines)
frontend/app/pages/content/questionnaires/new.vue (9 lines)
frontend/app/pages/dashboard.vue (159 lines)
frontend/app/pages/forgot-password.vue (102 lines)
frontend/app/pages/index.vue (25 lines)
frontend/app/pages/login.vue (238 lines)
frontend/app/pages/patients/[id]/index.vue (469 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (37 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (404 lines)
frontend/app/pages/programs/index.vue (285 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (375 lines)
frontend/app/pages/questionnaires/index.vue (209 lines)
frontend/app/pages/register/invitation.vue (379 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/services/index.vue (205 lines)
frontend/app/pages/settings/directories.vue (90 lines)
frontend/app/pages/settings/life-aspects.vue (382 lines)
frontend/app/pages/settings/profile.vue (265 lines)
frontend/app/pages/settings/security.vue (325 lines)
frontend/app/pages/settings/tags.vue (123 lines)
frontend/app/pages/users/index.vue (529 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 30*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (22 lines)
```
*Files: 2*

### composables

```
frontend/app/composables/useAppNavigation.js (199 lines)
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useProgramPrice.js (180 lines)
frontend/app/composables/useReadingProgress.js (203 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 7*

### stores

```
frontend/app/stores/articles.js (172 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/invitations.js (53 lines)
frontend/app/stores/life-aspects.js (158 lines)
frontend/app/stores/notifications.js (387 lines)
frontend/app/stores/patient-home.js (339 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (206 lines)
frontend/app/stores/services.js (159 lines)
frontend/app/stores/tag-access.js (210 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 16*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/doctor-only.js (14 lines)
frontend/app/middleware/life-aspect-manager.js (20 lines)
frontend/app/middleware/program-manager.js (19 lines)
frontend/app/middleware/service-manager.js (19 lines)
frontend/app/middleware/user-manager.js (19 lines)
```
*Files: 6*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*


---
Файлы, которые могут пригодиться:
<!-- ./frontend/app/components/programs/PatientProgress.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const loading = ref(true)
const errorMessage = ref('')

const selectedProgramIndex = ref(0)
const selectedStageIndexes = reactive({})

const selectedProgram = computed(
  () =>
    store.patientProgressPrograms[
      selectedProgramIndex.value
    ],
)

function getSelectedStage(program) {
  const index =
    selectedStageIndexes[program.id] || 0

  return program.stages[index]
}

function statusName(program) {
  if (!program.enrollment) {
    if (program.purchase_requested) {
      return 'Запрошена пациентом'
    }

    return 'Доступ открыт, не начата'
  }

  if (
    program.enrollment.status === 'completed'
  ) {
    return 'Завершена'
  }

  return 'В процессе'
}

onMounted(async () => {
  try {
    await store.fetchPatientProgramProgress(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы пациента'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="2"
  />

  <div
    v-else-if="errorMessage"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="store.patientProgressPrograms.length"
    class="space-y-5"
  >
    <div class="overflow-x-auto pb-1">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(program, index) in store.patientProgressPrograms"
          :key="program.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedProgramIndex === index,
          }"
          @click="selectedProgramIndex = index"
        >
          <Icon
            name="lucide:route"
            class="size-4"
          />
          {{ program.title }}
        </button>
      </div>
    </div>

    <template v-if="selectedProgram">
      <header
        class="bg-base-100 border-base-300 rounded-2xl border p-5"
      >
        <div
          class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"
        >
          <div>
            <h2 class="text-xl font-bold">
              {{ selectedProgram.title }}
            </h2>

            <p class="text-base-content/60 text-sm">
              {{ statusName(selectedProgram) }}
            </p>
          </div>

          <span
            class="badge"
            :class="{
              'badge-warning':
                selectedProgram.purchase_requested,
              'badge-success':
                selectedProgram.enrollment?.status
                  === 'completed',
              'badge-primary':
                selectedProgram.enrollment?.status
                  === 'active',
            }"
          >
            {{ selectedProgram.progress_percent }}%
          </span>
        </div>

        <progress
          class="progress progress-primary mt-4 w-full"
          :value="selectedProgram.progress_percent"
          max="100"
        />
      </header>

      <div class="overflow-x-auto pb-1">
        <div class="join">
          <button
            v-for="(stage, index) in selectedProgram.stages"
            :key="stage.id"
            type="button"
            class="btn join-item btn-sm"
            :class="{
              'btn-primary':
                (selectedStageIndexes[
                  selectedProgram.id
                ] || 0) === index,
            }"
            @click="
              selectedStageIndexes[
                selectedProgram.id
              ] = index
            "
          >
            <Icon
              :name="
                stage.status === 'completed'
                  ? 'lucide:circle-check'
                  : stage.status === 'overdue'
                    ? 'lucide:triangle-alert'
                    : 'lucide:circle'
              "
              class="size-4"
            />

            Этап {{ index + 1 }}
          </button>
        </div>
      </div>

      <ProgramsViewerStage
        v-if="getSelectedStage(selectedProgram)"
        :stage="getSelectedStage(selectedProgram)"
        :program-id="selectedProgram.id"
        :patient-id="patientId"
        :is-patient="false"
        />
    </template>
  </div>

  <div
    v-else
    class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:route-off"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Пациент пока не начал и не приобретал программы
    </p>
  </div>
</template>

<!-- ./frontend/app/components/programs/PatientOverview.vue -->
<script setup>
const store = useProgramsStore()

const loading = ref(true)
const errorMessage = ref('')

const activePrograms = computed(() =>
  store.programs.filter(
    (program) =>
      program.has_program_access
      || program.enrollment,
  ),
)

function statusText(program) {
  if (
    program.enrollment?.status === 'completed'
  ) {
    return 'Завершена'
  }

  if (program.enrollment) {
    return 'В процессе'
  }

  if (program.has_program_access) {
    return 'Доступна'
  }

  return ''
}

onMounted(async () => {
  try {
    await store.fetchProgramsForPatient()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section
    v-if="
      loading
      || errorMessage
      || activePrograms.length
    "
    class="space-y-4"
  >
    <div class="flex items-center justify-between gap-4">
      <div>
        <h2 class="text-xl font-bold sm:text-2xl">
          Мои программы
        </h2>

        <p class="text-base-content/60 text-sm">
          Приобретённые и начатые программы.
        </p>
      </div>

      <NuxtLink
        to="/programs"
        class="btn btn-ghost btn-sm"
      >
        Все программы
      </NuxtLink>
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="2"
    />

    <div
      v-else-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <NuxtLink
        v-for="program in activePrograms"
        :key="program.id"
        :to="`/programs/${program.id}`"
        class="card bg-base-100 border-primary/30 hover:border-primary border transition"
      >
        <div class="card-body">
          <div class="flex flex-wrap gap-2">
            <span
              class="badge"
              :class="
                program.enrollment?.status
                  === 'completed'
                  ? 'badge-success'
                  : 'badge-primary'
              "
            >
              {{ statusText(program) }}
            </span>

            <span
              v-if="program.has_program_access"
              class="badge badge-secondary"
            >
              Полный доступ
            </span>
          </div>

          <h3 class="card-title">
            {{ program.title }}
          </h3>

          <div v-if="program.enrollment">
            <div
              class="mb-1 flex justify-between text-xs"
            >
              <span>Прогресс</span>
              <strong>
                {{ program.progress_percent }}%
              </strong>
            </div>

            <progress
              class="progress progress-primary w-full"
              :value="program.progress_percent"
              max="100"
            />
          </div>

          <div class="card-actions mt-auto">
            <span class="btn btn-primary btn-sm">
              {{
                program.enrollment
                  ? 'Продолжить'
                  : 'Начать'
              }}
            </span>
          </div>
        </div>
      </NuxtLink>
    </div>
  </section>
</template>

<!-- ./frontend/app/components/programs/PatientAccess.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const confirmOpen = ref(false)
const selectedProgram = ref(null)

const errorMessage = ref('')

function requestToggle(program) {
  selectedProgram.value = program
  confirmOpen.value = true
}

async function confirmToggle() {
  if (!selectedProgram.value) return

  try {
    await store.setPatientProgramAccess(
      props.patientId,
      selectedProgram.value.program_id,
      !selectedProgram.value.is_active,
    )

    confirmOpen.value = false
    selectedProgram.value = null
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить доступ'
  }
}

const sortedPrograms = computed(() =>
  [...store.patientAccessPrograms].sort(
    (first, second) => {
      if (
        first.purchase_requested
        !== second.purchase_requested
      ) {
        return first.purchase_requested
          ? -1
          : 1
      }

      return first.title.localeCompare(
        second.title,
        'ru',
      )
    },
  ),
)

onMounted(async () => {
  try {
    await store.fetchPatientProgramAccess(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section
    class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
  >
    <div>
      <h2 class="text-xl font-bold">
        Доступ к программам
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Включение открывает Pro-контент только внутри
        выбранной программы.
      </p>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-4"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="3"
    />

    <div
      v-else
      class="mt-5 space-y-3"
    >
      <div
        v-for="program in sortedPrograms"
        :key="program.program_id"
        class="border-base-300 flex flex-col gap-4 rounded-2xl border p-4 sm:flex-row sm:items-center"
        :class="{
          'border-warning bg-warning/5 ring-warning/10 ring-4':
            program.purchase_requested,
        }"
      >
        <div class="min-w-0 flex-1">
          <div class="flex flex-wrap items-center gap-2">
            <p class="font-medium">
              {{ program.title }}
            </p>

            <span
              v-if="program.purchase_requested"
              class="badge badge-warning badge-sm gap-1"
            >
              <Icon
                name="lucide:shopping-cart"
                class="size-3"
              />
              Пациент запросил доступ
            </span>

            <span
              v-if="program.is_hidden"
              class="badge badge-ghost badge-sm"
            >
              Скрыта
            </span>
          </div>

          <div
            class="text-base-content/60 mt-2 flex flex-wrap items-center gap-2 text-sm"
          >
            <span
              v-if="program.service?.code"
              class="font-mono"
            >
              {{ program.service.code }}
            </span>

            <strong>
              {{ formatFinalPrice(program) }}
            </strong>

            <span
              v-if="hasDiscount(program)"
              class="text-base-content/40 line-through"
            >
              {{ formatOriginalPrice(program) }}
            </span>
          </div>
        </div>

        <label
          class="flex cursor-pointer items-center gap-3"
        >
          <span class="text-sm">
            {{
              program.is_active
                ? 'Доступ открыт'
                : 'Нет доступа'
            }}
          </span>

          <input
            type="checkbox"
            class="toggle toggle-success"
            :checked="program.is_active"
            @change.prevent="requestToggle(program)"
          >
        </label>
      </div>
    </div>
  </section>

  <UiResponsiveDialog
    v-model="confirmOpen"
    :title="
      selectedProgram?.is_active
        ? 'Отключить доступ'
        : 'Открыть доступ'
    "
    max-width-class="max-w-md"
  >
    <p>
      {{
        selectedProgram?.is_active
          ? 'Пациент потеряет доступ к Pro-контенту внутри программы.'
          : 'Пациент получит доступ ко всему Pro-контенту внутри программы.'
      }}
    </p>

    <p class="mt-3 font-semibold">
      {{ selectedProgram?.title }}
    </p>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          @click="confirmOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn"
          :class="
            selectedProgram?.is_active
              ? 'btn-error'
              : 'btn-success'
          "
          @click="confirmToggle"
        >
          Подтвердить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>
<!-- ./frontend/app/components/programs/VisibilityDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  program: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits([
  'hidden',
])

const store = useProgramsStore()

const hiding = ref(false)
const errorMessage = ref('')

async function hideProgram() {
  if (!props.program) return

  hiding.value = true
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      props.program.id,
      true,
    )

    emit('hidden', response)
    model.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось скрыть программу'
  } finally {
    hiding.value = false
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Скрыть программу"
    max-width-class="max-w-md"
  >
    <div class="space-y-4">
      <div
        class="bg-warning/10 border-warning/30 rounded-2xl border p-4"
      >
        <div class="flex gap-3">
          <Icon
            name="lucide:eye-off"
            class="text-warning mt-0.5 size-5 shrink-0"
          />

          <div>
            <p class="font-semibold">
              Программа исчезнет из каталога пациентов
            </p>

            <p class="text-base-content/70 mt-1 text-sm">
              Существующие данные прохождения сохранятся.
              Программу можно будет снова показать.
            </p>
          </div>
        </div>
      </div>

      <p>
        Вы действительно хотите скрыть программу:
      </p>

      <p class="font-semibold">
        {{ program?.title }}
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          :disabled="hiding"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-warning"
          :disabled="hiding"
          @click="hideProgram"
        >
          <span
            v-if="hiding"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:eye-off"
            class="size-4"
          />

          Скрыть
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>
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
  purchaseRequested: {
    type: Boolean,
    default: false,
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
        source: 'program',
        program_id: props.programId,
        program_stage_id: props.stage.id,

        // Пока сохраняем прежние параметры для
        // совместимости с существующим возвратом.
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
      v-if="!isPatient && stage.doctor_description"
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

                  <template v-else-if="item.pro_content">
                    <p class="text-base-content/60 mb-2 text-xs">
                      Этот материал доступен в программе сопровождения.
                    </p>

                    <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      :disabled="purchaseRequested"
                      @click="emit('purchase')"
                    >
                      <Icon
                        :name="
                          purchaseRequested
                            ? 'lucide:check'
                            : 'lucide:shopping-cart'
                        "
                        class="size-4"
                      />

                      {{
                        purchaseRequested
                          ? 'Запрос отправлен'
                          : purchaseLabel
                      }}
                    </button>
                  </template>

                  <p v-else class="text-base-content/60 text-sm">
                    Материал пока недоступен.
                  </p>
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

            Консультация входит в план программы. Дату и время согласует ассистент клиники.
          </div>
        </div>
      </article>
    </div>
  </section>
</template>
// ./frontend/app/stores/programs.js
export const useProgramsStore = defineStore(
  'programs',
  () => {
    const programs = ref([])
    const currentProgram = ref(null)

    const patientAccessPrograms = ref([])

    const loading = ref(false)
    const saving = ref(false)

    const patientProgressPrograms = ref([])

    async function fetchProgramsForStaff() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/manage',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramsForPatient() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/patient',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForStaff(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/manage/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForPatient(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/patient/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function createProgram(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          '/api/v1/programs/manage',
          {
            method: 'POST',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function updateProgram(
      programId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          `/api/v1/programs/manage/${programId}`,
          {
            method: 'PUT',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function setVisibility(
      programId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/manage/${programId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function startProgram(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/start`,
        {
          method: 'POST',
        },
      )
    }

    async function requestPurchase(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/request-purchase`,
        {
          method: 'POST',
        },
      )
    }

    async function fetchPatientProgramAccess(
      patientId,
    ) {
      const { $api } = useNuxtApp()

      patientAccessPrograms.value = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access`,
      )

      return patientAccessPrograms.value
    }

    async function setPatientProgramAccess(
      patientId,
      programId,
      isActive,
    ) {
      const { $api } = useNuxtApp()

      const response = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access/${programId}`,
        {
          method: 'PATCH',
          body: {
            is_active: isActive,
          },
        },
      )

      const item = patientAccessPrograms.value.find(
        (program) =>
          program.program_id === programId,
      )

      if (item) {
        Object.assign(item, response)
      }

      return response
    }

    async function fetchPatientProgramProgress(
        patientId,
        ) {
        const { $api } = useNuxtApp()

        patientProgressPrograms.value = await $api(
            `/api/v1/programs/manage/patient/${patientId}/progress`,
        )

        return patientProgressPrograms.value
        }

    return {
      programs,
      currentProgram,
      patientAccessPrograms,

      loading,
      saving,

      fetchProgramsForStaff,
      fetchProgramsForPatient,
      fetchProgramForStaff,
      fetchProgramForPatient,

      createProgram,
      updateProgram,
      setVisibility,

      startProgram,
      requestPurchase,

      fetchPatientProgramAccess,
      setPatientProgramAccess,

      patientProgressPrograms,
      fetchPatientProgramProgress,
    }
  },
)
<!-- ./frontend/app/layouts/default.vue -->
<script setup>
</script>

<template>
  <LayoutSidebar>
    <div
      class="bg-base-200 flex min-h-dvh min-w-0 flex-col"
    >
      <LayoutEmailVerificationBanner />
      <LayoutNavbar />

      <main
        class="mx-auto w-full max-w-7xl flex-1 px-4 py-6 sm:py-8"
      >
        <slot />
      </main>

      <LayoutFooter />
    </div>
  </LayoutSidebar>
</template>
<!-- ./frontend/app/pages/programs/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useProgramsStore()

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const errorMessage = ref('')

const visibilityDialogOpen = ref(false)
const selectedProgram = ref(null)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

function openHideDialog(program) {
  selectedProgram.value = program
  visibilityDialogOpen.value = true
}

async function showProgram(program) {
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      program.id,
      false,
    )

    Object.assign(program, response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось показать программу'
  }
}

function handleHidden(response) {
  const item = store.programs.find(
    (program) => program.id === response.id,
  )

  if (item) {
    Object.assign(item, response)
  }
}

onMounted(async () => {
  try {
    if (auth.activeRole === 'patient') {
      await store.fetchProgramsForPatient()
    } else {
      await store.fetchProgramsForStaff()
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Программы
        </h1>

        <p class="text-base-content/60 mt-1">
          Пошаговые программы работы с материалами.
        </p>
      </div>

      <NuxtLink
        v-if="canManage"
        to="/programs/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая программа
      </NuxtLink>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="store.programs.length"
      class="grid gap-5 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="program in store.programs"
        :key="program.id"
        :class="[
          program.is_popular
            ? 'aura aura-rainbow'
            : '',
          'h-full',
        ]"
      >
        <article
          class="card bg-base-100 border-base-300 relative h-full overflow-hidden border"
          :class="{
            'opacity-60': program.is_hidden,
          }"
        >
          <div
            v-if="program.is_popular"
            class="bg-warning text-warning-content absolute right-0 top-0 rounded-bl-2xl px-4 py-2 text-xs font-bold shadow"
          >
            <Icon
              name="lucide:flame"
              class="mr-1 inline size-4"
            />
            Популярное
          </div>

          <div class="card-body">
            <div class="flex flex-wrap gap-2 pr-24">
              <span
                v-if="hasDiscount(program)"
                class="badge badge-error gap-1 font-bold"
              >
                <Icon
                  name="lucide:badge-percent"
                  class="size-3"
                />
                −{{ program.service?.discount_percent }}%
              </span>

              <span
                v-if="program.has_program_access"
                class="badge badge-success"
              >
                Полный доступ
              </span>

              <span
                v-if="program.purchase_requested"
                class="badge badge-warning"
              >
                Запрос отправлен
              </span>

              <span
                v-if="program.is_hidden"
                class="badge badge-ghost"
              >
                Скрыта
              </span>
            </div>

            <h2 class="card-title mt-2">
              {{ program.title }}
            </h2>

            <p
              class="text-base-content/60 line-clamp-3 text-sm"
            >
              {{ program.description }}
            </p>

            <div class="mt-2 flex items-end gap-2">
              <span class="text-primary text-xl font-bold">
                {{ formatFinalPrice(program) }}
              </span>

              <span
                v-if="hasDiscount(program)"
                class="text-base-content/40 text-sm line-through"
              >
                {{ formatOriginalPrice(program) }}
              </span>
            </div>

            <div class="mt-2 flex flex-wrap gap-1">
              <span
                v-for="tag in program.tags"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <div class="card-actions mt-auto pt-5">
              <NuxtLink
                :to="`/programs/${program.id}`"
                class="btn btn-primary btn-sm"
              >
                Открыть
              </NuxtLink>

              <NuxtLink
                v-if="canManage"
                :to="`/programs/${program.id}/edit`"
                class="btn btn-outline btn-sm"
              >
                <Icon
                  name="lucide:pencil"
                  class="size-4"
                />
                Изменить
              </NuxtLink>

              <button
                v-if="canManage && !program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="openHideDialog(program)"
              >
                <Icon
                  name="lucide:eye-off"
                  class="size-4"
                />
                Скрыть
              </button>

              <button
                v-if="canManage && program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="showProgram(program)"
              >
                <Icon
                  name="lucide:eye"
                  class="size-4"
                />
                Показать
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:route"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Программ пока нет
      </p>
    </div>
  </div>

  <ProgramsVisibilityDialog
    v-model="visibilityDialogOpen"
    :program="selectedProgram"
    @hidden="handleHidden"
  />
</template>
<!-- ./frontend/app/pages/programs/[id]/index.vue -->
<script setup>
const route = useRoute()
const auth = useAuthStore()
const store = useProgramsStore()

const selectedStageIndex = ref(0)

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
  getPurchaseActionLabel,
} = useProgramPrice()

const purchaseActionLabel = computed(() =>
  getPurchaseActionLabel(program.value),
)

const loading = ref(true)
const starting = ref(false)
const purchaseDialogOpen = ref(false)

const message = ref('')
const errorMessage = ref('')

const program = computed(
  () => store.currentProgram,
)

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

const selectedStage = computed(
  () => program.value?.stages[
    selectedStageIndex.value
  ],
)

async function loadProgram() {
  loading.value = true
  errorMessage.value = ''

  try {
    if (isPatient.value) {
      await store.fetchProgramForPatient(
        route.params.id,
      )

      // Если вернулись из опросника программы,
      // открываем тот же этап.
      const requestedStageId =
        typeof route.query.stage === 'string'
          ? route.query.stage
          : null

      if (requestedStageId) {
        const requestedIndex =
          program.value.stages.findIndex(
            (stage) =>
              stage.id === requestedStageId,
          )

        if (requestedIndex >= 0) {
          selectedStageIndex.value =
            requestedIndex

          return
        }
      }

      // Если конкретный этап не был передан,
      // выбираем текущий активный этап.
      const preferredIndex =
        program.value.stages.findIndex(
          (stage) =>
            [
              'available',
              'in_progress',
              'overdue',
            ].includes(stage.status),
        )

      selectedStageIndex.value =
        preferredIndex >= 0
          ? preferredIndex
          : 0
    } else {
      await store.fetchProgramForStaff(
        route.params.id,
      )
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программу'
  } finally {
    loading.value = false
  }
}

async function startProgram() {
  starting.value = true
  errorMessage.value = ''
  if (starting.value || !program.value) return

  try {
    await store.startProgram(program.value.id)
    message.value = 'Программа начата'

    await loadProgram()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось начать программу'
  } finally {
    starting.value = false
  }
}

async function requestPurchase() {
  if (!program.value) return

  errorMessage.value = ''

  if (program.value.purchase_requested) {
    message.value =
      'Запрос уже отправлен медицинскому ассистенту.'
    return
  }

  purchaseDialogOpen.value = true
}

function handlePurchaseRequested({ programId, response }) {
  if (program.value?.id !== programId) return

  program.value.purchase_requested = true
  message.value = response.message
}

onMounted(loadProgram)
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="3"
  />

  <div
    v-else-if="errorMessage && !program"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="program"
    class="space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <div
        class="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between"
      >
        <div class="min-w-0 flex-1">
          <div
                class="flex flex-wrap items-center gap-2"
                >
                <span class="text-primary text-2xl font-bold">
                    {{ formatFinalPrice(program) }}
                </span>

                <span
                    v-if="hasDiscount(program)"
                    class="text-base-content/40 line-through"
                >
                    {{ formatOriginalPrice(program) }}
                </span>

                <span
                    v-if="hasDiscount(program)"
                    class="badge badge-error font-bold"
                >
                    −{{ program.service?.discount_percent }}%
                </span>

                <span
                    v-if="program.is_popular"
                    class="badge badge-warning gap-1"
                >
                    <Icon
                    name="lucide:flame"
                    class="size-3"
                    />

                    Популярное
                </span>

                <span
                    v-if="program.has_program_access"
                    class="badge badge-success"
                >
                    Полный доступ
                </span>
                </div>

          <h1
            class="mt-3 text-3xl font-bold sm:text-4xl"
          >
            {{ program.title }}
          </h1>

          <p
            v-if="program.description"
            class="text-base-content/70 mt-3 max-w-3xl"
          >
            {{ program.description }}
          </p>

          <p
            v-if="isPatient && program.service"
            class="border-primary/20 bg-primary/5 mt-4 rounded-2xl border p-4 text-sm"
          >
            Начать можно бесплатно. Материалы без отметки Pro доступны
            без покупки. Консультации и Pro-материалы относятся
            к программе сопровождения со специалистами.
          </p>

          <div
            v-if="program.service"
            class="border-base-300 mt-5 rounded-2xl border p-4"
          >
            <div class="flex flex-wrap items-center gap-2">
              <span
                v-if="program.service.code"
                class="badge badge-neutral font-mono"
              >
                {{ program.service.code }}
              </span>

              <span class="font-medium">
                {{ program.service.title }}
              </span>
            </div>

            <p
              v-if="program.service.description"
              class="text-base-content/60 mt-2 text-sm"
            >
              {{ program.service.description }}
            </p>
          </div>

          <div class="mt-4 flex flex-wrap gap-1">
            <span
              v-for="tag in program.tags"
              :key="tag.id"
              class="badge badge-outline"
            >
              {{ tag.name }}
            </span>
          </div>
        </div>

        <div class="flex flex-col gap-2 sm:flex-row">
          <NuxtLink
            v-if="canManage"
            :to="`/programs/${program.id}/edit`"
            class="btn btn-outline"
          >
            <Icon
              name="lucide:pencil"
              class="size-4"
            />
            Редактировать
          </NuxtLink>

          <button
            v-if="
              isPatient
              && !program.enrollment
            "
            type="button"
            class="btn btn-primary"
            :disabled="starting"
            @click="startProgram"
          >
            <span
              v-if="starting"
              class="loading loading-spinner loading-sm"
            />

            Начать программу
          </button>
        </div>
      </div>

      <div
        v-if="isPatient && program.enrollment"
        class="mt-6"
      >
        <div class="mb-2 flex justify-between text-sm">
          <span>
            Общий прогресс
          </span>

          <strong>
            {{ program.progress_percent }}%
          </strong>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="program.progress_percent"
          max="100"
        />

        <p class="text-base-content/50 mt-2 text-xs">
          День программы:
          {{ program.enrollment.elapsed_days }}
        </p>
      </div>
    </header>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div class="overflow-x-auto pb-2">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(stage, index) in program.stages"
          :key="stage.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedStageIndex === index,
          }"
          @click="selectedStageIndex = index"
        >
          <Icon
            :name="
              stage.status === 'completed'
                ? 'lucide:circle-check'
                : stage.status === 'overdue'
                  ? 'lucide:triangle-alert'
                  : 'lucide:circle'
            "
            class="size-4"
          />

          Этап {{ index + 1 }}
        </button>
      </div>
    </div>

    <ProgramsViewerStage
        v-if="selectedStage"
        :stage="selectedStage"
        :program-id="program.id"
        :is-patient="isPatient"
        :purchase-label="purchaseActionLabel"
        :purchase-requested="Boolean(program.purchase_requested)"
        @purchase="requestPurchase"
      />
      <PatientPurchaseDialog
        v-if="isPatient"
        v-model="purchaseDialogOpen"
        :program="program"
        @requested="handlePurchaseRequested"
      />
  </div>
</template>
<!-- ./frontend/app/components/layout/Navbar.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()
const ui = useUiStore()
const notifications = useNotificationsStore()

const {
  isStaff,
  activeRoleName,
  navigationGroups,
} = useAppNavigation()

const mobileMenuOpen = ref(false)

function closeMobileMenu() {
  mobileMenuOpen.value = false
}

const invitationsStore = useInvitationsStore()

const patientInviteOpen = ref(false)
const invitationLinkOpen = ref(false)

const createdPatientInvitation = ref(null)
const invitationEmailSent = ref(false)
const invitationEmailError = ref('')

const { isClientReady } = useClientReady()

const isDoctor = computed(() =>
  isClientReady.value
  && auth.activeRole === 'doctor',
)

function handlePatientInvitationCreated(
  invitation,
) {
  createdPatientInvitation.value = invitation
  invitationEmailSent.value = false
  invitationEmailError.value = ''
  invitationLinkOpen.value = true
}

async function sendPatientInvitationEmail() {
  if (!createdPatientInvitation.value) return

  invitationEmailError.value = ''

  try {
    const response =
      await invitationsStore
        .sendPatientInvitation(
          createdPatientInvitation.value
            .invitation_id,
        )

    // При отправке создаётся новая ссылка,
    // поэтому обновляем и QR-код, и ID.
    createdPatientInvitation.value = response

    invitationEmailSent.value = Boolean(
      response.email_sent_at
      && !response.email_send_error,
    )

    invitationEmailError.value =
      response.email_send_error || ''
  } catch (error) {
    invitationEmailSent.value = false
    invitationEmailError.value =
      error?.data?.detail
      || 'Не удалось отправить приглашение'
  }
}

async function handlePatientAttached(response) {
  await navigateTo(
    `/patients/${response.patient_id}`,
  )
}

const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient',
)

onMounted(() => {
  notifications.connect()

  void notifications.fetchUnreadCount().catch(() => {
    // Ошибка фоновой загрузки не блокирует навигацию.
  })
})

onBeforeUnmount(() => {
  notifications.disconnect()
})
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
      class="mx-auto grid min-h-16 w-full max-w-7xl items-center gap-2 px-3 py-1 sm:min-h-20 sm:px-4"
      :class="
        isPatient
          ? 'grid-cols-[minmax(0,1fr)_auto]'
          : 'grid-cols-[auto_minmax(0,1fr)_auto]'
      "
    >
      <div class="flex min-w-0 items-center gap-1">
        <template v-if="isPatient">
          <div class="patient-navbar-brand">
            <LayoutLogo
              to="/dashboard"
              variant="navbar"
            />
          </div>

          <LayoutPatientActions
            @menu="mobileMenuOpen = true"
          />
        </template>

        <template v-else>
          <button
            v-if="isStaff"
            type="button"
            class="btn btn-circle btn-ghost"
            :aria-label="
              ui.sidebarOpen
                ? 'Свернуть боковое меню'
                : 'Открыть боковое меню'
            "
            @click="ui.toggleSidebar"
          >
            <Icon
              :name="
                ui.sidebarOpen
                  ? 'lucide:panel-left-close'
                  : 'lucide:menu'
              "
              class="size-5"
            />
          </button>

          <button
            v-else
            type="button"
            class="btn btn-circle btn-ghost lg:hidden"
            aria-label="Открыть меню"
            @click="mobileMenuOpen = true"
          >
            <Icon
              name="lucide:menu"
              class="size-5"
            />
          </button>

          <LayoutLogo
            v-if="!isStaff"
            to="/dashboard"
            variant="navbar"
          />
        </template>
      </div>

      <div
        v-if="!isStaff && !isPatient"
        class="hidden min-w-0 items-center justify-center px-2 lg:flex"
      >
        <UiMegaMenu
          :groups="navigationGroups"
          size-class="megamenu-sm"
        />
      </div>

      <div
        v-else-if="isStaff"
        class="flex min-w-0 items-center px-2"
      >
        <button
          v-if="isDoctor"
          type="button"
          class="btn btn-primary btn-sm"
          @click="patientInviteOpen = true"
        >
          <Icon
            name="lucide:user-plus"
            class="size-4"
          />

          <span class="hidden sm:inline">
            Пригласить пациента
          </span>
        </button>

        <span
          v-else
          class="text-base-content/60 truncate text-sm"
        >
          ...
        </span>
      </div>

      <div
        class="flex shrink-0 items-center justify-end gap-1"
      >
        <NotificationsCenter />

        <LayoutThemeToggle />

        <div class="dropdown dropdown-end">
          <button
            type="button"
            tabindex="0"
            class="btn btn-ghost gap-2 px-2"
          >
            <div class="avatar avatar-placeholder">
              <div
                class="bg-primary text-primary-content w-9 rounded-full"
              >
                <span class="text-sm">
                  {{ userStore.initials }}
                </span>
              </div>
            </div>

            <div
              class="hidden max-w-44 text-left sm:block"
            >
              <p class="truncate text-sm font-medium">
                {{ userStore.fullName }}
              </p>

              <p
                class="text-base-content/60 min-h-4 truncate text-xs"
              >
                {{ activeRoleName }}
              </p>
            </div>

            <Icon
              name="lucide:chevron-down"
              class="hidden size-4 sm:block"
            />
          </button>

          <ul
            tabindex="0"
            class="menu dropdown-content bg-base-100 border-base-300 z-50 mt-2 w-64 rounded-box border p-2 shadow-xl"
          >
            <li class="menu-title">
              <span class="truncate">
                {{ userStore.user?.email }}
              </span>
            </li>

            <li>
              <NuxtLink to="/settings/profile">
                <Icon
                  name="lucide:user-round"
                  class="size-4"
                />
                Личные данные
              </NuxtLink>
            </li>

            <li>
              <NuxtLink to="/settings/security">
                <Icon
                  name="lucide:key-round"
                  class="size-4"
                />
                Passkey и пароль
              </NuxtLink>
            </li>

            <li v-if="isStaff">
              <NotificationsBrowserPermission />
            </li>

            <li>
              <button
                type="button"
                class="text-error"
                @click="auth.logout"
              >
                <Icon
                  name="lucide:log-out"
                  class="size-4"
                />
                Выйти
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>

  <UiBottomSheet
    v-if="!isStaff"
    v-model="mobileMenuOpen"
    title="Меню"
  >
    <nav>
      <ul class="menu w-full gap-1 p-0 text-base">
        <template
          v-for="group in navigationGroups"
          :key="group.key"
        >
          <li class="menu-title mt-2 first:mt-0">
            <span>{{ group.label }}</span>
          </li>

          <li
            v-for="link in group.links"
            :key="link.to"
          >
            <NuxtLink
              :to="link.to"
              @click="closeMobileMenu"
            >
              <Icon
                :name="link.icon"
                class="size-5"
              />
              {{ link.label }}
            </NuxtLink>
          </li>
        </template>
      </ul>
    </nav>

    <template #footer>
      <button
        type="button"
        class="btn btn-error btn-outline w-full"
        @click="auth.logout"
      >
        <Icon
          name="lucide:log-out"
          class="size-4"
        />
        Выйти
      </button>
    </template>
  </UiBottomSheet>

  <InvitationsPatientDialog
    v-if="isDoctor"
    v-model="patientInviteOpen"
    @created="handlePatientInvitationCreated"
    @attached="handlePatientAttached"
  />

  <InvitationsLinkDialog
    v-if="isDoctor"
    v-model="invitationLinkOpen"
    :url="
      createdPatientInvitation
        ?.registration_url || ''
    "
    :email="
      createdPatientInvitation?.email || ''
    "
    title="Приглашение пациента"
    description="Покажите пациенту QR-код, скопируйте ссылку или отправьте её на email."
    can-send-email
    :sending-email="
      invitationsStore.sendingEmail
    "
    :email-sent="invitationEmailSent"
    :email-error="invitationEmailError"
    @send-email="sendPatientInvitationEmail"
  />
</template>
<style scoped>
.patient-navbar-brand {
  width: clamp(3rem, 16vw, 5rem);
  min-width: 0;
  flex-shrink: 1;
}

.patient-navbar-brand :deep(a) {
  max-width: 100%;
  min-width: 0;
}

.patient-navbar-brand :deep(svg),
.patient-navbar-brand :deep(img) {
  max-width: 100%;
  height: auto;
}

@media (min-width: 640px) {
  .patient-navbar-brand {
    width: auto;
    max-width: 10rem;
  }
}
</style>
<!-- ./frontend/app/components/articles/ReaderAction.vue -->
<script setup>
const props = defineProps({
  target: {
    type: Object,
    default: null,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['close'])

const atBoundary = ref(true)
const scrolling = ref(false)

const showClose = computed(() =>
  atBoundary.value && !scrolling.value,
)

let frame = null
let scrollTimer = null
let resizeObserver = null
let mounted = false

const EDGE_DISTANCE = 48

function getBounds() {
  const element = props.target

  if (!element) return null

  const rect = element.getBoundingClientRect()
  const scrollY = window.scrollY
  const viewportHeight = window.innerHeight

  const maxScroll = Math.max(
    document.documentElement.scrollHeight - viewportHeight,
    0,
  )

  const articleTop = rect.top + scrollY
  const articleBottom = rect.bottom + scrollY

  const start = Math.min(
    maxScroll,
    Math.max(0, articleTop - 16),
  )

  const end = Math.min(
    maxScroll,
    Math.max(start, articleBottom - viewportHeight),
  )

  return {
    start,
    end,
    shortArticle: rect.height <= viewportHeight,
  }
}

function updateBoundary() {
  const bounds = getBounds()

  if (!bounds) {
    atBoundary.value = true
    return
  }

  atBoundary.value =
    bounds.shortArticle
    || window.scrollY <= bounds.start + EDGE_DISTANCE
    || window.scrollY >= bounds.end - EDGE_DISTANCE
}

function scheduleUpdate() {
  if (frame !== null) return

  frame = window.requestAnimationFrame(() => {
    frame = null
    updateBoundary()
  })
}

function handleScroll() {
  scrolling.value = true

  window.clearTimeout(scrollTimer)
  scheduleUpdate()

  scrollTimer = window.setTimeout(() => {
    scrolling.value = false
    updateBoundary()
  }, 180)
}

function scrollToStart() {
  const bounds = getBounds()

  if (!bounds) return

  const reduceMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)',
  ).matches

  window.scrollTo({
    top: bounds.start,
    behavior: reduceMotion ? 'instant' : 'smooth',
  })
}

function handleClick() {
  if (props.disabled) return

  if (showClose.value) {
    emit('close')
  } else {
    scrollToStart()
  }
}

function observeTarget() {
  resizeObserver?.disconnect()

  if (!mounted || !props.target) return

  resizeObserver = new ResizeObserver(scheduleUpdate)
  resizeObserver.observe(props.target)
  resizeObserver.observe(document.documentElement)

  scheduleUpdate()
}

watch(
  () => props.target,
  observeTarget,
  { flush: 'post' },
)

onMounted(() => {
  mounted = true
  observeTarget()
  updateBoundary()

  window.addEventListener('scroll', handleScroll, {
    passive: true,
  })
  window.addEventListener('resize', scheduleUpdate)
})

onBeforeUnmount(() => {
  mounted = false

  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', scheduleUpdate)

  window.clearTimeout(scrollTimer)
  resizeObserver?.disconnect()

  if (frame !== null) {
    window.cancelAnimationFrame(frame)
  }
})
</script>

<template>
  <div
    class="fixed z-[60]"
    style="
      right: calc(1rem + env(safe-area-inset-right, 0px));
      bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
    "
  >
    <button
      type="button"
      class="btn btn-circle btn-lg border-base-300 bg-base-200 text-base-content hover:bg-base-300 shadow-lg"
      :disabled="disabled"
      :aria-label="showClose ? 'Закрыть статью' : 'В начало статьи'"
      :title="showClose ? 'Закрыть статью' : 'В начало статьи'"
      @click="handleClick"
    >
      <span
        v-if="disabled"
        class="loading loading-spinner loading-sm"
      />

      <Icon
        v-else
        :name="showClose ? 'lucide:x' : 'lucide:arrow-up'"
        class="size-6"
      />
    </button>
  </div>
</template>
----

Сейчас не очень мне нравится интерфейс программы:
В карточке программы, которую выполняет пациент, при открытии программы в телефоне бОльшую чать занимает описание рпограммы, например:
Цена по запросу
Полный доступ
SMART Recovery
SMART Recovery — это программа, в которой мы будем шаг за шагом разбираться, какие изменения важны именно для вас и что может помочь сделать их устойчивыми. Начнём с ваших целей и мотивации, затем научимся лучше понимать тягу и её триггеры, замечать связь между мыслями, эмоциями и поведением, справляться со сложными моментами и постепенно возвращать в жизнь сон, отдых, отношения, интересы и другие важные опоры. На каждом этапе вы будете знакомиться с небольшими материалами и пробовать новые инструменты, а на консультациях с психиатром сможете обсуждать, что изменилось, что получилось и какие сложности возникли. Здесь не нужно стремиться пройти всё идеально: если что-то не сработало, появилась сильная тяга, случился срыв или изменились ваши цели, это можно вместе разобрать и скорректировать дальнейший план.

Начать можно бесплатно. Материалы без отметки Pro доступны без покупки. Консультации и Pro-материалы относятся к программе сопровождения со специалистами.

Комплекс Comfort+
аддикции
Общий прогресс

Давай сделаем отдельный layout для работы с программой, чтобы там в NavBar 
