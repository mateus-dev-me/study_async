# About the Project

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/release)
[![Django Version](https://img.shields.io/badge/Django-5.0%2B-green)](https://docs.djangoproject.com/en/stable/releases/)
[![HTML Version](https://img.shields.io/badge/HTML-5-orange)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS Version](https://img.shields.io/badge/CSS-3-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)


This project was developed during [PSW 9.0](https://pythonando.com.br/psw/inscricao/psw9.0) of [Pythonando](https://pythonando.com.br), serving as an application for studying and memorising flashcards. Users can create flashcards to solidify their knowledge of different subjects.

## Project dependencies

- Python 3.10 or higher. 
- Poetry (Package Manager).

## Application Preview

Include here representative images of the application's operation and interface.

**Example

![Login](docs/tela_login.png)

![Imagem 2](docs/tela_cadastro.png)

![Imagem 2](docs/tela_flashcards.png)

![Imagem 2](docs/tela_iniciar_desafio.png)

![Imagem 2](docs/tela_desafio.png)


## Project structure

The Django project consists of 5 applications, in addition to the central core.

```bash
.
├── backend
│ ├── core
│ ├── users
│ ├── flashcards 
│ ├── challenges
│ ├── books
│ ├── reports
│ ├── templates
│ └── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md

```

## Installing the dependencies

First install the project's dependencies in a virtual environment:

```bash
poetry install
```

## Activating the virtual environment

Run the command below to activate the virtual environment created by poetry:

```bash
poetry shell
```

## Run the migrations

Run the migrations using the following command:

```bash
task migrations
```

## Run the project

To start the project, use the following command:

```bash
task run
```
