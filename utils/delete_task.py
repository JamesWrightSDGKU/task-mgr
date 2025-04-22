import requests

from app.database import task

URL = "http://127.0.0.1:5000/tasks/<int:pk>"

def delete_task(pk):
    print(task.scan())
    deletion = input("Input id of task to delete: ")


