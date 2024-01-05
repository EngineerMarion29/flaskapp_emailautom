pipeline {
    agent any

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
                    sh 'sudo yum install openssl-devel -y && sudo yum install virtualenv -y'
                    sh 'source bin/activate && 'pip3.11 install -r requirements.txt'
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

