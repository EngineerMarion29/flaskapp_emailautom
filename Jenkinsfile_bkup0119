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

        stage('Copy to codebase Docker_K8S_Host') {
            steps {
                script {
                    // Replace the placeholders with your actual values
                    def dockerhostIp = '172.31.47.183'
                    def dockerhostUser = 'ansible_admin'
                    // def dockerhostKey = /.ssh/id_rsa.pub'
                    def projectDir = '/var/lib/jenkins/workspace/CI_CD_Pipeline_FlaskApp'

                    sh """
                        sudo rsync -r --delete ${projectDir} ${dockerhostUser}@${dockerhostIp}:~/
                    """
                    
                    // Send dockerization.yml to ansible_server
                    sh """
                        sudo rsync -r --delete ${projectDir} ${dockerhostUser}@172.31.46.38:~/
                    """
                }
            }
        }

        stage('Dockerization in Docker_k8S_Host') {
            steps {
                script {
                    // Dockerization via ansible playbook
                    sh "sudo ssh ansible_admin@172.31.46.38 'ansible-playbook -i ~/CI_CD_Pipeline_FlaskApp/inventory ~/CI_CD_Pipeline_FlaskApp/dockerbuild.yml'"
                    sh "sudo ssh ansible_admin@172.31.46.38 'ansible-playbook -i ~/CI_CD_Pipeline_FlaskApp/inventory ~/CI_CD_Pipeline_FlaskApp/k8s.yml'"
                }
            }
        }       
    }
}

