import json

from fastapi import FastAPI, HTTPException, Path

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

# student_id -> This is our Path Parameter.
@app.get("/students/{student_id}")
def get_id(
    student_id:str = Path(...,description="The Id of the student",examples=["S001"])
):
    data = load_data()
    if student_id not in data:
        raise HTTPException(status_code=404,detail=f"Student with Id '{student_id}' is not found")
    return data[student_id]
    