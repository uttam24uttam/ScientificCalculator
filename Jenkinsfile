pipeline {
    agent any

    environment {
        PYTHON = "python3"                        
        DOCKER_IMAGE = "uttamhamsaraj24/scientific-calculator:1.0"
        DOCKER_CRED = "docker-hub-cred"            
    }

    stages {
        stage('Checkout Code') {
            steps {
                
                git branch: 'main', url: 'https://github.com/uttam24uttam/ScientificCalculator.git'
            }
        }

        stage('Install Requirements') {
            steps {
                
                sh "${PYTHON} -m pip install --no-cache-dir -r requirements.txt || echo 'No requirements file, skipping'"
            }
        }

        stage('Run Tests') {
            steps {
                   //unit test
                sh "${PYTHON} -m unittest discover -s tests"
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                // Push Docker image to Docker Hub 
                withDockerRegistry([credentialsId: "${DOCKER_CRED}", url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
