pipeline {
  agent { label "james" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t meugiru .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm meugiru
        """
      }
    }
  }
}