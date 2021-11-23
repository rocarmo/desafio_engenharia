pipeline {
    agent { label "james" }
        stages {
            stage("build") {
                steps {
                    sh """
                        docker-compose build web django-admin startproject composeexample .
                    """
            }
        }
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