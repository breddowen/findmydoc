<!-- ./frontend/app/components/users/List.vue -->
<script setup>
defineProps({
  users: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'toggle-block',
  'delete',
])

const auth = useAuthStore()

const roleNames = {
  superuser: 'Суперпользователь',
  med_assistant: 'Медицинский ассистент',
  doctor: 'Врач',
  patient: 'Пациент',
  relative: 'Родственник',
}

function canBlock(user) {
  if (auth.activeRole === 'superuser') {
    return true
  }

  return !user.roles.includes('superuser')
}
</script>

<template>
  <div
    v-if="loading"
    class="flex justify-center py-16"
  >
    <span
      class="loading loading-spinner loading-lg text-primary"
    />
  </div>

  <div
    v-else-if="!users.length"
    class="border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:users"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Пользователи не найдены
    </p>
  </div>

  <div
    v-else
    class="space-y-3"
  >
    <article
      v-for="user in users"
      :key="user.id"
      class="card bg-base-100 border-base-300 border"
    >
      <div
        class="card-body flex-row items-center gap-4 p-4 sm:p-5"
      >
        <div
          class="bg-base-200 flex size-11 shrink-0 items-center justify-center rounded-full"
        >
          <Icon
            name="lucide:user"
            class="size-5"
          />
        </div>

        <div class="min-w-0 flex-1">
          <h3 class="truncate font-semibold">
            {{ user.full_name }}
          </h3>

          <p
            class="text-base-content/60 truncate text-sm"
          >
            {{ user.email }}
          </p>

          <div class="mt-2 flex flex-wrap gap-1">
            <span
              v-for="role in user.roles"
              :key="role"
              class="badge badge-sm badge-outline"
            >
              {{ roleNames[role] || role }}
            </span>

            <span
              v-if="user.is_blocked"
              class="badge badge-sm badge-error"
            >
              Заблокирован
            </span>

            <span
              v-else-if="!user.is_email_verified"
              class="badge badge-sm badge-warning"
            >
              Email не подтверждён
            </span>
          </div>
        </div>

        <div class="dropdown dropdown-end">
          <button
            type="button"
            tabindex="0"
            class="btn btn-circle btn-ghost btn-sm"
            aria-label="Действия"
          >
            <Icon
              name="lucide:ellipsis-vertical"
              class="size-5"
            />
          </button>

          <ul
            tabindex="0"
            class="menu dropdown-content bg-base-100 border-base-300 z-20 mt-2 w-56 rounded-box border p-2 shadow-xl"
          >
            <li v-if="canBlock(user)">
              <button
                type="button"
                @click="
                  emit(
                    'toggle-block',
                    user,
                    !user.is_blocked,
                  )
                "
              >
                <Icon
                  :name="
                    user.is_blocked
                      ? 'lucide:lock-open'
                      : 'lucide:ban'
                  "
                  class="size-4"
                />

                {{
                  user.is_blocked
                    ? 'Разблокировать'
                    : 'Заблокировать'
                }}
              </button>
            </li>

            <li v-if="auth.activeRole === 'superuser'">
              <button
                type="button"
                class="text-error"
                @click="emit('delete', user)"
              >
                <Icon
                  name="lucide:trash-2"
                  class="size-4"
                />
                Удалить
              </button>
            </li>
          </ul>
        </div>
      </div>
    </article>
  </div>
</template>