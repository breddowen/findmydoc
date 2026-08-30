staging:
# 1. Переключиться на develop ДО внесения изменений
git switch develop
# 2. Получить актуальный develop
git pull --ff-only origin develop
# 3. ВНОСИШЬ ИЗМЕНЕНИЯ В КОД
# После изменений проверяешь:
git status
git diff
# 4. Коммитишь изменения
git add .
git commit -m "Описание изменений"
# 5. Отправляешь в develop
# Это должно запустить deployment на STAGING
git push origin develop

--- После проверки staging перенесите в production ---

# 6. Убедиться, что незакоммиченных файлов нет
git status
# 7. Получить актуальное состояние сервера
git fetch origin
# 8. Переключиться на main
git switch main
# 9. Обновить локальный main
git pull --ff-only origin main
# 10. Влить проверенный develop в main
git merge --no-ff origin/develop -m "Promote develop to production"
# 11. Отправить main
# Это должно запустить deployment на PRODUCTION
git push origin main

# После успешного production deployment возвращаемся в рабочую ветку:
git switch develop
git pull --ff-only origin develop

# FindMyDoc: развёртывание и эксплуатация

Полная инструкция по запуску FindMyDoc на новом VDS:

- настройка домена и DNS;
- установка Docker;
- создание deployment-пользователя;
- настройка GitHub Actions;
- первый запуск staging и production;
- выпуск TLS-сертификатов;
- создание первого superuser;
- публикация обновлений;
- работа с ветками `develop` и `main`;
- создание миграций Alembic;
- резервное копирование;
- смена домена;
- диагностика.

---

# 1. Где выполнять команды

В инструкции используются четыре разных окружения.

## 1.1. Локальный компьютер

Это Windows-компьютер разработчика с локальным Git-репозиторием.

Приглашение выглядит примерно так:

```text
PS F:\Projects\findmydoc>
```

Здесь выполняются:

```text
git switch
git status
git add
git commit
git merge
git push
ssh
scp
```

## 1.2. VDS под пользователем root

Приглашение:

```text
root@server:~#
```

Здесь выполняются:

- установка Docker;
- создание пользователя `deploy`;
- настройка каталогов;
- изменение владельцев через `chown`;
- первоначальное создание Docker networks и volumes;
- системная настройка.

Подключение:

```powershell
ssh root@VDS_IP
```

## 1.3. VDS под пользователем deploy

Приглашение:

```text
deploy@server:~$
```

Здесь выполняются:

- ручные команды Docker Compose;
- создание superuser;
- просмотр логов;
- запуск backup;
- диагностика приложения.

Подключение:

```powershell
ssh deploy@VDS_IP
```

## 1.4. GitHub

В браузере на GitHub настраиваются:

- GitHub Environments;
- GitHub Secrets;
- GitHub Actions;
- Container Registry packages;
- protection rules.

---

# 2. Архитектура

Проект использует два окружения.

| Git-ветка | Окружение | Домен | Compose project |
|---|---|---|---|
| `develop` | staging | `staging.findmydoc.ru` | `findmydoc-staging` |
| `main` | production | `findmydoc.ru` | `findmydoc-prod` |

У каждого окружения отдельные:

- PostgreSQL;
- PostgreSQL volume;
- backend;
- frontend;
- внутренняя Docker network;
- env-файлы;
- backup.

Общие для обоих окружений:

- Docker network `findmydoc_proxy`;
- Nginx;
- Certbot;
- volumes с TLS-сертификатами.

## Важная особенность Nginx

Отдельного staging-Nginx нет.

Один контейнер:

```text
findmydoc-prod-nginx-1
```

обслуживает сразу:

```text
https://findmydoc.ru
https://www.findmydoc.ru
https://staging.findmydoc.ru
```

Это нормально.

Нельзя запускать два Nginx-контейнера на портах `80` и `443`, потому что эти порты уже заняты общим Nginx.

Если удалить production Nginx, перестанут открываться и production, и staging, даже если staging backend и frontend остаются healthy.

---

# 3. Важное правило Git

Поток изменений всегда направлен так:

```text
локальные изменения
        ↓
develop
        ↓
staging
        ↓
проверка
        ↓
main
        ↓
production
```

То есть:

```text
develop → main
```

Не наоборот.

Команда:

```bash
git switch develop
git merge main
```

не публикует staging в production. Она переносит изменения из `main` в `develop`.

Для production нужно:

```bash
git switch main
git merge origin/develop
```

---

# 4. Домены и DNS

Для текущего проекта используются:

```text
findmydoc.ru
www.findmydoc.ru
staging.findmydoc.ru
```

В DNS должны быть записи:

| Тип | Имя | Значение |
|---|---|---|
| `A` | `@` | IP VDS |
| `A` | `www` | IP VDS |
| `A` | `staging` | IP VDS |

Пример:

```text
findmydoc.ru          → 159.194.242.7
www.findmydoc.ru      → 159.194.242.7
staging.findmydoc.ru  → 159.194.242.7
```

Проверка на локальном компьютере:

```powershell
nslookup findmydoc.ru
nslookup www.findmydoc.ru
nslookup staging.findmydoc.ru
```

Все домены должны возвращать IP нового VDS.

Обновление DNS может занять от нескольких минут до суток.

Не запускайте Let's Encrypt до обновления DNS.

---

# 5. Подготовка нового VDS

## 5.1. Подключение

На локальном компьютере:

```powershell
ssh root@VDS_IP
```

На VDS проверить:

```bash
whoami
```

Ожидается:

```text
root
```

## 5.2. Обновление системы

На VDS под `root`:

```bash
apt update
apt upgrade -y
```

Установить инструменты:

```bash
apt install -y \
  ca-certificates \
  curl \
  gnupg \
  rsync \
  openssl \
  ufw
```

## 5.3. Установка Docker

```bash
install -m 0755 -d /etc/apt/keyrings
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
```

```bash
chmod a+r /etc/apt/keyrings/docker.asc
```

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" \
  > /etc/apt/sources.list.d/docker.list
```

```bash
apt update
```

```bash
apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

```bash
systemctl enable --now docker
```

Проверить:

```bash
docker version
docker compose version
```

## 5.4. Firewall

Сначала разрешить SSH:

```bash
ufw allow 22/tcp
```

Разрешить HTTP и HTTPS:

```bash
ufw allow 80/tcp
ufw allow 443/tcp
```

Включить firewall:

```bash
ufw enable
```

Проверить:

```bash
ufw status
```

## 5.5. Создание пользователя deploy

```bash
adduser \
  --disabled-password \
  --gecos "" \
  deploy
```

Добавить его в группу Docker:

```bash
usermod -aG docker deploy
```

Проверить:

```bash
id deploy
```

В списке должна присутствовать группа:

```text
docker
```

---

# 6. Deployment SSH-ключ

## 6.1. Генерация ключа

Выполняется на локальном компьютере, вне Git-репозитория.

На Windows PowerShell:

```powershell
ssh-keygen `
  -t ed25519 `
  -C "github-actions-findmydoc" `
  -f "$HOME\.ssh\findmydoc_deploy_key"
```

На запрос passphrase дважды нажать Enter.

Создадутся:

```text
~/.ssh/findmydoc_deploy_key
~/.ssh/findmydoc_deploy_key.pub
```

Приватный файл:

```text
findmydoc_deploy_key
```

никогда нельзя добавлять в Git.

## 6.2. Установка публичного ключа

На локальном компьютере:

```powershell
scp `
  "$HOME\.ssh\findmydoc_deploy_key.pub" `
  root@VDS_IP:/tmp/findmydoc_deploy_key.pub
```

Подключиться как root:

```powershell
ssh root@VDS_IP
```

На VDS:

```bash
install -d \
  -o deploy \
  -g deploy \
  -m 700 \
  /home/deploy/.ssh
```

```bash
install \
  -o deploy \
  -g deploy \
  -m 600 \
  /tmp/findmydoc_deploy_key.pub \
  /home/deploy/.ssh/authorized_keys
```

```bash
rm -f /tmp/findmydoc_deploy_key.pub
```

Проверить:

```bash
ssh-keygen -lf /home/deploy/.ssh/authorized_keys
```

## 6.3. Проверка подключения

На локальном компьютере:

```powershell
ssh `
  -i "$HOME\.ssh\findmydoc_deploy_key" `
  -o IdentitiesOnly=yes `
  deploy@VDS_IP
```

На VDS:

```bash
whoami
```

Ожидается:

```text
deploy
```

---

# 7. Подготовка каталогов VDS

Выполняется на VDS под `root`.

```bash
install -d -o deploy -g deploy -m 755 \
  /opt/findmydoc
```

```bash
install -d -o deploy -g deploy -m 755 \
  /opt/findmydoc/deploy \
  /opt/findmydoc/staging \
  /opt/findmydoc/production
```

```bash
install -d -o deploy -g deploy -m 700 \
  /opt/findmydoc/backups \
  /opt/findmydoc/backups/staging \
  /opt/findmydoc/backups/production
```

Создать общую proxy network:

```bash
docker network inspect findmydoc_proxy >/dev/null 2>&1 \
  || docker network create findmydoc_proxy
```

Создать volumes для сертификатов:

```bash
docker volume inspect findmydoc_letsencrypt >/dev/null 2>&1 \
  || docker volume create findmydoc_letsencrypt
```

```bash
docker volume inspect findmydoc_certbot_www >/dev/null 2>&1 \
  || docker volume create findmydoc_certbot_www
```

---

# 8. Production env-файлы

Реальные env-файлы хранятся только на VDS:

```text
/opt/findmydoc/production/compose.env
/opt/findmydoc/production/backend.env
/opt/findmydoc/production/frontend.env
```

Они не должны находиться в Git.

## 8.1. Генерация production-секретов

На VDS под `root`:

```bash
PRODUCTION_POSTGRES_PASSWORD="$(openssl rand -hex 32)"
PRODUCTION_SECRET_KEY="$(openssl rand -hex 64)"
```

Для `POSTGRES_PASSWORD` рекомендуется hex-пароль.

Не используйте в PostgreSQL-пароле символы:

```text
@ : / # % $
```

если пароль напрямую подставляется в `DATABASE_URL`.

## 8.2. Production `compose.env`

```bash
cat > /opt/findmydoc/production/compose.env <<EOF
BACKEND_IMAGE=ghcr.io/GITHUB_OWNER/GITHUB_REPOSITORY-backend:latest
FRONTEND_IMAGE=ghcr.io/GITHUB_OWNER/GITHUB_REPOSITORY-frontend:latest

BACKEND_ENV_FILE=/opt/findmydoc/production/backend.env
FRONTEND_ENV_FILE=/opt/findmydoc/production/frontend.env

BACKEND_NETWORK_ALIAS=backend-prod
FRONTEND_NETWORK_ALIAS=frontend-prod

POSTGRES_USER=findmydoc
POSTGRES_PASSWORD=${PRODUCTION_POSTGRES_PASSWORD}
POSTGRES_DB=findmydoc
EOF
```

Заменить:

```text
GITHUB_OWNER
GITHUB_REPOSITORY
```

Например:

```text
ghcr.io/breddowen/findmydoc-backend:latest
```

## 8.3. Production `backend.env`

```bash
cat > /opt/findmydoc/production/backend.env <<EOF
SECRET_KEY=${PRODUCTION_SECRET_KEY}
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
EOF
```

Заменить:

```text
SMTP_PASSWORD=CHANGE_ME
```

реальным SMTP-паролем.

## 8.4. Production `frontend.env`

```bash
cat > /opt/findmydoc/production/frontend.env <<'EOF'
NUXT_PUBLIC_API_BASE=https://findmydoc.ru
NUXT_PUBLIC_SITE_URL=https://findmydoc.ru

HOST=0.0.0.0
PORT=3000
NITRO_HOST=0.0.0.0
NITRO_PORT=3000
EOF
```

---

# 9. Staging env-файлы

Файлы:

```text
/opt/findmydoc/staging/compose.env
/opt/findmydoc/staging/backend.env
/opt/findmydoc/staging/frontend.env
```

## 9.1. Генерация staging-секретов

```bash
STAGING_POSTGRES_PASSWORD="$(openssl rand -hex 32)"
STAGING_SECRET_KEY="$(openssl rand -hex 64)"
```

## 9.2. Staging `compose.env`

```bash
cat > /opt/findmydoc/staging/compose.env <<EOF
BACKEND_IMAGE=ghcr.io/GITHUB_OWNER/GITHUB_REPOSITORY-backend:develop
FRONTEND_IMAGE=ghcr.io/GITHUB_OWNER/GITHUB_REPOSITORY-frontend:develop

BACKEND_ENV_FILE=/opt/findmydoc/staging/backend.env
FRONTEND_ENV_FILE=/opt/findmydoc/staging/frontend.env

BACKEND_NETWORK_ALIAS=backend-staging
FRONTEND_NETWORK_ALIAS=frontend-staging

POSTGRES_USER=findmydoc_staging
POSTGRES_PASSWORD=${STAGING_POSTGRES_PASSWORD}
POSTGRES_DB=findmydoc_staging
EOF
```

## 9.3. Staging `backend.env`

```bash
cat > /opt/findmydoc/staging/backend.env <<EOF
SECRET_KEY=${STAGING_SECRET_KEY}
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
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_USE_SSL=true
SMTP_USE_STARTTLS=false
SMTP_TIMEOUT_SECONDS=15

EMAIL_FROM_ADDRESS=noreply@findmydoc.ru
EMAIL_FROM_NAME=FindMyDoc Staging
EOF
```

## 9.4. Staging `frontend.env`

```bash
cat > /opt/findmydoc/staging/frontend.env <<'EOF'
NUXT_PUBLIC_API_BASE=https://staging.findmydoc.ru
NUXT_PUBLIC_SITE_URL=https://staging.findmydoc.ru

HOST=0.0.0.0
PORT=3000
NITRO_HOST=0.0.0.0
NITRO_PORT=3000
EOF
```

## 9.5. Права

```bash
chown -R deploy:deploy \
  /opt/findmydoc/staging \
  /opt/findmydoc/production
```

```bash
chmod 700 \
  /opt/findmydoc/staging \
  /opt/findmydoc/production
```

```bash
chmod 600 \
  /opt/findmydoc/staging/*.env \
  /opt/findmydoc/production/*.env
```

```bash
unset PRODUCTION_POSTGRES_PASSWORD
unset PRODUCTION_SECRET_KEY
unset STAGING_POSTGRES_PASSWORD
unset STAGING_SECRET_KEY
```

---

# 10. Доступ к приватным GHCR-образам

Если GHCR packages публичные, раздел можно пропустить.

Для приватных packages нужен GitHub token с правом:

```text
read:packages
```

На VDS войти под `deploy`:

```bash
su - deploy
```

```bash
read -r -s -p "GitHub package token: " GHCR_TOKEN
echo
```

```bash
printf '%s' "$GHCR_TOKEN" \
  | docker login ghcr.io \
      --username GITHUB_USERNAME \
      --password-stdin
```

```bash
unset GHCR_TOKEN
```

Ожидается:

```text
Login Succeeded
```

---

# 11. GitHub Environments

В GitHub открыть:

```text
Repository
→ Settings
→ Environments
```

Создать:

```text
staging
production
```

В каждом Environment создать secrets:

| Secret | Значение |
|---|---|
| `VPS_HOST` | IP или hostname, без `deploy@` |
| `VPS_PORT` | `22` |
| `VPS_USER` | `deploy` |
| `VPS_SSH_PRIVATE_KEY` | приватный deployment-ключ |
| `VPS_KNOWN_HOSTS` | SSH host keys VDS |

Правильно:

```text
VPS_HOST=159.194.242.7
VPS_USER=deploy
```

Неправильно:

```text
VPS_HOST=root@159.194.242.7
```

Неправильно:

```text
VPS_HOST=deploy@159.194.242.7
```

## Приватный ключ

На Windows:

```powershell
Get-Content `
  -Raw `
  "$HOME\.ssh\findmydoc_deploy_key" |
  Set-Clipboard
```

Вставить в `VPS_SSH_PRIVATE_KEY`.

## `known_hosts`

На Windows:

```powershell
ssh-keyscan -p 22 VDS_IP 2>$null
```

Скопировать весь вывод в `VPS_KNOWN_HOSTS`.

---

# 12. Первый запуск нового Git-репозитория

Этот раздел выполняется только один раз.

Перед началом GitHub Repository и GitHub Environments уже должны быть созданы.

## 12.1. Проверка секретов

На локальном компьютере:

```powershell
git status
```

Проверить, что среди файлов нет:

- `.env`;
- deployment private keys;
- базы данных;
- TLS-сертификатов;
- backup;
- production-паролей.

## 12.2. Создание main

```powershell
git init
```

```powershell
git switch -c main
```

```powershell
git add .
```

После `git add .` обязательно проверить:

```powershell
git status
```

```powershell
git diff --cached --stat
```

Проверить приватные ключи:

```powershell
git diff --cached --name-only |
    Select-String "deploy_key|id_ed25519|private"
```

Команда не должна ничего вывести.

Создать commit:

```powershell
git commit -m "Initial project"
```

Добавить remote:

```powershell
git remote add origin git@github.com:GITHUB_OWNER/GITHUB_REPOSITORY.git
```

Отправить именно текущий commit в `main`:

```powershell
git push -u origin HEAD:main
```

`HEAD:main` означает:

```text
текущий локальный commit → удалённая ветка main
```

## 12.3. Создание develop

```powershell
git switch -c develop
```

Проверить:

```powershell
git branch --show-current
```

Ожидается:

```text
develop
```

Отправить:

```powershell
git push -u origin HEAD:develop
```

После первого push:

- `main` запускает production deployment;
- `develop` запускает staging deployment.

---

# 13. Первый deployment

Порядок:

1. дождаться успешного production deployment;
2. дождаться успешного staging deployment;
3. убедиться, что backend/frontend обоих окружений работают;
4. выпустить TLS-сертификаты;
5. запустить общий Nginx.

Проверить контейнеры:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}"
```

До выпуска сертификатов должны работать:

```text
findmydoc-prod-postgres-1
findmydoc-prod-backend-1
findmydoc-prod-frontend-1

findmydoc-staging-postgres-1
findmydoc-staging-backend-1
findmydoc-staging-frontend-1
```

---

# 14. Выпуск TLS-сертификатов

Проверить DNS:

```bash
dig +short findmydoc.ru
dig +short www.findmydoc.ru
dig +short staging.findmydoc.ru
```

Подключиться как `deploy`:

```powershell
ssh deploy@VDS_IP
```

```bash
chmod +x /opt/findmydoc/deploy/scripts/*.sh
```

Запустить:

```bash
/opt/findmydoc/deploy/scripts/init-letsencrypt.sh \
  admin@findmydoc.ru
```

Проверить контейнеры:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Должны появиться:

```text
findmydoc-prod-nginx-1
findmydoc-prod-certbot-1
```

Проверить:

```bash
curl -I https://findmydoc.ru
curl -I https://staging.findmydoc.ru
```

---

# 15. Создание первого superuser

Production и staging имеют разные базы данных.

Поэтому superuser создаётся отдельно в каждом окружении.

Нельзя запускать в production:

```text
backend/seed/upload_users.py
```

Он содержит тестовых пользователей и тестовые пароли.

Используется:

```text
backend/seed/create_superuser.py
```

## 15.1. Важная проверка версии образа

Скрипт должен сначала попасть в нужную Git-ветку, затем GitHub Actions должен пересобрать Docker-образ.

Если скрипт есть в `develop`, но изменения ещё не перенесены в `main`, то:

- staging-образ содержит скрипт;
- production-образ не содержит скрипт.

Тогда production выдаст:

```text
python: can't open file '/app/seed/create_superuser.py'
```

Это означает, что актуальный `develop` ещё не был корректно перенесён в `main`.

## 15.2. Проверка скрипта в staging-образе

На VDS под `deploy`:

```bash
cd /opt/findmydoc/deploy
```

```bash
docker compose \
  --project-name findmydoc-staging \
  --env-file /opt/findmydoc/staging/compose.env \
  run --rm \
  backend \
  test -f /app/seed/create_superuser.py
```

Если команда завершилась без ошибки, файл присутствует.

## 15.3. Создание staging superuser

```bash
read -r -p "Superuser email: " \
  BOOTSTRAP_SUPERUSER_EMAIL
```

```bash
read -r -s -p "Superuser password: " \
  BOOTSTRAP_SUPERUSER_PASSWORD
echo
```

```bash
BOOTSTRAP_SUPERUSER_FIRST_NAME="Главный"
BOOTSTRAP_SUPERUSER_LAST_NAME="Администратор"
```

```bash
export BOOTSTRAP_SUPERUSER_EMAIL
export BOOTSTRAP_SUPERUSER_PASSWORD
export BOOTSTRAP_SUPERUSER_FIRST_NAME
export BOOTSTRAP_SUPERUSER_LAST_NAME
```

```bash
docker compose \
  --project-name findmydoc-staging \
  --env-file /opt/findmydoc/staging/compose.env \
  run --rm \
  -e BOOTSTRAP_SUPERUSER_EMAIL \
  -e BOOTSTRAP_SUPERUSER_PASSWORD \
  -e BOOTSTRAP_SUPERUSER_FIRST_NAME \
  -e BOOTSTRAP_SUPERUSER_LAST_NAME \
  backend \
  python seed/create_superuser.py
```

Ожидается:

```text
Superuser created: admin@example.com
```

Очистить:

```bash
unset BOOTSTRAP_SUPERUSER_EMAIL
unset BOOTSTRAP_SUPERUSER_PASSWORD
unset BOOTSTRAP_SUPERUSER_FIRST_NAME
unset BOOTSTRAP_SUPERUSER_LAST_NAME
```

## 15.4. Создание production superuser

Сначала убедиться, что deployment ветки `main` успешно завершён.

Проверить скрипт:

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  run --rm \
  backend \
  test -f /app/seed/create_superuser.py
```

Если команда завершилась успешно, заново ввести email и пароль:

```bash
read -r -p "Superuser email: " \
  BOOTSTRAP_SUPERUSER_EMAIL
```

```bash
read -r -s -p "Superuser password: " \
  BOOTSTRAP_SUPERUSER_PASSWORD
echo
```

```bash
BOOTSTRAP_SUPERUSER_FIRST_NAME="Главный"
BOOTSTRAP_SUPERUSER_LAST_NAME="Администратор"
```

```bash
export BOOTSTRAP_SUPERUSER_EMAIL
export BOOTSTRAP_SUPERUSER_PASSWORD
export BOOTSTRAP_SUPERUSER_FIRST_NAME
export BOOTSTRAP_SUPERUSER_LAST_NAME
```

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  run --rm \
  -e BOOTSTRAP_SUPERUSER_EMAIL \
  -e BOOTSTRAP_SUPERUSER_PASSWORD \
  -e BOOTSTRAP_SUPERUSER_FIRST_NAME \
  -e BOOTSTRAP_SUPERUSER_LAST_NAME \
  backend \
  python seed/create_superuser.py
```

Очистить:

```bash
unset BOOTSTRAP_SUPERUSER_EMAIL
unset BOOTSTRAP_SUPERUSER_PASSWORD
unset BOOTSTRAP_SUPERUSER_FIRST_NAME
unset BOOTSTRAP_SUPERUSER_LAST_NAME
```

---

# 16. Обычная публикация изменений в staging

Этот раздел выполняется для каждого обновления.

## 16.1. Перейти в develop

На локальном компьютере:

```powershell
git switch develop
```

Сразу проверить:

```powershell
$branch = git branch --show-current

if ($branch.Trim() -ne "develop") {
    throw "Current branch is not develop"
}
```

Если `git switch develop` завершился ошибкой, нельзя продолжать.

## 16.2. Проверить локальные изменения

```powershell
git status
```

Если есть незакоммиченные изменения, нужно либо:

- завершить их и закоммитить;
- отменить;
- временно положить в stash.

Сохранение в stash:

```powershell
git stash push -u -m "WIP before branch operation"
```

После этого:

```powershell
git status
```

должен показывать чистый рабочий каталог.

## 16.3. Получить актуальный develop

Только после проверки текущей ветки:

```powershell
git pull --ff-only origin develop
```

Если команда завершилась ошибкой:

```text
Not possible to fast-forward
```

нельзя выполнять следующие команды вслепую.

Нужно проверить:

```powershell
git status
git log --oneline --decorate --graph --all -15
```

## 16.4. Внести изменения

После редактирования:

```powershell
git status
```

Желательно добавлять конкретные файлы:

```powershell
git add backend/app/path/file.py
git add frontend/app/path/file.vue
```

Можно использовать:

```powershell
git add .
```

но только с последующей обязательной проверкой:

```powershell
git status
```

```powershell
git diff --cached --name-only
```

```powershell
git diff --cached
```

Проверить отсутствие ключей:

```powershell
git diff --cached --name-only |
    Select-String "deploy_key|id_ed25519|private"
```

Если команда нашла приватный ключ, commit создавать нельзя.

## 16.5. Commit

```powershell
git commit -m "Описание изменения"
```

## 16.6. Push именно в staging

Ещё раз проверить ветку:

```powershell
$branch = git branch --show-current

if ($branch.Trim() -ne "develop") {
    throw "Refusing staging push: current branch is not develop"
}
```

Отправить текущий commit именно в удалённый `develop`:

```powershell
git push origin HEAD:develop
```

Не использовать здесь:

```powershell
git push origin main
```

Проверить GitHub Actions и staging:

```text
https://staging.findmydoc.ru
```

---

# 17. Публикация проверенного staging в production

К этому разделу переходить только после успешного staging.

## 17.1. Рабочий каталог должен быть чистым

```powershell
git status
```

Если есть изменения, не переключать ветку.

Их нужно:

- закоммитить в `develop`;
- отменить;
- либо временно сохранить в stash.

Безопасный stash:

```powershell
git stash push -u -m "WIP before production promotion"
```

После этого:

```powershell
git status
```

должен быть чистым.

## 17.2. Получить удалённые ветки

```powershell
git fetch origin
```

## 17.3. Переключиться на main

```powershell
git switch main
```

Обязательно проверить результат:

```powershell
$branch = git branch --show-current

if ($branch.Trim() -ne "main") {
    throw "Current branch is not main. Production promotion stopped."
}
```

Если `git switch main` написал:

```text
Your local changes would be overwritten by checkout
```

переключение не состоялось.

Нельзя после этого выполнять:

```powershell
git pull origin main
git merge develop
git push origin main
```

Сначала нужно очистить рабочий каталог.

## 17.4. Обновить main

Только находясь в `main`:

```powershell
git pull --ff-only origin main
```

Если команда завершилась ошибкой, остановиться и проверить историю:

```powershell
git status
git log --oneline --decorate --graph --all -20
```

## 17.5. Перенести develop в main

Использовать актуальную удалённую ветку:

```powershell
git merge --no-ff origin/develop `
  -m "Promote develop to production"
```

Если merge сообщил конфликт или ошибку, push выполнять нельзя.

Проверить:

```powershell
git status
```

```powershell
git log --oneline --decorate -5
```

Проверить наличие важных файлов:

```powershell
git ls-tree -r HEAD --name-only |
    Select-String "^backend/seed/create_superuser.py$"
```

## 17.6. Push именно в production

Ещё раз проверить ветку:

```powershell
$branch = git branch --show-current

if ($branch.Trim() -ne "main") {
    throw "Refusing production push: current branch is not main"
}
```

Отправить текущий commit именно в удалённый `main`:

```powershell
git push origin HEAD:main
```

Дождаться успешного GitHub Actions.

Проверить:

```text
https://findmydoc.ru
```

## 17.7. Вернуться в develop

```powershell
git switch develop
```

Проверить:

```powershell
git branch --show-current
```

Ожидается:

```text
develop
```

```powershell
git pull --ff-only origin develop
```

---

# 18. Краткая безопасная памятка Git

## Staging

```powershell
git switch develop

$branch = git branch --show-current
if ($branch.Trim() -ne "develop") {
    throw "Not on develop"
}

git pull --ff-only origin develop

# Редактирование файлов

git status
git add <конкретные-файлы>
git diff --cached
git commit -m "Описание"
git push origin HEAD:develop
```

## Production

```powershell
git status
```

Рабочий каталог должен быть чистым.

```powershell
git fetch origin
git switch main

$branch = git branch --show-current
if ($branch.Trim() -ne "main") {
    throw "Not on main"
}

git pull --ff-only origin main
git merge --no-ff origin/develop `
  -m "Promote develop to production"

git push origin HEAD:main
git switch develop
```

---

# 19. Если ветка не переключается

Ошибка:

```text
Your local changes would be overwritten by checkout
```

означает, что текущие незакоммиченные файлы мешают переключению.

Посмотреть:

```powershell
git status
git diff
```

Вариант 1 — закоммитить изменение в текущую ветку:

```powershell
git add <file>
git commit -m "Описание"
```

Вариант 2 — отменить изменение:

```powershell
git restore <file>
```

Вариант 3 — временно сохранить:

```powershell
git stash push -u -m "Temporary local changes"
```

После переключения посмотреть stash:

```powershell
git stash list
```

```powershell
git stash show -p 'stash@{0}'
```

Применять stash следует в той ветке, для которой делались изменения:

```powershell
git switch develop
git stash pop
```

---

# 20. Если `git pull --ff-only` не работает

Ошибка:

```text
fatal: Not possible to fast-forward, aborting
```

означает, что локальная и удалённая ветки разошлись.

Нельзя сразу выполнять случайный merge или reset.

Сначала:

```powershell
git branch --show-current
git status
git fetch origin
git log --oneline --decorate --graph --all -20
```

Если локальные commits не нужны и все изменения уже сохранены в stash или GitHub, локальную ветку можно сбросить.

Для `main`:

```powershell
git switch main
git reset --hard origin/main
```

Для `develop`:

```powershell
git switch develop
git reset --hard origin/develop
```

`reset --hard` удаляет незакоммиченные изменения и локальные commits, поэтому его можно выполнять только после проверки и сохранения нужной работы.

---

# 21. Изменение структуры базы данных

Все изменения структуры БД выполняются через Alembic.

## 21.1. Изменить SQLModel-модель

Например:

```python
class User(SQLModel, table=True):
    new_field: str | None = Field(default=None)
```

## 21.2. Запустить локальный PostgreSQL

```powershell
docker run `
  --name findmydoc-migration-db `
  --detach `
  --rm `
  -e POSTGRES_USER=findmydoc `
  -e POSTGRES_PASSWORD=findmydoc_local `
  -e POSTGRES_DB=findmydoc `
  -p 5433:5432 `
  postgres:17-bookworm
```

## 21.3. Подготовить Python

Из корня проекта:

```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
pip install -r backend/requirements.txt
```

## 21.4. Указать DATABASE_URL

```powershell
$env:DATABASE_URL = "postgresql+psycopg://findmydoc:findmydoc_local@localhost:5433/findmydoc"
```

```powershell
cd backend
```

Применить существующие миграции:

```powershell
alembic upgrade head
```

## 21.5. Создать миграцию

После изменения моделей:

```powershell
alembic revision `
  --autogenerate `
  -m "add new field to users"
```

Будет создан файл:

```text
backend/alembic/versions/<revision>_add_new_field_to_users.py
```

Обязательно проверить:

```python
def upgrade():
    ...
```

```python
def downgrade():
    ...
```

## 21.6. Проверить миграцию

```powershell
alembic upgrade head
```

```powershell
alembic current
```

```powershell
alembic history
```

Если downgrade безопасен:

```powershell
alembic downgrade -1
alembic upgrade head
```

## 21.7. Commit миграции

Вернуться в корень проекта:

```powershell
cd ..
```

Убедиться, что текущая ветка `develop`:

```powershell
git switch develop
```

Добавить модель и миграцию:

```powershell
git add backend/app/modules/users/models.py
git add backend/alembic/versions/<migration_file>.py
```

Проверить:

```powershell
git diff --cached
```

Создать commit:

```powershell
git commit -m "Add database migration"
```

Отправить в staging:

```powershell
git push origin HEAD:develop
```

Deployment автоматически:

1. поднимет PostgreSQL;
2. создаст backup;
3. выполнит `alembic upgrade head`;
4. запустит новую версию backend.

Только после проверки staging миграция переносится в production через обычный merge `develop → main`.

## Правила миграций

1. Не изменять старую миграцию, уже применённую на сервере.
2. Для нового изменения создавать новую миграцию.
3. Модель и миграцию коммитить вместе.
4. Всегда проверять сгенерированный SQL.
5. Сначала применять на staging.
6. Только затем переносить в production.
7. Не удалять колонки и таблицы без backup и отдельной проверки.

---

# 22. Backup

Ручной staging backup:

```bash
/opt/findmydoc/deploy/scripts/backup.sh staging
```

Production backup:

```bash
/opt/findmydoc/deploy/scripts/backup.sh production
```

Файлы находятся:

```text
/opt/findmydoc/backups/staging
/opt/findmydoc/backups/production
```

Проверка:

```bash
find /opt/findmydoc/backups \
  -type f \
  -name '*.sql.gz' \
  -ls
```

Backup старше `14` дней удаляются автоматически.

---

# 23. Смена домена

Допустим:

```text
Старый домен: findmydoc.ru
Новый домен: newdomain.ru
Новый staging: staging.newdomain.ru
```

## 23.1. DNS

Создать:

```text
newdomain.ru          → VDS IP
www.newdomain.ru      → VDS IP
staging.newdomain.ru  → VDS IP
```

Проверить:

```bash
dig +short newdomain.ru
dig +short www.newdomain.ru
dig +short staging.newdomain.ru
```

## 23.2. Найти упоминания старого домена

На локальном компьютере:

```powershell
git grep -n "findmydoc\.ru"
```

Как минимум изменить:

```text
deploy/nginx/default.conf
deploy/scripts/deploy.sh
deploy/scripts/init-letsencrypt.sh
```

## 23.3. Изменить env-файлы на VDS

Production `backend.env`:

```env
FRONTEND_URL=https://newdomain.ru
WEBAUTHN_RP_ID=newdomain.ru
WEBAUTHN_ORIGIN=https://newdomain.ru
EMAIL_FROM_ADDRESS=noreply@newdomain.ru
```

Production `frontend.env`:

```env
NUXT_PUBLIC_API_BASE=https://newdomain.ru
NUXT_PUBLIC_SITE_URL=https://newdomain.ru
```

Staging `backend.env`:

```env
FRONTEND_URL=https://staging.newdomain.ru
WEBAUTHN_RP_ID=staging.newdomain.ru
WEBAUTHN_ORIGIN=https://staging.newdomain.ru
```

Staging `frontend.env`:

```env
NUXT_PUBLIC_API_BASE=https://staging.newdomain.ru
NUXT_PUBLIC_SITE_URL=https://staging.newdomain.ru
```

## 23.4. Развернуть через develop

```powershell
git switch develop
git pull --ff-only origin develop
```

Изменить файлы, затем:

```powershell
git add deploy/nginx/default.conf
git add deploy/scripts/deploy.sh
git add deploy/scripts/init-letsencrypt.sh
git commit -m "Change application domain"
git push origin HEAD:develop
```

После успешного staging:

```powershell
git fetch origin
git switch main
git pull --ff-only origin main
git merge --no-ff origin/develop `
  -m "Promote domain change to production"
git push origin HEAD:main
```

## 23.5. Выпустить сертификаты нового домена

На VDS остановить только Nginx:

```bash
docker rm -f findmydoc-prod-nginx-1 2>/dev/null || true
```

Запустить обновлённый скрипт:

```bash
/opt/findmydoc/deploy/scripts/init-letsencrypt.sh \
  admin@newdomain.ru
```

Проверить:

```bash
curl -I https://newdomain.ru
curl -I https://staging.newdomain.ru
```

---

# 24. Управление Nginx

Проверить:

```bash
docker ps --filter name=nginx
```

Запустить общий Nginx:

```bash
cd /opt/findmydoc/deploy
```

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  --profile edge \
  up -d nginx certbot
```

Проверить конфигурацию:

```bash
docker exec \
  findmydoc-prod-nginx-1 \
  nginx -t
```

Посмотреть логи:

```bash
docker logs \
  --tail 100 \
  findmydoc-prod-nginx-1
```

## Не удалять общий Nginx без необходимости

Следующая команда удаляет общий Nginx и отключает оба сайта:

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  --profile edge \
  down
```

Для перезапуска только backend лучше использовать:

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  restart backend
```

---

# 25. Диагностика

Все контейнеры:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Включая остановленные:

```bash
docker ps -a --format "table {{.Names}}\t{{.Status}}"
```

Staging backend:

```bash
docker logs \
  --tail 100 \
  findmydoc-staging-backend-1
```

Production backend:

```bash
docker logs \
  --tail 100 \
  findmydoc-prod-backend-1
```

Nginx:

```bash
docker logs \
  --tail 100 \
  findmydoc-prod-nginx-1
```

Порты:

```bash
ss -lntp | grep -E ':80 |:443 '
```

Сайты:

```bash
curl -I https://findmydoc.ru
curl -I https://staging.findmydoc.ru
```

---

# 26. Частые ошибки

<details>
<summary>SSH Permission denied</summary>

Проверить:

```text
VPS_HOST содержит только IP/hostname
VPS_USER=deploy
VPS_PORT=22
```

Проверить права:

```bash
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys
chown -R deploy:deploy /home/deploy/.ssh
```

</details>

<details>
<summary>failed to resolve host '@postgres'</summary>

Причина — символ `@` в PostgreSQL-пароле.

Использовать:

```bash
openssl rand -hex 32
```

Если PostgreSQL volume уже создан, изменение `compose.env` само по себе не меняет пароль внутри существующей базы.

</details>

<details>
<summary>rsync code 23</summary>

Проверить владельца:

```bash
chown -R deploy:deploy /opt/findmydoc/deploy
```

Проверить SQL-файл:

```bash
file /opt/findmydoc/deploy/postgres/init/01-enable-pgcrypto.sql
```

Это должен быть файл, не директория.

</details>

<details>
<summary>services.services must be a mapping</summary>

В `docker-compose.yml` нарушены отступы или дважды указан `services:`.

Проверить локально:

```bash
docker compose \
  -f deploy/docker-compose.yml \
  config --quiet
```

</details>

<details>
<summary>Staging backend healthy, но сайт не открывается</summary>

Проверить общий Nginx:

```bash
docker ps --filter name=nginx
```

Если его нет:

```bash
docker compose \
  --project-name findmydoc-prod \
  --env-file /opt/findmydoc/production/compose.env \
  --profile edge \
  up -d nginx certbot
```

</details>

<details>
<summary>create_superuser.py найден в staging, но не найден в production</summary>

Причина:

```text
develop содержит новый файл
main ещё не содержит новый файл
```

Нужно корректно выполнить:

```powershell
git fetch origin
git switch main
git pull --ff-only origin main
git merge --no-ff origin/develop `
  -m "Promote develop to production"
git push origin HEAD:main
```

Перед merge обязательно убедиться, что текущая ветка действительно `main`.

</details>

---

# 27. Безопасность

Никогда не добавлять в Git:

- приватные SSH-ключи;
- env-файлы;
- PostgreSQL-пароли;
- `SECRET_KEY`;
- SMTP-пароли;
- TLS private keys;
- backup базы;
- production seed с паролями.

Перед каждым commit:

```powershell
git status
git diff --cached --name-only
git diff --cached
```

Проверка ключей:

```powershell
git ls-files |
    Select-String "deploy_key|id_ed25519|private"
```

Если приватный ключ попал в Git:

1. немедленно создать новый ключ;
2. заменить `/home/deploy/.ssh/authorized_keys`;
3. заменить GitHub Secrets;
4. удалить старый ключ из текущего состояния репозитория;
5. считать старый ключ скомпрометированным навсегда.

---

# 28. Итоговая памятка

## Новое изменение

```text
1. Перейти в develop.
2. Убедиться, что текущая ветка develop.
3. Получить origin/develop.
4. Изменить код.
5. Проверить git status.
6. Добавить файлы.
7. Проверить git diff --cached.
8. Создать commit.
9. Push HEAD:develop.
10. Проверить staging.
```

## Production release

```text
1. Убедиться, что staging работает.
2. Убедиться, что рабочий каталог чистый.
3. Выполнить git fetch origin.
4. Переключиться на main.
5. Проверить, что текущая ветка main.
6. Получить origin/main.
7. Слить origin/develop в main.
8. Проверить результат merge.
9. Push HEAD:main.
10. Дождаться GitHub Actions.
11. Проверить production.
12. Вернуться в develop.
```

Главное правило:

```text
develop → staging → проверка → main → production
```