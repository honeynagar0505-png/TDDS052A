from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Hello World from FastAPI!"}

# About route
@app.get("/about")
def about():
    return {"about": "This is my first FastAPI project."}

# Users route
@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Honey"},
        {"id": 2, "name": "Kimu"},
        {"id": 3, "name": "Jeenu"}
    ]
    return users