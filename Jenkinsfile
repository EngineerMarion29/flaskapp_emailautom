pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Installing dependencies
                    sh "python3.11 --version"
                    sh "virtualenv ."
                    sh "source bin/activate"
                    sh 'pip3.11 install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3.11 test.py'
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    sh 'export PATH=$PATH:/var/lib/jenkins/.local/lib/python3.11/site-packages'
                    sh 'pip3.11 install pylint'
                    sh 'pylint main.py'
                }
            }
        }

        stage('Copy to Dockerhost') {
            steps {
                script {
                    // Replace the placeholders with your actual values
                    def dockerhostIp = '172.31.46.168'
                    def dockerhostUser = 'dockeradmin'
                    // def dockerhostKey = '/root/.ssh/id_rsa.pub'
                    def projectDir = '/var/lib/jenkins/workspace/PullCodeFromGH_BuildPipeline'

                    sh """
                        scp -i -r ${projectDir} ${dockerhostUser}@${dockerhostIp}:~/
                    """
                }
            }
        }
    }
}

