#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""

import csv
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

    csv_filename = sys.argv[1] + '.csv'
    with open(csv_filename, mode='w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'],
                            user['username'],
                            task['completed'],
                            task['title']])
