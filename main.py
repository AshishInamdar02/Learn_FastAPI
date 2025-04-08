from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def index():
    return{"messsage": "Hello World"}