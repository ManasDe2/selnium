pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code repository
                git 'https://github.com/ManasDe2/selnium.git'
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