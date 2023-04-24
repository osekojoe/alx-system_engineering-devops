#!/usr/bin/python3
"""
Use Rest API at https://jsonplaceholder.typicode.com/ for a given employee ID,
returns information about his/her TODO list progress.
- export data in the JSON format
"""


import sys, requests, json


def to_json(users=None, todos=None, userId=None):
    """export data in the json format"""
    data_list = []
    with open(sys.argv[1] + '.json', 'w') as f:
        for i in todos:
            data_list.append({"task": i.get('title'),
                              "completed": i.get('completed'),
                              "username": users[0].get('username')})
        data_json = {str(userId): data_list}
        json.dump(data_json, f)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_userId = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_userId).json()

        to_json(users, todos, sys.argv[1])
