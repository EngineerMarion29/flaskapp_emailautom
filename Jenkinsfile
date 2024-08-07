pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Install the Dependencies') {
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


##Update this, you don't need to send the code base to the docker host and ansible server. Just need to push it to the ansible server and add steps to push the codebase to
##the code base once you're starting to build already on the host.
        
        stage('Copy to codebase Docker_K8S_Host') {
            steps {
                script {
                    // Replace the placeholders with your actual values
                    def dockerhostIp = '172.31.47.183'
                    def dockerhostUser = 'ansible_admin'
                    // def dockerhostKey = /.ssh/id_rsa.pub'
                    def projectDir = '/var/lib/jenkins/workspace/CI_CD_Pipeline_FlaskApp'

                    sh """
                        sudo rsync -r --delete ${projectDir} root@${dockerhostIp}:~/
                    """
                    
                    // Send dockerization.yml to ansible_server
                    sh """
                        sudo rsync -r --delete ${projectDir} root@172.31.46.38:~/
                    """
                }
            }
        }

        stage('Dockerization in Docker_k8S_Host') {
            steps {
                script {
                    // Dockerization via ansible playbook
                    sh "sudo ssh root@172.31.46.38 'ansible-playbook -i ~/CI_CD_Pipeline_FlaskApp/inventory ~/CI_CD_Pipeline_FlaskApp/dockerbuild.yml'"
                    sh "sudo ssh root@172.31.46.38 'ansible-playbook -i ~/CI_CD_Pipeline_FlaskApp/inventory ~/CI_CD_Pipeline_FlaskApp/k8s.yml'"
                }
            }
        }       
    }
}

