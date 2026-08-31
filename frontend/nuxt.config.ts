// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  modules: [
    '@pinia/nuxt',
    '@nuxt/icon',
  ],
  icon: {
    serverBundle: {
      collections: [
        'lucide',
      ],
    },

    clientBundle: {
    scan: true,
    sizeLimitKb: 512,
    icons: [
      'lucide:bell',
      'lucide:brain-circuit',
      'lucide:chevron-down',
      'lucide:clipboard-list',
      'lucide:file-text',
      'lucide:key-round',
      'lucide:layout-dashboard',
      'lucide:log-out',
      'lucide:menu',
      'lucide:moon',
      'lucide:route',
      'lucide:shield-check',
      'lucide:sun',
      'lucide:users',
      'lucide:workflow',
    ],
  },
  },
  vite: {
    plugins: [tailwindcss() as any],
  },
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBase:
        process.env.NUXT_PUBLIC_API_BASE
        || 'http://localhost:8000',
      siteUrl:
        process.env.NUXT_PUBLIC_SITE_URL
        || 'http://localhost:3000',
    },
  },
  app: {
    head: {
      title: 'MentalMe',
      meta: [
        {
          charset: 'utf-8',
        },
        {
          name: 'viewport',
          content:
            'width=device-width, initial-scale=1, viewport-fit=cover',
        },
        {
          name: 'description',
          content: 'MentalMe — сервис сопровождения пациентов',
        },
        {
          name: 'theme-color',
          content: '#ffffff',
        },
      ],
    },
  },
})