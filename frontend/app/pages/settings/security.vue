<!-- ./frontend/app/pages/settings/security.vue -->
<script setup>
const { $api } = useNuxtApp()
const { isSupported, registerPasskey } = useWebAuthn()

const passkeys = ref([])
const loading = ref(false)
const creating = ref(false)

const nameDialogOpen = ref(false)
const passkeyName = ref('Мой passkey')

const message = ref('')
const errorMessage = ref('')

async function fetchPasskeys() {
  loading.value = true

  try {
    passkeys.value = await $api(
      '/api/v1/auth/passkeys',
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить passkey'
  } finally {
    loading.value = false
  }
}

async function createPasskey() {
  creating.value = true
  errorMessage.value = ''
  message.value = ''

  try {
    const optionsResponse = await $api(
      '/api/v1/auth/passkeys/registration/options',
      {
        method: 'POST',
        body: {
          name:
            passkeyName.value.trim()
            || 'Passkey',
        },
      },
    )

    const credential = await registerPasskey(
      optionsResponse.options,
    )

    const response = await $api(
      '/api/v1/auth/passkeys/registration/verify',
      {
        method: 'POST',
        body: {
          challenge_id: optionsResponse.challenge_id,
          name:
            passkeyName.value.trim()
            || 'Passkey',
          credential,
        },
      },
    )

    localStorage.setItem(
      'mentalme_passkey_registered',
      '1',
    )

    message.value = response.message
    nameDialogOpen.value = false

    await fetchPasskeys()
  } catch (error) {
    if (error?.name === 'NotAllowedError') {
      errorMessage.value =
        'Создание passkey отменено'
    } else {
      errorMessage.value =
        error?.data?.detail
        || error?.message
        || 'Не удалось добавить passkey'
    }
  } finally {
    creating.value = false
  }
}

async function deletePasskey(passkeyId) {
  if (!window.confirm('Удалить этот passkey?')) {
    return
  }

  errorMessage.value = ''
  message.value = ''

  try {
    await $api(
      `/api/v1/auth/passkeys/${passkeyId}`,
      {
        method: 'DELETE',
      },
    )

    message.value = 'Passkey удалён'
    await fetchPasskeys()

    if (passkeys.value.length === 0) {
      localStorage.removeItem(
        'mentalme_passkey_registered',
      )
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось удалить passkey'
  }
}

onMounted(fetchPasskeys)
</script>

<template>
  <div class="mx-auto max-w-3xl space-y-6">
    <div>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Безопасность
      </h1>

      <p class="text-base-content/60 mt-1">
        Управление способами входа в аккаунт.
      </p>
    </div>

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
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <AuthPasswordForm />

    <section
      class="card bg-base-100 border-base-300 border"
    >
      <div class="card-body p-5 sm:p-6">
        <div
          class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between"
        >
          <div>
            <h2 class="card-title">
              <Icon
                name="lucide:fingerprint"
                class="size-6"
              />
              Passkey
            </h2>

            <p class="text-base-content/60 mt-2 text-sm">
              Входите с помощью отпечатка пальца,
              распознавания лица или PIN устройства.
            </p>
          </div>

          <button
            type="button"
            class="btn btn-primary shrink-0"
            :disabled="!isSupported"
            @click="nameDialogOpen = true"
          >
            <Icon
              name="lucide:plus"
              class="size-4"
            />
            Добавить
          </button>
        </div>

        <div
          v-if="!isSupported"
          class="alert alert-warning mt-5"
        >
          Браузер не поддерживает WebAuthn.
        </div>

        <div
          v-if="loading"
          class="flex justify-center py-8"
        >
          <span
            class="loading loading-spinner loading-lg text-primary"
          />
        </div>

        <div
          v-else-if="passkeys.length"
          class="mt-6 space-y-3"
        >
          <div
            v-for="passkey in passkeys"
            :key="passkey.id"
            class="border-base-300 flex items-center gap-3 rounded-2xl border p-4"
          >
            <div
              class="bg-base-200 flex size-11 shrink-0 items-center justify-center rounded-xl"
            >
              <Icon
                name="lucide:key-round"
                class="size-5"
              />
            </div>

            <div class="min-w-0 flex-1">
              <p class="truncate font-medium">
                {{ passkey.name }}
              </p>

              <p class="text-base-content/50 text-xs">
                Добавлен
                {{
                  new Date(
                    passkey.created_at,
                  ).toLocaleDateString('ru-RU')
                }}
              </p>
            </div>

            <button
              type="button"
              class="btn btn-circle btn-ghost btn-sm text-error"
              aria-label="Удалить passkey"
              @click="deletePasskey(passkey.id)"
            >
              <Icon
                name="lucide:trash-2"
                class="size-4"
              />
            </button>
          </div>
        </div>

        <div
          v-else
          class="border-base-300 mt-6 rounded-2xl border border-dashed p-6 text-center"
        >
          <Icon
            name="lucide:fingerprint"
            class="text-base-content/30 mx-auto size-10"
          />

          <p class="mt-3 font-medium">
            Passkey пока не добавлены
          </p>
        </div>
      </div>
    </section>
  </div>

  <UiResponsiveDialog
    v-model="nameDialogOpen"
    title="Добавить passkey"
  >
    <label class="form-control block">
      <span class="label">
        <span class="label-text">
          Название
        </span>
      </span>

      <input
        v-model="passkeyName"
        type="text"
        maxlength="100"
        class="input input-bordered w-full"
        placeholder="Например, iPhone или ноутбук"
      >
    </label>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn"
          :disabled="creating"
          @click="nameDialogOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="creating || !passkeyName.trim()"
          @click="createPasskey"
        >
          <span
            v-if="creating"
            class="loading loading-spinner loading-sm"
          />

          Создать passkey
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>