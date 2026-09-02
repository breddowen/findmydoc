// ./frontend/app/composables/useAppNavigation.js
export function useAppNavigation() {
  const auth = useAuthStore()
  const { isClientReady } = useClientReady()

  const roleNames = {
    superuser: 'Суперпользователь',
    med_assistant: 'Медицинский ассистент',
    doctor: 'Врач',
    patient: 'Пациент',
    relative: 'Родственник',
  }

  const isStaff = computed(() =>
    isClientReady.value
    && [
      'doctor',
      'med_assistant',
      'superuser',
    ].includes(auth.activeRole),
  )

  const canManage = computed(() =>
    isClientReady.value
    && [
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole),
  )

  const activeRoleName = computed(() => {
    if (!isClientReady.value) {
      return ''
    }

    return (
      roleNames[auth.activeRole]
      || auth.activeRole
      || ''
    )
  })

  const navigationGroups = computed(() => {
    if (!isClientReady.value) {
      return []
    }

    const mainLinks = [
      {
        to: '/dashboard',
        label: 'Главная',
        icon: 'lucide:layout-dashboard',
        description: 'Обзор и последние действия',
      },
    ]

    if (isStaff.value) {
      mainLinks.push({
        to: '/patients',
        label: 'Пациенты',
        icon: 'lucide:users',
        description: 'Список и карточки пациентов',
      })
    }

    if (canManage.value) {
      mainLinks.push({
        to: '/users',
        label: 'Пользователи',
        icon: 'lucide:user-cog',
        description: 'Аккаунты и приглашения',
      })
    }

    const contentLinks = [
      {
        to: '/content/articles',
        label: 'Статьи',
        icon: 'lucide:file-text',
        description: 'Материалы для пользователей',
      },
      {
        to: '/programs',
        label: 'Программы',
        icon: 'lucide:route',
        description: 'Программы сопровождения',
      },
    ]

    if (auth.activeRole === 'patient') {
      contentLinks.push({
        to: '/questionnaires',
        label: 'Опросники',
        icon: 'lucide:clipboard-list',
        description: 'Назначенные опросники',
      })
    }

    if (canManage.value) {
      contentLinks.push({
        to: '/content/questionnaires',
        label: 'Опросники',
        icon: 'lucide:clipboard-list',
        description: 'Редактор опросников',
      })
    }

    const groups = [
      {
        key: 'main',
        label: 'Работа',
        icon: 'lucide:briefcase',
        links: mainLinks,
      },
      {
        key: 'content',
        label: 'Контент',
        icon: 'lucide:files',
        links: contentLinks,
      },
    ]

    if (canManage.value) {
      groups.push({
        key: 'management',
        label: 'Управление',
        icon: 'lucide:settings-2',
        links: [
          {
            to: '/programs/new',
            label: 'Конфигуратор',
            icon: 'lucide:workflow',
            description: 'Создание программ',
            exact: true,
          },
          {
            to: '/services',
            label: 'Услуги',
            icon: 'lucide:badge-russian-ruble',
            description: 'Цены, скидки и коды услуг',
          },
          {
            to: '/settings/directories',
            label: 'Справочники',
            icon: 'lucide:library',
            description: 'Специальности и теги',
          },
        ],
      })
    }

    const settingsLinks = [
      {
        to: '/settings/profile',
        label: 'Личные данные',
        icon: 'lucide:user-round',
        description: 'ФИО и данные аккаунта',
      },
    ]

    if (auth.activeRole === 'doctor') {
      settingsLinks.push({
        to: '/settings/tags',
        label: 'Мои теги',
        icon: 'lucide:tags',
        description: 'Индивидуальные настройки тегов',
      })
    }

    settingsLinks.push({
      to: '/settings/security',
      label: 'Безопасность',
      icon: 'lucide:shield-check',
      description: 'Пароль и passkey',
    })

    groups.push({
      key: 'settings',
      label: 'Настройки',
      icon: 'lucide:settings',
      links: settingsLinks,
    })

    return groups
  })

  return {
    isStaff,
    canManage,
    activeRoleName,
    navigationGroups,
  }
}