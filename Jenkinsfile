pipeline {
  agent {
    dockerfile {
        filename "Dockerfile"
        label "teste_giru"
    }
  }
  stages {
    stage("build") {
      steps {
        sh """
          print "esta mensagem indica que os comandos estão funcionando"
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