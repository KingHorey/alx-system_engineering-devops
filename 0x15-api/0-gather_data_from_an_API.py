#!/usr/bin/python3

""" import requests """
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
        name = user_data[0].get('name')
        done_tasks = 0
        unfinished_tasks = 0
        tasks_title = []
        """ get the number of completed tasks """
        for data in data.json():
            if data.get('completed') is True:
                tasks_title.append(data.get('title'))
                done_tasks += 1
            else:
                unfinished_tasks += 1
        print(f"Employee {name} is done with tasks({done_tasks}/{length}):")
        i = 0
        while (i < len(tasks_title)):
            if i == len(tasks_title) - 1:
                print("\t ", tasks_title[i])
            else:
                print("\t ", tasks_title[i], end="\n")
            i += 1


if __name__ == "__main__":
    gather_data()
