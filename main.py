from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Multiplication API")

# Request body model
class Numbers(BaseModel):
    a: float
    b: float

# POST endpoint to multiply two numbers
@app.post("/multiply")
def multiply(numbers: Numbers):
    result = numbers.a * numbers.b
    return {"a": numbers.a, "b": numbers.b, "result": result}
