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
        
        //install requirements
        stage('Install Requirements') {
            steps {
                sh "${PYTHON} -m pip install --no-cache-dir -r requirements.txt || echo 'No requirements file, skipping'"
            }
        }

        stage('Run Tests') {
         //unit test
            environment {
                PYTHONPATH = 'src'
            }
            steps {
                sh "${PYTHON} -m unittest discover -s tests"
            }
        }
        
        //build docker image
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        //push docker image to docker hub
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: "${DOCKER_CRED}", url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        
        //deploy using ansible
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