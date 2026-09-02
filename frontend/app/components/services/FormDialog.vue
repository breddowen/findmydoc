<!-- ./frontend/app/components/services/FormDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  service: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits([
  'saved',
])

const store = useServicesStore()

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()

const errorMessage = ref('')
const priceMode = ref('fixed')

const form = reactive({
  code: '',
  title: '',
  description: '',
  price_amount: '',
  currency: 'RUB',
  discount_percent: 0,
})

const dialogTitle = computed(() =>
  props.service
    ? 'Изменить услугу'
    : 'Новая услуга',
)

const previewService = computed(() => {
  const priceAmount =
    priceMode.value === 'request'
      ? null
      : Number(form.price_amount || 0)

  const discount =
    priceAmount === 0
      ? 0
      : Number(form.discount_percent || 0)

  return {
    price_amount: priceAmount,
    currency:
      priceMode.value === 'request'
        ? null
        : form.currency,
    discount_percent: discount,
    final_price_amount: null,
  }
})

function resetForm() {
  errorMessage.value = ''

  if (!props.service) {
    priceMode.value = 'fixed'

    Object.assign(form, {
      code: '',
      title: '',
      description: '',
      price_amount: '',
      currency: 'RUB',
      discount_percent: 0,
    })

    return
  }

  priceMode.value =
    props.service.price_amount === null
      ? 'request'
      : 'fixed'

  Object.assign(form, {
    code: props.service.code || '',
    title: props.service.title || '',
    description:
      props.service.description || '',
    price_amount:
      props.service.price_amount ?? '',
    currency:
      props.service.currency || 'RUB',
    discount_percent:
      props.service.discount_percent || 0,
  })
}

function validateForm() {
  if (!form.code.trim()) {
    return 'Введите код услуги'
  }

  if (!form.title.trim()) {
    return 'Введите название услуги'
  }

  if (
    priceMode.value === 'fixed'
    && (
      form.price_amount === ''
      || form.price_amount === null
    )
  ) {
    return 'Укажите стоимость услуги'
  }

  if (
    priceMode.value === 'fixed'
    && Number(form.price_amount) < 0
  ) {
    return 'Стоимость не может быть отрицательной'
  }

  return null
}

function buildPayload() {
  const priceAmount =
    priceMode.value === 'request'
      ? null
      : Number(form.price_amount)

  return {
    code: form.code.trim().toUpperCase(),
    title: form.title.trim(),
    description:
      form.description.trim() || null,

    price_amount: priceAmount,
    currency:
      priceMode.value === 'request'
        ? null
        : form.currency,

    discount_percent:
      priceMode.value === 'request'
      || priceAmount === 0
        ? 0
        : Number(form.discount_percent || 0),
  }
}

async function save() {
  errorMessage.value = validateForm() || ''

  if (errorMessage.value) return

  try {
    const payload = buildPayload()

    const response = props.service
      ? await store.updateService(
          props.service.id,
          payload,
        )
      : await store.createService(payload)

    model.value = false
    emit('saved', response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сохранить услугу'
  }
}

watch(
  [
    () => model.value,
    () => props.service,
  ],
  ([opened]) => {
    if (opened) {
      resetForm()
    }
  },
  {
    deep: true,
  },
)

watch(
  () => form.price_amount,
  (value) => {
    if (
      value !== ''
      && Number(value) === 0
    ) {
      form.discount_percent = 0
    }
  },
)

watch(priceMode, (value) => {
  if (value === 'request') {
    form.discount_percent = 0
  }
})
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    :title="dialogTitle"
    max-width-class="max-w-2xl"
  >
    <form
      id="medical-service-form"
      class="space-y-5"
      @submit.prevent="save"
    >
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

      <div class="grid gap-4 sm:grid-cols-2">
        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Код услуги
          </span>

          <input
            v-model="form.code"
            type="text"
            required
            maxlength="50"
            class="input input-bordered w-full font-mono uppercase"
            placeholder="PRG568"
            @input="
              form.code =
                $event.target.value.toUpperCase()
            "
          >

          <span class="text-base-content/50 mt-1 text-xs">
            Латинские буквы, цифры, дефис и
            нижнее подчёркивание.
          </span>
        </label>

        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Название
          </span>

          <input
            v-model="form.title"
            type="text"
            required
            maxlength="300"
            class="input input-bordered w-full"
          >
        </label>
      </div>

      <label class="form-control block">
        <span class="label-text mb-2">
          Описание
        </span>

        <textarea
          v-model="form.description"
          class="textarea textarea-bordered min-h-28 w-full"
        />
      </label>

      <fieldset
        class="border-base-300 rounded-2xl border p-4"
      >
        <legend class="px-2 font-medium">
          Тип стоимости
        </legend>

        <div class="flex flex-col gap-3 sm:flex-row">
          <label
            class="border-base-300 flex flex-1 cursor-pointer items-center gap-3 rounded-xl border p-3"
          >
            <input
              v-model="priceMode"
              type="radio"
              value="fixed"
              class="radio radio-primary"
            >

            <span>
              <span class="block font-medium">
                Фиксированная цена
              </span>

              <span
                class="text-base-content/50 text-xs"
              >
                Включая бесплатную услугу с ценой 0
              </span>
            </span>
          </label>

          <label
            class="border-base-300 flex flex-1 cursor-pointer items-center gap-3 rounded-xl border p-3"
          >
            <input
              v-model="priceMode"
              type="radio"
              value="request"
              class="radio radio-primary"
            >

            <span>
              <span class="block font-medium">
                Цена по запросу
              </span>

              <span
                class="text-base-content/50 text-xs"
              >
                Стоимость не показывается пациенту
              </span>
            </span>
          </label>
        </div>
      </fieldset>

      <div
        v-if="priceMode === 'fixed'"
        class="grid gap-4 sm:grid-cols-3"
      >
        <label class="form-control block">
          <span class="label-text mb-2">
            Стоимость
          </span>

          <input
            v-model="form.price_amount"
            type="number"
            required
            min="0"
            step="0.01"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Валюта
          </span>

          <select
            v-model="form.currency"
            class="select select-bordered w-full"
          >
            <option value="RUB">
              Рубли
            </option>

            <option value="UNIT">
              Условные единицы
            </option>
          </select>
        </label>

        <label class="form-control block">
          <span class="label-text mb-2">
            Скидка, %
          </span>

          <input
            v-model.number="form.discount_percent"
            type="number"
            min="0"
            max="100"
            step="1"
            class="input input-bordered w-full"
            :disabled="
              form.price_amount !== ''
              && Number(form.price_amount) === 0
            "
          >
        </label>
      </div>

      <div
        class="bg-base-200 rounded-2xl p-4"
      >
        <p class="text-base-content/50 text-xs">
          Пациент увидит
        </p>

        <div
          class="mt-1 flex flex-wrap items-center gap-2"
        >
          <strong class="text-primary text-xl">
            {{ formatFinalPrice(previewService) }}
          </strong>

          <span
            v-if="hasDiscount(previewService)"
            class="text-base-content/40 line-through"
          >
            {{ formatOriginalPrice(previewService) }}
          </span>

          <span
            v-if="hasDiscount(previewService)"
            class="badge badge-error"
          >
            −{{ form.discount_percent }}%
          </span>
        </div>
      </div>
    </form>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="submit"
          form="medical-service-form"
          class="btn btn-primary"
          :disabled="store.saving"
        >
          <span
            v-if="store.saving"
            class="loading loading-spinner loading-sm"
          />

          Сохранить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>