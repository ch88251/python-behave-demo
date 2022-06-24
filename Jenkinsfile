pipeline {
  agent any

  stages {
    stage('Acceptance Testing') {
      steps {
        sh(script: 'behave -f allure_behave.formatter:AllureFormatter -o allure-results features')
      }
    }
  }
}
