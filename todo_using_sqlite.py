from fastapi import FastAPI, Depends, status, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import time
import sqlite3

app = FastAPI()

class User(BaseModel):
    id:int
    todo:str

class Updatee(BaseModel):
    id:int
    todo:str


def db_conn():
    db = sqlite3.connect("todo.db")

    try:
        yield db
    finally:
        db.close()


def create_table():
    db = sqlite3.connect("todo.db")
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            todo TEXT
        )
    """)

    db.commit()
    db.close()




create_table()
@app.post("/todo/addtodo")
def insert(user:User,db:sqlite3.Connection = Depends(db_conn)):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO users (id,todo) VALUES(?,?)

        """,(user.id,user.todo))
    
    db.commit()
    db.close()
    return {"id":user.id,"todo":user.todo}


#after completing the task in todo we can remove that 
@app.delete("/todo/completed/{id}")
def delete(id:int,db:sqlite3.Connection = Depends(db_conn)):
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM users WHERE id = ?

""",(id,))
    db.commit()
    db.close()
    return {"message":f"data from id : {id} deleted "}


#know if we want to update the todo we can do use this
@app.put("/todo/update")
def update(update:Updatee,db:sqlite3.Connection = Depends(db_conn)):
    cursor = db.cursor()


    cursor.execute("""

            UPDATE users SET todo = ? WHERE id = ?

        """,(update.todo,update.id))
    db.commit()
    db.close()
    return{
        "message":"database updated",
        "id":update.id,
        "todo":update.todo
    }


