# 🚀 Task Manager CLI | DevOps-Oriented Python Project

A modular CLI (Command Line Interface) application built with Python to manage tasks directly from the terminal.

This project is part of my transition from **Manual QA → DevOps / Backend Engineering**, focusing on clean architecture, automation, and production-ready practices.

---

## 🧠 Key Concepts Applied

* Layered architecture (CLI → Service → Storage)
* Separation of concerns
* Data persistence using JSON
* Error handling and validation
* CLI development with `argparse`
* UUID-based entity management

---

## ⚙️ Features

* Add tasks
* List tasks
* Mark tasks as completed
* Remove tasks
* Prevent duplicate tasks
* JSON-based persistence

---

## 🏗 Architecture

```text
User Input (CLI)
        ↓
cli.py (interface)
        ↓
service.py (business logic)
        ↓
storage.py (data handling)
        ↓
tasks.json (data persistence)
```

---

## 📁 Project Structure

```text
task_manager_cli/
├── src/
│   └── taskcli/
│       ├── cli.py
│       ├── service.py
│       ├── model.py
│       └── storage.py
│
├── data/
│   └── tasks.json
│
├── tests/
│   └── test_service.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

Activate your virtual environment:

```bash
env\Scripts\activate
```

Run the CLI:

```bash
python src/taskcli/cli.py add "Learn DevOps"
python src/taskcli/cli.py list
python src/taskcli/cli.py complete <task_id>
python src/taskcli/cli.py remove <task_id>
```

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

---

## 🔄 CI/CD Pipeline

This project includes a GitHub Actions pipeline that:

* Runs automated tests with `pytest`
* Validates code quality (linting)
* Builds the Docker image

The pipeline is triggered on every push and pull request to the `main` branch.

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t taskcli .
```

Run the container:

```bash
docker run --rm taskcli
```

---

## 🎯 What This Project Demonstrates

* Ability to design modular Python applications
* Understanding of backend architecture principles
* CLI tool development (similar to DevOps tools like Docker or kubectl)
* Implementation of CI/CD pipelines with GitHub Actions
* Containerization using Docker

---

## 🚧 Future Improvements

* Add more unit tests
* Improve CLI user experience
* Add logging system
* Implement FastAPI layer (API version)
* Deploy to cloud (AWS)

---

## 👩‍💻 About Me

I am a QA professional transitioning into DevOps and Backend Engineering.

This project reflects my focus on:

* Automation
* Scalable system design
* Real-world engineering practices

---

## ⭐ Why This Project Matters

This is not just a task manager.

It is a **foundation project** that evolves into:

```text
CLI → API → Docker → CI/CD → Cloud Deployment
```
