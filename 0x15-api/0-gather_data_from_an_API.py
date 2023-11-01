#!/usr/bin/python3
"""
cript that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

    user = make_employee_request('users', ('id', sys.argv[1]))
    tasks = make_employee_request('todos', ('userId', sys.argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))
