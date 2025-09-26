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
                // Building Docker image
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                // Pushing Docker image to Docker Hub 
                withDockerRegistry([credentialsId: "${DOCKER_CRED}", url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                //Wrapping the command in withEnv to set the correct character encoding
                withEnv(['LC_ALL=en_US.UTF-8']) {
                    sh "ansible-playbook -i Deployment/inventory.ini Deployment/deploy.yml"
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






