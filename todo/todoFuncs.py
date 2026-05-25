from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
)

todos = {}
current_id = 1

class Todo(BaseModel):
    title: str
    completed: bool = False
@router.get("/sheets/{sheetId}/{sheetName}")
def get_sheet(sheetId: str, sheetName: str):
    data = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}")
    result = data.to_csv(sep=",", header=False)
    return result

@router.get("/hello")
def hello():
    return {"hello": "world"}

@router.get("/")
def get_all_todos():
    global todos
    return todos

@router.get("/{todo_id}")
def get_todo(todo_id: int):
    global todos
    return todos[todo_id]

@router.post("/postTodo")
def create_todo(todo: Todo):
    global todos
    global current_id

    result = Todo(title = todo.title)

    todos.update({ current_id : result })
    current_id += 1
    return result

@router.put("/updateTodo")
def update_todo(taskId: str, taskToChangeTo: str):
    global todos
    todos[taskId].title = taskToChangeTo

@router.delete("/deleteTodo")
def delete_todo(taskId: int):
    global todos
    if taskId in todos:
        del todos[taskId]
        return f"{taskId} has been deleted"
    else:
        return f"{taskId} does not exist"

@router.get("/totalTodos")
def get_total_todos():
    return current_id - 1

@router.get("/activeTodos")
def get_active_todos():
    return len(todos)