#!/usr/bin/python3

""" import requests """

import json
import requests as req
import sys


def gather_data():
    """ gets mock employee data from an API """

    user_url = f"https://jsonplaceholder.typicode.com/users/?id="
    todos_url = f"https://jsonplaceholder.typicode.com/todos/"
    todos = req.get(todos_url)
    if todos.status_code == 200:
        todos = todos.json()
        ids = []
        for todo in todos:
            ids.append(todo.get('userId'))
        ids = list(set(ids))
        tasks_title = []
        users_dict_data = {}
        """ write to CSV """

        for u_id in ids:
            name = req.get(user_url, params={'id': user_id})
            name = name.json()[0].get('username')
            todo = f"https://jsonplaceholder.typicode.com/users/{u_id}/todos"
            users_data = req.get(todo, params={'userId': u_id}).json()
            temp_list = []
            for data in users_data:
                temp_list.append({"username": name,
                                 "task": data.get('title'),
                                  "completed": data.get('completed')})
                tasks_title.extend(temp_list)
                users_dict_data[user_id] = tasks_title
                tasks_title = []

        with open(f"todo_all_employees.json", 'w') as file:
            file.write(json.dumps(users_dict_data))


if __name__ == "__main__":
    gather_data()
