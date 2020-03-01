pipeline {
     agent any
     stages {
         stage('Lint html files') {
              steps {
                  sh 'tidy -q -e *.html'
              }
         }
    }
}
