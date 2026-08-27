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