# 🧰 Task Manager CLI - DevOps Oriented Python Project

A modular CLI (Command Line Interface) application built with Python to manage tasks directly from the terminal.

This project is part of my transition from Manual QA to DevOps / Backend engineering, focusing on clean architecture, automation, and production-ready practices

---
## Key Concepts Applied

* Layered architecture (CLI -> Service-> Storage)
* Separation of concerns
* Data persistence using JSON
* Error handling and validation
* CLI development with argparse
* UUID-based entity management 

---

## 🚀 Features

* Add tasks
* List tasks
* Mark tasks as completed
* Remove tasks
* Prevent duplicate task
* JSON-based persistence

---

## 🧠 Architecture

This project follows a layered architecture:

```
CLI → Service → Storage → JSON
```

* **cli.py** → Handles user input from terminal
* **service.py** → Business logic (rules and validations)
* **model.py** → Data model (Task)
* **storage.py** → Data persistence (JSON file)

---

## 🛠 Tech Stack

* Python 3
* argparse (CLI)
* JSON (storage)
* UUID (unique IDs)
* Docker (coming soon)
* GitHub Actions (coming soon)

---

## 📦 Project Structure

```
task_manager_cli/
│
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
├── Dockerfile
├── pyproject.toml
└── README.md
```

---

## ⚙️ How to Run

1. Activate your environment:

```
env\Scripts\activate
```

2. Run the CLI:

```
python cli.py add "Learn DevOps"
python cli.py list
```

---

## 📌 Example

```
python cli.py add "Study Docker"
```

Output:

```
Tarea agregada: 1234-uuid - Study Docker
```

---

## Docker (Planned)

```
docker build -t taskcli .
docker run taskcli

```
---
## CI/CD (Planned)

This project will include: 
* GitHub Actions pipeline
* Automated testing with pytest
* Linting and code quality checks
---
## Testing (Planned)
```
pytest
```
---

## ⭐ Why this project demonstrates

This project demonstrates my ability to:

* Desing modular Python applications 
* Understandind of backend architecture principales
* CLI tool development (similar to DevOps tools lije, Docker, Kubectl)
* Preparatiom for DevOps workflows (Docker, CI/CD)

---

## 🚧 Next Improvements

* Add unit tests (pytest)
* Dockerize the application
* Implement CI/CD pipeline with GitHub Actions
* Improve CLI UX
* Add logging

---

## 👩‍💻 About Me

I am a QA professional transitioning into DevOps ad Backend Engineering. 

This project reflects my focus on: 
* Automations
* Scalable design 
* Real-world engineering practices 

---
## Why this Matters

This is not just a task manager. 
It is a foundation project that evolves into: 
* API 
* Containerized application
* CI/CD pipeline

---
## Future Version 

```

CLI → API → Docker → CI/CD → Cloud Deployment

```


