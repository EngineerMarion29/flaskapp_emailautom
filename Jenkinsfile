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
                    sh "pip3.11 install -r requirements.txt"
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
                    def dockerhostIp = '172.31.36.125'
                    def dockerhostUser = 'ansible_admin'
                    // def dockerhostKey = '/root/.ssh/id_rsa.pub'
                    def projectDir = '/var/lib/jenkins/workspace/CI_CD_Pipeline_FlaskApp'

                    sh """
                        sudo rsync -r --delete ${projectDir} root@${dockerhostIp}:~/
                    """
                    
                    // Send dockerization.yml to ansible_server
                    sh """
                        sudo scp ${projectDir}/k8s.yml root@172.31.46.38:~/
                    """
                    sh """
                        sudo scp ${projectDir}/flaskapp_pods.yaml root@172.31.46.38:~/
                    """
                    sh """
                        sudo scp ${projectDir}/flaskapp_service.yaml root@172.31.46.38:~/
                    """
                    sh """
                        sudo scp ${projectDir}/dockerbuild.yml root@172.31.46.38:~/
                    """
                }
            }
        }

        stage('Dockerization in Docker_k8S_Host') {
            steps {
                script {
                    // Dockerization via ansible playbook
                    sh "sudo ssh root@172.31.46.38 'ansible-playbook -i inventory dockerbuild.yml'"
                    sh "sudo ssh root@172.31.46.38 'ansible-playbook -i inventory k8s.yml'"
                }
            }
        }       
    }
}

