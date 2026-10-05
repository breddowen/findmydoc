// ./frontend/app/utils/videos.js

export function videoDuration(value) {
  const seconds = Math.max(
    0,
    Math.floor(Number(value) || 0),
  )

  return [
    Math.floor(seconds / 60),
    String(seconds % 60).padStart(2, '0'),
  ].join(':')
}

export function videoSize(value) {
  return `${(
    (Number(value) || 0) / 1024 / 1024
  ).toFixed(1)} МиБ`
}

export function videoApiUrl(base, path, query = {}) {
  const root = String(base || '').replace(/\/+$/, '')
  const parameters = new URLSearchParams()

  for (const [key, value] of Object.entries(query)) {
    if (value !== null && value !== undefined && value !== '') {
      parameters.set(key, String(value))
    }
  }

  const suffix = parameters.toString()

  return `${root}${path}${suffix ? `?${suffix}` : ''}`
}