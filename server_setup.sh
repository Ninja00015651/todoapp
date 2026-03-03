#!/bin/bash
# Server setup script for Ubuntu 22.04 (Eskiz Cloud)
# Run as root or with sudo

set -e

echo "🚀 Setting up TaskFlow server..."

# Update system
apt-get update && apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh
usermod -aG docker ubuntu

# Install Docker Compose plugin
apt-get install -y docker-compose-plugin

# Install Certbot
apt-get install -y certbot python3-certbot-nginx

# Configure UFW firewall
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

# Create app directory
mkdir -p /opt/todoapp

echo "✅ Server setup complete!"
echo "Next steps:"
echo "1. Clone your repo to /opt/todoapp"
echo "2. Get SSL certificate: certbot certonly --standalone -d yourdomain.uz"
echo "3. Create .env file from .env.example"
echo "4. Run: docker compose up -d"
