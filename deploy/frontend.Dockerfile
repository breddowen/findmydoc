FROM node:24.15.0-bookworm-slim AS builder

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm ci --include=dev

COPY frontend/ ./

ENV NODE_ENV=production

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