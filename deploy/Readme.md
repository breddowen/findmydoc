Хорошо, шифрование полей пока откладываем. Ниже — полный план подготовки deployment, PostgreSQL, SMTP, Nginx, SSL, staging и GitHub Actions.

Будем использовать:

- production: `https://findmydoc.ru`;
- staging: `https://staging.findmydoc.ru`;
- API на том же домене по `/api`;
- WebSocket на том же домене;
- приватные образы в GHCR;
- PostgreSQL 17 с `pgcrypto`;
- один backend worker, поскольку WebSocket-соединения хранятся в памяти;
- SQLite локально, PostgreSQL только на сервере.

---

# 1. Итоговая структура

Создайте:

```text
deploy/
├── backend.Dockerfile
├── frontend.Dockerfile
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── postgres/
│   └── init/
│       └── 01-enable-pgcrypto.sql
├── scripts/
│   ├── deploy.sh
│   ├── backup.sh
│   └── init-letsencrypt.sh
└── env/
    ├── compose.env.example
    ├── backend.env.example
    └── frontend.env.example

.github/
└── workflows/
    └── deploy.yml

.gitignore
.dockerignore
```

---

# 2. Исправить зависимости backend

В `backend/requirements.txt` должны присутствовать:

```text
alembic==1.19.1
psycopg==3.3.4
psycopg-binary==3.3.4
```

Можно заменить две последние строки одной:

```text
psycopg[binary]==3.3.4
```

То есть предпочтительный вариант:

```text
alembic==1.19.1
psycopg[binary]==3.3.4
```

Остальные зависимости оставьте без изменений.

---

# 3. Исправить запуск базы в backend

## `backend/app/main.py`

Сейчас `init_sqlite_db()` вызывается и для PostgreSQL. Это означает, что backend будет выполнять `SQLModel.metadata.create_all()` вместо нормальных миграций.

Замените lifespan:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_sqlite_db()
    yield
```

на:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.DATABASE_URL.startswith("sqlite"):
        init_sqlite_db()

    yield
```

В production таблицы будут создаваться только через:

```bash
alembic upgrade head
```

---

# 4. Улучшить подключение к PostgreSQL

В `backend/app/core/db.py` найдите:

```python
sqlite_engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args=connect_args,
)
```

Замените на:

```python
engine_kwargs = {
    "echo": False,
    "connect_args": connect_args,
    "pool_pre_ping": True,
}

if not DATABASE_URL.startswith("sqlite"):
    engine_kwargs.update({
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 1800,
    })

sqlite_engine = create_engine(
    DATABASE_URL,
    **engine_kwargs,
)
```

Название `sqlite_engine` пока можно оставить. Несмотря на название, объект сможет работать с PostgreSQL.

---

# 5. Исправить healthcheck

Текущий `/health` проверяет только то, что процесс FastAPI работает. Добавим проверку БД.

В `backend/app/main.py` добавьте импорты:

```python
from sqlalchemy import text
from sqlmodel import Session

from app.core.db import init_sqlite_db, sqlite_engine
```

Замените текущий healthcheck:

```python
@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}
```

на:

```python
@app.get("/health/live", tags=["System"])
async def liveness_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/health/ready", tags=["System"])
async def readiness_check() -> dict[str, str]:
    with Session(sqlite_engine) as session:
        session.exec(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }
```

Итоговый импорт из `app.core.db` должен выглядеть так:

```python
from app.core.db import init_sqlite_db, sqlite_engine
```

---

# 6. Подключить SMTP

<details>
<summary><strong>Изменения в конфигурации backend</strong></summary>

## `backend/app/core/config.py`

Добавьте в класс `Settings`:

```python
    EMAIL_BACKEND: str = "console"

    SMTP_HOST: str = "smtp.beget.com"
    SMTP_PORT: int = 465
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_USE_SSL: bool = True
    SMTP_USE_STARTTLS: bool = False
    SMTP_TIMEOUT_SECONDS: int = 15

    EMAIL_FROM_ADDRESS: str = "noreply@findmydoc.ru"
    EMAIL_FROM_NAME: str = "FindMyDoc"
```

Полный класс будет содержать как старые настройки, так и новые SMTP-параметры.

</details>

<details>
<summary><strong>Новая реализация backend/app/core/email.py</strong></summary>

Полностью замените `backend/app/core/email.py`:

```python
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr

from app.core.config import settings


def build_action_url(
    *,
    action_path: str | None,
    token: str | None,
    action_url: str | None,
) -> str | None:
    if action_url:
        return action_url

    if not action_path:
        return None

    frontend_url = settings.FRONTEND_URL.rstrip("/")
    path = action_path if action_path.startswith("/") else f"/{action_path}"

    result = f"{frontend_url}{path}"

    if token:
        separator = "&" if "?" in result else "?"
        result = f"{result}{separator}token={token}"

    return result


def build_email_body(
    *,
    message: str,
    action_url: str | None,
) -> str:
    parts = [message.strip()]

    if action_url:
        parts.extend([
            "",
            action_url,
        ])

    parts.extend([
        "",
        "Если вы не выполняли это действие, проигнорируйте письмо.",
    ])

    return "\n".join(parts)


def send_console_email(
    *,
    recipient: str,
    subject: str,
    message: str,
    action_path: str | None = None,
    token: str | None = None,
    action_url: str | None = None,
) -> None:
    resolved_action_url = build_action_url(
        action_path=action_path,
        token=token,
        action_url=action_url,
    )

    body = build_email_body(
        message=message,
        action_url=resolved_action_url,
    )

    print()
    print("=" * 80)
    print("EMAIL")
    print(f"Backend: {settings.EMAIL_BACKEND}")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print()
    print(body)
    print("=" * 80)
    print()

    if settings.EMAIL_BACKEND.lower() == "console":
        return

    if settings.EMAIL_BACKEND.lower() != "smtp":
        raise RuntimeError(
            f"Неизвестный EMAIL_BACKEND: {settings.EMAIL_BACKEND}"
        )

    if not settings.SMTP_USERNAME:
        raise RuntimeError("SMTP_USERNAME не настроен")

    if not settings.SMTP_PASSWORD:
        raise RuntimeError("SMTP_PASSWORD не настроен")

    email = EmailMessage()
    email["From"] = formataddr(
        (
            settings.EMAIL_FROM_NAME,
            settings.EMAIL_FROM_ADDRESS,
        )
    )
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(body)

    ssl_context = ssl.create_default_context()

    if settings.SMTP_USE_SSL:
        with smtplib.SMTP_SSL(
            host=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            timeout=settings.SMTP_TIMEOUT_SECONDS,
            context=ssl_context,
        ) as smtp:
            smtp.login(
                settings.SMTP_USERNAME,
                settings.SMTP_PASSWORD,
            )
            smtp.send_message(email)

        return

    with smtplib.SMTP(
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        timeout=settings.SMTP_TIMEOUT_SECONDS,
    ) as smtp:
        smtp.ehlo()

        if settings.SMTP_USE_STARTTLS:
            smtp.starttls(context=ssl_context)
            smtp.ehlo()

        smtp.login(
            settings.SMTP_USERNAME,
            settings.SMTP_PASSWORD,
        )
        smtp.send_message(email)
```

Имя `send_console_email` пока оставлено для совместимости. Поэтому менять все импорты прямо сейчас не обязательно. При `EMAIL_BACKEND=smtp` эта же функция отправит настоящее письмо.

</details>

## Исправить отправку referral-ссылки

В `backend/app/modules/referrals/routers.py` замените:

```python
    send_console_email(
        recipient=email,
        subject="Направление в MentalMe",
        message=(
            "Врач подготовил для вас персональное "
            "направление. Перейдите по ссылке:"
        ),
    )

    print(f"Referral link: {registration_url}")
```

на:

```python
    send_console_email(
        recipient=email,
        subject="Направление в FindMyDoc",
        message=(
            "Врач подготовил для вас персональное "
            "направление. Перейдите по ссылке:"
        ),
        action_url=registration_url,
    )
```

Иначе в реальном письме не будет ссылки.

---

# 7. Создать правильную initial migration

Текущую миграцию использовать нельзя: она не создает таблицы.

Это необходимо сделать до первого push и до первой сборки production image.

## 7.1. Удалить текущую миграцию

Удалите:

```text
backend/alembic/versions/0d94f719ce10_initial_migration.py
```

## 7.2. Поднять временный пустой PostgreSQL

В PowerShell:

```powershell
docker run --name findmydoc-migration-db `
  -e POSTGRES_USER=mentalme `
  -e POSTGRES_PASSWORD=mentalme_dev_password `
  -e POSTGRES_DB=mentalme `
  -p 5433:5432 `
  -d postgres:17-bookworm
```

Проверьте:

```powershell
docker ps
```

## 7.3. Установить переменную подключения

Из каталога `backend`:

```powershell
$env:DATABASE_URL="postgresql+psycopg://mentalme:mentalme_dev_password@localhost:5433/mentalme"
```

Проверьте, что база пустая:

```powershell
docker exec findmydoc-migration-db `
  psql -U mentalme -d mentalme -c "\dt"
```

## 7.4. Создать baseline migration

Находясь в `backend`:

```powershell
alembic revision --autogenerate -m "initial schema"
```

В `backend/alembic/versions/` появится новый файл.

Откройте его и проверьте:

- есть много вызовов `op.create_table(...)`;
- создается таблица `users`;
- создается таблица `articles`;
- создается таблица `programs`;
- создается таблица `questionnaires`;
- создаются внешние ключи и индексы;
- нет `batch_alter_table()` без предшествующего создания таблиц.

В начало функции `upgrade()` добавьте:

```python
op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
```

Например:

```python
def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    op.create_table(
        ...
    )
```

Не удаляйте `pgcrypto` в `downgrade()`, поскольку расширение может использоваться другими объектами БД.

## 7.5. Проверить миграцию

```powershell
alembic upgrade head
```

Затем:

```powershell
docker exec findmydoc-migration-db `
  psql -U mentalme -d mentalme -c "\dt"
```

Проверка `pgcrypto`:

```powershell
docker exec findmydoc-migration-db `
  psql -U mentalme -d mentalme `
  -c "SELECT extname FROM pg_extension WHERE extname = 'pgcrypto';"
```

Проверьте полный цикл:

```powershell
alembic downgrade base
alembic upgrade head
```

Если все прошло успешно, остановите временную БД:

```powershell
docker rm -f findmydoc-migration-db
```

Удалите переменную из текущей PowerShell-сессии:

```powershell
Remove-Item Env:DATABASE_URL
```

> Не запускайте `alembic stamp head` на пустой production-базе. Нужен именно `alembic upgrade head`.

---

# 8. Dockerfile для backend

Создайте `deploy/backend.Dockerfile`:

```dockerfile
FROM python:3.10-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN groupadd --system app \
    && useradd \
        --system \
        --gid app \
        --create-home \
        app

COPY backend/requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip \
    && python -m pip install \
        --requirement /app/requirements.txt

COPY backend/ /app/

RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD [
    "uvicorn",
    "app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000",
    "--workers",
    "1",
    "--proxy-headers",
    "--forwarded-allow-ips=*"
]
```

Используется один worker, потому что `websocket_manager` хранит соединения в оперативной памяти процесса.

---

# 9. Dockerfile для frontend

Создайте `deploy/frontend.Dockerfile`:

```dockerfile
FROM node:24.15.0-bookworm-slim AS builder

ENV NODE_ENV=production

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm ci

COPY frontend/ ./

RUN npm run build


FROM node:24.15.0-bookworm-slim AS runtime

ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=3000 \
    NITRO_HOST=0.0.0.0 \
    NITRO_PORT=3000

WORKDIR /app

COPY --from=builder --chown=node:node /app/.output ./.output

USER node

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
```

---

# 10. PostgreSQL и `pgcrypto`

Создайте `deploy/postgres/init/01-enable-pgcrypto.sql`:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Этот скрипт выполняется только при первом создании PostgreSQL volume.

Расширение также добавляется через Alembic — это намеренное дублирование с `IF NOT EXISTS`. Так новая БД будет корректно подготовлена независимо от способа создания.

---

# 11. Docker Compose

Создайте `deploy/docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:17-bookworm
    restart: unless-stopped
    shm_size: 256mb
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      TZ: UTC
      PGTZ: UTC
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgres/init/01-enable-pgcrypto.sql:/docker-entrypoint-initdb.d/01-enable-pgcrypto.sql:ro
    healthcheck:
      test:
        [
          "CMD-SHELL",
          "pg_isready -U \"$${POSTGRES_USER}\" -d \"$${POSTGRES_DB}\""
        ]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 20s
    networks:
      - internal
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  migrate:
    image: ${BACKEND_IMAGE}
    profiles:
      - tools
    restart: "no"
    env_file:
      - ${BACKEND_ENV_FILE}
    environment:
      DATABASE_URL: postgresql+psycopg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
    command:
      - alembic
      - upgrade
      - head
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - internal

  backend:
    image: ${BACKEND_IMAGE}
    restart: unless-stopped
    env_file:
      - ${BACKEND_ENV_FILE}
    environment:
      DATABASE_URL: postgresql+psycopg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health/ready', timeout=5)"
        ]
      interval: 15s
      timeout: 7s
      retries: 10
      start_period: 30s
    networks:
      internal:
      proxy:
        aliases:
          - ${BACKEND_NETWORK_ALIAS}
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  frontend:
    image: ${FRONTEND_IMAGE}
    restart: unless-stopped
    env_file:
      - ${FRONTEND_ENV_FILE}
    healthcheck:
      test:
        [
          "CMD",
          "node",
          "-e",
          "fetch('http://127.0.0.1:3000').then(r => { if (!r.ok) process.exit(1) }).catch(() => process.exit(1))"
        ]
      interval: 15s
      timeout: 7s
      retries: 10
      start_period: 30s
    networks:
      proxy:
        aliases:
          - ${FRONTEND_NETWORK_ALIAS}
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  nginx:
    image: nginx:1.28-alpine
    profiles:
      - edge
    restart: unless-stopped
    command:
      - /bin/sh
      - -c
      - |
        while true; do
          sleep 6h
          nginx -s reload || true
        done &
        exec nginx -g 'daemon off;'
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
      - letsencrypt:/etc/letsencrypt:ro
      - certbot_www:/var/www/certbot:ro
    networks:
      - proxy
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  certbot:
    image: certbot/certbot:latest
    profiles:
      - edge
    restart: unless-stopped
    entrypoint:
      - /bin/sh
    command:
      - -c
      - |
        trap exit TERM
        while true; do
          certbot renew \
            --webroot \
            --webroot-path=/var/www/certbot \
            --quiet
          sleep 12h &
          wait $${!}
        done
    volumes:
      - letsencrypt:/etc/letsencrypt
      - certbot_www:/var/www/certbot
    networks:
      - proxy

volumes:
  postgres_data:

  letsencrypt:
    name: findmydoc_letsencrypt

  certbot_www:
    name: findmydoc_certbot_www

networks:
  internal:
    internal: true

  proxy:
    name: findmydoc_proxy
    external: true
```

## Почему два окружения не конфликтуют

Compose будет запускаться с разными project names:

```text
findmydoc-prod
findmydoc-staging
```

Поэтому будут разные:

- PostgreSQL-контейнеры;
- volumes базы;
- backend;
- frontend;
- внутренние сети.

Общая только сеть:

```text
findmydoc_proxy
```

Nginx запускается только в production Compose project с профилем `edge`.

---

# 12. Конфигурация Nginx

Создайте `deploy/nginx/default.conf`:

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server_tokens off;

client_max_body_size 10m;

server {
    listen 80;
    listen [::]:80;

    server_name
        findmydoc.ru
        www.findmydoc.ru
        staging.findmydoc.ru;

    location ^~ /.well-known/acme-challenge/ {
        root /var/www/certbot;
        default_type text/plain;
        try_files $uri =404;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/findmydoc.ru/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;

    resolver 127.0.0.11 valid=30s ipv6=off;

    location /api/ {
        set $backend_upstream backend-prod;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }

    location = /docs {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /openapi.json {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /health/ {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
    }

    location / {
        set $frontend_upstream frontend-prod;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name www.findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/findmydoc.ru/privkey.pem;

    return 301 https://findmydoc.ru$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name staging.findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/staging.findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/staging.findmydoc.ru/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    add_header X-Robots-Tag "noindex, nofollow, noarchive" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    resolver 127.0.0.11 valid=30s ipv6=off;

    location /api/ {
        set $backend_upstream backend-staging;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }

    location = /docs {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /openapi.json {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /health/ {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
    }

    location / {
        set $frontend_upstream frontend-staging;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}
```

WebSocket будет проксироваться через тот же `/api/`. Отдельный location для `/ws` не нужен.

---

# 13. Примеры environment-файлов

## `deploy/env/compose.env.example`

```dotenv
BACKEND_IMAGE=ghcr.io/github-owner/repository-backend:latest
FRONTEND_IMAGE=ghcr.io/github-owner/repository-frontend:latest

BACKEND_ENV_FILE=/opt/findmydoc/production/backend.env
FRONTEND_ENV_FILE=/opt/findmydoc/production/frontend.env

BACKEND_NETWORK_ALIAS=backend-prod
FRONTEND_NETWORK_ALIAS=frontend-prod

POSTGRES_USER=mentalme
POSTGRES_PASSWORD=CHANGE_ME
POSTGRES_DB=mentalme
```

## `deploy/env/backend.env.example`

```dotenv
SECRET_KEY=CHANGE_ME
ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=1440
ROLE_SELECTION_TOKEN_EXPIRE_MINUTES=5
ACTION_TOKEN_EXPIRE_MINUTES=60
INVITATION_EXPIRE_HOURS=72

FRONTEND_URL=https://findmydoc.ru

WEBAUTHN_RP_ID=findmydoc.ru
WEBAUTHN_RP_NAME=FindMyDoc
WEBAUTHN_ORIGIN=https://findmydoc.ru
WEBAUTHN_CHALLENGE_EXPIRE_SECONDS=300

EMAIL_BACKEND=smtp

SMTP_HOST=smtp.beget.com
SMTP_PORT=465
SMTP_USERNAME=noreply@findmydoc.ru
SMTP_PASSWORD=CHANGE_ME
SMTP_USE_SSL=true
SMTP_USE_STARTTLS=false
SMTP_TIMEOUT_SECONDS=15

EMAIL_FROM_ADDRESS=noreply@findmydoc.ru
EMAIL_FROM_NAME=FindMyDoc
```

## `deploy/env/frontend.env.example`

```dotenv
NUXT_PUBLIC_API_BASE=https://findmydoc.ru
NUXT_PUBLIC_SITE_URL=https://findmydoc.ru

HOST=0.0.0.0
PORT=3000
NITRO_HOST=0.0.0.0
NITRO_PORT=3000
```

Полный URL в `NUXT_PUBLIC_API_BASE` нужен из-за текущего вычисления WebSocket URL:

```javascript
config.public.apiBase
  .replace(/^http:/, 'ws:')
  .replace(/^https:/, 'wss:')
```

---

# 14. Скрипт backup

Создайте `deploy/scripts/backup.sh`:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

TARGET="${1:-production}"

case "$TARGET" in
  production)
    PROJECT="findmydoc-prod"
    ENV_FILE="/opt/findmydoc/production/compose.env"
    ;;
  staging)
    PROJECT="findmydoc-staging"
    ENV_FILE="/opt/findmydoc/staging/compose.env"
    ;;
  *)
    echo "Unknown environment: $TARGET" >&2
    exit 1
    ;;
esac

DEPLOY_DIR="/opt/findmydoc/deploy"
BACKUP_DIR="/opt/findmydoc/backups/${TARGET}"

mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

TIMESTAMP="$(date -u +'%Y-%m-%d_%H-%M-%S')"
BACKUP_FILE="${BACKUP_DIR}/database_${TIMESTAMP}.sql.gz"

cd "$DEPLOY_DIR"

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  exec -T postgres \
  sh -c 'pg_dump \
    --username="$POSTGRES_USER" \
    --dbname="$POSTGRES_DB" \
    --no-owner \
    --no-privileges' \
  | gzip -9 > "$BACKUP_FILE"

chmod 600 "$BACKUP_FILE"

find "$BACKUP_DIR" \
  -type f \
  -name "database_*.sql.gz" \
  -mtime +14 \
  -delete

echo "Backup created: $BACKUP_FILE"
```

---

# 15. Скрипт deployment

Создайте `deploy/scripts/deploy.sh`:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

TARGET="${1:?Environment is required}"
IMAGE_PREFIX="${2:?Image prefix is required}"
IMAGE_TAG="${3:?Image tag is required}"

case "$TARGET" in
  production)
    PROJECT="findmydoc-prod"
    ENV_DIR="/opt/findmydoc/production"
    ;;
  staging)
    PROJECT="findmydoc-staging"
    ENV_DIR="/opt/findmydoc/staging"
    ;;
  *)
    echo "Unknown environment: $TARGET" >&2
    exit 1
    ;;
esac

DEPLOY_DIR="/opt/findmydoc/deploy"
ENV_FILE="${ENV_DIR}/compose.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Environment file does not exist: $ENV_FILE" >&2
  exit 1
fi

exec 9>/tmp/findmydoc-deploy.lock
flock -x 9

set_env_value() {
  local key="$1"
  local value="$2"
  local file="$3"

  if grep -q "^${key}=" "$file"; then
    sed -i "s|^${key}=.*|${key}=${value}|" "$file"
  else
    printf '%s=%s\n' "$key" "$value" >> "$file"
  fi
}

BACKEND_IMAGE="${IMAGE_PREFIX}-backend:${IMAGE_TAG}"
FRONTEND_IMAGE="${IMAGE_PREFIX}-frontend:${IMAGE_TAG}"

set_env_value \
  "BACKEND_IMAGE" \
  "$BACKEND_IMAGE" \
  "$ENV_FILE"

set_env_value \
  "FRONTEND_IMAGE" \
  "$FRONTEND_IMAGE" \
  "$ENV_FILE"

cd "$DEPLOY_DIR"

echo "Pulling images..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  pull postgres backend frontend migrate

echo "Starting PostgreSQL..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  up -d --wait postgres

if docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  ps --status running postgres \
  | grep -q postgres
then
  echo "Creating database backup..."

  if ! "$DEPLOY_DIR/scripts/backup.sh" "$TARGET"; then
    echo "Backup failed; deployment stopped." >&2
    exit 1
  fi
fi

echo "Running database migrations..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  run --rm migrate

echo "Starting application services..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  up -d --wait backend frontend

if [[ "$TARGET" == "production" ]]; then
  if docker run --rm \
    -v findmydoc_letsencrypt:/etc/letsencrypt:ro \
    alpine:3.22 \
    test -f \
    /etc/letsencrypt/live/findmydoc.ru/fullchain.pem
  then
    echo "Starting Nginx and Certbot..."

    docker compose \
      --project-name "$PROJECT" \
      --env-file "$ENV_FILE" \
      --profile edge \
      up -d nginx certbot
  else
    echo "TLS certificates are not initialized yet."
    echo "Run init-letsencrypt.sh after the first deployment."
  fi
fi

echo "Current services:"

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  ps

docker image prune -f

echo "Deployment completed: $TARGET"
```

---

# 16. Инициализация Let's Encrypt

Создайте `deploy/scripts/init-letsencrypt.sh`:

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT="findmydoc-prod"
DEPLOY_DIR="/opt/findmydoc/deploy"
ENV_FILE="/opt/findmydoc/production/compose.env"
LETSENCRYPT_EMAIL="${1:?Let's Encrypt email is required}"

cd "$DEPLOY_DIR"

if docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt:ro \
  alpine:3.22 \
  test -f /etc/letsencrypt/live/findmydoc.ru/fullchain.pem
then
  echo "Certificates are already initialized."
  exit 0
fi

docker network inspect findmydoc_proxy >/dev/null 2>&1 \
  || docker network create findmydoc_proxy

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  create nginx certbot

echo "Creating temporary certificates..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine/openssl \
  req \
  -x509 \
  -nodes \
  -newkey rsa:2048 \
  -days 1 \
  -keyout /etc/letsencrypt/live/findmydoc.ru/privkey.pem \
  -out /etc/letsencrypt/live/findmydoc.ru/fullchain.pem \
  -subj /CN=findmydoc.ru

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine/openssl \
  req \
  -x509 \
  -nodes \
  -newkey rsa:2048 \
  -days 1 \
  -keyout /etc/letsencrypt/live/staging.findmydoc.ru/privkey.pem \
  -out /etc/letsencrypt/live/staging.findmydoc.ru/fullchain.pem \
  -subj /CN=staging.findmydoc.ru

echo "Starting Nginx with temporary certificates..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  up -d nginx

sleep 5

echo "Removing temporary certificates..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine:3.22 \
  sh -c '
    rm -rf /etc/letsencrypt/live/findmydoc.ru
    rm -rf /etc/letsencrypt/archive/findmydoc.ru
    rm -f /etc/letsencrypt/renewal/findmydoc.ru.conf

    rm -rf /etc/letsencrypt/live/staging.findmydoc.ru
    rm -rf /etc/letsencrypt/archive/staging.findmydoc.ru
    rm -f /etc/letsencrypt/renewal/staging.findmydoc.ru.conf
  '

echo "Requesting production certificate..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  run --rm \
  --entrypoint certbot \
  certbot \
  certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  --email "$LETSENCRYPT_EMAIL" \
  --agree-tos \
  --no-eff-email \
  --cert-name findmydoc.ru \
  -d findmydoc.ru \
  -d www.findmydoc.ru

echo "Requesting staging certificate..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  run --rm \
  --entrypoint certbot \
  certbot \
  certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  --email "$LETSENCRYPT_EMAIL" \
  --agree-tos \
  --no-eff-email \
  --cert-name staging.findmydoc.ru \
  -d staging.findmydoc.ru

echo "Restarting Nginx and starting renewal service..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  up -d --force-recreate nginx certbot

echo "Let's Encrypt initialization completed."
```

## Важное исправление для временных сертификатов

`openssl` не создаст отсутствующие родительские каталоги. Поэтому перед командами `openssl` в скрипте нужно создать каталоги.

Замените первый блок создания production-сертификата на:

```bash
docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  --entrypoint sh \
  alpine/openssl \
  -c '
    mkdir -p /etc/letsencrypt/live/findmydoc.ru
    openssl req \
      -x509 \
      -nodes \
      -newkey rsa:2048 \
      -days 1 \
      -keyout /etc/letsencrypt/live/findmydoc.ru/privkey.pem \
      -out /etc/letsencrypt/live/findmydoc.ru/fullchain.pem \
      -subj /CN=findmydoc.ru
  '
```

А staging-блок на:

```bash
docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  --entrypoint sh \
  alpine/openssl \
  -c '
    mkdir -p /etc/letsencrypt/live/staging.findmydoc.ru
    openssl req \
      -x509 \
      -nodes \
      -newkey rsa:2048 \
      -days 1 \
      -keyout /etc/letsencrypt/live/staging.findmydoc.ru/privkey.pem \
      -out /etc/letsencrypt/live/staging.findmydoc.ru/fullchain.pem \
      -subj /CN=staging.findmydoc.ru
  '
```

---

# 17. `.gitignore`

Создайте `.gitignore` в корне:

```gitignore
# Environment files
.env
.env.*
!.env.example

backend/app/.env
frontend/.env

deploy/*.env
deploy/env/*.env
!deploy/env/*.env.example

# Python
__pycache__/
*.py[cod]
*.pyo
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/

# Local databases
*.db
*.sqlite
*.sqlite3

# Nuxt / Node
frontend/node_modules/
frontend/.nuxt/
frontend/.output/
frontend/.data/
frontend/dist/
npm-debug.log*

# IDE
.idea/
.vscode/
*.iml

# OS
.DS_Store
Thumbs.db

# Certificates and secrets
*.pem
*.key
*.crt

# Backups
backups/
*.sql
*.sql.gz
```

Если `backend/test_database.db` нужен как тестовый fixture, решите отдельно. По умолчанию его лучше не коммитить.

---

# 18. `.dockerignore`

Создайте `.dockerignore` в корне:

```dockerignore
.git
.github

**/.env
**/.env.*
!**/.env.example

**/__pycache__
**/*.pyc
**/*.pyo

backend/*.db
backend/*.sqlite
backend/*.sqlite3

frontend/node_modules
frontend/.nuxt
frontend/.output

.idea
.vscode

deploy
!deploy/backend.Dockerfile
!deploy/frontend.Dockerfile

*.pem
*.key
*.crt
*.sql.gz
```

Здесь важно, чтобы `backend/app/.env` не попал в Docker image.

---

# 19. Проверить Docker-сборку локально

Из корня проекта:

```powershell
docker build `
  -f deploy/backend.Dockerfile `
  -t findmydoc-backend:test `
  .
```

Frontend:

```powershell
docker build `
  -f deploy/frontend.Dockerfile `
  -t findmydoc-frontend:test `
  .
```

Проверьте наличие Alembic:

```powershell
docker run --rm findmydoc-backend:test alembic --version
```

Проверьте импорт приложения:

```powershell
docker run --rm findmydoc-backend:test `
  python -c "from app.main import app; print(app.title)"
```

---

# 20. GitHub Actions

Создайте `.github/workflows/deploy.yml`:

```yaml
name: Build and deploy

on:
  push:
    branches:
      - main
      - develop

  workflow_dispatch:

permissions:
  contents: read
  packages: write

concurrency:
  group: findmydoc-vds-deployment
  cancel-in-progress: false

jobs:
  build:
    name: Build and publish images
    runs-on: ubuntu-24.04

    outputs:
      image_prefix: ${{ steps.names.outputs.image_prefix }}
      image_tag: ${{ steps.names.outputs.image_tag }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Prepare image names
        id: names
        shell: bash
        run: |
          REPOSITORY="$(echo '${{ github.repository }}' | tr '[:upper:]' '[:lower:]')"

          echo "image_prefix=ghcr.io/${REPOSITORY}" >> "$GITHUB_OUTPUT"
          echo "image_tag=${GITHUB_SHA}" >> "$GITHUB_OUTPUT"

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push backend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/backend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-backend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-backend:${{ github.ref_name }}
          cache-from: type=gha,scope=backend
          cache-to: type=gha,mode=max,scope=backend

      - name: Build and push frontend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/frontend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ github.ref_name }}
          cache-from: type=gha,scope=frontend
          cache-to: type=gha,mode=max,scope=frontend

  deploy:
    name: Deploy
    needs:
      - build

    runs-on: ubuntu-24.04

    environment:
      name: ${{ github.ref_name == 'main' && 'production' || 'staging' }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Determine target environment
        id: target
        shell: bash
        run: |
          if [[ "${GITHUB_REF_NAME}" == "main" ]]; then
            echo "name=production" >> "$GITHUB_OUTPUT"
          elif [[ "${GITHUB_REF_NAME}" == "develop" ]]; then
            echo "name=staging" >> "$GITHUB_OUTPUT"
          else
            echo "Unsupported deployment branch: ${GITHUB_REF_NAME}" >&2
            exit 1
          fi

      - name: Configure SSH
        shell: bash
        env:
          SSH_PRIVATE_KEY: ${{ secrets.VPS_SSH_PRIVATE_KEY }}
          VPS_KNOWN_HOSTS: ${{ secrets.VPS_KNOWN_HOSTS }}
        run: |
          mkdir -p ~/.ssh
          chmod 700 ~/.ssh

          printf '%s\n' "$SSH_PRIVATE_KEY" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519

          printf '%s\n' "$VPS_KNOWN_HOSTS" > ~/.ssh/known_hosts
          chmod 600 ~/.ssh/known_hosts

      - name: Upload deployment configuration
        shell: bash
        env:
          VPS_HOST: ${{ secrets.VPS_HOST }}
          VPS_PORT: ${{ secrets.VPS_PORT }}
          VPS_USER: ${{ secrets.VPS_USER }}
        run: |
          rsync \
            --archive \
            --compress \
            --delete \
            -e "ssh -p ${VPS_PORT}" \
            deploy/ \
            "${VPS_USER}@${VPS_HOST}:/opt/findmydoc/deploy/"

      - name: Run deployment
        shell: bash
        env:
          VPS_HOST: ${{ secrets.VPS_HOST }}
          VPS_PORT: ${{ secrets.VPS_PORT }}
          VPS_USER: ${{ secrets.VPS_USER }}
          TARGET: ${{ steps.target.outputs.name }}
          IMAGE_PREFIX: ${{ needs.build.outputs.image_prefix }}
          IMAGE_TAG: ${{ needs.build.outputs.image_tag }}
        run: |
          ssh \
            -p "${VPS_PORT}" \
            "${VPS_USER}@${VPS_HOST}" \
            "chmod +x /opt/findmydoc/deploy/scripts/*.sh && \
             /opt/findmydoc/deploy/scripts/deploy.sh \
             '${TARGET}' \
             '${IMAGE_PREFIX}' \
             '${IMAGE_TAG}'"
```

---

# 21. Создать Git-репозиторий

В корне проекта:

```bash
git init
git branch -M main
git add .
git status
```

Перед commit внимательно проверьте, что в staged files нет:

```text
backend/app/.env
frontend/.env
test_database.db
паролей
SMTP_PASSWORD
SECRET_KEY
```

Затем:

```bash
git commit -m "Prepare Docker deployment"
```

На GitHub:

1. Нажмите **New repository**.
2. Название, например:

   ```text
   findmydoc
   ```

3. Visibility:

   ```text
   Private
   ```

4. Не добавляйте автоматически README и `.gitignore`, если они уже локально.
5. После создания выполните команды, которые покажет GitHub:

```bash
git remote add origin git@github.com:breddowen/findmydoc.git
git push -u origin main
```

Создайте staging-ветку:

```bash
git checkout -b develop
git push -u origin develop
git checkout main
```

---

# 22. DNS в Beget

До получения сертификатов создайте записи:

| Тип | Имя | Значение |
|---|---|---|
| `A` | `@` | IPv4 вашего VDS |
| `A` | `www` | IPv4 вашего VDS |
| `A` | `staging` | IPv4 вашего VDS |

Проверка:

```bash
dig +short findmydoc.ru
dig +short www.findmydoc.ru
dig +short staging.findmydoc.ru
```

Все должны возвращать IP VDS.

---

# 23. Подготовить Ubuntu VDS

Подключитесь как root:

```bash
ssh root@VDS_IP
```

Обновите систему:

```bash
apt update
apt upgrade -y
```

Установите необходимые пакеты:

```bash
apt install -y \
  ca-certificates \
  curl \
  gnupg \
  rsync \
  openssl \
  ufw
```

## Установить Docker

```bash
install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc

chmod a+r /etc/apt/keyrings/docker.asc
```

Добавьте репозиторий:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  > /etc/apt/sources.list.d/docker.list
```

Установите:

```bash
apt update

apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

Проверьте:

```bash
docker --version
docker compose version
systemctl enable --now docker
```

---

# 24. Создать deployment-пользователя

```bash
adduser deploy
usermod -aG docker deploy
```

Создайте каталоги:

```bash
mkdir -p \
  /opt/findmydoc/deploy \
  /opt/findmydoc/production \
  /opt/findmydoc/staging \
  /opt/findmydoc/backups/production \
  /opt/findmydoc/backups/staging
```

Назначьте владельца:

```bash
chown -R deploy:deploy /opt/findmydoc
chmod 700 /opt/findmydoc/production
chmod 700 /opt/findmydoc/staging
chmod 700 /opt/findmydoc/backups
```

Создайте общую proxy-сеть:

```bash
docker network create findmydoc_proxy
```

---

# 25. Настроить SSH для GitHub Actions

На локальной машине создайте отдельный ключ:

```bash
ssh-keygen -t ed25519 -C "github-actions-findmydoc" -f ./findmydoc_deploy_key
```

Для автоматического deployment ключ должен быть без passphrase.

Скопируйте публичный ключ на сервер:

```bash
cat .\findmydoc_deploy_key.pub

```

Или вручную добавьте содержимое:

```text
findmydoc_deploy_key.pub
```

в:

```text
/home/deploy/.ssh/authorized_keys
```

Права:

```bash
chown -R deploy:deploy /home/deploy/.ssh
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys
```

Проверьте вход:

```bash
ssh -i ./findmydoc_deploy_key deploy@159.194.242.7

```

---

# 26. Настроить GitHub Environments и Secrets

В GitHub откройте:

```text
Repository
→ Settings
→ Environments
```

Создайте:

```text
production
staging
```

Для `production` при доступности этой функции включите required reviewers.

В каждом environment создайте одинаково названные secrets:

| Secret | Значение |
|---|---|
| `VPS_HOST` | IP или hostname VDS |
| `VPS_PORT` | `22` |
| `VPS_USER` | `deploy` |
| `VPS_SSH_PRIVATE_KEY` | содержимое приватного deployment-ключа | cat ./findmydoc_deploy_key.pub
| `VPS_KNOWN_HOSTS` | запись SSH host key |

Получить `VPS_KNOWN_HOSTS` можно локально:

```bash
ssh-keyscan -H 159.194.242.7
```

Лучше сначала вручную сверить fingerprint сервера:

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

После добавления ключа в GitHub удалите его локальную незашифрованную копию либо храните в защищенном password manager.

---

# 27. Авторизовать VDS в приватном GHCR

GitHub Actions сможет загружать private images через `GITHUB_TOKEN`. Но VDS нужен отдельный токен для скачивания.

https://github.com/settings/tokens
В GitHub создайте Personal Access Token с минимальным правом:

```text
read:packages
```

Для classic PAT:

```text
Settings
→ Developer settings
→ Personal access tokens
→ Tokens (classic)
```

На VDS под пользователем `deploy`:

```bash
su - deploy
```

Выполните:

```bash
echo "YOUR_GITHUB_PAT" \
  | docker login ghcr.io \
      --username YOUR_GITHUB_USERNAME \
      --password-stdin
```

Проверьте:

```bash
cat ~/.docker/config.json
```

Файл должен принадлежать `deploy`:

```bash
chmod 600 ~/.docker/config.json
```

Токен в environment-файлы помещать не нужно.

---

# 28. Создать server environment-файлы

## Генерация секретов

На VDS:

```bash
openssl rand -hex 48
```

Для PostgreSQL:

```bash
openssl rand -hex 32
```
Используйте буквенно-цифровой или hex-пароль. Это важно, потому что пароль подставляется непосредственно в PostgreSQL URL.

## Production Compose env

Создайте:

```bash
nano /opt/findmydoc/production/compose.env
```

Содержимое:

```dotenv
BACKEND_IMAGE=ghcr.io/YOUR_GITHUB_OWNER/YOUR_REPOSITORY-backend:main
FRONTEND_IMAGE=ghcr.io/YOUR_GITHUB_OWNER/YOUR_REPOSITORY-frontend:main

BACKEND_ENV_FILE=/opt/findmydoc/production/backend.env
FRONTEND_ENV_FILE=/opt/findmydoc/production/frontend.env

BACKEND_NETWORK_ALIAS=backend-prod
FRONTEND_NETWORK_ALIAS=frontend-prod

POSTGRES_USER=mentalme
POSTGRES_PASSWORD=Admin21i03i85@
POSTGRES_DB=mentalme
```

## Production backend env

```bash
nano /opt/findmydoc/production/backend.env
```

```dotenv
SECRET_KEY=GENERATED_LONG_SECRET
ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=1440
ROLE_SELECTION_TOKEN_EXPIRE_MINUTES=5
ACTION_TOKEN_EXPIRE_MINUTES=60
INVITATION_EXPIRE_HOURS=72

FRONTEND_URL=https://findmydoc.ru

WEBAUTHN_RP_ID=findmydoc.ru
WEBAUTHN_RP_NAME=FindMyDoc
WEBAUTHN_ORIGIN=https://findmydoc.ru
WEBAUTHN_CHALLENGE_EXPIRE_SECONDS=300

EMAIL_BACKEND=smtp
SMTP_HOST=smtp.beget.com
SMTP_PORT=465
SMTP_USERNAME=noreply@findmydoc.ru
SMTP_PASSWORD=REAL_MAILBOX_PASSWORD
SMTP_USE_SSL=true
SMTP_USE_STARTTLS=false
SMTP_TIMEOUT_SECONDS=15

EMAIL_FROM_ADDRESS=noreply@findmydoc.ru
EMAIL_FROM_NAME=FindMyDoc
```

## Production frontend env

```bash
nano /opt/findmydoc/production/frontend.env
```

```dotenv
NUXT_PUBLIC_API_BASE=https://findmydoc.ru
NUXT_PUBLIC_SITE_URL=https://findmydoc.ru

HOST=0.0.0.0
PORT=3000
NITRO_HOST=0.0.0.0
NITRO_PORT=3000
```

## Staging Compose env

```bash
nano /opt/findmydoc/staging/compose.env
```

```dotenv 
BACKEND_IMAGE=ghcr.io/YOUR_GITHUB_OWNER/YOUR_REPOSITORY-backend:develop
FRONTEND_IMAGE=ghcr.io/YOUR_GITHUB_OWNER/YOUR_REPOSITORY-frontend:develop

BACKEND_ENV_FILE=/opt/findmydoc/staging/backend.env
FRONTEND_ENV_FILE=/opt/findmydoc/staging/frontend.env

BACKEND_NETWORK_ALIAS=backend-staging
FRONTEND_NETWORK_ALIAS=frontend-staging

POSTGRES_USER=mentalme_staging  
POSTGRES_PASSWORD=ANOTHER_GENERATED_HEX_PASSWORD
POSTGRES_DB=mentalme_staging
```

## Staging backend env

```bash
nano /opt/findmydoc/staging/backend.env
```

```dotenv
SECRET_KEY=ANOTHER_GENERATED_LONG_SECRET
ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=1440
ROLE_SELECTION_TOKEN_EXPIRE_MINUTES=5
ACTION_TOKEN_EXPIRE_MINUTES=60
INVITATION_EXPIRE_HOURS=72

FRONTEND_URL=https://staging.findmydoc.ru

WEBAUTHN_RP_ID=staging.findmydoc.ru
WEBAUTHN_RP_NAME=FindMyDoc Staging
WEBAUTHN_ORIGIN=https://staging.findmydoc.ru
WEBAUTHN_CHALLENGE_EXPIRE_SECONDS=300

EMAIL_BACKEND=console

SMTP_HOST=smtp.beget.com
SMTP_PORT=465
SMTP_USERNAME=noreply@findmydoc.ru
SMTP_PASSWORD=
SMTP_USE_SSL=true
SMTP_USE_STARTTLS=false
SMTP_TIMEOUT_SECONDS=15

EMAIL_FROM_ADDRESS=noreply@findmydoc.ru
EMAIL_FROM_NAME=FindMyDoc Staging
```

## Staging frontend env

```bash
nano /opt/findmydoc/staging/frontend.env
```

```dotenv
NUXT_PUBLIC_API_BASE=https://staging.findmydoc.ru
NUXT_PUBLIC_SITE_URL=https://staging.findmydoc.ru

HOST=0.0.0.0
PORT=3000
NITRO_HOST=0.0.0.0
NITRO_PORT=3000
```

Установите права:

```bash
chmod 600 \
  /opt/findmydoc/production/*.env \
  /opt/findmydoc/staging/*.env

chown deploy:deploy \
  /opt/findmydoc/production/*.env \
  /opt/findmydoc/staging/*.env
```

---

# 29. Firewall

Сначала убедитесь, что SSH доступен.

```bash
ufw allow OpenSSH
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
ufw status
```

Если SSH работает на нестандартном порту:

```bash
ufw allow YOUR_SSH_PORT/tcp
```

Только после этого включайте UFW.

PostgreSQL-порт `5432` открывать не нужно. Он доступен только внутри Docker-сети.

---

# 30. Первый deployment

## Рекомендуемый порядок

### Шаг 1. Push в `develop`

```bash
git checkout develop
git merge main
git push origin develop 
```
```bash
git checkout develop
git merge main
git status 
git add .   
git commit -m "Fix deployment configuration"
git push origin develop
```

GitHub Actions:

- соберет backend;
- соберет frontend;
- загрузит образы в GHCR;
- скопирует `deploy/` на VDS;
- поднимет staging PostgreSQL;
- применит миграции;
- поднимет staging frontend/backend.

Nginx пока не запустится, потому что сертификатов еще нет.

### Шаг 2. Push в `main`

```bash
git checkout main
git push origin main
```

Будут подняты production PostgreSQL, frontend и backend.

### Шаг 3. Получить сертификаты

На VDS:

```bash
su - deploy
```

Затем:

```bash
chmod +x /opt/findmydoc/deploy/scripts/*.sh
```

Запустите:

```bash
/opt/findmydoc/deploy/scripts/init-letsencrypt.sh maxim-titkov@yandex.ru
```

Email здесь используется Let's Encrypt для уведомлений о сертификате. Это может быть не `noreply`, а ваш административный адрес.

После этого должны открываться:

```text
https://findmydoc.ru
https://www.findmydoc.ru
https://staging.findmydoc.ru
https://findmydoc.ru/docs
https://staging.findmydoc.ru/docs
```

---

# 31. Проверки после deployment

## Контейнеры production

```bash
cd /opt/findmydoc/deploy

docker compose \
  -p findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  --profile edge \
  ps
```

## Контейнеры staging

```bash
docker compose \
  -p findmydoc-staging \
  --env-file /opt/findmydoc/staging/compose.env \
  ps
```

## Логи backend

Production:

```bash
docker compose \
  -p findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  logs --tail=200 -f backend
```

Staging:

```bash
docker compose \
  -p findmydoc-staging \
  --env-file /opt/findmydoc/staging/compose.env \
  logs --tail=200 -f backend
```

## Логи Nginx

```bash
docker compose \
  -p findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  --profile edge \
  logs --tail=200 -f nginx
```

## Проверка API

```bash
curl -i https://findmydoc.ru/health/live
curl -i https://findmydoc.ru/health/ready
curl -i https://staging.findmydoc.ru/health/ready
```

## Проверка PostgreSQL

```bash
docker compose \
  -p findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  exec postgres \
  psql -U mentalme -d mentalme -c "\dt"
```

Проверка `pgcrypto`:

```bash
docker compose \
  -p findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  exec postgres \
  psql -U mentalme -d mentalme \
  -c "SELECT extname FROM pg_extension WHERE extname = 'pgcrypto';"
```

---

# 32. Настроить ежедневные backup

Под пользователем `deploy`:

```bash
crontab -e
```

Добавьте:

```cron
15 2 * * * /opt/findmydoc/deploy/scripts/backup.sh production >> /opt/findmydoc/backups/production/backup.log 2>&1
45 2 * * * /opt/findmydoc/deploy/scripts/backup.sh staging >> /opt/findmydoc/backups/staging/backup.log 2>&1
```

Это локальные backups на том же VDS. Для production этого недостаточно: поломка или удаление VDS уничтожит и базу, и backup.

Позже стоит добавить выгрузку в:

- Beget S3;
- другой S3-compatible storage;
- отдельный backup-сервер.

---

# 33. Как будет работать CI/CD

## Staging

```text
feature branch
    ↓
Pull Request в develop
    ↓
merge в develop
    ↓
сборка Docker images
    ↓
push в GHCR с тегами SHA и develop
    ↓
backup staging
    ↓
alembic upgrade head
    ↓
обновление staging frontend/backend
    ↓
https://staging.findmydoc.ru
```

## Production

```text
develop проверен
    ↓
Pull Request develop → main
    ↓
merge в main
    ↓
сборка Docker images
    ↓
push в GHCR с тегами SHA и main
    ↓
ручное подтверждение GitHub Environment, если включено
    ↓
backup production
    ↓
alembic upgrade head
    ↓
обновление production frontend/backend
    ↓
https://findmydoc.ru
```

Docker images разворачиваются по неизменяемому SHA:

```text
ghcr.io/owner/repository-backend:<commit-sha>
ghcr.io/owner/repository-frontend:<commit-sha>
```

Теги `main` и `develop` создаются только для удобства. Deployment использует SHA.

---

# 34. Важные замечания

1. **Не запускайте несколько backend workers.** Текущий WebSocket manager не поддерживает несколько процессов. Для масштабирования потребуется Redis Pub/Sub.

2. **Не запускайте seed автоматически при каждом deployment.** Иначе можно получить дубли или перезапись данных. Seed выполняйте отдельной ручной командой после проверки скриптов.

3. **Не удаляйте PostgreSQL volume при обновлении:**

   ```bash
   docker compose down
   ```

   допустимо, но:

   ```bash
   docker compose down -v
   ```

   удалит базу.

4. **SMTP работает синхронно.** Для текущей нагрузки это допустимо. В дальнейшем лучше вынести письма в очередь задач.

5. **SQLite и PostgreSQL немного различаются.** Перед production обязательно проверьте новую baseline migration на временном PostgreSQL.

6. **Production backup создается до миграции.** Но откат Docker image не всегда означает автоматический откат схемы БД. Для опасных миграций нужен отдельный rollback-план.

7. **Смена `SECRET_KEY` завершит все JWT-сессии.** Не генерируйте его при каждом deployment.

8. **Смена WebAuthn RP ID или домена может сделать passkeys недоступными.**

9. После настройки SMTP проверьте SPF, DKIM и DMARC в панели Beget. Иначе письма могут попадать в спам.