// ./frontend/app/composables/useBodyScrollLock.js
let lockCount = 0
let previousOverflow = ''

export function useBodyScrollLock(locked) {
  function lock() {
    if (!import.meta.client) return

    if (lockCount === 0) {
      previousOverflow = document.body.style.overflow
      document.body.style.overflow = 'hidden'
    }

    lockCount += 1
  }

  function unlock() {
    if (!import.meta.client || lockCount === 0) return

    lockCount -= 1

    if (lockCount === 0) {
      document.body.style.overflow = previousOverflow
    }
  }

  watch(
    locked,
    (value, oldValue) => {
      if (value && !oldValue) {
        lock()
      }

      if (!value && oldValue) {
        unlock()
      }
    },
    {
      immediate: true,
    },
  )

  onBeforeUnmount(() => {
    if (locked.value) {
      unlock()
    }
  })
}