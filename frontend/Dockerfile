# =============================================================================
# Intelligent Security Analytics Platform - Frontend Dockerfile
#
# Only needed if you want to deploy the frontend as a Docker
# container (e.g. to a VPS or Render's Docker service). If you're
# using Vercel or Netlify instead, you don't need this file at all -
# see SETUP_GUIDE.md.
#
# Build from the PROJECT ROOT (not from inside frontend/):
#     docker build -f frontend/Dockerfile \
#         --build-arg VITE_API_BASE_URL=https://your-backend-url.com \
#         -t isap-frontend .
#
# Run:
#     docker run -p 8080:80 isap-frontend
# =============================================================================

FROM node:20-alpine AS build

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ ./

ARG VITE_API_BASE_URL

ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
