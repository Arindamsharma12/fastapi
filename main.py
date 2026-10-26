from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"Hello and Welcome to Arindam Sharma AI School!"}