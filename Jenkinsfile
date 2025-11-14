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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker compose down || true'
                    sh 'docker compose up --build -d'
                }
            }
        }
    }
}