from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#todo app
todo = []

class Todo(BaseModel):
    id:int
    todo:str
    status:bool
@app.post("/todo")
def create_todo(todos:Todo):
    todo.append(todos)
    return {"message":"todo added","ToDo":todos}
@app.get("/todo")
def home():

    return {"message":"this are the list of thing you need to complete" ,"list":todo}


#know we try to get the data based on id
@app.get("/todo/{id}")
def filter_data(id:int):
   for todoo in todo:
      if todoo["id"] == id:
         return todoo
      
   return{"message":"invalid id"}
   



#updating existing data using put or patch