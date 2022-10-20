import json
import datetime

emp_details = "employee_list.json"
tasks = "tasks.json"
notification_list = "notification_file.json"
permission_list="permission_file.json"


class GManager_task_assignment:

    def __init__(self, role):
        self.role = role

    def task_list_for_general_manager(self):
        with open(emp_details) as emp_data:
            file_data = json.load(emp_data)

        for val in file_data:
            if val['role'] == self.role:
                if val['task_count'] == 3:
                    print("Task cannot be assigned as worker has already been assigned 3 tasks")
                    return False

                else:
                    val['task_count'] += 1
                    with open(emp_details, mode="w") as emp_data:
                        json.dump(file_data, emp_data)
                    return True


def task_check_gm(role):

    task_count = GManager_task_assignment(role)
    return task_count.task_list_for_general_manager()


def open_tasks():

    with open(tasks) as task_file:
        task_list = json.load(task_file)

    for val in task_list:
        print(val)


class Notification:
    def __init__(self, work_id, department, assigned_to):
        self.work_id = work_id
        self.department = department
        self.assigned_to = assigned_to

    def notification_update(self):
        current_time = datetime.datetime.now()

        work = str("Work ID: "+self.work_id+"Department: "+self.department +"Assigned to:"+self.assigned_to+"Time " + current_time.strftime("%d/%m/%Y"))
        with open(notification_list) as json_file:
            notification = json.load(json_file)
        notification.append(
            {
                "notification_list": work,
                "department": self.department
            }
        )

        with open(notification_list, mode="w") as json_file:
            json.dump(notification, json_file)


class View_notification:
    def notifications_work_view(self, role):
        if role == "0":
            with open(notification_list) as json_file:
                notification = json.load(json_file)
            for val in notification:
                print(val)
        elif role == "1":
            with open(notification_list) as json_file:
                notification = json.load(json_file)
            for val in notification:
                if val['department'] == 'Delivery':
                    print(val)
        elif role == "2":
            with open(notification_list) as json_file:
                notification = json.load(json_file)
            for val in notification:
                if val['department'] == 'Marketing':
                    print(val)


class Permission:
    def __init__(self, work_id, department, permission):
        self.work_id = work_id
        self.department = department
        self.permission = permission

    def permission_message(self):
        with open(permission_list) as json_file:
            permissions = json.load(json_file)

        permissions.append(
            {
                "work_id": self.work_id,
                "department": self.department,
                "permission": self.permission
            }
        )

        with open(permission_list, mode="w") as json_file:
            json.dump(permissions, json_file)


def general_manager_notification(work_id, department, assigned_to):
    notifications = Notification(work_id, department, assigned_to)
    notifications.notification_update()


def general_manager_notification_look_up(role):
    notifications = View_notification()
    notifications.notifications_work_view(role)


def permission_look_up(work_id, department, permission):
    permissions = Permission(work_id, department, permission)
    permissions.permission_message()

