// ./frontend/app/utils/media.js

export const MEDIA_PRESETS = Object.freeze({
  doctor: {
    ratio: 1,
    width: 512,
    height: 512,
    label: 'Фотография врача',
  },
  article: {
    ratio: 16 / 9,
    width: 1600,
    height: 900,
    label: 'Обложка статьи',
  },
  questionnaire: {
    ratio: 16 / 9,
    width: 1600,
    height: 900,
    label: 'Обложка опросника',
  },
  program: {
    ratio: 16 / 9,
    width: 1600,
    height: 900,
    label: 'Обложка программы',
  },
  life_aspect: {
    ratio: 3,
    width: 1800,
    height: 600,
    label: 'Обложка сферы жизни',
  },
})

export const MEDIA_MAX_BYTES = 10 * 1024 * 1024
export const MEDIA_MAX_PIXELS = 24_000_000

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i

export function isMediaId(value) {
  return typeof value === 'string'
    && UUID_PATTERN.test(value)
}

export function mediaEntityPath(purpose, entityId) {
  if (!MEDIA_PRESETS[purpose] || !isMediaId(entityId)) {
    throw new Error('Некорректный адрес изображения')
  }

  return `/api/v1/media/images/${purpose}/${entityId}`
}

export function mediaErrorText(error, fallback) {
  const detail = error?.data?.detail

  if (typeof detail === 'string') {
    return detail
  }

  if (Array.isArray(detail)) {
    const messages = detail
      .map(item => item?.msg)
      .filter(message => typeof message === 'string')

    if (messages.length) {
      return messages.join('; ')
    }
  }

  return fallback
}

export function readImageDimensions(url) {
  return new Promise((resolve, reject) => {
    const image = new Image()

    image.onload = () => {
      resolve({
        width: image.naturalWidth,
        height: image.naturalHeight,
      })

      image.onload = null
      image.onerror = null
    }

    image.onerror = () => {
      image.onload = null
      image.onerror = null

      reject(new Error('Не удалось прочитать изображение'))
    }

    image.src = url
  })
}