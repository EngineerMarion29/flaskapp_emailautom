pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        VENV_NAME = 'venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies 2') {
            steps {
                script {
                    // Installing dependencies
                    sh "python3.11 --version"
                    sh "python3.11 -m venv ${VENV_NAME}"
                    sh "source ${VENV_NAME}/bin/activate"
                    sh '/usr/local/bin/pip3.11 install -r requirements.txt'
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
                    sh 'pip3 install pylint'
                    sh 'pylint main.py'
                }
            }
        }

        stage('Copy to Dockerhost') {
            steps {
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

