# Student Task Manager

tasks = []
next_id = 1

def add_task(title):
    global next_id
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1
    return task

def display_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "[x]" if t["completed"] else "[ ]"
        print(f'{t["id"]}. {status} {t["title"]}')

def complete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            return True
    return False

def delete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return True
    return False
