pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Building image..."'
                sh 'docker-compose up -d'
                sh 'docker-compose down'
                sh 'echo "Image built"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "unit test"'
            }
        }
        stage('Code quality') {
            steps {
                sh 'echo "flake8 test"'
            }
        }
        stage('Package') {
            steps {
                sh 'echo "preparing package..."'
            }
        }
    }
}

