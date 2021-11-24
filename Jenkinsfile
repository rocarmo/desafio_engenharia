pipeline {
    agent { label "james" }
        stages {
            stage("create server") {
                steps {
                    sh """
                        docker build -t django-server .
                    """
                }
            }
            stage("run server") {
                steps {
                    sh """
                        docker run django-server
                    """
                }
            }
        }
}
