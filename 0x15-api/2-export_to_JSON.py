#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""

from json import dump
import requests
import sys

if __name__ == "__main__":

    def make_employee_request(resource, param=None):
        """
        Retrieve employee from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # request
        res = requests.get(url)

        # json response
        res = res.json()
        return res

    user = make_employee_request('users', ('id', sys.argv[1]))[0]
    tasks = make_employee_request('todos', ('userId', sys.argv[1]))

    # format and export
    user_id = user['id']
    export = {user_id: []}
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': user['username']})

    filename = sys.argv[1] + '.json'
    with open(filename, mode='w') as f:
        dump(export, f)
