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
                    sh 'pip3.11 install pylint'
                    
                    def pylintExecutable = sh(script: 'find /var/lib/jenkins -type f -name pylint -print -quit', returnStdout: true).trim()
                    
                    if (pylintExecutable) {
                        // Run pylint using the located executable
                        sh "${pylintExecutable} main.py"
                    } else {
                        error "pylint executable not found"

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

