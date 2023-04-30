pipeline {
    agent any

    stages {
        stage('Checkout - checkout the repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Danino7/Wog.git'
            }
        }
        stage('Build - Build DockerImage') {
            steps {
                sh 'docker build -f "ScoreFile/Dockerfile" -t danino7/wog:latest .'
                    }
    }
        stage('Run - will run our dockerized application') {
            steps {
                sh 'docker-compose -f "ScoreFile/docker-compose.yml" up -d'
      }
    }
        stage('Test') {
            steps {
                   sh "pip3 install selenium"
                   sh 'python3 Test/e2e.py'
                    
                  }
    }
        stage('Finalize') {
            steps {
                   sh 'docker-compose -f "ScoreFile/docker-compose.yml" down'
                   sh 'docker push danino7/wog:latest'
                  }
    }

}

}

