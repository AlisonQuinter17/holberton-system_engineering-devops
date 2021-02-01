#!/usr/bin/python3
""" Gather data from an API. """
import requests
import sys

if __name__ == "__main__":

    todos_content = requests.get("https://jsonplaceholder.typicode.com/todos").json()
users_content = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(sys.argv[1])).json()
user_name = requests.get('name')
user_id = requests.get('id')
tasks = []

for status in todos_content:
    if user_id == status.get('userId') and status.get('completed') == True:
