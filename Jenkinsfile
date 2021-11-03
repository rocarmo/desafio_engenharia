pipeline {
  agent { label "james"
  environment {
    PATH = "C:\Program Files\Docker\Docker\resources\bin"
    PATH = "C:\ProgramData\DockerDesktop\version-bin"
    }
  }
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