#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests

def get_employee_todo_progress(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data['name']
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        if todos_response.status_code == 200:
            todos_data = todos_response.json()
            total_tasks = len(todos_data)
            done_tasks = [todo['title'] for todo in todos_data if todo['completed']]
            print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
            for task_title in done_tasks:
                print(f"\t{task_title}")
        else:
            print(f"Failed to retrieve TODO list for employee ID {employee_id}.")
    else:
        print(f"Failed to retrieve employee data for ID {employee_id}.")
employee_id = 1
get_employee_todo_progress(employee_id)
