from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# ReST - Representational State Transfer
# ReST is an architectural design pattern for building network-connected services
@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.create_task(task_data)
    return "", 204

@app.put("/tasks/<int:pk>")
def update_task_by_id(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task_by_id(pk):
    task.delete_by_id(pk)
    return "", 204

@app.patch("/tasks/<int:pk>") 
def deactivate_task(pk):
    task.deactivate_task(pk)
    return "", 204

# change task.py functions to not return tasks where is_done is TRUE