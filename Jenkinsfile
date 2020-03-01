pipeline {
     agent any
     stages {
         stage('Lint html files') {
              steps {
                  sh 'tidy -q -e *.html'
              }
         }
         stage('Build') {
             steps {
                sh 'echo "Docker build app"'
                sh "docker build --tag flask-app-deployment ."
             }
         }
         stage('Push') {
             steps {
                sh 'echo "Docker push on ECR"'
                script {
                  docker.withRegistry('https://501235109294.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:MyCredentials') {
                    docker.image("flask-app-deployment").push()
                  }
                }
            }
        }
    }
}
