pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *')
        githubPush()
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'Master',
                    credentialsId: 'SillyCookies-s/**************************', 
                    url: 'https://github.com/SillyCookies-s/ci-cd-application.git'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up --build -d'
            }
        }
    }
}