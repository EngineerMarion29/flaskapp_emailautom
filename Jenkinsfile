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

        stage('Test codebase') {
            steps {
                script {
                    sh 'python3.11 test.py'
                }
            }
        }

        stage('Copy to codebase Dockerhost') {
            steps {
                script {
                    // Replace the placeholders with your actual values
                    def dockerhostIp = '172.31.46.168'
                    def dockerhostUser = 'dockeradmin'
                    // def dockerhostKey = '/root/.ssh/id_rsa.pub'
                    def projectDir = '/var/lib/jenkins/workspace/PullCodeFromGH_BuildPipeline'

                    sh """
                        sudo scp -r ${projectDir} ${dockerhostUser}@${dockerhostIp}:~/
                    """
                }
            }
        }

        stage('Dockerization') {
            steps {
                script {
                    // Dockerization via ansible playbook
                    sh 'ansible-playbook dockerization.yml'
                }
            }
        }       
    }
}

