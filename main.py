import json

from fastapi import FastAPI

app = FastAPI()

"""
HTTP Methods:

1. GET: Retrieve data from the server.
2. POST: Send data to the server to create a new resource.
3. PUT: Update an existing resource on the server.
4. DELETE: Remove an existing resource from the server.

"""

@app.get("/")
def greet():
    return {"Hello and Welcome to Arindam Sharma AI School!"}

@app.get("/hello")
def hello():
    return {"This is hello page"}

# Helper Function
def load_data():
    with open("students.json") as f:
        return json.load(f)

@app.get("/students")
def students():
    return load_data()