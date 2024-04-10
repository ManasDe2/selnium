pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                script {
                    def output = sh(script: 'python3 test.py', returnStdout: true).trim()
                    println "Output of test.py: ${output}"
                    
                    if (output.contains('Passed')) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Create Image'){
            steps {
                script {
                    sh 'docker build -t my-apache2 .'
                    echo 'Image built'
                }
            }
        }
        stage('Container run'){
            steps {
                script {
                    sh 'docker run -dit --name my-running-app -p 3000:80 my-apache2'
                    echo 'Image built'
                }
            }
        }
        stage('Deployment') {
            when {
                expression {
                    // Only run the Deployment stage if the Test stage was successful
                    return currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    sh 'sudo -S cp -r ./*.html /var/www/html/'
                    sh 'sudo -S systemctl restart nginx'
                }
            }
        }
    }
}
