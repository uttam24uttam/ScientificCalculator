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
            emailext (
                to: 'uttamhamsaraj24@gmail.com',
                subject: "SUCCESS: Pipeline '${currentBuild.fullDisplayName}'",
                mimeType: 'text/html',
                body: """
                    <h2>SUCCESS: Pipeline '${currentBuild.fullDisplayName}'</h2>
                    <p>The pipeline completed successfully.</p>
                    <p>
                        <strong>Project:</strong> ${env.JOB_NAME}<br>
                        <strong>Build Number:</strong> ${env.BUILD_NUMBER}<br>
                        <strong>Build URL:</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a>
                    </p>
                """
            )
        }
        failure {
            emailext (
                to: 'uttamhamsaraj24@gmail.com',
                subject: "FAILED: Pipeline '${currentBuild.fullDisplayName}'",
                mimeType: 'text/html',
                body: """
                    <h2>FAILED: Pipeline '${currentBuild.fullDisplayName}'</h2>
                    <p>The pipeline failed. Please check the console output.</p>
                    <p>
                        <strong>Project:</strong> ${env.JOB_NAME}<br>
                        <strong>Build Number:</strong> ${env.BUILD_NUMBER}<br>
                        <strong>Error:</strong> ${currentBuild.result}<br>
                        <strong>Console Output:</strong> <a href="${env.BUILD_URL}">Click here to view the logs</a>
                    </p>
                """
            )
        }
    }
}