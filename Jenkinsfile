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
                sh 'python3 your_testing_script.py'
            }
        }
    }
}