pipeline {
  agent { label "james" }
  stages {
    stage("build") {
      steps {
        sh """
          -Dorg.jenkinsci.plugins.durabletask.BourneShellScript.LAUNCH_DIAGNOSTICS=true
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