pipeline {
    agent { label "james" }
        stages {
            stage("create aux container") {
                steps {
                    sh """
                        docker build -t django-aux-jenkins .
                    """
                }
            }
        }

        stages {
            stage("create django") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
                    """
                }
            }
        }
        stages {
            stage("run server") {
                steps {
                    sh """
                        docker run django-aux-jenkins
                    """
                }
            }
        }
}
