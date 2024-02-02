# Sobre o Projeto

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/release)
[![Django Version](https://img.shields.io/badge/Django-5.0%2B-green)](https://docs.djangoproject.com/en/stable/releases/)
[![HTML Version](https://img.shields.io/badge/HTML-5-orange)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS Version](https://img.shields.io/badge/CSS-3-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)


Este projeto foi desenvolvido durante a PSW 9.0 da Pythonando, servindo como um aplicativo para estudos e memorização por meio de flashcards. Os usuários podem criar flashcards para solidificar seus conhecimentos em diferentes assuntos.

## Dependências do projeto

- Python 3.10 ou superior. 
- Poetry (Gerenciador de pacotes).

## Estrutura do projeto

O projeto Django é composto por 5 aplicativos, além do núcleo central.

```bash
.
├── backend
│   ├── core
│   ├── users
│   ├── flashcards 
│   ├── challenges
│   ├── books
│   ├── reports
│   ├── templates
│   └── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md

```

## Instalando as dependências

Primeiro instale as dependências do projeto em um ambiente virtual:

```bash
poetry install
```

## Ativando o ambiente virtual

Execute o comando abaixo para ativar o ambiente virtual criado pelo poetry:

```bash
poetry shell
```

## Execute as migrações

Execute as migrações utilizando o seguinte comando:

```bash
task migrations
```

## Execute o projeto

Para iniciar o projeto, utilize o seguinte comando:

```bash
task run
```
