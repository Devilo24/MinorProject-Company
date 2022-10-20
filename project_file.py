import new_task
import json
import gmanager
import manager
import employee_self_task_assignment
task_list = "tasks.json"
emp_details = "employee_list.json"
notification_details = "notification_file.json"
permission_details = "permission_file.json"

def task_registration():
    assigned_by = ""
    role = ""
    print("Welcome to task assign portal")
    name = input("Enter task name:")
    work_id = input("Enter work ID of task:")
    department = input("Enter the department name")
    print("Task status: \nUnassigned \nAssigned \nCancel task \nReassign Task")
    status = input("Enter the task status:")
    if status == "assigned":
        print("Roles \n0:General Manager\n1:Manager Delivery \n2:Manager Markerting,\n3-5:Workers Delivery,\n6-9:Workers Marketing \n")
        role = input("Enter the role to whom task will be assigned:")
        final_result = gmanager.task_check_gm(role)
        if final_result:
            assigned_by = input("Enter the name of the person who is assigning the task:")
            new_task.create_task(name, work_id, department, role, assigned_by, status, role)
            gmanager.general_manager_notification(work_id, department, role)
    elif status == "unassigned":
        role = input("Enter the role of the person to whom task will be assigned ")
        result = gmanager.task_check_gm(role)
        if result:
            assigned_by = input("Enter the name who is assigning task: ")
            assigned_to = input("Enter the name to whom task is assigned: ")
            with open(task_list) as json_file:
                data = json.load(json_file)
            for val in data:
                if val['name'] == name and val['status'] == 'unassigned':
                    val['status'] = 'assigned'
                    val['assigned_by'] = assigned_by
                    val['assigned_to'] = assigned_to
            with open(task_list, mode="w") as json_file:
                json.dump(data, json_file)
            with open(emp_details) as json_file:
                data=json.load(json_file)
            with open(emp_details) as emp_data:
                file_data = json.load(emp_data)
            for val in file_data:
                if val['role'] == role:
                    val['task_count'] += 1
            with open(emp_details, mode="w") as emp_data:
                json.dump(file_data, emp_data)
            print('Task Assigned to '+assigned_to)


def login():

    name = input("Enter your name:")
    password = input("Enter password:")

    with open(employee_self_task_assignment.emp) as json_file:
        data = json.load(json_file)
    for i in data:
        if i["name"] == name and i["password"] == password:
            if i["role"] == "0":
                role = "General Manager"
                department = i['department']
                print("Welcome "+i['name'] + " " + role + "\nDepartment:" + department)
                selection = int(input("Please select the required option:\n0-For assigning tasks \n1-For task status \n2-For Unassigned tasks \n3-Permission \n4-Notification"))
                if selection == 0:
                    task_registration()
                elif selection == 1:
                    gmanager.open_tasks()
                elif selection == 2:
                    task_registration()
                elif selection == 3:
                    with open(permission_details) as view_permission:
                        permissions = json.load(view_permission)
                    for val in permissions:
                        if val["permission"] == 'cancel' or i["permission'"] == 'reassign':
                            print(val)
                    selection_permission = input('Selection appropriate option to cancel or reassign tasks \n1-yes \n2-no')
                    if selection_permission == '1':
                        work_id = input("Enter the work id:")
                        department = input("Enter department name:")
                        task_status = input("Enter task status:")
                        with open(task_list) as task_file:
                            tasks = json.load(task_file)
                        for val in tasks:
                            if val['department'] == department and val['work_id'] == work_id:
                                val['role'] = ''
                                val['status'] = task_status
                                val['assigned_to'] = ''
                                val['assigned_by'] = ''
                                print("Permission Given")
                                break
                        with open(task_list, mode="w") as task_file:
                            json.dump(tasks, task_file)
                        with open(permission_details) as task_file:
                            tasks_updated = json.load(task_file)
                        for val1 in tasks_updated:
                            if val1['work_id'] == work_id:
                                del val1['work_id']
                                del val1['department']
                                del val1['permission']
                        with open(permission_details, mode="w") as permission_file:
                            json.dump(tasks_updated, permission_file)

                    elif selection_permission == "2":
                        pass

                elif selection == 4:
                    gmanager.general_manager_notification_look_up(i['role'])

            elif i["role"] == "1":
                role = "Manager Delivery"
                department = i['department']
                print("Welcome "+i['name'] + " " + role + "\nDepartment:" + department)
                selection = int(input("Please select the required option:\n0-For assigning tasks \n1-For Unassigned tasks \n2-Notification \n3-Cancel/Reasssign tasks"))
                if selection == 0:
                    manager.manager_as_task_assigne(department)
                elif selection == 1:
                    manager.manager_as_task_assigne(department)
                elif selection == 2:
                    gmanager.general_manager_notification_look_up(i["role"])
                elif selection == 3:
                    with open(task_list) as task_file:
                        tasks = json.load(task_file)
                    for val in tasks:
                        if val["department"] == "Delivery":
                            print(val)
                    selection_task = int(input('Selection appropriate option  \n1-cancel \n2-reassign'))
                    if selection_task == 1:
                        work_id = input("Enter task work id:")
                        department = input("Enter department name:")
                        status = 'cancel'
                        gmanager.permission_look_up(work_id, department, status)
                    elif selection_task == 2:
                        work_id = input("Enter task work id:")
                        department = input("Enter department name:")
                        status = 'reassign'
                        gmanager.permission_look_up(work_id, department, status)


            elif i["role"] == "2":
                role = "Manager Marketing"
                department = i['department']
                print("Welcome "+i['name'] + " " + role + "\nDepartment:" + department)
                selection = int(input("Please select the required option:\n0-For assigning tasks \n1-For Unassigned tasks \n2-Notification \n3-Cancel/Reasssign tasks"))
                if selection == 0:
                    manager.manager_as_task_assigne(department)
                elif selection == 1:
                    manager.manager_as_task_assigne(department)
                elif selection == 2:
                    gmanager.general_manager_notification_look_up(i["role"])
                elif selection == 3:
                    with open(task_list) as task_file:
                        tasks = json.load(task_file)
                    for val in tasks:
                        if val["department"] == "Marketing":
                            print(val)
                    selection_task = int(input('Selection appropriate option  \n1-cancel \n2-reassign'))
                    if selection_task == 1:
                        work_id = input("Enter task work id:")
                        department = input("Enter department name:")
                        status = 'cancel'
                        return gmanager.permission_look_up(work_id,department,status)
                    elif selection_task == 2:
                        work_id = input("Enter task work id:")
                        department = input("Enter department name:")
                        status = 'reassign'
                        return gmanager.permission_look_up(work_id,department,status)

            elif i["role"] == "3" or i["role"] == "4" or i["role"] == "5":
                role = "Delivery department worker"
                department = i['department']
                roles = i['role']
                name = i['name']
                print("Welcome "+i['name'] + " " + role + "\nDepartment:" + department)
                return employee_self_task_assignment.worker_self_task_assignment(department, roles, name)

            elif i["role"] == "6" or i["role"] == "7" or i["role"] == "8" or i["role"] == "9":
                role = "Marketing department worker"
                department = i['department']
                roles = i['role']
                name = i['name']
                print("Welcome "+i['name'] + " " + role + "\nDepartment:" + department)
                return employee_self_task_assignment.worker_self_task_assignment(department, roles, name)
            break


if __name__ == '__main__':
    while True:
        login()

