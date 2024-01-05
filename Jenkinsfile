pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                // This stage runs your test.py
                script {
                    sh 'python test.py'
                }
            }
        }

        stage('Lint') {
            steps {
                // This stage performs linting using your linting tools
                script {
                    sh 'pip install pylint'
                    sh 'pylint main.py'
                }
            }
        }

        stage('Copy to Dockerhost') {
            steps {
                // This stage uses a simple SSH command to copy the project directory
                script {
                    // Replace the placeholders with your actual values
                    def dockerhostIp = '172.31.32.140'
                    def dockerhostUser = 'dockeradmin'
                    def dockerhostKey = '/root/.ssh/id_rsa.pub'
                    def projectDir = '/home/dockeradmin'

                    sh """
                        scp -i ${dockerhostKey} -r ${projectDir} ${dockerhostUser}@${dockerhostIp}:~/                        
                    """
                }
            }
        }
    }
}

