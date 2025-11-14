pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *')
        githubPush()
    }
    
    stages {
        stage('Code Clone from Github') {
            steps {
                git url: "https://github.com/NamanSondhiya/ci-cd-application.git", branch: "Master"
                echo "Code Clonned Successfully"    
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