from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
todo = []
class Todo(BaseModel):
    id: int = 1
    todo: str = "learn fast API"
    status: bool





@app.get("/")
def home():
    return {"list": todo}
    
@app.post("/todo",status_code =status.HTTP_201_CREATED)
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


#checking responce header
class UserResponse(BaseModel):
    name:str
    age:int
    

@app.get("/responcecheck",response_model=UserResponse)
def responce():
    return {

        "name":"saroj pathak",
        "age":21,
        "password":"saroj@%123"

    }#as we have assign responce model the password will not be visible to user 



#from fastapi import status

# status.HTTP_200_OK
# status.HTTP_201_CREATED
# status.HTTP_204_NO_CONTENT

# status.HTTP_400_BAD_REQUEST
# status.HTTP_401_UNAUTHORIZED
# status.HTTP_403_FORBIDDEN
# status.HTTP_404_NOT_FOUND

# status.HTTP_422_UNPROCESSABLE_ENTITY

# status.HTTP_500_INTERNAL_SERVER_ERROR


# FastAPI status 
# status is a module in FastAPI that provides named HTTP status code constants.
# It makes code more readable than using numeric values directly.
# Commonly used in route decorators and HTTPException.

# FastAPI JSONResponse 
# JSONResponse is a response class used to manually create and customise an HTTP JSON response.
# It allows you to set:
# Custom status code
# Custom JSON content
# Custom headers (and cookies if needed)
# FastAPI automatically creates a JSONResponse when you return a dictionary, so explicit use is only needed when you want more control.
# from fastapi import status
# from fastapi.responses import JSONResponse

# return JSONResponse(
#     status_code=status.HTTP_201_CREATED,
#     content={"message": "Todo created successfully"}
# )
@app.get("/errorhandling/{id}")
def check(id:int):
    if id != 1:#if id is not 1 then it will raise HTTP exception
        raise HTTPException(status_code=404,detail="user not found")
    return {"id":1,"name":"Saroj"}
    