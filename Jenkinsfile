pipeline {
    agent any

    environment {
        SECRET_KEY = credentials('django-personal-secret-key')
        IS_DEBUGGING = credentials('django-personal-is-debugging')
    }

    stages {

        stage('Build images'){
            steps{
                echo "Building images..."
                sh 'docker compose build'
            }
        }

        stage('Test') {
            steps {
                echo "Testing.."
                echo "Testing webhook CI/CD"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Shutting down docker containers...'
                sh 'docker compose down'
                echo 'Starting up containers...'
                sh 'docker compose up -d'
            }
        }

    }
}

