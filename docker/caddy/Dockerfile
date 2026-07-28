# docker/caddy/Dockerfile
###############################################
# Stage 1
###############################################

FROM node:22-alpine AS frontend-builder

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ .

RUN npm run build


###############################################
# Stage 2
###############################################

FROM caddy:2-alpine

COPY docker/caddy/Caddyfile /etc/caddy/Caddyfile

COPY --from=frontend-builder /app/dist /srv
