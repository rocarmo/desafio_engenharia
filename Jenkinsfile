pipeline {
<<<<<<< Updated upstream
  agent any 
=======
  agent { label "linux" }
>>>>>>> Stashed changes
  stages {
    stage("build") {
      steps {
        sh """
<<<<<<< Updated upstream
          docker build -t teste_atual .
=======
          docker build -t meu_giru .
>>>>>>> Stashed changes
        """
      }
    }
    stage("run") {
      steps {
        sh """
<<<<<<< Updated upstream
          docker run --rm teste_atual
=======
          docker run --rm meu_giru
>>>>>>> Stashed changes
        """
      }
    }
  }
}