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
                // Run Selenium testing script
                sh 'python3 test.py'
            }
        }
    }
}