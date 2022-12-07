pipeline {
    agent any

    //environment {
    //    
    //}

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

