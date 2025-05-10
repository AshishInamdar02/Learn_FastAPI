import uvicorn
from fastapi import FastAPI
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


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)