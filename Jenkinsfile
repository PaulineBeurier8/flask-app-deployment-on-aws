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
                sh "docker build --tag pauline08/flask-app-deployment-on-aws:latest ."
             }
         }
         stage('Push') {
             steps {
                sh 'echo "Docker push on ECR"'
                script {
                  docker.withRegistry('501235109294.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-2:MyCredentials') {
                    docker.image("pauline08/flask-app-deployment-on-aws:latest").push()
                  }
                }
            }
        }
    }
}
