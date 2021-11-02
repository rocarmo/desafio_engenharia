pipeline {
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