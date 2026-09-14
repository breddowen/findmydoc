// ./frontend/app/composables/usePatientProgramGroups.js

export function usePatientProgramGroups(
  programsSource,
  aspectsSource,
) {
  function comparePrograms(left, right) {
    const priorityDifference =
      (Number(right.home_priority) || 0)
      - (Number(left.home_priority) || 0)

    if (priorityDifference) {
      return priorityDifference
    }

    return String(left.title || '').localeCompare(
      String(right.title || ''),
      'ru',
      { sensitivity: 'base' },
    ) || String(left.id).localeCompare(String(right.id))
  }

  const orderedPrograms = computed(() =>
    [...(toValue(programsSource) || [])].sort(
      comparePrograms,
    ),
  )

  const recommendedPrograms = computed(() =>
    orderedPrograms.value.filter(
      program => program.is_recommended === true,
    ),
  )

  const otherPrograms = computed(() =>
    orderedPrograms.value.filter(
      program => program.is_recommended !== true,
    ),
  )

  const groupedAspects = computed(() => {
    const otherProgramsById = new Map(
      otherPrograms.value.map(program => [
        program.id,
        program,
      ]),
    )

    return [...(toValue(aspectsSource) || [])]
      .sort(
        (left, right) =>
          left.order_index - right.order_index
          || left.name.localeCompare(right.name, 'ru')
          || left.id.localeCompare(right.id),
      )
      .map(aspect => ({
        ...aspect,

        // Берём полные данные программы:
        // услугу, доступ, прогресс и участие.
        programs: [
          ...new Set(
            (aspect.programs || []).map(
              program => program.id,
            ),
          ),
        ]
          .map(id => otherProgramsById.get(id))
          .filter(Boolean)
          .sort(comparePrograms),
      }))
      .filter(aspect => aspect.programs.length > 0)
  })

  const unclassifiedPrograms = computed(() => {
    const groupedIds = new Set(
      groupedAspects.value.flatMap(
        aspect => aspect.programs.map(
          program => program.id,
        ),
      ),
    )

    return otherPrograms.value.filter(
      program => !groupedIds.has(program.id),
    )
  })

  return {
    recommendedPrograms,
    groupedAspects,
    unclassifiedPrograms,
  }
}