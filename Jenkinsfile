pipeline {
     agent any
     stages {
         stage('Requirement install') {
              steps {
                  sh 'echo "Install requirements.txt"'
                  sh 'make install'
              }
         }
         stage('Lint app.py') {
              steps {
                  sh 'echo "Tidy step to lint the app"'
                  sh 'make lint'
              }
         }
    }
  }
}