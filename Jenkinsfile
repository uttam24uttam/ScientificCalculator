pipeline {
    agent any
    environment {
        PYTHON = "python3"
        DOCKER_IMAGE = "uttamhamsaraj24/scientific-calculator:1.0"
        DOCKER_CRED = "docker-hub-cred"
    }
    stages {
        // Checkout code from GitHub
        stage('STAGE 1:Checkout Code') {
         steps {
            git branch: 'main', url: 'https://github.com/uttam24uttam/ScientificCalculator.git'
         }
        }
        // Install Python dependencies
        stage('STAGE 2:Install Requirements') {
         steps {
            sh "${PYTHON} -m pip install --no-cache-dir -r requirements.txt"
            }
        }
        // Run unit tests
        stage('STAGE 3:Run Tests') {
            environment {
                PYTHONPATH = 'src'
            }
            steps {
                sh "${PYTHON} -m unittest discover -s tests"
            }
        }
        // Build Docker image
        stage('STAGE 4:Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        // Push Docker image
        stage('STAGE 5:Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: "${DOCKER_CRED}", url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        // Deploy with Ansible
        stage('STAGE 6:Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'Deployment/deploy.yml',
                    inventory: 'Deployment/inventory.ini',
                    installation: 'Ansible-default'
                )
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