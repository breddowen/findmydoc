// ./frontend/app/stores/ui.js
export const useUiStore = defineStore('ui', () => {
  const theme = ref('light')
  const initialized = ref(false)

  const sidebarInitialized = ref(false)
  const isDesktopViewport = ref(false)

  // Сохраняем только предпочтение для компьютера.
  const desktopSidebarOpen = ref(false)

  // Мобильное состояние всегда временное.
  const mobileSidebarOpen = ref(false)

  let desktopMediaQuery = null

  const isDark = computed(
    () => theme.value === 'dark',
  )

  const sidebarOpen = computed({
    get() {
      return isDesktopViewport.value
        ? desktopSidebarOpen.value
        : mobileSidebarOpen.value
    },

    set(value) {
      setSidebarOpen(value)
    },
  })

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

      theme.value = prefersDark
        ? 'dark'
        : 'light'
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

  function persistDesktopSidebar() {
    if (!import.meta.client) return

    localStorage.setItem(
      'mentalme_sidebar_open',
      desktopSidebarOpen.value
        ? '1'
        : '0',
    )
  }

  function handleViewportChange(event) {
    isDesktopViewport.value = event.matches

    // Мобильное меню никогда не открывается
    // автоматически при изменении ширины окна.
    mobileSidebarOpen.value = false
  }

  function initSidebar() {
    if (
      !import.meta.client
      || sidebarInitialized.value
    ) {
      return
    }

    desktopMediaQuery = window.matchMedia(
      '(min-width: 1024px)',
    )

    isDesktopViewport.value =
      desktopMediaQuery.matches

    desktopSidebarOpen.value =
      localStorage.getItem(
        'mentalme_sidebar_open',
      ) === '1'

    // На телефоне sidebar после перезагрузки закрыт,
    // независимо от desktop-предпочтения.
    mobileSidebarOpen.value = false

    desktopMediaQuery.addEventListener(
      'change',
      handleViewportChange,
    )

    sidebarInitialized.value = true
  }

  function setSidebarOpen(value) {
    const normalized = Boolean(value)

    if (isDesktopViewport.value) {
      desktopSidebarOpen.value = normalized
      persistDesktopSidebar()
      return
    }

    mobileSidebarOpen.value = normalized
  }

  function openSidebar() {
    setSidebarOpen(true)
  }

  function closeSidebar() {
    setSidebarOpen(false)
  }

  function closeMobileSidebar() {
    mobileSidebarOpen.value = false
  }

  function toggleSidebar() {
    setSidebarOpen(!sidebarOpen.value)
  }

  return {
    theme,
    initialized,
    isDark,

    sidebarInitialized,
    isDesktopViewport,
    sidebarOpen,

    initTheme,
    setTheme,
    toggleTheme,

    initSidebar,
    setSidebarOpen,
    openSidebar,
    closeSidebar,
    closeMobileSidebar,
    toggleSidebar,
  }
})