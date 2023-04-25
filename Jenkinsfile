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
                sh 'docker build -f "ScoreFile/Dockerfile" -t wog .'
                    }
    }
        stage('Run') {
      steps {
        sh 'docker run -d -p 8777:8777 wog'
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
                   sh "docker tag wog  danino7/wog"
                   sh 'docker push danino7/wog:latest'
                  }
    }
}

}

