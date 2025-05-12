import uvicorn
from fastapi import FastAPI, Path, Query
app = FastAPI()

@app.get("/")
async def index(): # This is a basic function.
    return{"messsage": "Hello World"}

@app.get("/users/{name}/greet") # This is for Path Parameter.
async def greet(name: str):
    return{"Hello": name}

@app.get("/users/{name}/{age}/greet") # This is for Path Parameter.
async def greet_age(name: str, age: int):
    return{"Hi": name, "Your age is:": age}

@app.get("/users/{name}/greet-with-age") # This is for Query Parameter.
async def greet_query(name: str, age: int):
    return{"Hi":name, "Your age is": age}

@app.get("/users/{name}/{age}/greet-with-validations") # This is for Path Parameter with Validations.
async def greet_validations(name: str=Path(...,min_length=3, max_length=10), age: int=Path(..., ge=1, le=100)):
    return{"Hi": name, "Age": age}

@app.get("/users/{name}/{age}/greet-with-validations-perc") # This is for Query Parameter with Validations.
async def greet_validations(*,name: str=Path(...,min_length=3, max_length=10), age: int=Path(...,ge=1, le=100), perc: float=Query(...,ge=0, le=100)):
    return{"Hi": name, "Age": age, "Perc": perc}

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)