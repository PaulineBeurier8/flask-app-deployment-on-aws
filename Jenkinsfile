pipeline {
     agent any
     stages {
         stage('Lint app.py') {
              steps {
                  sh 'echo "Tidy step to lint the app"'
                  sh 'make lint'
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
                withDockerRegistry('501235109294.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-2:MyCredentials') {
                sh "docker push pauline08/flask-app-deployment-on-aws:latest"
             }
         }
     }
}
