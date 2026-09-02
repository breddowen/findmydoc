<!-- ./frontend/app/components/programs/configurator/Editor.vue -->
<script setup>
import { VueDraggable } from 'vue-draggable-plus'

const props = defineProps({
  programId: {
    type: String,
    default: null,
  },
})

const { $api } = useNuxtApp()
const store = useProgramsStore()
const servicesStore = useServicesStore()

const articles = ref([])
const questionnaires = ref([])
const specialities = ref([])
const tags = ref([])

const loadingSources = ref(true)
const loadingProgram = ref(Boolean(props.programId))

const activeStageIndex = ref(0)
const mobileLibraryOpen = ref(false)

const errorMessage = ref('')

const form = reactive({
  title: '',
  description: '',

  service_id: null,
  is_popular: false,

  tag_ids: [],
  stages: [],
})

function createStage() {
  const previous =
    form.stages[form.stages.length - 1]

  const dayFrom = previous
    ? Number(previous.day_to) + 1
    : 0

  return {
    client_id: crypto.randomUUID(),
    title: `Этап ${form.stages.length + 1}`,
    description: '',
    doctor_description: '',

    day_from: dayFrom,
    day_to: dayFrom + 7,
    order_index: form.stages.length,

    items: [],
  }
}

function addStage() {
  form.stages.push(createStage())
  activeStageIndex.value = form.stages.length - 1
}

function removeStage(index) {
  if (!window.confirm('Удалить этот этап?')) {
    return
  }

  form.stages.splice(index, 1)
  normalizeStages()

  activeStageIndex.value = Math.max(
    0,
    Math.min(
      activeStageIndex.value,
      form.stages.length - 1,
    ),
  )
}

function normalizeStages() {
  form.stages.forEach((stage, stageIndex) => {
    stage.order_index = stageIndex

    stage.items.forEach((item, itemIndex) => {
      item.order_index = itemIndex
    })
  })
}

function addItemToActiveStage(item) {
  const stage = form.stages[activeStageIndex.value]

  if (!stage) {
    errorMessage.value =
      'Сначала добавьте этап'
    return
  }

  item.order_index = stage.items.length
  stage.items.push(item)

  mobileLibraryOpen.value = false
}

function openLibrary(stageIndex) {
  activeStageIndex.value = stageIndex
  mobileLibraryOpen.value = true
}

function mapProgramToForm(program) {
  form.title = program.title || ''
  form.description = program.description || ''

  form.service_id = program.service?.id || null

  form.tag_ids = (program.tags || []).map(
    (tag) => tag.id,
  )


  form.is_popular = Boolean(
    program.is_popular,
    )

  form.stages = (program.stages || []).map(
    (stage, stageIndex) => ({
      client_id: crypto.randomUUID(),

      title: stage.title,
      description: stage.description || '',
      doctor_description:
        stage.doctor_description || '',

      day_from: stage.day_from,
      day_to: stage.day_to,
      order_index: stageIndex,

      items: (stage.items || []).map(
        (item, itemIndex) => ({
          client_id: crypto.randomUUID(),

          item_type: item.item_type,
          order_index: itemIndex,

          title: item.title,
          description: item.description,
          pro_content: item.pro_content,

          article_id:
            item.item_type === 'article'
              ? item.content_id
              : null,

          questionnaire_id:
            item.item_type === 'questionnaire'
              ? item.content_id
              : null,

          speciality_id:
            item.item_type === 'consultation'
              ? item.speciality_id
              : null,

          speciality_name: item.speciality_name,

          consultation_title:
            item.item_type === 'consultation'
              ? item.title
              : null,

          consultation_description:
            item.item_type === 'consultation'
              ? item.description || ''
              : null,
        }),
      ),
    }),
  )

  if (!form.stages.length) {
    addStage()
  }
}

async function loadSources() {
  loadingSources.value = true

  try {
    const [
      articleItems,
      questionnaireItems,
      specialityItems,
      tagItems,
    ] = await Promise.all([
      $api('/api/v1/articles'),
      $api('/api/v1/questionnaires'),
      $api('/api/v1/specialities'),
      $api('/api/v1/tags'),

      // Скрытые услуги нужны, чтобы корректно
      // отобразить старую связь при редактировании.
      servicesStore.fetchServices(true),
    ])

    articles.value = articleItems
    questionnaires.value = questionnaireItems
    specialities.value = specialityItems
    tags.value = tagItems
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить библиотеку'
  } finally {
    loadingSources.value = false
  }
}

async function loadProgram() {
  if (!props.programId) {
    addStage()
    return
  }

  loadingProgram.value = true

  try {
    const program =
      await store.fetchProgramForStaff(
        props.programId,
      )

    mapProgramToForm(program)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программу'
  } finally {
    loadingProgram.value = false
  }
}

function validateForm() {
  if (!form.title.trim()) {
    return 'Введите название программы'
  }

  if (!form.stages.length) {
    return 'Добавьте хотя бы один этап'
  }

  const sortedPeriods = [...form.stages].sort(
    (first, second) =>
      first.day_from - second.day_from,
  )

  for (
    let index = 0;
    index < sortedPeriods.length;
    index += 1
  ) {
    const stage = sortedPeriods[index]

    if (!stage.title.trim()) {
      return `Введите название этапа №${index + 1}`
    }

    if (stage.day_to < stage.day_from) {
      return (
        `В этапе «${stage.title}» последний день `
        + 'меньше первого'
      )
    }

    const previous = sortedPeriods[index - 1]

    if (
      previous
      && stage.day_from <= previous.day_to
    ) {
      return 'Периоды этапов не должны пересекаться'
    }
  }

  return null
}

function buildPayload() {
  normalizeStages()

  return {
    title: form.title.trim(),
    description: form.description.trim() || null,

    service_id: form.service_id || null,

    price_amount:
      form.price_amount === ''
      || form.price_amount === null
        ? null
        : Number(form.price_amount),

    currency:
      form.price_amount === ''
      || form.price_amount === null
        ? null
        : form.currency,

    tag_ids: form.tag_ids,

    discount_percent:
        form.price_amount === ''
        || form.price_amount === null
            ? 0
            : Number(form.discount_percent || 0),

    is_popular: form.is_popular,

    stages: form.stages.map(
      (stage, stageIndex) => ({
        title: stage.title.trim(),
        description:
          stage.description.trim() || null,
        doctor_description:
          stage.doctor_description.trim() || null,

        day_from: Number(stage.day_from),
        day_to: Number(stage.day_to),
        order_index: stageIndex,

        items: stage.items.map(
          (item, itemIndex) => ({
            item_type: item.item_type,
            order_index: itemIndex,

            article_id:
              item.item_type === 'article'
                ? item.article_id
                : null,

            questionnaire_id:
              item.item_type === 'questionnaire'
                ? item.questionnaire_id
                : null,

            speciality_id:
              item.item_type === 'consultation'
                ? item.speciality_id
                : null,

            consultation_title:
              item.item_type === 'consultation'
                ? item.consultation_title?.trim()
                  || null
                : null,

            consultation_description:
              item.item_type === 'consultation'
                ? item.consultation_description
                    ?.trim()
                  || null
                : null,
          }),
        ),
      }),
    ),
  }
}

async function save() {
  errorMessage.value = validateForm() || ''

  if (errorMessage.value) {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    })
    return
  }

  try {
    const payload = buildPayload()

    const program = props.programId
      ? await store.updateProgram(
          props.programId,
          payload,
        )
      : await store.createProgram(payload)

    await navigateTo(`/programs/${program.id}`)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить программу'
  }
}

onMounted(async () => {
  await Promise.all([
    loadSources(),
    loadProgram(),
  ])
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 xl:flex-row xl:items-center xl:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          {{
            programId
              ? 'Редактирование программы'
              : 'Новая программа'
          }}
        </h1>

        <p class="text-base-content/60 mt-1">
          Сформируйте этапы и расположите задания
          в нужном порядке.
        </p>
      </div>

      <div class="flex gap-2">
        <NuxtLink
          to="/programs"
          class="btn"
        >
          Отмена
        </NuxtLink>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="store.saving"
          @click="save"
        >
          <span
            v-if="store.saving"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:save"
            class="size-4"
          />

          Сохранить
        </button>
      </div>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <UiContentSkeleton
      v-if="loadingProgram"
      variant="card"
      :count="3"
    />

    <template v-else>
      <section
            class="bg-base-100 border-base-300 grid gap-5 rounded-3xl border p-5 sm:grid-cols-2 sm:p-6"
            >
            <label class="form-control block sm:col-span-2">
                <span class="label-text mb-2 font-medium">
                Название
                </span>

                <input
                v-model="form.title"
                type="text"
                class="input input-bordered w-full"
                >
            </label>

            <label class="form-control block sm:col-span-2">
                <span class="label-text mb-2">
                Описание
                </span>

                <textarea
                v-model="form.description"
                class="textarea textarea-bordered min-h-28 w-full"
                />
            </label>

            <ProgramsConfiguratorServiceSelect
              v-model="form.service_id"
              :services="servicesStore.services"
              :loading="loadingSources"
            />

            <label
                class="border-base-300 flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4"
            >
                <span>
                <span class="block font-medium">
                    Популярная программа
                </span>

                <span class="text-base-content/50 text-xs">
                    Карточка будет выделена в каталоге.
                </span>
                </span>

                <input
                v-model="form.is_popular"
                type="checkbox"
                class="toggle toggle-warning"
                >
            </label>

            <div class="sm:col-span-2">
                <p class="mb-3 font-medium">
                Теги программы
                </p>

                <ContentTagSelector
                v-model="form.tag_ids"
                :tags="tags"
                :loading="loadingSources"
                />
            </div>
            </section>

      <div
        class="grid items-start gap-6 lg:grid-cols-[20rem_minmax(0,1fr)]"
      >
        <aside
          class="bg-base-100 border-base-300 sticky top-20 hidden max-h-[calc(100dvh-6rem)] overflow-y-auto rounded-3xl border p-4 lg:block"
        >
          <h2 class="mb-4 font-bold">
            Библиотека
          </h2>

          <ProgramsConfiguratorLibrary
            :articles="articles"
            :questionnaires="questionnaires"
            :specialities="specialities"
            :loading="loadingSources"
            draggable
            @add="addItemToActiveStage"
          />
        </aside>

        <main class="min-w-0 space-y-4">
          <div
            class="flex items-center justify-between gap-4"
          >
            <div>
              <h2 class="text-xl font-bold">
                Этапы
              </h2>

              <p class="text-base-content/50 text-sm">
                Перетаскивайте этапы за handle
              </p>
            </div>

            <button
              type="button"
              class="btn btn-primary btn-sm"
              @click="addStage"
            >
              <Icon
                name="lucide:plus"
                class="size-4"
              />
              Добавить этап
            </button>
          </div>

          <VueDraggable
            v-model="form.stages"
            handle=".stage-drag-handle"
            :animation="180"
            class="space-y-4"
            @update="normalizeStages"
          >
            <ProgramsConfiguratorStage
              v-for="(stage, stageIndex) in form.stages"
              :key="stage.client_id"
              v-model="form.stages[stageIndex]"
              :index="stageIndex"
              :total="form.stages.length"
              :active="
                activeStageIndex === stageIndex
              "
              @activate="
                activeStageIndex = stageIndex
              "
              @remove="removeStage(stageIndex)"
              @open-library="
                openLibrary(stageIndex)
              "
            />
          </VueDraggable>
        </main>
      </div>
    </template>
  </div>

  <UiBottomSheet
    v-model="mobileLibraryOpen"
    title="Добавить в этап"
  >
    <ProgramsConfiguratorLibrary
      :articles="articles"
      :questionnaires="questionnaires"
      :specialities="specialities"
      :loading="loadingSources"
      :draggable="false"
      @add="addItemToActiveStage"
    />
  </UiBottomSheet>
</template>