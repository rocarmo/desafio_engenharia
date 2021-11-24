django-admin startproject desafio_engenharia

stage("create django") {
                steps {
                    sh """
                        docker-compose run web django-admin startproject desafio_engenharia .
                    """
                }
            }