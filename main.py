from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request/response validation
class Todo(BaseModel):
    id: int
    task: str
    done: bool = False

# In-memory database
todos = {}

# Create a Todo
@app.post("/todos")
def create_todo(todo: Todo):
    if todo.id in todos:
        raise HTTPException(status_code=400, detail="Todo already exists")
    todos[todo.id] = todo.model_dump()
    return {"message": "Todo created", "todo": todos[todo.id]}

# Get all Todos
@app.get("/todos")
def get_todos():
    return todos

# Get a specific Todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

# Update a Todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = todo.model_dump()
    return {"message": "Todo updated", "todo": todos[todo_id]}

# Delete a Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": "Todo deleted"}
