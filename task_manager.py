# Student Task Manager

tasks = []
next_id = 1

def add_task(title):
    global next_id
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1
    return task
