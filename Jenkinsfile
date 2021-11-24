pipeline {
    agent { label "james" }
        stages {
            stage("create django") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
                    """
                }
            }
            stage("run server") {
                steps {
                    sh """
                        docker-compose up
                    """
                }
            }
        }
}
