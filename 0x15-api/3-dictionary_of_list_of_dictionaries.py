#!/usr/bin/python3
""" Dictionary of list of dictionaries. """
import json
import requests
import sys

if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    to_dict = {u.get('id'): [{"task": t.get('title'),
                              "completed": t.get('completed'),
                              "username": u.get('username')}
                             for t in todos] for u in users}

    with open("todo_all_employees.json", mode="w") as id_json:
            json.dump(to_dict, id_json)
