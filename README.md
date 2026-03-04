# TaskFlow

**Manage your tasks efficiently. Simple, fast, and containerized.**

TaskFlow is a Django-based task management web application built with modern DevOps practices. It supports user authentication, task creation with priorities and categories, commenting, and is fully containerized with Docker and deployed on a cloud server with HTTPS.

---

## Features

- User registration, login, and logout
- Create, read, update, and delete tasks (full CRUD)
- Assign priority levels: Low, Medium, High
- Track task status: Pending, In Progress, Done
- Organize tasks with categories (many-to-many)
- Add comments to tasks
- Admin panel for management
- Responsive UI with Bootstrap
- Static and media file handling

---

## Technologies Used

| Layer | Technology |
|---|---|
| Backend | Django 4.2, Gunicorn |
| Database | PostgreSQL 15 |
| Web Server | Nginx 1.25 |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| Cloud | GCP (Google Cloud Platform) |
| SSL | Self-signed certificate (HTTPS) |

---

## Database Schema

- **User** (Django built-in)
- **Category** — belongs to a User (many-to-one), has color and name
- **Task** — belongs to a User (many-to-one), has many Categories (many-to-many), priority, status, due date
- **Comment** — belongs to a Task (many-to-one) and a User (many-to-one)

---

## Local Setup Instructions

### Prerequisites

- Docker and Docker Compose installed
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Ninja00015651/todoapp.git
cd todoapp

# 2. Copy environment file
cp .env.example .env

# 3. Edit .env with your values
# (see Environment Variables section below)

# 4. Start with development compose
docker compose -f docker-compose.dev.yml up --build

# 5. Access the app
# http://localhost:8000
```

---

## Deployment Instructions

```bash
# 1. SSH into your server
ssh user@your-server-ip

# 2. Clone the repo
git clone https://github.com/Ninja00015651/todoapp.git /opt/todoapp
cd /opt/todoapp

# 3. Create .env file
cp .env.example .env
nano .env  # fill in production values

# 4. Start all services
docker compose up -d

# 5. Access the app
# https://your-server-ip
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | `django-insecure-...` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hosts | `35.242.212.39,localhost` |
| `POSTGRES_DB` | Database name | `todoapp` |
| `POSTGRES_USER` | Database user | `todoapp` |
| `POSTGRES_PASSWORD` | Database password | `strongpassword` |
| `POSTGRES_HOST` | Database host | `db` |
| `DOCKERHUB_USERNAME` | Docker Hub username | `muzaffar04` |

---

## CI/CD Pipeline

On every push to `main`, GitHub Actions automatically:

1. Runs flake8 code quality checks
2. Runs 12 automated tests with pytest
3. Builds Docker image
4. Tags image with `latest` and commit SHA
5. Pushes to Docker Hub
6. SSHs into the GCP server and redeploys

### Required GitHub Secrets

| Secret | Description |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `GCP_HOST` | Server IP address |
| `GCP_USER` | Server SSH username |
| `GCP_SSH_KEY` | Server private SSH key |

---

## Live Access

- **Application URL:** https://35.242.212.39
- **GitHub Repository:** https://github.com/Ninja00015651/todoapp
- **Docker Hub:** https://hub.docker.com/r/muzaffar04/todoapp

### Test Credentials

| Field | Value |
|---|---|
| Username | `testuser` |
| Password | `testpass123` |

---

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Task List
![Task List](screenshots/tasks.png)

---

## Project Structure

```
todoapp/
├── config/              # Django settings, urls, wsgi
├── tasks/               # Main app: models, views, templates, tests
│   ├── templates/       # HTML templates
│   ├── models.py        # Task, Category, Comment models
│   ├── views.py         # CRUD views
│   └── tests.py         # 12 automated tests
├── nginx/               # Nginx configuration
├── .github/workflows/   # CI/CD pipeline
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Production services
├── docker-compose.dev.yml # Development services
└── requirements.txt     # Python dependencies
```

---

*TaskFlow © 2026 — Distributed Systems and Cloud Computing CW*
