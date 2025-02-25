# Extension Pop-up Powered AI Deployment Guide

This guide covers how to deploy the Extension Pop-up Powered AI system to production environments.

## Prerequisites

Before deploying, ensure you have:

- Docker and Docker Compose installed
- A server with at least 2GB RAM and 1 CPU
- Domain name (optional, but recommended)
- API keys for any external services

## Backend Deployment

### Using Docker

The simplest way to deploy the backend is using Docker:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/extension-popup-powered-ai.git
   cd extension-popup-powered-ai/backend
   ```

2. Create and configure the environment file:
   ```bash
   cp .env.example .env
   # Edit .env with your production settings and API keys
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up -d
   ```

The API will be available at `http://your-server-ip:8000`.

### Using a Cloud Provider

#### Heroku Deployment

1. Install the Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. Login to Heroku:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create extension-popup-ai-backend
   ```

4. Add PostgreSQL add-on:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. Configure environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set OPENAI_API_KEY=your-openai-api-key
   # Add other environment variables as needed
   ```

6. Deploy the backend:
   ```bash
   git subtree push --prefix backend heroku main
   ```

#### AWS Elastic Beanstalk

1. Initialize Elastic Beanstalk:
   ```bash
   pip install awsebcli
   cd backend
   eb init
   ```

2. Create an environment:
   ```bash
   eb create extension-popup-ai-production
   ```

3. Configure environment variables:
   ```bash
   eb setenv SECRET_KEY=your-secret-key OPENAI_API_KEY=your-openai-api-key
   ```

4. Deploy:
   ```bash
   eb deploy
   ```

## Extension Deployment

### Chrome Web Store

To publish the extension to the Chrome Web Store:

1. Create a production build:
   ```bash
   cd extension
   # Update the API_BASE_URL in content.js and popup.js to point to your production backend
   ```

2. Zip the extension folder:
   ```bash
   zip -r extension.zip *
   ```

3. Go to the [Chrome Developer Dashboard](https://chrome.google.com/webstore/developer/dashboard)

4. Create a new item and upload the `extension.zip` file

5. Fill in all required details and submit for review

### Self-distribution

For enterprise or self-distribution:

1. Create a production build with appropriate settings
2. Zip the extension folder
3. Distribute the ZIP file to users
4. Users can install by:
   - Going to `chrome://extensions/`
   - Enabling "Developer mode"
   - Clicking "Load unpacked" and selecting the extracted folder

## Setting Up HTTPS

It's recommended to use HTTPS for production:

### Using Nginx as a Reverse Proxy

1. Install Nginx:
   ```bash
   sudo apt update
   sudo apt install nginx
   ```

2. Configure Nginx:
   ```bash
   sudo nano /etc/nginx/sites-available/extension-popup-ai
   ```

3. Add the following configuration:
   ```
   server {
       listen 80;
       server_name your-domain.com;
   
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

4. Enable the site:
   ```bash
   sudo ln -s /etc/nginx/sites-available/extension-popup-ai /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

5. Set up SSL with Let's Encrypt:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

## Database Migration

To manage database migrations in production:

```bash
cd backend
alembic upgrade head
```

## Monitoring and Logging

### Setting Up Logging

1. Configure logging in your backend:
   ```python
   # In app/core/config.py
   LOGGING_CONFIG = {
       "version": 1,
       "disable_existing_loggers": False,
       "formatters": {
           "default": {
               "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
           },
       },
       # Add handlers and loggers configuration
   }
   ```

2. Implement the logging configuration in your main app

### Monitoring Tools

Consider setting up:

- Prometheus and Grafana for metrics
- Sentry for error tracking
- ELK Stack (Elasticsearch, Logstash, Kibana) for log analysis

## Scaling

### Horizontal Scaling

To handle more traffic:

1. Deploy multiple instances of the API behind a load balancer
2. Use a managed database service for better reliability
3. Implement caching with Redis for frequently requested data

### Vertical Scaling

If your workload requires more compute power:

1. Increase server resources (CPU, RAM)
2. Optimize database queries
3. Consider using GPU instances for ML-heavy workloads

## Backup Strategy

Implement regular backups:

```bash
# Backup database (if using PostgreSQL)
pg_dump -U username -d dbname > backup.sql

# Set up a cron job for daily backups
0 0 * * * pg_dump -U username -d dbname > /path/to/backups/backup-$(date +\%Y\%m\%d).sql
```

## Continuous Integration/Deployment

Set up CI/CD using GitHub Actions:

1. Create `.github/workflows/deploy.yml`:
   ```yaml
   name: Deploy to Production
   
   on:
     push:
       branches: [ main ]
   
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.11'
             
         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r backend/requirements.txt
             
         - name: Run tests
           run: |
             cd backend
             pytest
             
         - name: Deploy to server
           uses: appleboy/ssh-action@master
           with:
             host: ${{ secrets.HOST }}
             username: ${{ secrets.USERNAME }}
             key: ${{ secrets.SSH_KEY }}
             script: |
               cd /path/to/extension-popup-powered-ai
               git pull
               cd backend
               docker-compose down
               docker-compose up -d --build
   ```

2. Set up the required secrets in your GitHub repository

## Maintenance

### Regular Updates

1. Keep dependencies updated:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. Apply security patches promptly

3. Monitor for API changes in external services

### Performance Tuning

1. Optimize database queries
2. Add caching where appropriate
3. Consider using a CDN for static assets 