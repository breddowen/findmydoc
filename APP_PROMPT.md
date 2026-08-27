Надо сделать приложение для работы с пациентом в основном в психотерапевтическом ключе.
Роли: Superuser, Patient, Doctor, Relative, Med_assistant

---
ПОЛЬЗОВАТЕЛИ и сущности:

--
Doctor:
Имя: необязательный парам
Пол: необязательный парам
Специальность: обязательное поле. Но давай его сделаем не в виде enum, а в виде отдельной сущености в базе
email: обязательное поле для врача

Superuser и Med_assistant могут добавлять врача также через ссылку, как врач может добавлять пациентов. При этом, при создании ссылки вводят почту, специальность и ФИО. Врач потом может изменить ФИО, специальность или почту. Аккаунт может восстановить с подтверждением (пока письмо со ссылкой на восстановление почты "отправляется" в консоль)

При создании врача, он наследует теги специальности, например: Неврология содержит теги Мигрень, Инсульт, и т.д., психиатр: Тревога, Депрессия, ...., Кардиолог: также Тревога, Гипертензия, и т.д.
Но Врач индивидуально может себе изменить теги: удалить или добавить и кастомизированные теги имеют приоритет над дефолтными

Врач может добавлять пациента (потом на фронтенде он будет нажимать на кнопку и там будет открываться qr код или кнопка копировать ссылку) и пациент регистрируется. При регистрации пациент автоматически наследует теги врача.
Врач заполняет обязатлеьные поля: record_id и email. Тогда пациент при заходе видит свою почту и record_id. Почту он может при желании изменить и вбить пароль с проверкой пароля и сразу же заходит в аккаунт, но у него будет писаться, что аккаунт необходимо активировать, ссылка выслана на почту. Пока не делаем никаких ограничений для пациентов, которые не подтвердили аккаунт. Просто, на фронтенде сделаем яркий баннер в навбаре с кнопкой Отправить ссылку повторно, если предыдущая уже протухла.
Также врач может сам при формировании сслыки заполнить необязательное поле ФИО у пациента и/или дату рождения, пол и пациент при первичной регистрации будет в окне регистрации видеть эти данные и сможет менять их при желании (кроме record_id).

Если другой врач также хочет привязать пациента, который уже зарегистрирован, он также вводит номер карты пациента, нажимает сформировать ссылку, но там будет окно с надписью: пациент уже зарегистрирован, добавить его? И тогда если врач нажимает ок, пациент к нему привязывается и наследует его теги.

Теги добавленного врача также добавляются к пациенту (разумеется, без дублей, например у кардиолога и психиатра есть тег тревога, соответственно, у пациента тревога будет один раз)

Врач у себя может отвязать пациента и тогда пациент перестает видеть этого врача и теги будут отвязываться
Теги нужны для фильтрации контента

СПЕЦИАЛЬНОСТЬ: 
Название: обязательный парам
Описание: необязательный парам
Теги(необязательный парам): каждый тег тоже отдельная сущность

ТЕГ:
название: обязательный
описание: необязательный парам
--
Patient:
record_id: обязательное и основное поле - это id электронной карты пациента. Врач при формировании ссылки обязательно должен ввести record_id пациента. Если пациент уже зарегистрирован в системе, врач должен видеть об этом оповещение после нажатие на Сформировать ссылку и подтвердить, что он хочет добавиться к пациенту
email: необязательное поле
fullname: необязатлеьное поле
dob: необязательное поле
---
Relative: 
Родстенник пациента. Родстенник может быть у нескольких пациентов. Один пациент может иметь несколько родственников. Пока что, я не придумал, как лучше задействовать родственника в работе пациента. Пусть пока что будет базовый функционал, чтобы я потом доделал.
врач может привязывать родственника к конкретному пациенту. Пациент может привязывать родственника к себе, создавая ссылку. Пациент или врач могут отвязать родственника. Пока что родственник просто может видеть список людей, к которым он привязан. Ну, можно сделать степень родства. Теги родстеник наследует от пациента, но также к нему добавляется тег relative. 
Есть проблема: допустим, родственник решил стать пациентом. Давай сделаем так, чтобы если врач регистрирует пациента, который является родственником, родственник регистрируется как обычно, но 
---
Med_assistant:
Имеет те же права, что и superuse, кроме возможности удаления аккаунтов. Блокировать аккаунты ассистент может.

-----------
ARTICLE:
title
content
теги: по ним будет фильтроваться контент для пациентов 
также, пусть тут будет переключатель , он по умолчанию будет активен. Если он активен, то статья будет недоступна до тех пор, пока врач/медицинский ассистент или суперпольователь не нажал у пациента переключатлеь pro

QUESTIONNAIRE:
опросник с разными типами вопросов. Желательно, чтобы в одном опроснике можно было вводить несколько типов вопросов, например шкалы от ... до ..., один из, множество, и т.д.
title
description
теги для фильтрации
pro_content

PROGRAM:
Программа вмещает в себя наборы опросников и статей. И внутри они должны делиться на этапы. Например, я могу сделать программу для SMART Recovery. Впервый этап я укажу в интервале 0-7 дней. там будут материалы из статей и опросников, которые пациент заполняет в течение недели (пациент на фронтенде будет видеть этапы разделенные по времени. пока пациент не выполнил текущий этап, он не может приступать к следующему этапу). Следующий этап 8-10 дней, и так далее.
title
description
теги для фильтрации
pro_content тут пусть будет false

pro_content нужен для того, чтобы пациент, который еще не заказывал, мог посмотреть первые n статей/опросников и понять, в чем продукт и стоит ли его покупать

PRODUCT:
это уже платная программа, которую выбирает пациент. платная программа включает в себя комплект консультаций разных специалистов, например, пациент с тревогой и дискомфортом в животе может купить продукт с пакетом консультаций психиатра, психотерапевта, гастроэнтеролога, проктолога (анализы и исследования не вклдючены), плюс там может быть одна или несколько PROGRAM
Допустим мы делаем стартовый продукт для пациентов с алкогольной зависимостью. Туда входит набор из 10 консультаций врача психиатра, 2 консультации психотерапевта, программа по SMART recoverty, 1 консультация гастроэнетеролога-гепатолога, ну ты понял
Пациент может нажать на PRODUCT и познакомиться с контентом там, который pro_content false

PRODUCT поля:
name
description
price: пусть тут будет руб и у.е.
собственно, количество консультиаций и специальность
программы, которяе входят в продукт

Еще раз:
Статья и опросник - элементарные строительные блоки
Программа состоит из этапов. Каждый этап содержит период дней, в течение которого его нужно выполнить. Внутри этапа произвольное количество статей и опросникуов. Выполнение этапа - это чтение статей, заполение опросников. Прочитанная статья/заполненный опросник регистирируются в Event. Этапы - это условное понятие. Допустим, Этап 1 0-7 дней, а Этап 2 8-14 дней. Пациент что-то не сделал в Этап 1. Этап 2 все равно разблокирвется на 8 день, но в Этапе 1 будут яркими цветами отмечаться то, что он не пройден. 
-------
Теперь отдельно давай сделаем сущность EVENT (как и отдельный модуль). В ней пусть будет записываться конкретно, что и когда пациент выполнил: заполнил опросник/прочитал статью. Ведь, одну статьи и один опросник один и тот же пациент может прочитаь/заполнить несколько раз. Врач/суперпользователь/ассистент может видеть в админке, например, внутри пациента то, что он закончил. Ну, там, например, будет типа Программа -> заходим внутрь -> видим выполненные блоки, например статью и сколько раз прочитана. Короче, смысл в том, что нам надо понимать, что пациент работает с контентом и не пропускает его, чтобы на консультациях работать с возражениями или прокрастинацией.

events надо сделать гибко, чтобы можно было в каком-то месте добавлять какие-то функции и event записывался, но если эти функции убрать, то event перестанет записываться. Я не знаю, кду лучше добавить регистрацию событий, на фронтенд или на бекенд. Предложи.
----
Также, надо сделать возможность логина через passkey. Пусть в настройках будет функционал для добавления passkey у любого пользователя. елси passkey на данном устройстве нет, пусть в навбаре предлагается это сделать.
----
Все пользователи могут менять логин/пароль и почту, им должна приходить ссылка на почту. Пока сделай заглушку пока без почтового сервера, пусть пишет ссылку как будто это письмо в консоль
---
Все id uuid
-----------------------------
СПЕЦИФИКА БЕКЕНДА
Структура директорий:
 База пока на sqlite, файл базы хранится в ./backend/test_database.db, само приложение с main.py лежит в ./backend/app
в ./backend/app/modules/ лежат папки каждой сущности, например:
./backend/app/modules/users содержит: models.py - с моделями, enums.py - с видами ролей (и еще чем-то, если надо), utils.py - со служебными функциями, routers.py - с роутами, schemas.py - схемы
Затем роуты из всех модулей импортируются в main.py
./app/core содержит служебные файлы: db.py, security.py с функциями для Depends, config.py - где будет settings брать переменые из ./app/.env или по дефолту

Думаю, .env будет таким, но если надо, добавь поля:
```env
# ./backend/app/.env
DATABASE_URL=sqlite:///./test_database.db
SECRET_KEY=your-super-secret-key-change-in-production-123456789
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
FRONTEND_URL=http://localhost:3000
```

Соответственно, config такой:
```python
# ./backend/app/core/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test_database.db"
    SECRET_KEY: str = "your-super-secret-key-change-in-production-123456789"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    FRONTEND_URL: str = "http://localhost:3000"
    
    class Config:
        env_file = "./backend/app/.env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
```

Пожалуйста, на самой первой строке каждого файла пиши в комментариях его относительный путь, например: # ./app/core/config.py
Все id UUID

Пример моделей sqlmodels из другого проекта:
# ./backend/app/modules/users/models.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
import uuid

from .enums import UserRole, Gender, AgeGroup, OnboardingStatus

# Для избежания циклических импортов
if TYPE_CHECKING:
    from .models import DoctorProfile, PatientProfile


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    uid: str = Field(default_factory=lambda: str(uuid.uuid4()), unique=True, index=True)
    email: Optional[str] = Field(default=None, unique=True, index=True)
    hashed_password: Optional[str] = None
    
    role: UserRole = Field(default=UserRole.PATIENT)
    
    # Общие данные
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[Gender] = None
    
    # Статусы
    is_active: bool = True
    
    # Временные метки
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships - указываем foreign_keys явно
    doctor_profile: Optional["DoctorProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"foreign_keys": "DoctorProfile.user_id"}
    )
    patient_profile: Optional["PatientProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"foreign_keys": "PatientProfile.user_id"}
    )


class DoctorProfile(SQLModel, table=True):
    __tablename__ = "doctor_profiles"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True)
    
    # Специальность
    speciality_code: str = Field(index=True)
    speciality_name: str
    
    # Место работы
    
    # Статистика
    patients_referred: int = Field(default=0)
    patients_converted: int = Field(default=0)
    
    # Глубина заполнения профиля
    profile_depth: float = Field(default=0.0)
    profile_entropy: float = Field(default=1.0)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship
    user: Optional[User] = Relationship(
        back_populates="doctor_profile",
        sa_relationship_kwargs={"foreign_keys": "[DoctorProfile.user_id]"}
    )


class PatientProfile(SQLModel, table=True):
    __tablename__ = "patient_profiles"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", unique=True)
    
    # Врач, который направил (отдельный FK, НЕ используется для relationship с User)
    referred_by_doctor_id: Optional[int] = Field(default=None, foreign_key="users.id")
    referral_token: Optional[str] = Field(default=None, unique=True, index=True)
    
    # Статус направления к психиатру
    psychiatrist_visited: bool = Field(default=False)
    psychiatrist_visit_date: Optional[datetime] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship - явно указываем какой FK использовать
    user: Optional[User] = Relationship(
        back_populates="patient_profile",
        sa_relationship_kwargs={"foreign_keys": "[PatientProfile.user_id]"}
    )


class ReferralLink(SQLModel, table=True):
    """Ссылки для направления пациентов"""
    __tablename__ = "referral_links"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    token: str = Field(unique=True, index=True)
    doctor_id: int = Field(foreign_key="users.id")
    
    # Опциональные метаданные о пациенте
    patient_gender_hint: Optional[Gender] = None
    patient_age_hint: Optional[int] = None
    primary_complaint_hint: Optional[str] = None
    
    is_used: bool = Field(default=False)
    used_by_patient_id: Optional[int] = Field(default=None, foreign_key="users.id")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None

но ты можешь делать любые модели, главное тут поле Relationship , потому что по-другому выдает ошибки

В # ./backend/app/core/db.py сделай так, чтобы если файл базы отсутствует, он создавался заново, например:
def init_sqlite_db():
    """
    Инициализация SQLite базы данных.
    Если файл БД уже существует, создаются только недостающие таблицы.
    """
    db_path = get_db_path()
    
    if os.path.exists(db_path):
        print(f"📁 Database file already exists: {db_path}")
        print("   Checking for missing tables...")
        # create_all создаст только недостающие таблицы
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Tables synchronized")
    else:
        print(f"📁 Creating new database: {db_path}")
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Database created")

---

в localhost:8000/docs сделай так, чтобы я удобно мог вводить пароль, а не копировал с эндпоинта login jwt токен

Каждый файл python начиная с # относительный путь файла, например: # ./backend/app/modules/users/models.py

разумеется, везде, где надо, функции надо делать асинхронными
Сами запросы к базе пусть будут обычными

Я веду разработку на windows, vscode

Очень прошу, пусть __init__.py будут пустыми и будет традиционный импорт. Никак не могу привыкнуть к такому:

# ./backend/app/core/email/__init__.py
from .service import email_service

__all__ = ["email_service"]

а потом непонятно как импортировать

--------------------------------------
СПЕЦИФИКА ФРОНТЕНДА:
Фронтед на nuxt4, pinia store, tailwinds, daisyui
tailwinds и daisyui уже подключены так:
Install Tailwind CSS and daisyUI
Terminal
npm install tailwindcss@latest @tailwindcss/vite@latest daisyui@latest
Add Tailwind CSS to Vite config

nuxt.config.ts
import tailwindcss from "@tailwindcss/vite";
export default defineNuxtConfig({
  vite: {
    plugins: [tailwindcss() as any],
  },
  css: ['~/assets/css/main.css'],
});
Put Tailwind CSS and daisyUI in your CSS file (and remove old styles)

app/assets/css/main.css
@import "tailwindcss";
@plugin "daisyui";
----
В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

если какие-то компоненты общие и относятся к ui, располагай их в ./fronted/app/components/ui/

старайся делить на логические составляющие, например если ./fronted/app/components/doctors/patients/list.vue, то сделай ./fronted/app/components/doctors/patients/item.vue, тогда внутри компонента DoctorsPatientsList будет компонент DoctorsPatientsItem, ну ты понял

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api. Пример:
// stores/user.js
export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const doctorProfile = ref(null)
  const patientProfile = ref(null)
  const loading = ref(false)

  const fullName = computed(() => {
    if (!user.value) return ''
    const { first_name, last_name } = user.value
    return [first_name, last_name].filter(Boolean).join(' ') || 'Пользователь'
  })

  const isOnboardingComplete = computed(() => {
    return user.value?.onboarding_status === 'completed'
  })

  async function fetchMe() {
    const { $api } = useNuxtApp()
    loading.value = true
    try {
      user.value = await $api('api/v1/users/me')
      return user.value
    } finally {
      loading.value = false
    }
  }

  async function fetchDoctorProfile() {
    const { $api } = useNuxtApp()
    loading.value = true
    try {
      doctorProfile.value = await $api('api/v1/users/me/doctor-profile')
      return doctorProfile.value
    } finally {
      loading.value = false
    }
  }

  async function fetchPatientProfile() {
    const { $api } = useNuxtApp()
    loading.value = true
    try {
      patientProfile.value = await $api('api/v1/users/me/patient-profile')
      return patientProfile.value
    } finally {
      loading.value = false
    }
  }

...
  return {
    user,
    doctorProfile,
    patientProfile,
    loading,
...
    fetchMe,
    fetchDoctorProfile,
    fetchPatientProfile,
...
  }
})

// middleware/auth.global.js
// Глобальный middleware - проверяет авторизацию на всех страницах
const publicPaths = ['/', '/login', '/register', '/register/patient']

export default defineNuxtRouteMiddleware((to) => {
  // Только на клиенте
  if (process.server) return

  const auth = useAuthStore()
  
  // Инициализация из localStorage
  if (!auth.isInitialized) {
    auth.initFromStorage()
  }

  // Проверяем публичные пути
  const isPublic = publicPaths.some(p => {
    if (p === '/') return to.path === '/'
    return to.path.startsWith(p)
  })
  
  if (isPublic) {
    // Если авторизован и на странице логина/регистрации - редирект
    if (auth.isAuthenticated && (to.path === '/login' || to.path === '/register')) {
      return navigateTo('/dashboard')
    }
    return
  }

  // Защищённые маршруты - проверяем авторизацию
  if (!auth.isAuthenticated) {
    return navigateTo(`/login?redirect=${encodeURIComponent(to.fullPath)}`)
  }
})

для этого middleware, не надо на страницах делать  definePageMeta({ 
  middleware: ['default'],
}), потому что он и так подгрузится. А для остальных middleware это надо указывать

nuxt.config.ts должен быть примерно таким:

export default defineNuxtConfig({
  devtools: { enabled: false },
  ssr: false,
  
  modules: [
    '@pinia/nuxt',
    '@nuxt/icon',
  ],

  vite: {
    plugins: [tailwindcss() as any],
  },
  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'http://localhost:3000',
    },
  },

  app: {
    head: {
      title: 'MentalMe',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'называпние проекта' },
      ],
    },
  },

})

Если тебе для создания нужно посмотреть какой-то файл бекенда, не придумывай код, попроси прислать файл или список файлов и жди их перед написанием фронтенда

в коде надо, чтобы был такой порядок:
<script setup></script>
<template></template>
<style></style> - если нужно

не забывай оборачивать код, чтобы я мог его легко скопировать

Для логина делаем отдельный layout

для хранения состояний ui, пусть будет отдельный store ui.js

Например, давай сразу сделаем в самом верху небольшую кнопку переключения темной/светлой темы:
<label class="swap swap-rotate">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" />

  <!-- sun icon -->
  <svg
    class="swap-on h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
  </svg>

  <!-- moon icon -->
  <svg
    class="swap-off h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
  </svg>
</label>

только вот это <path
      d="M21. ...

замени на @nuxt/icon

в документации к daisyui указан такой способ смены тем:
How to use daisyUI themes?

daisyUI comes with 35 built-in themes that instantly transform your website's entire look - a time-saver that lets you focus on building rather than deciding on colors.
You can also create your own custom themes or customize built-in themes.

You can manage themes by adding brackets in front of @plugin "daisyui" in your CSS file.

main.css
  @import "tailwindcss";
 @plugin "daisyui";
 @plugin "daisyui" {
   themes: light --default, dark --prefersdark;
 }
themes is a comma-separated list of theme names you want to enable.
You can set --default flag for a theme to make it the default theme.
You can also set --prefersdark flag for a theme to make it the default theme for dark mode (prefers-color-scheme: dark).

ui должен быть адаптивным  и удобным как для pc, так и для мобильных телефонов

-----------
План работы:
1. Сначала задай дополнительные вопросы по сервису, если они есть.
2. Будем делать поэтапно: сначала базовые вещи: логин, пароль, passkey, пользователи на бекенде, на фронтенде делаем соответственно, логин/пароль, регистрацию, чтобы я мог сайт создавать постеменно и сразу тестировать. При создании, надо сделать ./backend/seed/data/users.json и ./backend/seed/upload_users.py, чтобы после создания бекенда можно было подгрузить тестовые данные. Почта будет домен у всех example.com, у врачей будет: doctor1@example.com, doctor2@example.com, и т.д. У пациентов будет patient1@example.com, и т.д. суперпользоватлеь пока один: superuser@example.com, медассистент сделай пока одного, но с индексом: medassistant1@example.com. У всех пароль secret















































------------------------
1. Один пользователь может иметь несколько ролей? Смотри... допустим, пациент еще зареган как родственник. Тогда, он при логине будет выбирать, в качествен кого он заходит: пациента или родстенника. Ну да, это многоуровневая модель. но, чтобы не усложнять интерфейс, давай сделаем выбор роли при логине
2. Как пользователи регистрируются самостоятельно? Да, публичной регистрации пока нет
3. Email пациента: обязательный или необязательный? email обязатлеьный. Это я там ошибся.
4. Уникальность record_id: да, номер карты обязатлеьный. Клиника одна. не надо делать несколько клиник
5. Привязка существующего пациента к новому врачу. Давай, как ты предложил: сделаем статусы, но после доавления арча статус сразу будет ACTIVE, минуя PENDING
6. Поведение приглашений: ок. Насчет нескольких приглашений для одного пациента... ну, сделай как проще. это не принципиально
7. Авторизация через JWT: ок
8. Passkey/WebAuthn: если пользователь добавил passkey, то можно входить без email
9. Подтверждение email и изменение email: давай сделаем без изменения email, чтобы не раздувать код. Только восстановление пароля
10. Блокировка и удаление: ок
11. Проект создаётся с нуля? да, с нуля
12. Версии окружения - да, ок
13. Название директории фронтенда: ./frontend
Сколько тестовых врачей и пациентов нужно? - как ты предложил: 2 врача, 2 пациента, один ассистент и один суперпользователь
Какие специальности назначить врачам? - давай терапевт и психиатр
Должны ли seed-пользователи иметь подтверждённый email? ну, давай
Добавлять ли тестового родственника, например relative1@example.com? Давай. пусть будет привязан к первому пациенту

Предложение по EVENT
надо сделать код максимально прозрачным и переисползлованным, потому что я потом захочу еще добавлять какие-то events. Как ты предложил, вроде, нормально.








































------------------------------------
Источники направления: ну, тут главное не перегнуть палку с объемом вводимой информации врачом. Ведь у врача вообще нет времени на заполнение формы пациента. Давай, если направляет не психиатр, это будет KVB_DOCTOR, а если психиатр, то PSYCHIATRY_EXISTING. А ассистент сможет у пациента переставить на чекап или другое постфактум

Канал передачи: блин, давай не будем сейчас это раздувать код MVP проекта. пока будем думать, что канал всегда по ссылке

Почему нужна snapshot-атрибуция - ок

2. Разделение приглашения и направления:
Пациенту создаются назначения:
опросник; статья; при необходимости программа. они будут фильтроваться по тегам, который наследуются от врача. В некоторых случаях, надо, чтобы врач мог редактировать теги пациента, чтобы вручную отфильтровать контент

3. Согласия и предпочтения контакта:
ну, давай сделаем:
PERSONAL_DATA_PROCESSING - согласие на обработку персональных данных - ок, сделай эндпоинт, но на фронтенде подключим потом
MEDICAL_DATA_PROCESSING - аналогично
ASSISTANT_CONTACT - это надо сделать и на фронтенде и на бекенде
ANALYTICS_PROCESSING - это пока  не надо. можешь внести в enums, но пока не используй.

Разрешение на звонок - ок

ой, ну пока эти не надо:
VERBAL_PERMISSION_RECORDED_BY_DOCTOR
PATIENT_CONFIRMED_IN_APPLICATION
PATIENT_REQUESTED_CONTACT

4. Назначения контента: ок, согласен

5. Изменение структуры ProgramStep - да, со всем согласен

6. Интерфейс ассистента: - ок

Предпочтения оплаты - ну ок, давай так... 

Коммерческие возражения - супер
остальные тоже отлично!

Как должен работать выбор - отлично!!!

7. Очередь ассистента - да, класс

8. Опросники и повышенный результат - слушай, так будет очень сложно читать код... Давай сделаем уже созданные опросники неизменяемыми. Но будет кнопка копировать опросник и кнопка скрыть опросник. В этом случае, исправленные опросники будут заполняться как новая версия, а старые просто можно будет рпосматривать внутри пациентов. Вообще, не сильно заморачивайся с версированием, потому что работа с контентом будет проводиться не так активно

Опасный результат - не надо. Врач сам будет оценивать результат

9. События и воронка: 
Обязательные события пилота: убери тут consultation_completed, потому что не думаю, что врач будет отмечать в приложении оконченную консультацию. То, что пациент пришел фактически на консультацию пусть будет возможность у ассистенту отмечать. Вообще, тут надо максимально разгрухить врача, где возможно, потому что предполагается, что это приложение добавит врачу нагрузки

Идемпотентность - умоляю, не заморачивайся сильно на эту тему. это раздует код MVP

Помни, что мы разрабатываем MVP. Приоритет - прозрачность и читаемость кода, модульность, возможность масштабировать, а не разрастание функционала, которым пока можно пожертвовать.

Где создавать события - ок, согласен, но выдели в комментарии, пожалуйста этот момент. И просмотр страницы не на до делать событием, чтобы не раздувать базу данных

Внешняя аналитика - пока вообще не планируется внешняя анализитк,А умоляю, не заморачивайся на эту тему

10. Коммерческий контур: - ок

Платежи и возвраты - ок, но предполагается, что этими моментами управляет ассистент (или суперпользователь) - то есть, выставляет вручную у себя в админке

11. Поэтапная оплата - нет, не надо это делать! Это усложнит и раздует код

12. Интерфейс врача - вкладки - ну ок, только не делай так, чтоыб сильно усложнить код
Врач должен видеть только: - да, ок

13. Дашборд аналитики - ок

число пилотных врачей - вот не надо усложнять пожалуйста. просто число врачей

Прозрачность кода, не мельчи, модульность, переиспользование компонентов, ладно? Если понял, что я имею ввиду, начни писать код. 





























-------------------
отлично! теперь сделаем возможность для пользователей просматривать статьи и проходить опросники, а для врачей просматривать результаты. Плюс, суперпользователь и медицинский ассистент могут просматривать результат любого пользователя. Пусть прочтение статьи будет в % и вычисляться автоматически по скроллам, или как там лучше сделать. Также, хотелось бы, чтобы при чтении статьи в самом верхнем краю экрана был очень узкий индикатор прогресса в виде заполняющейся линии, сколько осталось до конца. Пусть элемент для чтения статьи для пациента и других пользователей будет одним и тем же, но для пациентов там будет триггерить на прочтение, а для остальных просто показывать индикатор чтения. Когда это не пациент, пусть будет небольшая кнопка редактировать в верхнем правом углу экрана. У врача, пусть эта кнопка будет только если врач является автором.
У daisyui есть такой компонент:
<progress class="progress progress-secondary w-56" value="0" max="100"></progress>
<progress class="progress progress-secondary w-56" value="10" max="100"></progress>
<progress class="progress progress-secondary w-56" value="40" max="100"></progress>
<progress class="progress progress-secondary w-56" value="70" max="100"></progress>
<progress class="progress progress-secondary w-56" value="100" max="100"></progress>

но ты сам реши, какой лучше. После 100% пусть это запоминается в event. Пусть там будет кнопка закрыть в виде стандартного креста. Если пользователь на нее нажимает, пусть запоминает текущий процент. Но как сделать расчет процента, если пользователь просто ушел со страницы, я не знаю.

Опросники желательно сделать так, чтобы результат сохранялся после каждого ответа, чтобы если пользователь внезапно выйдет, у него тотом в отдельном разделе будут поросники, которые он не прошел до конца. Ну, врач тоже сможет видеть, что пациент не прошел до конца.

Врач, медицинский ассистент и суперпользователь на самой первой странице должны видеть список пациентов. У каждого пациента в списке пусть будет статус регистрации, дата и время последней активности, если пациент нажал на разрешение с ним связаться, пусть будет трубка телефона зелена, а если не дал разрешения, то перечеркнутая. При нажатии на пациента, можно зайти в details и видеть, что он прошел и прочитал, список врачей, которые к нему привязаны.

переключатели, думаю, сделать типо таких:
<input type="checkbox" checked="checked" class="toggle toggle-primary" />
<input type="checkbox" checked="checked" class="toggle toggle-secondary" />
<input type="checkbox" checked="checked" class="toggle toggle-accent" />
<input type="checkbox" checked="checked" class="toggle toggle-neutral" />

<input type="checkbox" checked="checked" class="toggle toggle-info" />
<input type="checkbox" checked="checked" class="toggle toggle-success" />
<input type="checkbox" checked="checked" class="toggle toggle-warning" />
<input type="checkbox" checked="checked" class="toggle toggle-error" />

Пусть пользователи на главной странице видят спиоск релевантных статей, которые отфильтрованы по тегам. Опросники пусть будут в отдельном разделе.

На мобильных устройствах надо что-то придумать, чтобы улучшить ui для статей и опросников. ну, пусть пока карточки располагаются одна под другой. Потом подумаю, как лучше сделать Я думал типо такого:
<div class="stack">
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 1</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 2</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 3</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
</div>

При загрузке карточек статей и опросников пусть будет skeleton (сделай его в виде отдельного компонента, который можно переиспользовать)
<div class="flex w-52 flex-col gap-4">
  <div class="flex items-center gap-4">
    <div class="skeleton h-16 w-16 shrink-0 rounded-full"></div>
    <div class="flex flex-col gap-4">
      <div class="skeleton h-4 w-20"></div>
      <div class="skeleton h-4 w-28"></div>
    </div>
  </div>
  <div class="skeleton h-32 w-full"></div>
</div>
или
<div class="flex w-52 flex-col gap-4">
  <div class="skeleton h-32 w-full"></div>
  <div class="skeleton h-4 w-28"></div>
  <div class="skeleton h-4 w-full"></div>
  <div class="skeleton h-4 w-full"></div>
</div>
или
<span class="skeleton skeleton-text">AI is thinking harder...</span>

Не забывай делать пагинацию для длинных списков. Скажем, больше 10

сделай элемент footer пока там пусть будет просто информация что-то типа: Разработка - Максим Титков mtitkov@emcmos.ru 2026 год, все права сохранены, или типа того
<footer class="footer sm:footer-horizontal bg-neutral text-neutral-content items-center p-4">
  <aside class="grid-flow-col items-center">
    <svg
      width="36"
      height="36"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p>Copyright © {new Date().getFullYear()} - All right reserved</p>
  </aside>
  <nav class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
      </svg>
    </a>
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
      </svg>
    </a>
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
      </svg>
    </a>
  </nav>
</footer>


-------



































Отлично!
Я там кое что изменил:
def patient_can_see_content(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    is_hidden: bool,
) -> bool:
    if is_hidden:
        return False

    # Контент без тегов считается общим.
    if not content_tag_ids:
        return True

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    return bool(
        patient_tag_ids.intersection(content_tag_ids)
    )
def patient_can_access_content(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    pro_content: bool,
    is_hidden: bool,
) -> bool:
    if not patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=content_tag_ids,
        is_hidden=is_hidden,
    ):
        return False

    if pro_content and not patient.pro_enabled:
        return False

    return True

articles/routers.py
from app.modules.content.utils import (
    ensure_patient_content_access,
    get_patient_profile_by_user_id,
    patient_can_access_content,
    patient_can_see_content,
)
@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    articles = session.exec(
        select(Article).order_by(
            Article.created_at.desc()
        )
    ).all()

    if auth.active_role != UserRole.PATIENT:
        return [
            serialize_article_list_item(
                session=session,
                article=article,
            )
            for article in articles
        ]

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    result: list[ArticleListItem] = []

    for article in articles:
        tag_ids = get_article_tag_ids(
            session=session,
            article_id=article.id,
        )

        # Показываем только подходящие пациенту
        # и нескрытые статьи.
        if not patient_can_see_content(
            session=session,
            patient=patient,
            content_tag_ids=tag_ids,
            is_hidden=article.is_hidden,
        ):
            continue

        # Pro влияет на возможность открыть статью,
        # но не на её присутствие в каталоге.
        can_access = (
            not article.pro_content
            or patient.pro_enabled
        )

        result.append(
            serialize_article_list_item(
                session=session,
                article=article,
                can_access=can_access,
            )
        )

    return result

class ArticleListItem(BaseModel):
    id: uuid.UUID
    title: str

    pro_content: bool
    is_hidden: bool
    can_access: bool = True

    tags: list[ArticleTagResponse]

    created_at: datetime
    updated_at: datetime

def serialize_article_list_item(
    *,
    session: Session,
    article: Article,
    can_access: bool = True,
) -> ArticleListItem:
    full_response = serialize_article(
        session=session,
        article=article,
    )

    return ArticleListItem(
        id=full_response.id,
        title=full_response.title,
        pro_content=full_response.pro_content,
        is_hidden=full_response.is_hidden,
        can_access=can_access,
        tags=full_response.tags,
        created_at=full_response.created_at,
        updated_at=full_response.updated_at,
    )

<!-- ./frontend/app/components/articles/PatientOverview.vue -->
<script setup>
const store = useArticlesStore()

const articles = ref([])
const loading = ref(true)
const errorMessage = ref('')

function canReadArticle(article) {
  return article.can_access !== false
}

function articleAuraClass(article) {
  if (!article.pro_content) {
    return ''
  }

  return canReadArticle(article)
    ? 'aura aura-rainbow'
    : 'aura aura-silver'
}

onMounted(async () => {
  try {
    const response = await store.fetchArticles()

    articles.value = response.slice(0, 6)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить статьи'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="space-y-4">
    <div
      class="flex items-center justify-between gap-4"
    >
      <div>
        <h2 class="text-xl font-bold sm:text-2xl">
          Рекомендуемые статьи
        </h2>

        <p class="text-base-content/60 text-sm">
          Материалы подобраны по вашим тегам.
        </p>
      </div>

      <NuxtLink
        to="/content/articles"
        class="btn btn-ghost btn-sm"
      >
        Все статьи
      </NuxtLink>
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-else-if="articles.length"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="article in articles"
        :key="article.id"
        :class="[
          articleAuraClass(article),
          'h-full',
        ]"
      >
        <!-- Доступная статья -->
        <NuxtLink
          v-if="canReadArticle(article)"
          :to="`/content/articles/${article.id}`"
          class="card bg-base-100 border-base-300 hover:border-primary h-full border transition"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                v-if="article.pro_content"
                class="badge badge-secondary badge-sm"
              >
                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-primary btn-sm"
              >
                Читать
              </span>
            </div>
          </div>
        </NuxtLink>

        <!-- Заблокированная Pro-статья -->
        <div
          v-else
          class="card bg-base-100 h-full"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                class="badge badge-secondary badge-sm gap-1"
              >
                <Icon
                  name="lucide:sparkles"
                  class="size-3"
                />

                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <p
              class="text-base-content/60 text-sm"
            >
              Статья доступна пользователям Pro.
            </p>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-disabled btn-sm gap-1"
              >
                <Icon
                  name="lucide:lock"
                  class="size-4"
                />

                Только Pro
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p
      v-else
      class="text-base-content/50"
    >
      Подходящих статей пока нет.
    </p>
  </section>
</template>

чтобы не pro статьи все равно отображались, но пользователь видел, что они недоступны

Теперь надо сделать следующее:
Давай добавим модуль notifications. Это будут уведомления. На фронтенде у всех пользователей будет располагаться иконка колокольчика. Если там есть непрочитанные сообщения, там будет:
<div class="indicator">
  <span class="indicator-item badge badge-secondary">12</span>
  <button class="btn">inbox</button>
</div>

Врач, суперпользователь или медицинский ассистент могут назначать пользовтелю статью или опросник. и тогда пользователь видит этот опросник у себя на dashboard и он будет отображаться как Назначенный и располагаться в самом верху дашборда контента в разделе назначенное.

давай даже у назначенного сделаем такую рамку:
<div class="aura aura-gold">
  <div class="card bg-base-100">
    <div class="card-body">
      <p>This card has gold aura</p>
    </div>
  </div>
</div>

Помощь с записью убери в самый низ

Пациент
Здравствуйте, Иван
Базовая авторизация настроена и работает. надо убрать. ну, или сделать очень компактным в самом верху.

Также, хотелось бы, чтобы notifications работали через websockets. Если можешь это сделать, то было бы отлично! сам функционал вебсокетов тогда лучше сделать в ./backend/app/core/websockets/

notifications надо сделать максимально гибко. В идеале, хотелось бы, чтобы это были небольшая функция/функции, где указывается uuid любого пользователя и другие параметры, при вызове этой функции, сообщение бы отправлялось заданному пользователю. Например, после регистрации пациента, врачу будет отправлено уведомление, что пользователь зарегистрировался. или когда пользователь завершил опросник, врач также получал уведомление. При прочтении статей не надо слать уведомения.

А потом я планирую как-то наладить воздействие на пациентов, чтобы стимулировать их к работе.

И надо, чтобы у этой функции/функций был параметр, каким путем отправить уведомление: по почте, на сайт (в колокольчик) и в браузере. В браузере надо чтобы уведомления приходили, как это обычно происходит. Я знаю, что пользователь при этом должен будет их разрешить. Надо сделать такой функционал, чтобы была возможность отправлять уведомления разными путями.


















-------------
Ок, все работает. Теперь сделай функционал для назначения контента пациенту. Врач может назначать любой контент: статью или опросник независимо от тегов. То есть, по умолчанию у пациента контент фильтруется по тегам, но если срач назначил что-то, это имеет приоритет выше того, которое было отфильтровано: оно отображается у пациента в самом верху в рамке. Хотелось бы, чтобы когда врач назначает что-то пациенту, это по вебсокетам показывлось в уведомлении и сразу появлялось в виде карточек в самом верху страницы без обновления страниы, если это возможно, конечно. 

Врач может назначать контент пациенту, перейдя в detil пациента. пусть там в верху будет кнопка: Назначить контент. Он нажимает на кнопку и открывается modal на pc или bottomsheet на мобильных устройствах и там он выбирает, что отправить... не знаю, как лучше сделать, чтобы отделить статьи от опросников. если можешь, сделай их там в разных вкладках. Разумеется, постарайся разделить все на компоненты, где это уместно.






-----------------




















ок. Теперь давай сделаем конфигуратор программ. насколько я понял, эндпоинты сделаны на бекенде. теперь давай сделаем на фронтенде.

Программу могут создавать только суперпользователь и ассистент

Пусть будет отдельная страница, на которой можно создавать программу. 
В идеале, там надо сделать так:
Я вижу в боковой панели статьи и опросники в разных вкладках. 
В рабочем поле конфигуратора я могу нажать Добавить этап. Там я задаю параметры: период выполнения, и т.д.
Я могу мышькой перетаскивать статью или опросник на этап или менять их порядок.

И смотри... в самом начале я тебе писал про PRODUCT... короче, не надо его делать. мы этото функционал сделаем в программах, чтобы не раздувать код. 

У нас будет еще одна вкладка в Программе - консультации. Там я открываю и будут существующие специальности. Я могу любую специальность также перетащить внутрь этапа и это уже будет консультация специалиста, например: Кардиология переношу в конец первого этапа и пациент будет видеть, что по итогу выполенния этапа будет консультация кардиолога... Наверное, надо как-то переработать специальности - добавить поле с назначением консультации.

Разумеется, тут надо  доработать модуль с программами: добавить стоимость программы.

Пусть у программ также будут теги, соответственно их также можно фильтровать для пациентов

Если пациент не купил программу, он все равно может просматривать содержимое, но если туда входят Pro, он не может их читать.

Предполагается, что сам сервис будет бесплатным для пациента и он может проходить программу с контентом, который не Pro. Но если пациент покупает какую-то программу, он получает пакет консультаций специалистов, идущих в опроседеленном порядке по мере выполения программы: чтения статей и заполнения опросников. Пока покупка условна - то есть, медицинский ассистент будет связываться с пациентом и если пациент оплатил, ассистент будет нажиматьу пациента на Pro переключатель. 

У врача убери этот Pro переключатель у пациентов - это могут делать только ассистенты и суперпользоватлеь.
Добавть к Pro переключателю подтверждение в виде модального окна или bottomsheet в зависимости от устройства.

Создавать и изменять программу мгут только мед ассистенты и суперпользователи

отображение рограммы будет в отдельной вкладке у врачей/супервользователя/мед ассисента. Я думаю, лучше представить ее как-то в виде шагов:
<ul class="steps">
  <li data-content="?" class="step step-neutral">Step 1</li>
  <li data-content="!" class="step step-neutral">Step 2</li>
  <li data-content="✓" class="step step-neutral">Step 3</li>
  <li data-content="✕" class="step step-neutral">Step 4</li>
  <li data-content="★" class="step step-neutral">Step 5</li>
  <li data-content="" class="step step-neutral">Step 6</li>
  <li data-content="●" class="step step-neutral">Step 7</li>
</ul>
или 
<div class="overflow-x-auto">
  <ul class="steps">
    <li class="step">start</li>
    <li class="step step-secondary">2</li>
    <li class="step step-secondary">3</li>
    <li class="step step-secondary">4</li>
    <li class="step">5</li>
    <li class="step step-accent">6</li>
    <li class="step step-accent">7</li>
    <li class="step">8</li>
    <li class="step step-error">9</li>
    <li class="step step-error">10</li>
    <li class="step">11</li>
    <li class="step">12</li>
    <li class="step step-warning">13</li>
    <li class="step step-warning">14</li>
    <li class="step">15</li>
    <li class="step step-neutral">16</li>
    <li class="step step-neutral">17</li>
    <li class="step step-neutral">18</li>
    <li class="step step-neutral">19</li>
    <li class="step step-neutral">20</li>
    <li class="step step-neutral">21</li>
    <li class="step step-neutral">22</li>
    <li class="step step-neutral">23</li>
    <li class="step step-neutral">end</li>
  </ul>
</div>

или придумай. Надо одновременно и детально и компактно и чтобы было понятно, что это именно шаги. Плюс, на мобильных устройствах надо сделать вертикально, навероне.
<ul class="steps steps-vertical">
  <li class="step step-primary">Register</li>
  <li class="step step-primary">Choose plan</li>
  <li class="step">Purchase</li>
  <li class="step">Receive Product</li>
</ul>
даже не знаю, как лучше
Я думаю, можно на одной странице изображать каждый этам с упражнениями идущими по порядку в виде шагов, а где-то вверху будет переключатель каждого этапа:
<!-- name of each tab group should be unique -->
<div class="tabs tabs-box">
  <input type="radio" name="my_tabs_1" class="tab" aria-label="Tab 1" />
  <input type="radio" name="my_tabs_1" class="tab" aria-label="Tab 2" checked="checked" />
  <input type="radio" name="my_tabs_1" class="tab" aria-label="Tab 3" />
</div>
или

<div role="tablist" class="tabs tabs-lift tabs-xs">
  <a role="tab" class="tab">Xsmall</a>
  <a role="tab" class="tab tab-active">Xsmall</a>
  <a role="tab" class="tab">Xsmall</a>
</div>

<div role="tablist" class="tabs tabs-lift tabs-sm">
  <a role="tab" class="tab">Small</a>
  <a role="tab" class="tab tab-active">Small</a>
  <a role="tab" class="tab">Small</a>
</div>

<div role="tablist" class="tabs tabs-lift">
  <a role="tab" class="tab">Medium</a>
  <a role="tab" class="tab tab-active">Medium</a>
  <a role="tab" class="tab">Medium</a>
</div>

<div role="tablist" class="tabs tabs-lift tabs-lg">
  <a role="tab" class="tab">Large</a>
  <a role="tab" class="tab tab-active">Large</a>
  <a role="tab" class="tab">Large</a>
</div>

<div role="tablist" class="tabs tabs-lift tabs-xl">
  <a role="tab" class="tab">Xlarge</a>
  <a role="tab" class="tab tab-active">Xlarge</a>
  <a role="tab" class="tab">Xlarge</a>
</div>
или
<div class="join">
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 1" />
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 2" />
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 3" />
</div>
но тут тогда с отметкой, что этап пройден
у каждого шага есть description. может, сделать как-то так для описания шагов:
<ul class="timeline timeline-snap-icon max-md:timeline-compact timeline-vertical">
  <li>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">1984</time>
      <div class="text-lg font-black">First Macintosh computer</div>
      The Apple Macintosh—later rebranded as the Macintosh 128K—is the original Apple Macintosh
      personal computer. It played a pivotal role in establishing desktop publishing as a general
      office function. The motherboard, a 9 in (23 cm) CRT monitor, and a floppy drive were housed
      in a beige case with integrated carrying handle; it came with a keyboard and single-button
      mouse.
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end md:mb-10">
      <time class="font-mono italic">1998</time>
      <div class="text-lg font-black">iMac</div>
      iMac is a family of all-in-one Mac desktop computers designed and built by Apple Inc. It has
      been the primary part of Apple's consumer desktop offerings since its debut in August 1998,
      and has evolved through seven distinct forms
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">2001</time>
      <div class="text-lg font-black">iPod</div>
      The iPod is a discontinued series of portable media players and multi-purpose mobile devices
      designed and marketed by Apple Inc. The first version was released on October 23, 2001, about
      8+1⁄2 months after the Macintosh version of iTunes was released. Apple sold an estimated 450
      million iPod products as of 2022. Apple discontinued the iPod product line on May 10, 2022. At
      over 20 years, the iPod brand is the oldest to be discontinued by Apple
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end md:mb-10">
      <time class="font-mono italic">2007</time>
      <div class="text-lg font-black">iPhone</div>
      iPhone is a line of smartphones produced by Apple Inc. that use Apple's own iOS mobile
      operating system. The first-generation iPhone was announced by then-Apple CEO Steve Jobs on
      January 9, 2007. Since then, Apple has annually released new iPhone models and iOS updates. As
      of November 1, 2018, more than 2.2 billion iPhones had been sold. As of 2022, the iPhone
      accounts for 15.6% of global smartphone market share
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">2015</time>
      <div class="text-lg font-black">Apple Watch</div>
      The Apple Watch is a line of smartwatches produced by Apple Inc. It incorporates fitness
      tracking, health-oriented capabilities, and wireless telecommunication, and integrates with
      iOS and other Apple products and services
    </div>
  </li>
</ul>

или вообще сделать отдельный layout с sidebar, где будут разделы с шагами:
<div class="drawer lg:drawer-open">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle inline" />
  <div class="drawer-content">
    <!-- Navbar -->
    <nav class="navbar w-full bg-base-300">
      <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost drawer-button">
        <!-- Sidebar toggle icon -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"></path><path d="M9 4v16"></path><path d="M14 10l2 2l-2 2"></path></svg>
      </label>
      <div class="px-4">Navbar Title</div>
    </nav>
    <!-- Page content here -->
    <div class="p-4">Page Content</div>
  </div>

  <div class="drawer-side is-drawer-close:overflow-visible">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-14 is-drawer-open:w-64">
      <!-- Sidebar content here -->
      <ul class="menu w-full grow">
        <!-- List item -->
        <li>
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="Homepage">
            <!-- Home icon -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"></path><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span class="is-drawer-close:hidden">Homepage</span>
          </button>
        </li>

        <!-- List item -->
        <li>
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="Settings">
            <!-- Settings icon -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M20 7h-9"></path><path d="M14 17H5"></path><circle cx="17" cy="17" r="3"></circle><circle cx="7" cy="7" r="3"></circle></svg>
            <span class="is-drawer-close:hidden">Settings</span>
          </button>
        </li>
      </ul>
    </div>
  </div>
</div>
или скомбинировать разные шаги

Тут главное сделать удобно и компактно, чтобы даже на мобильных устройствах пациент понимал, на кокаом он шаге, что от него требуется в данный момеент сделать, после какого выполения задания планируется консультация специалиста (сама консультация там просто юотображается, не надо об этом где-то уведомлять). Тут главное, чтобы визуально был виден прогремм и пошаговое выполение. 

Если надо, сначала задай дополнительные вопросы, а после ответа на них, уже вторым этапом будм писать код



































-----------------
Пусть на заблокированном Pro будет кнопка: купить программу

1. Как пациент начинает программу? - да, давай так
2. Доступ к платной программе - блин, ну смотри. допустим пациент купил каую-то одну программу и ассистент открыл Pro контент. Тогда, он может нажать на другую программу и сможет видеть всеь Pro контент и в ней, хотя он ее не покупал... Давай переделаем... пусть будет такой функционал: Внутри пациента ассистент или суперпользователь будут видеть список программ (программ будет вообще не много, поэтому не надо их фильтровать у ассистентов). Ассистент сможет активировать переключатель у какой-то одной программы и пациент будет получать доступ внутри программы в Pro контенту. Думаю, так будет гибко. А переключатель Pro пусть остается. он нужен, чтобы открывать доступ к отдельным Pro статьям .
3. Поле pro_content у самой программы - да, все правильно, пациент видит все программы и может зайти и познакомиться с бесплатным контентом
4. Стоимость программы - да. Цена либо в рублях, либо в у.е.
5. Что означает консультация внутри этапа? - да, отлично. давай так сделаем
6. «Назначение консультации» у специальности - так давай так сделаем в CONSULTATION - пусть при добавлении какой-то консультации в этап , у консультации будет дефолтное описание ,но также можно будет изменить описание для конкретного шага, если мы хотим объяснить, зачем в данном шаге нужна конслуьтация врача.
7. Можно ли несколько раз добавить одну специальность? - разумеется, сколько угодно
8. Редактирование программы - да, ок
9. Статусы этапа - ок, отлично. в Event давай добавим IN_PROGRESS (но однократно, чтобы не забивать базу) и COMPLETED
10. Pro-переключатель: ок



у меня пока нет alembic. Сделай отдельный файл для миграций, где миграция будет выполняться вручную . Напиши код для добавления полей 

