pipeline {
    agent { label "james" }
        stages {
            stage("run") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
                    """
                }
        }
            stage("start compose AAAAAAA") {
                steps {
                    sh """
                        docker-compose up
                    """
                }
            }
        }
}