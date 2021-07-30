pipeline {
  agent { label "linux" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t teste_atual .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm teste_atual
        """
      }
    }
  }
}