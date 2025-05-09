import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def index():
    return{"messsage": "Hello World"}

@app.get("/greet/{name}")
async def greet(name: str):
    return{"Hello": name}

@app.get("/greet/{name}/{age}")
async def greet_age(name: str, age: int):
    return{"Hi": name, "Your age is:": age}

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)