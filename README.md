FastAPI Todo App

Overview

This is a beginner-friendly backend project built with FastAPI and Pydantic, demonstrating CRUD operations (Create, Read, Update, Delete) using in-memory storage.The project simulates a task management system where users can create, view, update and delete todos  similar to what a small backend API would do in a real-world application.

While this is primarily a backend project, it was developed with the help of generative AI (ChatGPT) to Scaffold endpoints and Pydantic models, Implement error handling for missing or duplicate todos and Generate example requests and README documentation.

The AI Prompt Journal included in this repository shows exactly how AI was used to assist learning and implementation.This project was completed as part of the Moringa School backend development learning track.


 Features

* Create, view, update, and delete todo items
* Interactive API docs via FastAPI
* In-memory storage (resets on restart)

Tech Summary

FastAPI: Modern Python web framework for building APIs with high performance, automatic validation and interactive docs.
Use case:Simple task tracker for personal or team todos.


Setup

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install fastapi pydantic uvicorn

# Run the app
uvicorn main:app --reload
```

API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


API Endpoints

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | `/todos`      | Create a todo    |
| GET    | `/todos`      | Get all todos    |
| GET    | `/todos/{id}` | Get a todo by ID |
| PUT    | `/todos/{id}` | Update a todo    |
| DELETE | `/todos/{id}` | Delete a todo    |

---

Example Requests

Create a Todo

```bash
curl -X POST 'http://127.0.0.1:8000/todos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "id": 1,
  "task": "Learn FastAPI",
  "done": false
}'
```

Get All Todos

```bash
curl -X GET 'http://127.0.0.1:8000/todos'
```

---


