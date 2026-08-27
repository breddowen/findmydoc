// ./frontend/app/composables/useProgramPrice.js
export function useProgramPrice() {
  function getCurrencySuffix(currency) {
    return currency === 'RUB'
      ? '₽'
      : 'у. е.'
  }

  function getDiscountedPrice(program) {
    if (program.price_amount === null) {
      return null
    }

    const price = Number(program.price_amount)
    const discount = Number(
      program.discount_percent || 0,
    )

    return Math.max(
      price * (1 - discount / 100),
      0,
    )
  }

  function formatAmount(
    amount,
    currency,
  ) {
    if (amount === null) {
      return 'Бесплатно'
    }

    const formatted = new Intl.NumberFormat(
      'ru-RU',
      {
        maximumFractionDigits: 2,
      },
    ).format(amount)

    return `${formatted} ${getCurrencySuffix(currency)}`
  }

  function formatOriginalPrice(program) {
    if (program.price_amount === null) {
      return 'Бесплатно'
    }

    return formatAmount(
      Number(program.price_amount),
      program.currency,
    )
  }

  function formatFinalPrice(program) {
    return formatAmount(
      getDiscountedPrice(program),
      program.currency,
    )
  }

  return {
    getDiscountedPrice,
    formatAmount,
    formatOriginalPrice,
    formatFinalPrice,
  }
}