

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


