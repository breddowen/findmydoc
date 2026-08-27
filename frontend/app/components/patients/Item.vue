<!-- ./frontend/app/components/patients/Item.vue -->
<script setup>
defineProps({
  patient: {
    type: Object,
    required: true,
  },
})

function formatDate(value) {
  if (!value) return '—'

  return new Intl.DateTimeFormat(
    'ru-RU',
    {
      dateStyle: 'short',
      timeStyle: 'short',
    },
  ).format(new Date(value))
}
</script>

<template>
  <NuxtLink
    :to="`/patients/${patient.patient_id}`"
    class="card bg-base-100 border-base-300 hover:border-primary block border transition"
  >
    <div class="card-body p-4">
      <div class="flex items-start gap-3">
        <div
          class="avatar avatar-placeholder shrink-0"
        >
          <div
            class="bg-primary/10 text-primary size-11 rounded-full"
          >
            <Icon
              name="lucide:user-round"
              class="size-5"
            />
          </div>
        </div>

        <div class="min-w-0 flex-1">
          <h2 class="truncate font-semibold">
            {{ patient.fullname }}
          </h2>

          <p class="text-base-content/60 truncate text-sm">
            {{ patient.email }}
          </p>

          <p class="text-base-content/50 mt-1 text-xs">
            Карта: {{ patient.record_id }}
          </p>
        </div>

        <PatientsContactStatus
          :allowed="patient.assistant_contact_allowed"
          :do-not-call="patient.do_not_call"
          :show-text="false"
        />
      </div>

      <div
        class="border-base-300 mt-3 grid grid-cols-2 gap-3 border-t pt-3 text-sm"
      >
        <div>
          <p class="text-base-content/50 text-xs">
            Регистрация
          </p>

          <p>
            {{
              patient.registration_status
                === 'registered'
                ? 'Завершена'
                : 'Email не подтверждён'
            }}
          </p>
        </div>

        <div>
          <p class="text-base-content/50 text-xs">
            Последняя активность
          </p>

          <p>
            {{ formatDate(patient.last_activity_at) }}
          </p>
        </div>
      </div>

      <div class="mt-3 flex flex-wrap gap-2">
        <span
          v-if="patient.pro_enabled"
          class="badge badge-secondary"
        >
          Pro
        </span>

        <span class="badge badge-outline">
          Врачей: {{ patient.doctors_count }}
        </span>
      </div>
    </div>
  </NuxtLink>
</template>