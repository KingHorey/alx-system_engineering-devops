#!/usr/bin/python3


""" import requests module """

import requests
import sys


def number_of_subscribers():
    """ function that eries the Reddit API and returns the number of
    subscribers """
    subrdt = sys.argv[1]
    url = 'https://www.reddit.com/r/{}/about.json'.format(subrdt)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        data = response.json().get('data').get('subscribers')
        return data


if __name__ == '__main__':
    print(number_of_subscribers())
