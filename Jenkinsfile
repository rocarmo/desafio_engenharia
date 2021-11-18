pipeline {
  agent { label "james" }
  stages {
    stage("build") {
      steps {
        sh """
          docker --help
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