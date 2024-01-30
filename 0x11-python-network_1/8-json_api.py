#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    ch = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post(url, data={'q': ch})
    try:
        body = res.json()
        if body:
            print("[{}] {}".format(body['id'], body['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
