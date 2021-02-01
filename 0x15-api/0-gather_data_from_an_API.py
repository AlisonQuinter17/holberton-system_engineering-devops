#!/usr/bin/python3
""" Gather data from an API. """
import requests
import sys

if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()
    user_name = users.get('name')
    user_id = users.get('id')
    tasks = []
    done_tasks = 0
    total_tasks = 0

    for status in todos:
        if user_id == status.get('userId'):
            if status.get('completed') is True:
                done_tasks += 1
                tasks.append(status.get('title'))
            total_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, done_tasks, total_tasks))

    for title in tasks:
        print('\t', title)
