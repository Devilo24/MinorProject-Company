import json

tasks = "tasks.json"


class Task:

    def __init__(self, name, work_id, department, role, assigned_by, status, assigned_to):
        self.name = name
        self.work_id = work_id
        self.department = department
        self.role = role
        self.assigned_by = assigned_by
        self.status = status
        self.assigned_to = assigned_to


def create_task(name, work_id, department, role, assigned_by, status, assigned_to):

    task = Task(name, work_id, department, role, assigned_by, status, assigned_to)
    with open(tasks) as task_file:
        data = json.load(task_file)

    data.append(
        {
            "name": task.name,
            "work_id": task.work_id,
            "department": task.department,
            "role": task.role,
            "assignedBy": task.assigned_by,
            "status": task.status,
            "assignedTo": task.assigned_to
        }
    )
    with open(tasks, mode="w") as task_file:
        json.dump(data, task_file)
        print("Task Created ")

