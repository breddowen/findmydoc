

Описание архитектуры:

Роли: Superuser, Patient, Doctor, Relative, Med_assistant


User пока просто пусть будет, но для него пока логин и регистрацию не делаем

Superuser логин-пароль сделаем файл в ./backend/seed/data/users.json и файл ./backend/seed/upload_users.py в нем сделаем загрузку логина и пароля в базу

Также, надо сделать загрузчик баз данных:
./backend/seed/data/DRUGS_base.jsonl
./backend/seed/data/drugs_reviews.jsonl

соответственно, сделай загрузчики в sql

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

Пока делаем бекенд. Фронтенд потом скажу как.

Если тебе надо задать вопросы, сначала задай, без кода.