#!/usr/bin/python3
"""
Use Rest API at https://jsonplaceholder.typicode.com/ for a given employee ID,
returns information about his/her TODO list progress.
"""


import sys, requests, csv


def to_csv(users=None, todos=None):
    """export data in the CSV format"""
    fieldnames = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]

    with open(sys.argv[1] + '.csv', 'w') as csvfile:
        #map dictionary into output rows
        write = csv.DictWriter(csvfile, fieldnames=fieldnames,
                               quoting=csv.QUOTE_ALL)
        for i in todos:
            write.writerow({"USER_ID": i.get('userId'),
                           "USERNAME": users[0].get('username'),
                           "TASK_COMPLETED_STATUS": i.get('completed'),
                           "TASK_TITLE": i.get('title')})

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_userId = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_userId).json()
        todos_len = 0
        todos_arr = []
        for i in todos:
            if i.get("completed"):
                todos_arr.append(i)
                todos_len += 1

        to_csv(users, todos)