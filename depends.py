# from fastapi import FastAPI,status,Depends
# from  fastapi.responses import JSONResponse
# app = FastAPI()
# def depend_1():
#     return {"message":"this is depend_1 function"}
# def depend_2():
#     return {"message":"this is depend_2 function"}
# @app.get("/depend1")
# def depend1(data = Depends(depend_1)):
#     return JSONResponse(
#         status_code = status.HTTP_200_OK,
#         content = data
#     )
# @app.get("/depend2")
# def depend2(data = Depends(depend_2)):
#     return JSONResponse(
#         status_code = status.HTTP_200_OK,
#         content = data
#     )
# @app.get("/")
# def home():
#     return {
#         "message":"welcome to new home page"
#     }
from fastapi import FastAPI, Depends

app = FastAPI()

# 1. Define your dependency function
def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# 2. Inject it into a route
@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons