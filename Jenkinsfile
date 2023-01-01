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
        // stage('Update DB'){
        //     steps {
        //         echo "Updating DB..."
        //         sh 'docker exec -it django_personal-site sh'
        //         sh 'cd src'
        //         sh 'python manage.py migrate'
        //         sh 'exit'
        //         echo "DB has been updated"
        //     }
        // }

    }
}

