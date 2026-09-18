// ./frontend/app/utils/test-styles.js
import originalCss from '../assets/css/main.css?raw'

export const STYLE_VERSION = 1

export const COLOR_FIELDS = [
  { key: '--color-base-100', label: 'Основная поверхность' },
  { key: '--color-base-200', label: 'Фон страницы' },
  { key: '--color-base-300', label: 'Границы и разделители' },
  { key: '--color-base-content', label: 'Основной текст' },

  { key: '--color-primary', label: 'Основной акцент' },
  { key: '--color-primary-content', label: 'Текст на основном акценте' },

  { key: '--color-secondary', label: 'Дополнительный цвет' },
  { key: '--color-secondary-content', label: 'Текст на дополнительном цвете' },

  { key: '--color-accent', label: 'Акцентный цвет' },
  { key: '--color-accent-content', label: 'Текст на акцентном цвете' },

  { key: '--color-neutral', label: 'Нейтральный цвет' },
  { key: '--color-neutral-content', label: 'Текст на нейтральном цвете' },

  { key: '--color-info', label: 'Информация' },
  { key: '--color-info-content', label: 'Текст информационного блока' },

  { key: '--color-success', label: 'Успех' },
  { key: '--color-success-content', label: 'Текст успешного состояния' },

  { key: '--color-warning', label: 'Предупреждение' },
  { key: '--color-warning-content', label: 'Текст предупреждения' },

  { key: '--color-error', label: 'Ошибка' },
  { key: '--color-error-content', label: 'Текст ошибки' },
]

export const NUMBER_FIELDS = [
  {
    key: '--radius-selector',
    label: 'Скругление переключателей',
    unit: 'rem',
    min: 0,
    max: 3,
    step: 0.125,
  },
  {
    key: '--radius-field',
    label: 'Скругление кнопок и полей',
    unit: 'rem',
    min: 0,
    max: 3,
    step: 0.125,
  },
  {
    key: '--radius-box',
    label: 'Скругление контейнеров daisyUI',
    unit: 'rem',
    min: 0,
    max: 3,
    step: 0.125,
  },
  {
    key: '--size-selector',
    label: 'Базовый размер переключателей',
    unit: 'rem',
    min: 0.125,
    max: 0.5,
    step: 0.025,
  },
  {
    key: '--size-field',
    label: 'Базовый размер кнопок и полей',
    unit: 'rem',
    min: 0.125,
    max: 0.5,
    step: 0.025,
  },
  {
    key: '--border',
    label: 'Толщина границ daisyUI',
    unit: 'px',
    min: 0,
    max: 4,
    step: 1,
  },
  {
    key: '--depth',
    label: 'Эффект глубины daisyUI',
    unit: '',
    min: 0,
    max: 1,
    step: 1,
  },
  {
    key: '--noise',
    label: 'Эффект шума daisyUI',
    unit: '',
    min: 0,
    max: 1,
    step: 1,
  },
]

export const FONT_OPTIONS = [
  {
    id: 'system',
    label: 'Системный',
    css: 'ui-sans-serif, system-ui, sans-serif',
  },
  {
    id: 'arial',
    label: 'Arial',
    css: 'Arial, Helvetica, sans-serif',
  },
  {
    id: 'georgia',
    label: 'Georgia',
    css: 'Georgia, "Times New Roman", serif',
  },
]

const ALL_FIELDS = [...COLOR_FIELDS, ...NUMBER_FIELDS]

function themeBlocksPattern() {
  return /@plugin\s+"daisyui\/theme"\s*\{[^}]*\}/g
}

function themeName(block) {
  return block.match(/\bname:\s*"(light|dark)"/)?.[1]
}

export function cloneStyles(value) {
  return JSON.parse(JSON.stringify(value))
}

function readOriginalThemes() {
  const themes = {}

  for (const block of originalCss.match(themeBlocksPattern()) || []) {
    const name = themeName(block)
    if (!name) continue

    const values = Object.fromEntries(
      [...block.matchAll(/(--[\w-]+)\s*:\s*([^;]+);/g)]
        .map((match) => [match[1], match[2].trim()]),
    )

    for (const field of ALL_FIELDS) {
      if (!(field.key in values)) {
        throw new Error(
          `В main.css отсутствует ${field.key} для темы ${name}`,
        )
      }
    }

    themes[name] = Object.fromEntries(
      ALL_FIELDS.map((field) => [field.key, values[field.key]]),
    )
  }

  if (!themes.light || !themes.dark) {
    throw new Error('В main.css должны быть темы light и dark')
  }

  return themes
}

const ORIGINAL_THEMES = readOriginalThemes()

const ORIGINAL_TYPOGRAPHY = {
  enabled: false,
  font: 'system',
  size: 16,
  lineHeight: 1.5,
}

export function createDefaultStyles() {
  return {
    themes: cloneStyles(ORIGINAL_THEMES),
    typography: { ...ORIGINAL_TYPOGRAPHY },
  }
}

function normalizeNumber(value, min, max, label) {
  const number = Number(value)

  if (
    !Number.isFinite(number)
    || number < min
    || number > max
  ) {
    throw new Error(`Некорректное значение: ${label}`)
  }

  return Number(number.toFixed(4))
}

export function normalizeStyles(input) {
  if (!input || typeof input !== 'object') {
    throw new Error('Некорректные настройки оформления')
  }

  const result = createDefaultStyles()

  for (const name of ['light', 'dark']) {
    const theme = input.themes?.[name]

    if (!theme || typeof theme !== 'object') {
      throw new Error(`Отсутствуют настройки темы ${name}`)
    }

    for (const field of COLOR_FIELDS) {
      const value = theme[field.key]

      if (
        typeof value !== 'string'
        || !/^#[0-9a-f]{6}$/i.test(value)
      ) {
        throw new Error(`Некорректный цвет: ${field.label}`)
      }

      result.themes[name][field.key] = value.toLowerCase()
    }

    for (const field of NUMBER_FIELDS) {
      const raw = theme[field.key]

      if (typeof raw !== 'string') {
        throw new Error(`Некорректное значение: ${field.label}`)
      }

      const pattern = field.unit
        ? new RegExp(`^(\\d+(?:\\.\\d+)?)${field.unit}$`)
        : /^([01])$/

      const match = raw.match(pattern)

      if (!match) {
        throw new Error(`Некорректное значение: ${field.label}`)
      }

      const value = normalizeNumber(
        match[1],
        field.min,
        field.max,
        field.label,
      )

      result.themes[name][field.key] = `${value}${field.unit}`
    }
  }

  if (input.typography?.enabled === true) {
    const typography = input.typography

    if (!FONT_OPTIONS.some((font) => font.id === typography.font)) {
      throw new Error('Неизвестный шрифт')
    }

    result.typography = {
      enabled: true,
      font: typography.font,
      size: normalizeNumber(
        typography.size,
        12,
        22,
        'Размер текста',
      ),
      lineHeight: normalizeNumber(
        typography.lineHeight,
        1.2,
        2,
        'Межстрочный интервал',
      ),
    }
  }

  return result
}

export function stylesAreDefault(settings) {
  return JSON.stringify(normalizeStyles(settings))
    === JSON.stringify(normalizeStyles(createDefaultStyles()))
}

function typographyCss(typography) {
  if (!typography.enabled) return ''

  const font = FONT_OPTIONS.find(
    (item) => item.id === typography.font,
  )

  return `
/* Глобальная типографика, согласованная в студии оформления. */
html {
  font-family: ${font.css};
  font-size: ${typography.size}px;
  line-height: ${typography.lineHeight};
}

body {
  font-family: inherit;
  line-height: inherit;
}
`
}

export function buildAppliedCss(input) {
  const settings = normalizeStyles(input)

  const themes = ['light', 'dark'].map((name) => {
    const declarations = Object.entries(settings.themes[name])
      .map(([key, value]) => `  ${key}: ${value};`)
      .join('\n')

    return `:root[data-theme="${name}"] {\n${declarations}\n}`
  })

  return [
    ...themes,
    typographyCss(settings.typography),
  ].join('\n\n')
}

export function buildExportCss(input) {
  const settings = normalizeStyles(input)

  const result = originalCss.replace(
    themeBlocksPattern(),
    (block) => {
      const name = themeName(block)
      if (!name) return block

      return block.replace(
        /(--[\w-]+)\s*:\s*([^;]+);/g,
        (declaration, key) => {
          const value = settings.themes[name][key]

          return value === undefined
            ? declaration
            : `${key}: ${value};`
        },
      )
    },
  )

  const header = '/* ./frontend/app/assets/css/main.css */'

  return [
    result.trimStart().startsWith(header) ? '' : header,
    result.trim(),
    typographyCss(settings.typography).trim(),
    '',
  ].filter((part, index) => part || index > 0).join('\n')
}

export function buildPreviewStyle(input, theme) {
  const settings = normalizeStyles(input)
  const style = { ...settings.themes[theme] }

  if (settings.typography.enabled) {
    const typography = settings.typography
    const font = FONT_OPTIONS.find(
      (item) => item.id === typography.font,
    )

    style.fontFamily = font.css
    style.fontSize = `${typography.size}px`
    style.lineHeight = String(typography.lineHeight)
  }

  return style
}

export function downloadStyles(css) {
  const blob = new Blob([css], {
    type: 'text/css;charset=utf-8',
  })

  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')

  link.href = url
  link.download = 'main.css'
  document.body.appendChild(link)
  link.click()
  link.remove()

  window.setTimeout(() => URL.revokeObjectURL(url), 1000)
}