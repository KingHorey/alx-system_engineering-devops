#!/usr/bin/python3

""" import requests """

import json
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
        tasks_title = []
        """ write to CSV """
        for data in data.json():
            tasks_title.append({"username": name,
                                "task": data.get('title'),
                                "completed": data.get('completed')
                                })
        with open(f"todo_all_employees.json", 'w') as file:
            file.write(json.dumps({user_id: tasks_title}))


if __name__ == "__main__":
    gather_data()
