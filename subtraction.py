# import FastAPI and BaseModel
from fastapi import FastAPI
from pydantic import BaseModel
# Create FastAPI app instance
app = FastAPI()
@app.get("/home")
def home():
    return{
        "Your FastAPI was created successfully"
    }
    
# Create BaseModel for input validation
class Numbers(BaseModel):
    n1: int
    n2: int
   
# POST method to perform addition 
@app.post("/addition")
def add(data: Numbers):
    result = data.n1 - data.n2
    return{
        "operation":"addition",
        "result":result
    }