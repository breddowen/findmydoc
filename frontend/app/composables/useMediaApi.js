// ./frontend/app/composables/useMediaApi.js

import { mediaEntityPath } from '~/utils/media'

export function useMediaApi() {
  const { $api } = useNuxtApp()

  async function upload(
    purpose,
    cropped,
    { signal } = {},
  ) {
    const body = new FormData()

    body.append('purpose', purpose)
    body.append('crop_left', '0')
    body.append('crop_top', '0')
    body.append('crop_width', String(cropped.width))
    body.append('crop_height', String(cropped.height))
    body.append('file', cropped.blob, 'crop.png')

    return await $api('/api/v1/media/uploads', {
      method: 'POST',
      body,
      signal,
      retry: 0,
    })
  }

  async function getEntityImage(
    purpose,
    entityId,
    { signal } = {},
  ) {
    return await $api(
      mediaEntityPath(purpose, entityId),
      {
        signal,
        retry: 0,
        cache: 'no-store',
      },
    )
  }

  async function updateEntityImage(
    purpose,
    entityId,
    {
      imageId,
      expectedImageId,
      signal,
    },
  ) {
    return await $api(
      mediaEntityPath(purpose, entityId),
      {
        method: 'PATCH',
        body: {
          image_id: imageId,
          expected_image_id: expectedImageId,
        },
        signal,
        retry: 0,
      },
    )
  }

  return {
    upload,
    getEntityImage,
    updateEntityImage,
  }
}