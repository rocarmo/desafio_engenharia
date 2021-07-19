pipeline {
  agent { label "windows" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t teste_jenkins .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm teste_jenkins
        """
      }
    }
  }
}