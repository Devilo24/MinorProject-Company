import new_task
import gmanager
import json
task_list = "tasks.json"

class Manager_task_assignment:

    def __init__(self, department):
        self.department = department

    def task_assignment_delivery_department(self):
        assigned_by = ""
        roles = ""
        print("Welcome to task portal")
        name = input("Enter the name of the task: ")
        work_id = input("Enter the id of the task: ")
        department = input("Enter the department name :")
        if department == self.department:
            print("Status \n1:Unassigned \n2:Assigned \n3:Cancelled \n4:Resolved")

            status = input("Enter task status (unassigned/assigned/pending/resolved):")  # unassigned, assigned, pending, resolved

            if status == "assigned":
                print("Roles \n0:General Manager\n1:Manager Delivery \n2:Manager Markerting,\n3-5:Workers Delivery,\n6-9:Workers Marketing")
                role = input(
                    "Enter the role to assign Task (3-5:Workers Delivery): ")  # role:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H
                roles = role
                result = gmanager.task_check_gm(role)  # this result is counting assigned task is 3 or less\

                #after assigning task a notification need to sent. notification module will be created here.
                if result:
                    assigned_by = input("Enter the name who is assigning task: ")
                    assigned_to = input("Enter the name to whom task is assigned: ")
                    new_task.create_task(name, work_id, department, roles, assigned_by, status, assigned_to)
                    gmanager.general_manager_notification(work_id, department, assigned_to)

            elif status == "unassigned":
                assigned_by = input("enter the name who is assigning the work: ")
                print("Roles \n0:General Manager\n1:Manager Delivery \n2:Manager Markerting,\n3-5:Workers Delivery,\n6-9:Workers Marketing")
                role = input("Enter the role to assign Task (3-5:Workers Delivery): ")
                roles = role
                result = gmanager.task_check_gm(role)
                if result:
                    assigned_by = input("Enter the name who is assigning task: ")
                    assigned_to = input("Enter the name to whom task is assigned: ")
                    with open(task_list) as json_file:
                        data = json.load(json_file)
                    for val in data:
                        if val['name']==name and val['status']=='unassigned':
                            val['status']='assigned'
                            val['assigned_by']=assigned_by
                            val['assigned_to']=assigned_to
                    with open(task_list, mode="w") as json_file:
                        json.dump(data, json_file)
                    print('Task Assigned to'+assigned_to)
                #new_task.create_task(name, work_id, department, roles, assigned_by, status, assigned_to)

        else:
            print("Task assigned to wrong department")
            return False

    def task_assignment_marketing_department(self):

        assigned_by = ""
        roles = ""
        print("Welcome to task portal")
        name = input("Enter the name of the task: ")
        work_id = input("Enter the id of the task: ")
        department = input("enter the department name :")

        if department == self.department:
            print("Status \n1:Unassigned \n2:Assigned \n3:Cancelled \n4:Resolved")
            status = input("Enter task status (unassigned/assigned/pending/resolved):")  # unassigned, assigned, pending, resolved

            if department == self.department:
                print("Status \n1:Unassigned \n2:Assigned \n3:Cancelled \n4:Resolved")

            status = input("Enter task status \n1:unassigned \n2:assigned \n 3:pending \n 4:resolved):")  # unassigned, assigned, pending, resolved

            if status == "assigned":
                print("Roles \n0:General Manager\n1:Manager Delivery \n2:Manager Markerting,\n3-5:Workers Delivery,\n6-9:Workers Marketing")
                role = input(
                    "Enter the role to assign Task (6-9:Workers Marketing): ")  # role:0--GM,1:M_S,2:M_H,3-5:W_S,6-9:W_H
                roles = role
                result = gmanager.task_check_gm(role)  # this result is counting assigned task is 3 or less\

                #after assigning task a notification need to sent. notification module will be created here.
                if result:
                    assigned_by = input("Enter the name who is assigning task: ")
                    assigned_to = input("Enter the name to whom task is assigned: ")
                    new_task.create_task(name, work_id, department, role, assigned_by, status, assigned_to)
                    gmanager.general_manager_notification(work_id, department, assigned_to)

            elif status == "unassigned":
                assigned_by = input("enter the name who is assigning the work: ")
                print("Roles \n0:General Manager\n1:Manager Delivery \n2:Manager Markerting,\n3-5:Workers Delivery,\n6-9:Workers Marketing")
                role = input("Enter the role to assign Task (3-5:Workers Delivery): ")
                roles = role
                result = gmanager.task_check_gm(role)
                if result:
                    assigned_by = input("Enter the name who is assigning task: ")
                    assigned_to = input("Enter the name to whom task is assigned: ")
                    with open(task_list) as json_file:
                        data = json.load(json_file)
                    for val in data:
                        if val['name']==name and val['status']=='unassigned':
                            val['status']='assigned'
                            val['assigned_by']=assigned_by
                            val['assigned_to']=assigned_to
                    with open(task_list, mode="w") as json_file:
                        json.dump(data, json_file)
                    print('Task Assigned to '+assigned_to)
        else:
            print("Task assigned to wrong department")
            return False


def manager_as_task_assigne(department):

    m = Manager_task_assignment(department)
    if department == "Delivery":
        m.task_assignment_delivery_department()
    else:
        m.task_assignment_marketing_department()


