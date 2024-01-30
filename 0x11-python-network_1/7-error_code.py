#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL and
displays the body of the response or the error code state
"""


import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
