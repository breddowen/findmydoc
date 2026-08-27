// ./frontend/app/composables/useWebAuthn.js
export function useWebAuthn() {
  const isSupported = computed(
    () =>
      import.meta.client
      && Boolean(window.PublicKeyCredential),
  )

  function base64UrlToArrayBuffer(value) {
    const padding = '='.repeat(
      (4 - (value.length % 4)) % 4,
    )

    const base64 = value
      .replace(/-/g, '+')
      .replace(/_/g, '/')
      + padding

    const binary = window.atob(base64)
    const bytes = new Uint8Array(binary.length)

    for (let index = 0; index < binary.length; index += 1) {
      bytes[index] = binary.charCodeAt(index)
    }

    return bytes.buffer
  }

  function arrayBufferToBase64Url(value) {
    if (!value) return null

    const bytes = new Uint8Array(value)
    let binary = ''

    for (const byte of bytes) {
      binary += String.fromCharCode(byte)
    }

    return window
      .btoa(binary)
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=+$/g, '')
  }

  function prepareRegistrationOptions(options) {
    return {
      ...options,
      challenge: base64UrlToArrayBuffer(
        options.challenge,
      ),
      user: {
        ...options.user,
        id: base64UrlToArrayBuffer(options.user.id),
      },
      excludeCredentials: (
        options.excludeCredentials || []
      ).map((credential) => ({
        ...credential,
        id: base64UrlToArrayBuffer(credential.id),
      })),
    }
  }

  function prepareAuthenticationOptions(options) {
    return {
      ...options,
      challenge: base64UrlToArrayBuffer(
        options.challenge,
      ),
      allowCredentials: (
        options.allowCredentials || []
      ).map((credential) => ({
        ...credential,
        id: base64UrlToArrayBuffer(credential.id),
      })),
    }
  }

  function serializeCredential(credential) {
    const response = credential.response

    const serializedResponse = {
      clientDataJSON: arrayBufferToBase64Url(
        response.clientDataJSON,
      ),
    }

    if ('attestationObject' in response) {
      serializedResponse.attestationObject =
        arrayBufferToBase64Url(
          response.attestationObject,
        )

      if (typeof response.getTransports === 'function') {
        serializedResponse.transports =
          response.getTransports()
      }
    }

    if ('authenticatorData' in response) {
      serializedResponse.authenticatorData =
        arrayBufferToBase64Url(
          response.authenticatorData,
        )

      serializedResponse.signature =
        arrayBufferToBase64Url(response.signature)

      serializedResponse.userHandle =
        response.userHandle
          ? arrayBufferToBase64Url(response.userHandle)
          : null
    }

    return {
      id: credential.id,
      rawId: arrayBufferToBase64Url(
        credential.rawId,
      ),
      type: credential.type,
      authenticatorAttachment:
        credential.authenticatorAttachment || null,
      clientExtensionResults:
        credential.getClientExtensionResults(),
      response: serializedResponse,
    }
  }

  async function registerPasskey(options) {
    if (!isSupported.value) {
      throw new Error(
        'Этот браузер не поддерживает passkey',
      )
    }

    const credential = await navigator.credentials.create({
      publicKey: prepareRegistrationOptions(options),
    })

    if (!credential) {
      throw new Error('Passkey не был создан')
    }

    return serializeCredential(credential)
  }

  async function authenticateWithPasskey(options) {
    if (!isSupported.value) {
      throw new Error(
        'Этот браузер не поддерживает passkey',
      )
    }

    const credential = await navigator.credentials.get({
      publicKey: prepareAuthenticationOptions(options),
      mediation: 'optional',
    })

    if (!credential) {
      throw new Error('Passkey не был выбран')
    }

    return serializeCredential(credential)
  }

  return {
    isSupported,
    registerPasskey,
    authenticateWithPasskey,
  }
}