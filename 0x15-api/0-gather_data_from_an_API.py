#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{employee_id}'"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
