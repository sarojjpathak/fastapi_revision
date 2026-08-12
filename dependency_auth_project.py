from fastapi import FastAPI,status,Depends
from  fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
login = False
server_data = {
"username":"saroj",
"password":5769,
"JWT":"djrign"
}
def server_authentication():
    return server_data

class userAuth(BaseModel):
    username:str
    password:int

@app.post("/login")
def login(user:userAuth,data=Depends(server_authentication)):
    if user.username == data["username"] and user.password == data["password"]:
        global login
        login = True
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message":"login successful",
                                     "JWT":data["JWT"]
                                     }
                            )
    else:
        
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"message":"login failed"}
                            )
@app.get("/dashboard")
def dashboard(data=Depends(server_authentication)):
    if login:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message":"welcome to dashboard",
                                     "username":data["username"],
                                     "JWT":data["JWT"]
                                     }
                            )
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"message":"login failed"}
                            )
@app.get("/")
def home():
    return {"message":"welcome to home page"}