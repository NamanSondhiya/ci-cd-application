# CI/CD Application

Hey there! Welcome to my full-stack application, now streamlined with Docker and Jenkins for reliable CI/CD. I'm excited to share the latest enhancements that make deployment a breeze.

## Recent Updates
- **Jenkins Integration**: Switched to Jenkins for automated builds, testing, and deployments via the included Jenkinsfile. It polls for changes and deploys seamlessly using Docker Compose.
- **Repository URL Update**: Updated clone URL to the correct repository for easier access.

## Structure
- Frontend: Flask (Port 5000)
- Backend: Python (Port 3000)

## Branches
- `Master`: Base application
- `master02`: With GitHub Actions (legacy setup)

## Usage
```bash
# Clone the repository
git clone https://github.com/NamanSondhiya/ci-cd-application.git
cd ci-cd-application

# Run with Docker Compose
docker-compose up -d
```

## Access
- Frontend: http://localhost:5000
- Backend: http://localhost:3000