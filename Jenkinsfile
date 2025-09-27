pipeline {
    agent any
    environment {
        PYTHON = "python3"
        DOCKER_IMAGE = "uttamhamsaraj24/scientific-calculator:1.0"
        DOCKER_CRED = "docker-hub-cred"
    }
    stages {
        //STAGE 1
        stage('Checkout Code') {
         steps {
            git branch: 'main', url: 'https://github.com/uttam24uttam/ScientificCalculator.git'
         }
        }
        //STAGE 2
        stage('Install Requirements') {
         steps {
            sh "${PYTHON} -m pip install --no-cache-dir -r requirements.txt"
            }
        }
        //STAGE 3
        stage('Run Tests') {
            environment {
                PYTHONPATH = 'src'
            }
            steps {
                sh "${PYTHON} -m unittest discover -s tests"
            }
        }
        //Stage 4
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        //Stage 5
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: "${DOCKER_CRED}", url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        //Stage 6
        stage('Deploy with Ansible') {
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