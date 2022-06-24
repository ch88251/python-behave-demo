pipeline {
  agent any

  stages {
    stage('Acceptance Testing') {
      steps {
        sh(script: 'behave --junit')
      }
    }    
  }
}
