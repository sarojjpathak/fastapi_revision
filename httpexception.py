from fastapi import FastAPI,HTTPException,status
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/user/{user_id}")
def home(user_id:int):
    if user_id != 10:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User {user_id} not found")
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":f"User {user_id} found"})



def dependency():
    
