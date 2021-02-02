#!/usr/bin/python3
""" Export to JSON. """
import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()
    _name = users.get('username')
    _id = users.get('id')
    to_dict = {_id: [{"task": i.get('title'),
                      "completed": i.get('completed'),
                      "username": _name} for i in todos]}

    with open("{}.json".format(sys.argv[1]), mode="w") as id_json:
            json.dump(to_dict, id_json)
