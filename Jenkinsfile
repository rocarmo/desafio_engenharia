pipeline {
  agent { label "james" }
  stages {
    stage("run") {
      steps {
        sh """
          docker-compose run web django-admin startproject composeexample .
        """
      }
    }
    stage("start compose") {
        steps {
            sh """
                docker-compose up
            """
        }
    }
  }
}