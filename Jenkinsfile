pipeline {
  agent { docker { image python:3.9 } }
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