# 🏨 Hotel Reservation Dashboard (HotelBoard)

A modern hotel guest service platform built with **React**, **Django**, and **Docker**.

Guests simply scan a **QR code** located in their hotel room and are taken directly to a web application where they can request hotel services without calling the front desk.

> **Purpose:** A portfolio project demonstrating production-style full-stack web development using modern React, Django, Docker, PostgreSQL, Redis, Celery, and Caddy.

---

# ✨ Features

## 🧹 Housekeeping

Guests can submit housekeeping requests such as:

- Clean room
- Change towels
- Refill amenities
- Make up room
- Remove Do Not Disturb

---

## 🔧 Engineering

Guests can report maintenance issues including:

- Air conditioner problems
- Door lock issues
- TV not working
- Broken lights
- Plumbing problems
- Electrical issues
- Furniture damage

---

## 🍽️ Room Service

Guests can order food and beverages directly from their room.

Examples include:

- Breakfast
- Lunch
- Dinner
- Drinks
- Desserts
- Snacks

---

# 🚀 Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- React Router
- Axios
- React Hook Form
- Zod
- TanStack Query
- TanStack Table
- Lucide React
- Sonner
- React Context API

## Backend

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Celery
- django-celery-beat
- Redis

## DevOps

- Docker
- Docker Compose
- Caddy
- Gunicorn

---

# 🏗️ Architecture

```
                    Guest
                      │
                      ▼
               Scan QR Code
                      │
                      ▼
                 Caddy Server
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    React Frontend         Django REST API
                                  │
              ┌───────────────────┼──────────────────┐
              ▼                   ▼                  ▼
         PostgreSQL            Redis            Celery Worker
                                                    │
                                                    ▼
                                              Celery Beat
```

---

# 🐳 Docker Services

The project is fully containerized using Docker Compose.

| Service    | Purpose                                    |
| ---------- | ------------------------------------------ |
| Backend    | Django + Gunicorn                          |
| PostgreSQL | Primary database                           |
| Redis      | Message broker and cache                   |
| Worker     | Celery background task worker              |
| Beat       | Celery scheduler                           |
| Caddy      | Reverse proxy and static/media file server |

---

# 🚀 Getting Started

## Requirements

- Docker
- Docker Compose

---

## Clone the repository

```bash
git clone https://github.com/flat07/hotelboard.git

cd hotelboard
```

---

## Create environment file

Create a file named:

```text
.env.development
```

Configure your environment variables.

---

## Build containers

```bash
docker compose build
```

---

## Start the application

```bash
docker compose up
```

Or run in detached mode:

```bash
docker compose up -d
```

---

## Run database migrations

```bash
docker compose exec backend python manage.py migrate
```

---

## Create a superuser

```bash
docker compose exec backend python manage.py createsuperuser
```

---

## Collect static files

```bash
docker compose exec backend python manage.py collectstatic --noinput
```

---

## Stop containers

```bash
docker compose down
```

---

# 📂 Project Structure

```
hotelboard/

├── backend/
│   ├── apps/
│   ├── config/
│   ├── tests/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── vite.config.ts
│
├── docker/
│   ├── backend/
│   └── caddy/
│
├── docker-compose.yml
├── .env.development
└── README.md
```

---

# 🎯 Project Goals

This project demonstrates:

- Production-ready Django architecture
- Modern React application development
- Feature-based frontend architecture
- RESTful API design
- JWT authentication
- Background task processing with Celery
- Scheduled tasks using Celery Beat
- Dockerized deployment
- Reverse proxy configuration using Caddy
- PostgreSQL database design
- Reusable UI components
- Form validation with React Hook Form and Zod
- Server state management using TanStack Query
- Automated testing using Pytest and Vitest

---

# 📸 Screenshots

Screenshots and GIFs will be added as development progresses.

---

# 🚧 Project Status

**Active Development**

Planned features include:

- ✅ Guest QR Code access
- ✅ Staff authentication
- 🚧 Housekeeping workflow
- 🚧 Engineering request tracking
- 🚧 Room service ordering
- 🚧 Background notifications
- 🚧 Request status updates
- 🚧 Admin dashboard
- 🚧 Search, filtering, and pagination
- 🚧 Responsive UI
- 🚧 Dark mode
- 🚧 CI/CD pipeline

---

# 🤝 Contributing

Contributions, suggestions, and issue reports are welcome.

---

# 📄 License

This project is licensed under the MIT License.
