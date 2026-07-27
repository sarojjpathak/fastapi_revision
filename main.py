from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message":"hello world"}
#path parameter
@app.get("/user/{name}/{age}")
def user_page(name:str,age:int):
    if name != None:
     return {"message":"hello "+ name,"age":age}
    else:
       return {"message":"hello world"}
#query parameter(optional value,default value)
@app.get("/salary")
def sal(sal:int=None):#in place to None if we put 10000 it will be default value  and None is for optional value it none will give null
   return {"salary":sal}
@app.get("/product")
def product(name:str=None,price:int=1000):
   return{"productName":name,"Price":price}

#application of query parameter in real life project
#filtering price and different thing in E commerce website
#pagination etc


#POST API

@app.post("/details")
def det(user:dict):
   return{"message":"welcome THIS IS POST API","users":user}
       
#we cannot directly handle post api in browser
#we are using swager for this
#the above function doesnot ensures right data , for eg age should be int but users may give string to solve this problem we use pydantic BASEMODEL
from pydantic import BaseModel
class User(BaseModel):
   name:str="Give a name mate"
   age:int=18


#know we can use User as datatype
@app.post("/detail")
def detail(user:User):
   return{"message":"welcome THIS IS POST API","users":user}