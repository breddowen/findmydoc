<!-- ./frontend/app/components/programs/consultations/Items.vue -->
<script setup>
const model = defineModel({
  type: Array,
  default: () => [],
})

const props = defineProps({
  specialities: {
    type: Array,
    default: () => [],
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const visibleSpecialities = computed(() =>
  props.specialities.filter(
    speciality => !speciality.is_hidden,
  ),
)

function move(index, direction) {
  if (props.disabled) return

  const item = model.value[index]

  if (item?.item_type !== 'consultation') return

  const target = index + direction

  if (target < 0 || target >= model.value.length) return

  const items = [...model.value]

  ;[items[index], items[target]] = [
    items[target],
    items[index],
  ]

  model.value = items
}

function remove(index) {
  if (props.disabled) return
  if (model.value[index]?.item_type !== 'consultation') return

  model.value = model.value.filter(
    (_, itemIndex) => itemIndex !== index,
  )
}

function addConsultation() {
  if (props.disabled) return

  model.value = [
    ...model.value,
    {
      client_id: crypto.randomUUID(),
      id: null,
      item_type: 'consultation',
      speciality_id: '',
      speciality_name: null,
      consultation_title: '',
      consultation_description: '',
    },
  ]
}

function specialityIsListed(id) {
  return visibleSpecialities.value.some(
    speciality => speciality.id === id,
  )
}
</script>

<template>
  <div class="space-y-3">
    <article
      v-for="(item, index) in model"
      :key="item.client_id || item.id"
      class="border-base-300 rounded-xl border"
      :class="
        item.item_type === 'consultation'
          ? 'bg-base-100 p-4'
          : 'bg-base-200/60 p-3'
      "
    >
      <template v-if="item.item_type !== 'consultation'">
        <div class="flex items-start gap-3">
          <Icon
            :name="
              item.item_type === 'article'
                ? 'lucide:book-open'
                : 'lucide:clipboard-list'
            "
            class="text-base-content/50 mt-0.5 size-5 shrink-0"
          />

          <div class="min-w-0 flex-1">
            <p class="text-sm font-medium wrap-anywhere">
              {{ item.title }}
            </p>

            <p class="text-base-content/50 mt-1 text-xs">
              {{
                item.item_type === 'article'
                  ? 'Статья'
                  : 'Опросник'
              }}
              · Не изменяется

              <span v-if="item.is_hidden">
                · Скрыт
              </span>
            </p>
          </div>

          <Icon
            name="lucide:lock-keyhole"
            class="text-base-content/30 size-4 shrink-0"
          />
        </div>
      </template>

      <template v-else>
        <header class="mb-4 flex flex-wrap items-center justify-between gap-2">
          <p class="flex items-center gap-2 font-medium">
            <Icon name="lucide:stethoscope" class="size-4" />
            Консультация
          </p>

          <div class="flex gap-1">
            <button
              type="button"
              class="btn btn-square btn-ghost btn-sm"
              aria-label="Переместить консультацию выше"
              :disabled="disabled || index === 0"
              @click="move(index, -1)"
            >
              <Icon name="lucide:arrow-up" class="size-4" />
            </button>

            <button
              type="button"
              class="btn btn-square btn-ghost btn-sm"
              aria-label="Переместить консультацию ниже"
              :disabled="disabled || index === model.length - 1"
              @click="move(index, 1)"
            >
              <Icon name="lucide:arrow-down" class="size-4" />
            </button>

            <button
              type="button"
              class="btn btn-square btn-ghost btn-sm text-error"
              aria-label="Удалить консультацию"
              :disabled="disabled"
              @click="remove(index)"
            >
              <Icon name="lucide:trash-2" class="size-4" />
            </button>
          </div>
        </header>

        <div class="space-y-4">
          <label class="block">
            <span class="mb-2 block text-sm font-medium">
              Специальность
            </span>

            <select
              v-model="item.speciality_id"
              class="select w-full"
              :disabled="disabled"
            >
              <option value="" disabled>
                Выберите специальность
              </option>

              <option
                v-if="
                  item.speciality_id
                  && !specialityIsListed(item.speciality_id)
                "
                :value="item.speciality_id"
                disabled
              >
                {{
                  item.speciality_name
                  || 'Текущая специальность'
                }}
                — недоступна для нового выбора
              </option>

              <option
                v-for="speciality in visibleSpecialities"
                :key="speciality.id"
                :value="speciality.id"
              >
                {{ speciality.name }}
              </option>
            </select>
          </label>

          <label class="block">
            <span class="mb-2 block text-sm font-medium">
              Название консультации на этом этапе
            </span>

            <input
              v-model="item.consultation_title"
              type="text"
              maxlength="300"
              class="input w-full"
              placeholder="Если пусто — название из справочника"
              :disabled="disabled"
            >
          </label>

          <label class="block">
            <span class="mb-2 block text-sm font-medium">
              Зачем нужна консультация на этом этапе
            </span>

            <textarea
              v-model="item.consultation_description"
              maxlength="50000"
              class="textarea min-h-32 w-full"
              placeholder="Если пусто — описание из справочника"
              :disabled="disabled"
            />
          </label>
        </div>
      </template>
    </article>

    <button
      type="button"
      class="btn btn-outline w-full"
      :disabled="disabled || model.length >= 1000"
      @click="addConsultation"
    >
      <Icon name="lucide:plus" class="size-4" />
      Добавить консультацию
    </button>
  </div>
</template>