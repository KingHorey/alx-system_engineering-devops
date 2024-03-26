#!/usr/bin/python3

""" import requests """

import csv
import requests as req
import sys


def gather_data():
    """ gets mock employee data from an API """

    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    data = req.get(url)
    if data.status_code == 200:
        length = len(data.json())
        user_url = "https://jsonplaceholder.typicode.com/users"
        user_data = req.get(user_url, params=({'id': user_id}))
        user_data = user_data.json()
        name = user_data[0].get('username')
        done_tasks = 0
        unfinished_tasks = 0
        tasks_title = []
        """ write to CSV """
        with open("USER_ID.csv", mode='w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            for data in data.json():
                writer.writerow([user_id, name, data.get('completed'),
                                data.get('title')])


if __name__ == "__main__":
    gather_data()
