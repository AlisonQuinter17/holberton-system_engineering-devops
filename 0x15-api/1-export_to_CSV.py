#!/usr/bin/python3
""" Export to CSV. """
import csv
import requests
import sys

if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()
    _name = users.get('username')
    _id = users.get('id')

    with open('{}.csv'.format(sys.argv[1]), mode='w') as id_csv:
        f = csv.writer(id_csv, quoting=csv.QUOTE_ALL)

        for r in todos:
            f.writerow([_id, _name, r.get('completed'), r.get('title')])
