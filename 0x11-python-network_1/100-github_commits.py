#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
