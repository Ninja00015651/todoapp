# TaskFlow — Django Task Manager

A fully containerized Django web application for managing tasks, built for the Distributed Systems & Cloud Computing module.

## Features

- 🔐 User authentication (register, login, logout)
- ✅ Full CRUD for Tasks (create, read, update, delete)
- 🏷️ Categories with color coding
- 💬 Comments on tasks
- 📊 Dashboard with task statistics
- 🔍 Filter tasks by status and priority
- 📱 Responsive Bootstrap 5 UI

## Technologies

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2, Gunicorn |
| Database | PostgreSQL 15 |
| Reverse Proxy | Nginx |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| SSL | Let's Encrypt (Certbot) |
| Cloud | Eskiz Cloud Server |

## Database Schema

- **User** (Django built-in) — one-to-many with Task, Category, Comment
- **Task** — ForeignKey to User (owner), ManyToMany with Category
- **Category** — ForeignKey to User (created_by), ManyToMany with Task
- **Comment** — ForeignKey to Task, ForeignKey to User

## Local Setup (Development)

### Prerequisites
- Docker & Docker Compose installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/todoapp.git
cd todoapp

# 2. Copy environment file
cp .env.example .env
# Edit .env with your values

# 3. Start development environment
docker compose -f docker-compose.dev.yml up --build

# 4. In another terminal, run migrations
docker compose -f docker-compose.dev.yml exec web python manage.py migrate

# 5. Create superuser
docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

# 6. Visit http://localhost:8000
```

## Production Deployment

### Server Setup (Ubuntu 22.04)

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot certonly --standalone -d yourdomain.uz

# Clone repo
sudo mkdir -p /opt/todoapp
cd /opt/todoapp
git clone https://github.com/YOUR_USERNAME/todoapp.git .

# Create .env file
cp .env.example .env
nano .env  # fill in production values

# Start services
docker compose up -d
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `yourdomain.uz` |
| `POSTGRES_DB` | Database name | `todoapp` |
| `POSTGRES_USER` | DB username | `todoapp_user` |
| `POSTGRES_PASSWORD` | DB password | `strongpassword` |
| `POSTGRES_HOST` | DB host | `db` |
| `DOCKERHUB_USERNAME` | Docker Hub username | `yourusername` |

## GitHub Secrets (for CI/CD)

Set these in your GitHub repository Settings → Secrets:

- `DOCKERHUB_USERNAME` — your Docker Hub username
- `DOCKERHUB_TOKEN` — Docker Hub access token
- `SSH_PRIVATE_KEY` — private SSH key for server access
- `SSH_HOST` — server IP address
- `SSH_USERNAME` — server username (e.g. `ubuntu`)

## Running Tests

```bash
pip install pytest pytest-django
pytest tasks/tests.py -v
```

## Live Application

- 🌐 **Live URL**: https://yourdomain.uz
- 🐳 **Docker Hub**: https://hub.docker.com/r/yourusername/todoapp
- 💻 **GitHub**: https://github.com/yourusername/todoapp

## Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Regular User | `testuser` | `testpass123` |
| Admin | `admin` | `admin123` |
