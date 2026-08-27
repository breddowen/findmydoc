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