pipeline {
    agent { label "james" }
        stages {
            stage("build") {
                steps {
                    sh """
                        docker-compose build
                    """
            }
        }
            stage("run") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
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