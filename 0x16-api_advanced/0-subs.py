#!/usr/bin/python3

''' import requests module for making HTTP requests '''
import requests


def number_of_subscribers(subreddit):
    ''' function that eries the Reddit API and returns the number of
    subscribers '''
    subrdt = subreddit
    url = 'https://www.reddit.com/r/{}/about.json'.format(subrdt)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        data = response.json().get('data').get('subscribers')
        if data is None:
            return 0
        return data
