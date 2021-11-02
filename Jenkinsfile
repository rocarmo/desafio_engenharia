pipeline {
  agent { label "agent1" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t meu_giru .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm meu_giru
        """
      }
    }
  }
}