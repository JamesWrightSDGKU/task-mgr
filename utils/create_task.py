import requests


URL = "http://127.0.0.1:5000/tasks"

def create_task(name, summary, description):
    task_data = {
        "name": name,
        "summary": summary,
        "description": description
    }
    response = requests.post(URL, json=task_data)
    if response.status_code == 204:
        print("Task created successfully!")
    else:
        print("Request failed with status code: %s" % response.status_code)


if __name__ == "__main__":
    print("Create task:")
    name = input("Task name: ")
    summary = input("Task summary: ")
    description = input("Task description: ")
    create_task(name, summary, description)