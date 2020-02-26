pipeline {
     agent any
     stages {
         stage('Lint app.py') {
              steps {
                  sh 'echo "Tidy step to lint the app"'
                  sh 'make lint'
              }
         }
    }
}
