from fastapi import FastAPI ,status,Depends,Request
from fastapi.responses import JSONResponse
import time
app = FastAPI()

def timeofreq():
    return time.time()


@app.middleware("http")
async def my_middleware(request:Request,call_next):
    
    start = time.time()
    print(f"starts time {start}")
    response = await call_next(request)
    processTime = time.time()-start
    print(f"process time : {processTime}\npath{request.url.path}")
    return response

@app.get("/home")
def home(time = Depends(timeofreq)):
    print(f"in end path{time}")
    return {"message":"welcome to our home"}
@app.get("/school")
def school(time = Depends(timeofreq)):
    print(f"in end path{time}")
    return {"message":"welcome to our school"}
@app.get("/college")
def college(time = Depends(timeofreq)):
    print(f"in end path{time}")
    return {"message":"welcome to out clz"}
    
    
