# 📚 About the Project

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/release)
[![Django Version](https://img.shields.io/badge/Django-5.0%2B-green)](https://docs.djangoproject.com/en/stable/releases/)
[![HTML Version](https://img.shields.io/badge/HTML-5-orange)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS Version](https://img.shields.io/badge/CSS-3-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)

This project was developed during [PSW 9.0](https://pythonando.com.br/psw/inscricao/psw9.0) by [Pythonando](https://pythonando.com.br). It is a study-focused application that uses **flashcards**, allowing users to create cards to review and strengthen their knowledge on various topics.

---

## 🌐 Access the Application

The project is deployed and accessible at: [pyflaskcards.mateus-dev-me.com.br](https://pyflaskcards.mateus-dev-me.com.br)

---

## 🚀 Features

- Create flashcards for different subjects.
- Challenge mode to test your knowledge.
- Reports to track performance.

---

## ⚙️ Requirements

- **Python**: 3.10 or higher.
- **Poetry**: Python dependency manager.

---

## 🖼️ Application Preview

Here are some screenshots of the application in action:

- **Login Screen**  
  ![Login](docs/tela_login.png)

- **User Registration**  
  ![Registration](docs/tela_cadastro.png)

- **Flashcards List**  
  ![Flashcards](docs/tela_flashcards.png)

- **Start Challenge**  
  ![Start Challenge](docs/tela_iniciar_desafio.png)

- **Challenge Mode**  
  ![Challenge](docs/tela_desafio.png)

---

## 🗂️ Project Structure

Below is the main structure of the Django project, which is composed of 5 applications and a central core:

```bash
.
├── core               # Project configuration and core
├── users              # User management
├── flashcards         # Flashcard creation and management logic
├── challenges         # Challenge module
├── books              # Management of complementary materials
├── reports            # Report generation
├── templates          # HTML templates
├── manage.py          # Django's main command
├── poetry.lock        # Poetry-managed dependencies file
├── pyproject.toml     # Project configurations
├── requirements.txt   # Python dependencies file
├── Dockerfile         # Docker container instructions
├── compose.yml        # Docker Compose configuration
├── .env.example       # Example environment variables file
└── README.md          # Project documentation
```

---

## 🛠️ How to Run the Project

Follow these steps to set up and run the project locally:

1. **Install Dependencies**  
   Install the project dependencies in a virtual environment:
   ```bash
   poetry install
   ```

2. **Activate the Virtual Environment**  
   Activate the virtual environment created by Poetry:
   ```bash
   poetry shell
   ```

3. **Run the Application**  
   Start the application with the following command:
   ```bash
   task run
   ```

Once the server is running, you can access the application in your browser at `http://localhost:8000`.

---

## 🧬 Future Testing

To ensure the quality and reliability of the application, testing will be implemented in future updates. The planned testing framework and strategy include:

1. **Testing Framework**  
   The application will use [Pytest](https://pytest.org/) for writing and running test cases. Additional plugins like `pytest-django` will be used for Django-specific tests.

2. **Testing Levels**  
   - **Unit Tests**: To verify individual components such as models, views, and utility functions.
   - **Integration Tests**: To ensure components work seamlessly together (e.g., views and templates).
   - **End-to-End (E2E) Tests**: To test the entire user flow using tools like Selenium or Playwright.

3. **How to Run Tests**  
   Once tests are implemented, you will be able to run them using:
   ```bash
   pytest
   ```

4. **Continuous Integration**  
   CI pipelines will be configured (e.g., using GitHub Actions) to run tests automatically on every push or pull request.

5. **Testing To-Do List**  
   Below are the specific components that will be tested:
   
   ### Core
   - [ ] Models
   - [ ] Views

   ### Users
   - [ ] Models
   - [ ] Views

   ### Flashcards
   - [ ] Models
   - [ ] Views

   ### Challenges
   - [ ] Models
   - [ ] Views

   ### Books
   - [ ] Models
   - [ ] Views

   ### Reports
   - [ ] Models
   - [ ] Views

Stay tuned for updates as we enhance the project's testing capabilities! 🚀

---

Let me know if you'd like further additions or adjustments! 😊


