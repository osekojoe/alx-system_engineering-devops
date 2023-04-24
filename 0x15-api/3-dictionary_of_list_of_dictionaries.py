#!/usr/bin/python3
"""
Use Rest API at https://jsonplaceholder.typicode.com/ for a given employee ID,
returns information about his/her TODO list progress.
- export data in the JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        users = users.json()
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = todos.json()

        todos_dict = {}

        for user in users:
            task_list = []
            for task in todos:
                if task.get('userId') == user.get('id'):
                    task_dict = {"username": user.get('username'),
                                 "task": task.get('title'),
                                 "completed": task.get('completed')}
                    task_list.append(task_dict)
            todos_dict[user.get('id')] = task_list

        with open('todo_all_employees.json', mode='w') as file:
            json.dump(todos_dict, file)
