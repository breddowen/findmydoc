// ./frontend/app/stores/emc-app.js
export const useEmcAppStore = defineStore(
  'emc-app',
  () => {
    const doctors = ref([
      {
        id: 'demo-psychiatrist',
        fullName: 'Мовина Лариса Георгиевна',
        speciality: 'Психиатр',
        initials: 'ЛГ',
        clinic: 'EMC',
        address: 'Щепкина, 35',
        isDemo: true,
      },
      {
        id: 'demo-addiction-specialist',
        fullName: 'Титков Максим Сергеевич',
        speciality: 'Специалист по аддикциям',
        initials: 'МТ',
        clinic: 'EMC',
        address: 'Щепкина, 35',
        isDemo: true,
      },
    ])

    const nearestDays = ref([])

    function refreshDemoDays() {
      const formatter = new Intl.DateTimeFormat(
        'ru-RU',
        {
          day: 'numeric',
          month: 'long',
        },
      )

      const today = new Date()

      nearestDays.value = [1, 2].map(offset => {
        const date = new Date(
          today.getFullYear(),
          today.getMonth(),
          today.getDate() + offset,
          12,
        )

        return {
          id: `demo-day-${offset}`,
          label: offset === 1 ? 'Завтра' : 'Послезавтра',
          dateLabel: formatter.format(date),
        }
      })
    }

    return {
      doctors,
      nearestDays,
      refreshDemoDays,
    }
  },
)