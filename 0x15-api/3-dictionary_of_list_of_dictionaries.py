#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""

from json import dump
import requests

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

    export = {}

    users = make_employee_request('users')
    for user in users:
        user_id = user['id']
        export.update({user_id: []})
        tasks_by_user = make_employee_request(
            'todos', ('userId', str(user_id)))
        for task in tasks_by_user:
            export[user_id].append({'username': user['username'],
                                    'task': task['title'],
                                    'completed': task['completed']})

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        dump(export, f)
