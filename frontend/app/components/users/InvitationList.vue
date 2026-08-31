<!-- ./frontend/app/components/users/InvitationList.vue -->
<script setup>
defineProps({
  invitations: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
  processingId: {
    type: String,
    default: '',
  },
})

const emit = defineEmits([
  'send',
  'revoke',
])

const roleNames = {
  superuser: 'Суперпользователь',
  med_assistant: 'Медицинский ассистент',
  doctor: 'Врач',
  patient: 'Пациент',
  relative: 'Родственник',
}

const statusData = {
  pending: {
    label: 'Активно',
    class: 'badge-info',
  },
  accepted: {
    label: 'Принято',
    class: 'badge-success',
  },
  revoked: {
    label: 'Отозвано',
    class: 'badge-error',
  },
  expired: {
    label: 'Истекло',
    class: 'badge-warning',
  },
}

function formatDate(value) {
  if (!value) return '—'

  return new Date(value).toLocaleString('ru-RU', {
    dateStyle: 'short',
    timeStyle: 'short',
  })
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
    v-else-if="!invitations.length"
    class="border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:mail-plus"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Приглашений пока нет
    </p>
  </div>

  <div
    v-else
    class="space-y-3"
  >
    <article
      v-for="invitation in invitations"
      :key="invitation.id"
      class="card bg-base-100 border-base-300 border"
    >
      <div class="card-body gap-4 p-4 sm:p-5">
        <div
          class="flex flex-col gap-3 sm:flex-row sm:items-start"
        >
          <div class="min-w-0 flex-1">
            <div class="flex flex-wrap items-center gap-2">
              <h3 class="truncate font-semibold">
                {{ invitation.email }}
              </h3>

              <span class="badge badge-outline">
                {{
                  roleNames[invitation.invitation_type]
                  || invitation.invitation_type
                }}
              </span>

              <span
                class="badge"
                :class="
                  statusData[invitation.status]?.class
                "
              >
                {{
                  statusData[invitation.status]?.label
                  || invitation.status
                }}
              </span>
            </div>

            <dl
              class="text-base-content/60 mt-3 grid gap-x-6 gap-y-1 text-sm sm:grid-cols-2"
            >
              <div v-if="invitation.record_id">
                <dt class="inline">Record ID:</dt>
                <dd class="inline font-mono">
                  {{ invitation.record_id }}
                </dd>
              </div>

              <div v-if="invitation.speciality_name">
                <dt class="inline">Специальность:</dt>
                <dd class="inline">
                  {{ invitation.speciality_name }}
                </dd>
              </div>

              <div>
                <dt class="inline">Создано:</dt>
                <dd class="inline">
                  {{ formatDate(invitation.created_at) }}
                </dd>
              </div>

              <div>
                <dt class="inline">Действует до:</dt>
                <dd class="inline">
                  {{ formatDate(invitation.expires_at) }}
                </dd>
              </div>

              <div>
                <dt class="inline">Создал:</dt>
                <dd class="inline">
                  {{ invitation.creator.full_name }}
                </dd>
              </div>

              <div>
                <dt class="inline">Письмо:</dt>
                <dd class="inline">
                  {{
                    invitation.email_sent_at
                      ? formatDate(
                          invitation.email_sent_at,
                        )
                      : invitation.email_send_error
                        ? 'Ошибка отправки'
                        : 'Не отправлялось'
                  }}
                </dd>
              </div>
            </dl>

            <p
              v-if="invitation.email_send_error"
              class="text-error mt-2 text-sm"
            >
              {{ invitation.email_send_error }}
            </p>
          </div>

          <div
            v-if="
              invitation.can_resend
              || invitation.can_revoke
            "
            class="flex shrink-0 flex-wrap gap-2"
          >
            <button
              v-if="invitation.can_resend"
              type="button"
              class="btn btn-primary btn-sm"
              :disabled="
                processingId === invitation.id
              "
              @click="emit('send', invitation)"
            >
              <span
                v-if="processingId === invitation.id"
                class="loading loading-spinner loading-xs"
              />

              <Icon
                v-else
                name="lucide:send"
                class="size-4"
              />

              Отправить
            </button>

            <button
              v-if="invitation.can_revoke"
              type="button"
              class="btn btn-ghost btn-sm text-error"
              :disabled="
                processingId === invitation.id
              "
              @click="emit('revoke', invitation)"
            >
              Отозвать
            </button>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>