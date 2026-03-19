# 🧰 Task Manager CLI - DevOps Project

CLI (Command Line Interface) application built with Python to manage tasks from the terminal.

This project was designed as part of my transition from Manual QA to DevOps / Backend engineering, focusing on clean architecture, modular design, and automation-friendly tools.

---

## 🚀 Features

* Add tasks
* List tasks
* Mark tasks as completed
* Remove tasks
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

## 🎯 What I Learned

* Building CLI tools in Python
* Structuring applications using layered architecture
* Managing data persistence with JSON
* Handling errors and validations
* Thinking in terms of scalable backend design

---

## 🚧 Next Steps

* Add unit tests (pytest)
* Dockerize the application
* Add CI/CD pipeline with GitHub Actions
* Improve CLI UX

---

## 👩‍💻 About Me

I am transitioning from Manual QA to DevOps/Backend engineering, focusing on automation, cloud, and scalable systems.

---

## ⭐ Why this project matters

This project demonstrates my ability to:

* Design clean and maintainable code
* Build tools used in automation workflows
* Think beyond scripts and towards real software architecture
