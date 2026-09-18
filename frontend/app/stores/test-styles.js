// ./frontend/app/stores/test-styles.js
import {
  STYLE_VERSION,
  buildAppliedCss,
  buildExportCss,
  cloneStyles,
  normalizeStyles,
  stylesAreDefault,
} from '~/utils/test-styles'

export const useTestStylesStore = defineStore(
  'test-styles',
  () => {
    const storageKey = ref(null)
    const saved = ref(null)
    const enabled = ref(false)
    const storageError = ref('')

    const available = computed(() => Boolean(storageKey.value))

    const hasCustomStyles = computed(() =>
      Boolean(
        saved.value
        && !stylesAreDefault(saved.value.settings),
      ),
    )

    const appliedCss = computed(() => {
      if (
        !available.value
        || !enabled.value
        || !hasCustomStyles.value
      ) {
        return ''
      }

      return buildAppliedCss(saved.value.settings)
    })

    const exportCss = computed(() =>
      saved.value
        ? buildExportCss(saved.value.settings)
        : '',
    )

    function accountIdFromToken(token) {
      try {
        const part = token.split('.')[1]
        if (!part) return null

        const base64 = part
          .replace(/-/g, '+')
          .replace(/_/g, '/')

        const padded = base64.padEnd(
          Math.ceil(base64.length / 4) * 4,
          '=',
        )

        const payload = JSON.parse(atob(padded))

        return (
          typeof payload.sub === 'string'
          && /^[0-9a-f-]{36}$/i.test(payload.sub)
        )
          ? payload.sub.toLowerCase()
          : null
      } catch {
        return null
      }
    }

    function normalizeSnapshot(snapshot) {
      if (!snapshot || typeof snapshot !== 'object') {
        throw new Error('Некорректный сохранённый вариант')
      }

      const name = snapshot.name ?? ''
      const comment = snapshot.comment ?? ''

      if (
        typeof name !== 'string'
        || name.length > 120
        || /[\r\n]/.test(name)
        || typeof comment !== 'string'
        || comment.length > 3000
      ) {
        throw new Error('Некорректное описание варианта')
      }

      return {
        settings: normalizeStyles(snapshot.settings),
        name: name.trim(),
        comment: comment.trim(),
      }
    }

    function setContext(token, role) {
      const accountId = (
        token && role === 'superuser'
      )
        ? accountIdFromToken(token)
        : null

      const nextKey = accountId
        ? `mentalme_test_styles_v${STYLE_VERSION}:${accountId}`
        : null

      if (nextKey === storageKey.value) return

      saved.value = null
      enabled.value = false
      storageError.value = ''
      storageKey.value = nextKey

      if (!nextKey) return

      try {
        const raw = localStorage.getItem(nextKey)
        if (!raw) return

        const record = JSON.parse(raw)

        if (
          record.version !== STYLE_VERSION
          || typeof record.enabled !== 'boolean'
        ) {
          throw new Error('Неподдерживаемый формат настроек')
        }

        saved.value = normalizeSnapshot(record.snapshot)
        enabled.value = record.enabled
      } catch {
        storageError.value = (
          'Не удалось прочитать локальные настройки. '
          + 'Используется исходное оформление. '
          + 'Вы можете сохранить новый вариант или удалить настройку.'
        )
      }
    }

    function persist(snapshot, nextEnabled) {
      if (!storageKey.value) {
        throw new Error('Студия доступна только суперпользователю')
      }

      try {
        localStorage.setItem(
          storageKey.value,
          JSON.stringify({
            version: STYLE_VERSION,
            enabled: nextEnabled,
            snapshot,
          }),
        )
      } catch {
        throw new Error(
          'Браузер не разрешил сохранить настройки. '
          + 'Проверьте доступность localStorage и свободное место.',
        )
      }

      storageError.value = ''
    }

    function save(settings, name = '', comment = '') {
      const snapshot = normalizeSnapshot({
        settings,
        name,
        comment,
      })

      const nextEnabled = !stylesAreDefault(snapshot.settings)

      // Сначала записываем. При ошибке сохранения
      // уже применённый вариант остаётся прежним.
      persist(snapshot, nextEnabled)

      saved.value = cloneStyles(snapshot)
      enabled.value = nextEnabled
    }

    function toggle() {
      if (!saved.value || !hasCustomStyles.value) return

      const nextEnabled = !enabled.value

      persist(saved.value, nextEnabled)
      enabled.value = nextEnabled
    }

    function remove() {
      if (!storageKey.value) return

      try {
        localStorage.removeItem(storageKey.value)
      } catch {
        throw new Error('Браузер не разрешил удалить настройку')
      }

      saved.value = null
      enabled.value = false
      storageError.value = ''
    }

    return {
      saved,
      enabled,
      available,
      hasCustomStyles,
      storageError,
      appliedCss,
      exportCss,

      setContext,
      save,
      toggle,
      remove,
    }
  },
)