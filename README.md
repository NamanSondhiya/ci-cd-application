# CI/CD Application

Full-stack application with automated CI/CD pipeline using Jenkins and Docker.

## Architecture
- **Frontend**: Flask (Port 5000)
- **Backend**: Python (Port 3000)
- **CI/CD**: Jenkins with Docker Compose
- **Containerization**: Docker

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Jenkins (for CI/CD)
- Git

**Automated Setup**: Use [shell-scripts repository](https://github.com/NamanSondhiya/shell-scripts.git) for automated installation of Docker, Docker Compose, and Jenkins on new machines.

### Local Development
```bash
git clone https://github.com/NamanSondhiya/ci-cd-application.git
cd ci-cd-application
docker-compose up -d
```

### Jenkins Setup
1. **Configure Credentials**:
   - Add Docker Hub credentials with ID: `dockerhub-creds`
   - Username/Password or Personal Access Token

2. **Create Pipeline Job**:
   - New Item → Pipeline
   - Pipeline script from SCM
   - Repository URL: `https://github.com/NamanSondhiya/ci-cd-application.git`
   - Branch: `Master`

3. **Pipeline Parameters**:
   - `STOP`: Boolean (default: false) - Auto-stop after 1 minute

### Pipeline Features
- **Auto-polling**: Checks for changes every minute
- **Webhook support**: GitHub push triggers
- **Controlled deployment**: Optional auto-stop functionality
- **Secure credentials**: Masked Docker Hub authentication

## Access Points
- Frontend: http://localhost:5000
- Backend: http://localhost:3000

## Usage Modes
- **Continuous**: Set `STOP=false` for persistent deployment
- **Testing**: Set `STOP=true` for 1-minute temporary deployment