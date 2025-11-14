pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *')
        // githubPush
    }
    
    parameters {
        booleanParam(name: 'STOP', defaultValue: false, description: 'Stop the application after deployment')
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

        stage('Auto Stop') {
            when {
                params.STOP == true
            }
            steps {
                echo 'Application will run for a minutes before stopping...'
                sleep time: 1, unit: 'MINUTES'
                sh 'docker compose down'
                echo 'Application stopped after a minutes'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
            sh 'docker logout || true'
        }
    }
}