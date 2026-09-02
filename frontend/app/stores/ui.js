// ./frontend/app/stores/ui.js
export const useUiStore = defineStore('ui', () => {
  const theme = ref('light')
  const initialized = ref(false)

  // false: узкая панель на компьютере
  // и полностью скрытая панель на телефоне.
  const sidebarOpen = ref(false)

  const isDark = computed(
    () => theme.value === 'dark',
  )

  function applyTheme() {
    if (!import.meta.client) return

    document.documentElement.setAttribute(
      'data-theme',
      theme.value,
    )
  }

  function initTheme() {
    if (!import.meta.client || initialized.value) {
      return
    }

    const storedTheme = localStorage.getItem(
      'mentalme_theme',
    )

    if (
      storedTheme === 'light'
      || storedTheme === 'dark'
    ) {
      theme.value = storedTheme
    } else {
      const prefersDark = window.matchMedia(
        '(prefers-color-scheme: dark)',
      ).matches

      theme.value = prefersDark ? 'dark' : 'light'
    }

    applyTheme()
    initialized.value = true
  }

  function setTheme(value) {
    if (
      value !== 'light'
      && value !== 'dark'
    ) {
      return
    }

    theme.value = value

    if (import.meta.client) {
      localStorage.setItem(
        'mentalme_theme',
        value,
      )
    }

    applyTheme()
  }

  function toggleTheme() {
    setTheme(
      isDark.value ? 'light' : 'dark',
    )
  }

  function openSidebar() {
    sidebarOpen.value = true
  }

  function closeSidebar() {
    sidebarOpen.value = false
  }

  function toggleSidebar() {
    sidebarOpen.value = !sidebarOpen.value
  }

  return {
    theme,
    initialized,
    isDark,

    sidebarOpen,

    initTheme,
    setTheme,
    toggleTheme,

    openSidebar,
    closeSidebar,
    toggleSidebar,
  }
})