# Projeto Python com Jenkins

Este projeto foi criado para demonstrar, de forma simples, como usar Python, testes de unidade e Jenkins.

## Objetivo

A cada commit no GitHub, o Jenkins pode executar automaticamente:

1. Criação do ambiente virtual Python.
2. Instalação das dependências.
3. Execução dos testes unitários.
4. Geração do relatório de testes.
5. Validação do build da aplicação.
6. Execução da aplicação de exemplo.

## Estrutura do projeto

```text
projeto-python-jenkins/
├── app/
│   ├── __init__.py
│   ├── calculadora.py
│   └── main.py
├── tests/
│   └── test_calculadora.py
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Como executar localmente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente virtual

No Linux/macOS:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python -m app.main
```

### 5. Executar os testes

```bash
pytest
```

### 6. Executar testes com relatório para Jenkins

```bash
pytest --junitxml=relatorios/testes.xml --cov=app --cov-report=term-missing
```

## Como importar no Eclipse/PyDev

1. Abra o Eclipse.
2. Vá em `File > Import`.
3. Escolha `Existing Projects into Workspace`.
4. Selecione a pasta `projeto-python-jenkins`.
5. Configure o interpretador Python em `Project > Properties > PyDev - Interpreter/Grammar`.
6. Marque a pasta do projeto como fonte, se necessário.

## Como usar com Jenkins

1. Suba este projeto para um repositório no GitHub.
2. No Jenkins, crie um item do tipo `Pipeline`.
3. Configure o repositório GitHub na seção `Pipeline script from SCM`.
4. Informe o caminho do arquivo:

```text
Jenkinsfile
```

5. Execute o job.

## Observação para Windows

O `Jenkinsfile` usa comandos `sh`, comuns em Jenkins rodando no Linux.

Se o Jenkins estiver rodando no Windows, substitua os comandos `sh` por `bat`.
