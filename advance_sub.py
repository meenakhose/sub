from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Create FastAPI app with metadata
app = FastAPI(
    title="Advanced Math API",
    description="This API allows you to do basic math operations like addition and subtraction",
    version="1.0.0",
)

# Input validation with Pydantic
class Numbers(BaseModel):
    n1: int = Field(..., ge=0, description="First number (must be >= 0)")
    n2: int = Field(..., ge=0, description="Second number (must be >= 0)")

@app.get("/", tags=["Info"])
def home():
    return {"message": "Welcome to the Advanced Math API!"}

@app.get("/operations", tags=["Info"])
def list_operations():
    return {"available_operations": ["addition", "subtraction"]}

@app.post("/addition", tags=["Math"])
def add(data: Numbers):
    result = data.n1 + data.n2
    return {
        "operation": "addition",
        "result": result
    }

@app.post("/subtraction", tags=["Math"])
def subtract(data: Numbers):
    if data.n1 < data.n2:
        raise HTTPException(status_code=400, detail="n1 must be greater or equal to n2 for subtraction")
    result = data.n1 - data.n2
    return {
        "operation": "subtraction",
        "result": result
    }
