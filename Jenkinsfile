pipeline {
    agent { label "james" }
        stages {
            stage("run") {
            stage("create django") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
                    """
                }
            }
            stage("run project") {
                steps {
                    sh ('docker-compose up -d -p 8000:8000')
                }
        }
}
