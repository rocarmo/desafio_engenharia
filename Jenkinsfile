pipeline {
    agent { label "james" }
        stages {
            stage("remove trash") {
                steps {
                    sh './trash_remover.sh'
                }
            }
            stage("create django") {
                steps {
                    sh """
                        docker build -t desafio_engenharia .
                    """
                }
            }
            stage("run django") {
                steps {
                    sh ('docker run -d -p 8000:8000 desafio_engenharia')
                }
            }
        }
}
