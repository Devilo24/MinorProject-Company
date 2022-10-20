Company task Asssignment project is based on OOPs
Concept used in this project are classes and methods.

project_file.py is the main file in which all the files are imported and fuctions calls are done and to run project project_file.py needs run

For storing employee,notification,tasks, persmission data 4 json files are used with name employee_list.json,notification_file.json,permission_file.json,tasks.json 

employee_list.json contains data of 10 employees:
Hierarchy of positions is assigned according the role values
Lower the role value higher the position
role-0->General Manager Marketing and Delivery Department
role-1->Manager Delivery
role-2->Manager Marketing
role-3-5->Workers Delivery
role-6-9->Workers Marketing

In order to do count number of tasks assigned to the emloyees task_count is defined in the employee_list.json file

tasks.json file contains the list of tasks assigned to the workers

notification_file.json file contains the permissions requested by the managers to cancel tasks.

notification_file.json contains the list of notifications which are sent to managers and employees when a task is assigned to the employee.

*****************Program Flow*********************
1->Run program_file.py in terminal enter the name of the employee and the password
2->Once logged in the option list is different for every role as general manager will have the ability to check task status and and have authority to cancel tasks
3->Case-1 when general manager logs in from employee_list.json file details are fetched and once verified multiple options are displayed and accordinly function calls are made to other python files example is something related to tasks are done then functions are called from gmanager.py file and same goes for the permission and notifications as all the functions are defined the respective file of General Manager
4->Case-2 if logged in as manager of either of the two departments multiple options are displayed such as assign tasks or check for unassigned tasks or notification or ask for persmission to cancel task from the general manager. Function call related to assigning tasks made to the manager.py file and permission functions are made to the gmmanager.py file
5->Case-3 if logged in as employee the only option employees have is to assign tasks to themselves and functions specific to employees of the marketing or delivery department are defined in the employee_self_task_assignment.py file

