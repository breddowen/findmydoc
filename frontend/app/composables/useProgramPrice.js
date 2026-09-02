// ./frontend/app/composables/useProgramPrice.js
export function useProgramPrice() {
  function resolveService(source) {
    if (!source) return null

    // Если передана программа, цена находится
    // внутри связанной услуги.
    if (
      Object.prototype.hasOwnProperty.call(
        source,
        'service',
      )
    ) {
      return source.service
    }

    // Это позволяет использовать composable
    // непосредственно в конструкторе услуг.
    return source
  }

  function getCurrencySuffix(currency) {
    if (currency === 'RUB') {
      return '₽'
    }

    if (currency === 'UNIT') {
      return 'у. е.'
    }

    return ''
  }

  function getPriceKind(source) {
    const service = resolveService(source)

    if (!service) {
      return 'free'
    }

    if (
      service.price_amount === null
      || service.price_amount === undefined
    ) {
      return 'request'
    }

    if (Number(service.price_amount) === 0) {
      return 'free'
    }

    return 'paid'
  }

  function getDiscountedPrice(source) {
    const service = resolveService(source)

    if (
      !service
      || service.price_amount === null
      || service.price_amount === undefined
    ) {
      return null
    }

    // Предпочитаем рассчитанную backend-ом цену.
    if (
      service.final_price_amount !== null
      && service.final_price_amount !== undefined
    ) {
      return Number(service.final_price_amount)
    }

    const price = Number(service.price_amount)
    const discount = Number(
      service.discount_percent || 0,
    )

    return Math.max(
      price * (1 - discount / 100),
      0,
    )
  }

  function hasDiscount(source) {
    const service = resolveService(source)

    return (
      getPriceKind(source) === 'paid'
      && Number(service?.discount_percent || 0) > 0
    )
  }

  function formatAmount(amount, currency) {
    if (
      amount === null
      || amount === undefined
      || Number.isNaN(Number(amount))
    ) {
      return '—'
    }

    const formatted = new Intl.NumberFormat(
      'ru-RU',
      {
        maximumFractionDigits: 2,
      },
    ).format(Number(amount))

    const suffix = getCurrencySuffix(currency)

    return suffix
      ? `${formatted} ${suffix}`
      : formatted
  }

  function formatOriginalPrice(source) {
    const kind = getPriceKind(source)

    if (kind === 'free') {
      return 'Бесплатно'
    }

    if (kind === 'request') {
      return 'Цена по запросу'
    }

    const service = resolveService(source)

    return formatAmount(
      service.price_amount,
      service.currency,
    )
  }

  function formatFinalPrice(source) {
    const kind = getPriceKind(source)

    if (kind === 'free') {
      return 'Бесплатно'
    }

    if (kind === 'request') {
      return 'Цена по запросу'
    }

    const service = resolveService(source)

    return formatAmount(
      getDiscountedPrice(source),
      service.currency,
    )
  }

  function getPurchaseActionLabel(source) {
    const kind = getPriceKind(source)

    if (kind === 'request') {
      return 'Узнать стоимость'
    }

    if (kind === 'free') {
      return 'Запросить полный доступ'
    }

    return 'Купить программу'
  }

  return {
    resolveService,
    getCurrencySuffix,
    getPriceKind,
    getDiscountedPrice,
    hasDiscount,
    formatAmount,
    formatOriginalPrice,
    formatFinalPrice,
    getPurchaseActionLabel,
  }
}