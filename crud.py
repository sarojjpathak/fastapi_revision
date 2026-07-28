from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todo = []
class Todo(BaseModel):
    id: int = 1
    todo: str = "learn fast API"
    status: bool
@app.get("/")
def home():
    return {"list": todo}
@app.post("/todo")
def create_todo(todos: Todo):
    todo.append(todos)
    return {
        "message": "Todo added successfully",
        "todo": todos
    }


# Get todo by ID
@app.get("/todo/{id}")
def filter_data(id: int):
    for todoo in todo:
        if todoo.id == id:
            return {"data": todoo}

    return {"message": "Invalid ID"}


# Update existing todo
@app.put("/update/{userid}")
def update(userid: int, updatedtodo: Todo):
    for index, todoo in enumerate(todo):
        if todoo.id == userid:
            todo[index] = updatedtodo
            return {
                "message": "Updated successfully",
                "todo": updatedtodo
            }

    return {"message": "Todo not found"}


# Delete todo
@app.delete("/delete/{id_to_delete}")
def delete(id_to_delete: int):
    for index, todoo in enumerate(todo):
        if todoo.id == id_to_delete:
            del todo[index]
            return {
                "message": "Deleted successfully",
                "list": todo
            }

    return {"message": "Todo not found"}