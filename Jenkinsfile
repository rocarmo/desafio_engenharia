pipeline {
  agent {
    label "james"
        docker {
            alwaysPull true
        }
   }
  stages {
    stage("build") {
      steps {
        sh """
          echo esta mensagem indica que os comandos estão funcionando
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