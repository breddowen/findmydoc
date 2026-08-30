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
      -subj "/CN=findmydoc.ru"
  '

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
      -subj "/CN=staging.findmydoc.ru"

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
  rm -rf \
    /etc/letsencrypt/live/findmydoc.ru \
    /etc/letsencrypt/archive/findmydoc.ru \
    /etc/letsencrypt/renewal/findmydoc.ru.conf \
    /etc/letsencrypt/live/staging.findmydoc.ru \
    /etc/letsencrypt/archive/staging.findmydoc.ru \
    /etc/letsencrypt/renewal/staging.findmydoc.ru.conf

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

echo "Let Encrypt initialization completed."