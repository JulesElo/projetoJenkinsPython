pipeline {
    agent any

    stages {
        stage('Preparar ambiente') {
            steps {
                echo 'Criando ambiente virtual Python...'
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && python -m pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Executar testes') {
            steps {
                echo 'Executando testes unitários...'
                sh '. .venv/bin/activate && pytest --junitxml=relatorios/testes.xml --cov=app --cov-report=term-missing'
            }
            post {
                always {
                    junit 'relatorios/testes.xml'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Validando build da aplicação...'
                sh '. .venv/bin/activate && python -m compileall app'
            }
        }

        stage('Executar aplicação') {
            steps {
                echo 'Executando aplicação de exemplo...'
                sh '. .venv/bin/activate && python -m app.main'
            }
        }
    }
}
