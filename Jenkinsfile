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
                    // Install build dependencies
                    sh 'sudo yum -y install gcc openssl-devel bzip2-devel sqlite-devel make wget'

                    // Download and install Python 3.11.3
                    sh 'wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz'
                    sh 'tar xzf Python-3.11.3.tgz'
                    sh 'cd Python-3.11.3 && ./configure --enable-optimizations'
                    sh 'cd Python-3.11.3 && make altinstall'

                    // Verify Python installation
                    sh 'sudo python3.11 --version'

            	    // Create a symbolic link to the Python executable in /usr/local/bin/
                    sh 'sudo ln -s /usr/local/bin/python3.11 /usr/local/bin/python'
                }
            }
        }


        stage('Install Dependencies 2') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python test.py'
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    sh 'pip install pylint'
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

