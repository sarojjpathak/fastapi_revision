from fastapi import FastAPI,status,Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

todo = []
app = FastAPI()
def common_logic():
    return {

        "message":"welcome saroj"
    }
def home():
    return {"message":"complete user details are listed below ","user":todo}
class User(BaseModel):
    name:str="saroj"
    age:int=21
    todo:str="complete FasrAPI"
@app.post("/")

#learning dependency injection in fastapi
def user(user:User,wish = Depends(common_logic)):
    todo.append(user)
    return {"message":"complete user details are listed below ","user":todo,"wish":wish}
@app.get("/dependency")
def dependency(data = Depends(common_logic)):
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=data
                        )



def details_dependency():
    return{
      "name":"saroj pathak",
      "age":21,
      "profession":"software engineer"



    }

@app.get("/profile")
def profile(data:dict=Depends(details_dependency)):
    return JSONResponse(
        status_code=200,
        content=data
    )


@app.get("/dash")
def dash(data:dict=Depends(details_dependency)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"Name of user ":data["name"],
                 "Age of user ":data["age"],
                 "Profession of user ":data["profession"]
                 }
    )
class UserAuth(BaseModel):
    username:str
    password:str

details_in_server = {
    "username":"saroj",
    "password":"saroj@%123",
    "JWT":"eyJhbG"
}


@app.post("/authentication")
def authentication(user:UserAuth):
    if user