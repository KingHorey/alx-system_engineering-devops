#!/usr/bin/python3

""" import the requests module for HTTP requests """
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit."""

    subrdt = subreddit
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subrdt)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
