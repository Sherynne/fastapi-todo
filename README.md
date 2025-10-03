FastAPI Todo API

Overview

This is a beginner-friendly backend project built with FastAPI and Pydantic, demonstrating CRUD operations (Create, Read, Update, Delete) using in-memory storage.The project simulates a task management system where users can create, view, update and delete todos  similar to what a small backend API would do in a real-world application.

While this is primarily a backend project, it was developed with the help of generative AI (ChatGPT) to Scaffold endpoints and Pydantic models, Implement error handling for missing or duplicate todos and Generate example requests and README documentation.

The AI Prompt Journal included in this repository shows exactly how AI was used to assist learning and implementation.This project was completed as part of the Moringa School backend development learning track.


 Features

* Create a todo item
* Retrieve all todos
* Retrieve a specific todo by ID
* Update a todo item
* Delete a todo item

---

 Installation & Setup

1. Clone the project

```bash
git clone <your-repo-link>
cd PythonProject2
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

* Windows (PowerShell):

```bash
.venv\Scripts\Activate
```

* Linux/Mac:

```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

5. Run the app

```bash
uvicorn main:app --reload


The API will run at: `http://127.0.0.1:8000`
Interactive docs available at: `http://127.0.0.1:8000/docs`



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
curl -X POST 'http://127.0.0.1:8000/todos' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"id": 1, "task": "Learn FastAPI", "done": false}'
```

Get All Todos

bash
curl -X GET 'http://127.0.0.1:8000/todos'


Update a Todo

bash
curl -X PUT 'http://127.0.0.1:8000/todos/1' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"task": "Learn FastAPI deeply", "done": true}'



AI Prompt Journal

| Prompt Used                              | AI Response Summary                                               | Reflection                                                                      |
| ---------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| "Create a FastAPI CRUD Todo API"         | Provided a basic structure with endpoints and Pydantic model      | Helped understand request validation, route definitions, and response structure |
| "How to handle duplicate IDs in FastAPI" | Suggested raising HTTPException with status code 400              | Enabled robust error handling in the API                                        |
| "Generate README for FastAPI project"    | Supplied a formatted README with setup instructions and endpoints | Helped produce professional documentation for submission                        |

Reflection: Using AI allowed me to quickly scaffold the project, learn best practices for FastAPI, and draft clear documentation, saving significant time while ensuring correctness.


Common Errors & Fixes

1. Pydantic not found

   * Cause: Dependencies not installed in virtual environment.
   * Solution: `pip install pydantic fastapi uvicorn`

2. Virtual environment activation issues

   * Cause: Using wrong activation command for PowerShell.
   * Solution: Use `.venv\Scripts\Activate` for Windows PowerShell.

3. Merge conflicts when pushing to GitHub

   * Cause: Remote repository had pre-existing files.
   * Solution: `git pull origin main --allow-unrelated-histories`, resolve conflicts, then `git push`.

4. Accidentally committing `.idea` or `__pycache__`

   * Cause: IDE and cache files included in commit.
   * Solution: Add `.gitignore` with `.venv/`, `__pycache__/`, `.idea/`, then remove cached files using `git rm -r --cached <files>`.

5. SyntaxError in main.py

   * Cause: Extra text or copy-paste errors in Python file.
   * Solution: Remove any trailing text after `return` statements and validate code.

 References

* [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://docs.pydantic.dev/)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* Tutorials and blogs on FastAPI CRUD applications






