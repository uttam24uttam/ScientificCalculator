pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/uttam24uttam/ScientificCalculator.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t uttamhamsaraj24/scientific-calculator:1.0 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-cred', url: '']) {
                    sh 'docker push uttamhamsaraj24/scientific-calculator:1.0'
                }
            }
        }
    }
}
