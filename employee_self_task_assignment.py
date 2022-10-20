
import json
task = "tasks.json"
emp = "employee_list.json"



class Employee:

    def __init__(self, name, emp_id, role, department, password, task_count):

        self.name = name
        self.emp_id = emp_id
        self.role = role
        self.department = department
        self.password = password
        self.task_count = task_count


class Workers_task_assignment:

    def __init__(self, department, role, name):
        self.department = department
        self.role = role
        self.name = name

    def assign_delivery_tasks(self):
        with open(task) as json_file:
            data = json.load(json_file)
        with open(emp) as json_file:
            data_1 = json.load(json_file)

        for val in data:
            if val["status"] == "unassigned" and val['department'] == self.department:
                print(val)

        task_self = int(input("Want to assign task to yourself? \n0: yes \n1:No  "))

        if task_self == 0:
            for i in data_1:
                if i['role'] == self.role:
                    if i['count'] == 3:
                        print("you cannot assign task to yourself because you have reached the max number of work")
                    else:
                        id_work = input("Please select the id of the work: ")
                        for val in data:
                            if val['work_id'] == id_work:
                                val['role'] = self.role
                                val['status'] = 'assigned'
                                val['assigned_to'] = self.name
                                with open(task, mode="w") as json_file:
                                    json.dump(data, json_file)
                                break
                        for i in data_1:
                            if i['role'] == self.role:
                                i['task_count'] += 1
                                with open(emp, mode="w") as json_file:
                                    json.dump(data_1, json_file)
                                print("Task Assign to yourself")
                                return True

        else:
            return False

    def assign_marketing_tasks(self):
        with open(task) as json_file:
            data = json.load(json_file)
        with open(emp) as json_file:
            data_1 = json.load(json_file)

        for i in data:
            if i["status"] == "unassigned" and i['department'] == self.department:
                print(i)

        task_self = int(input("Want to assign task to yourself? \n0: yes \n1:No  "))
        if task_self == 0:
            for i in data_1:
                if i['role'] == self.role:
                    if i['count'] == 3:
                        print("you cannot assign task to yourself because you have reached the max number of work")
                    else:
                        work_id = input("Please select the id of the work: ")
                        for val in data:
                            if val['work_id'] == work_id:
                                val['role'] = self.role
                                val['status'] = 'assigned'
                                val['assigned_to'] = self.name
                                with open(task, mode="w") as json_file:
                                    json.dump(data, json_file)
                                break

                        for val in data_1:
                            if val['role'] == self.role:
                                val[''] += 1
                                with open(emp, mode="w") as json_file:
                                    json.dump(data_1, json_file)
                                print("Task Assign to yourself")
                                return True

        else:
            return False


def worker_self_task_assignment(department, role, name):
    a=Workers_task_assignment(department, role, name)
    if department == "Delivery":
        a.assign_delivery_tasks()
    else:
        a.assign_marketing_tasks()






