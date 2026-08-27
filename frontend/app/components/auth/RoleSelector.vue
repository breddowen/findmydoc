<!-- ./frontend/app/components/auth/RoleSelector.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const auth = useAuthStore()

const emit = defineEmits([
  'selected',
])

const errorMessage = ref('')

const roleMeta = {
  superuser: {
    title: 'Суперпользователь',
    description: 'Управление системой',
    icon: 'lucide:shield',
  },
  med_assistant: {
    title: 'Медицинский ассистент',
    description: 'Администрирование сервиса',
    icon: 'lucide:clipboard-plus',
  },
  doctor: {
    title: 'Врач',
    description: 'Работа с пациентами',
    icon: 'lucide:stethoscope',
  },
  patient: {
    title: 'Пациент',
    description: 'Программы и материалы',
    icon: 'lucide:user-round',
  },
  relative: {
    title: 'Родственник',
    description: 'Связанные пациенты',
    icon: 'lucide:users-round',
  },
}

async function selectRole(role) {
  errorMessage.value = ''

  try {
    await auth.selectRole(role)
    model.value = false
    emit('selected', role)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось выбрать роль'
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Выберите роль"
    :close-on-backdrop="false"
    :show-close-button="false"
  >
    <p class="text-base-content/70 mb-4 text-sm">
      У аккаунта несколько ролей. Выберите, в каком
      качестве вы хотите войти.
    </p>

    <div
      v-if="errorMessage"
      class="alert alert-error mb-4"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <div class="grid gap-3">
      <button
        v-for="roleItem in auth.availableRoles"
        :key="roleItem.role"
        type="button"
        class="border-base-300 hover:border-primary hover:bg-primary/5 flex min-h-20 w-full items-center gap-4 rounded-2xl border p-4 text-left transition"
        :disabled="auth.loading"
        @click="selectRole(roleItem.role)"
      >
        <div
          class="bg-primary/10 text-primary flex size-12 shrink-0 items-center justify-center rounded-2xl"
        >
          <Icon
            :name="
              roleMeta[roleItem.role]?.icon
              || 'lucide:user'
            "
            class="size-6"
          />
        </div>

        <div class="min-w-0 flex-1">
          <p class="font-semibold">
            {{
              roleMeta[roleItem.role]?.title
              || roleItem.role
            }}
          </p>

          <p class="text-base-content/60 text-sm">
            {{
              roleMeta[roleItem.role]?.description
            }}
          </p>
        </div>

        <span
          v-if="roleItem.is_primary"
          class="badge badge-primary badge-outline"
        >
          Основная
        </span>

        <Icon
          name="lucide:chevron-right"
          class="size-5 shrink-0"
        />
      </button>
    </div>
  </UiResponsiveDialog>
</template>