import uvicorn
from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel, Field
app = FastAPI()

class User(BaseModel): # This is for Pydantic Model
    name: str=  Field(..., max_length=10, title="Max length of name should be 10")
    age: int
    email: str = Field(None) # This will not accept NULL.
    phone_no: Optional[str]=Field(None, max_length=13) # Allows NULL values.

@app.get("/")
async def index(): # This is a basic function.
    return{"messsage": "Hello World"}

@app.get("/users/{name}/greet") # This is for Path Parameter.
def greet(name: str):
    return{"Hello": name}

@app.get("/users/{name}/{age}/greet") # This is for Path Parameter.
def greet_age(name: str, age: int):
    return{"Hi": name, "Your age is:": age}

@app.get("/users/{name}/greet-with-age") # This is for Query Parameter.
def greet_query(name: str, age: int):
    return{"Hi":name, "Your age is": age}

@app.get("/users/{name}/{age}/greet-with-validations") # This is for Path Parameter with Validations.
def greet_validations(name: str=Path(...,min_length=3, max_length=10), age: int=Path(..., ge=1, le=100)):
    return{"Hi": name, "Age": age}

@app.get("/users/{name}/{age}/greet-with-validations-perc") # This is for Query Parameter with Validations.
def greet_validations_perc(*,name: str=Path(...,min_length=3, max_length=10), age: int=Path(...,ge=1, le=100), perc: float=Query(...,ge=0, le=100)):
    return{"Hi": name, "Age": age, "Perc": perc}

@app.post("/create-user") # This is for Pydantic Model
def create_user(user: User):
    return{f"User {user.name} has been created with data {user}"} 


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)