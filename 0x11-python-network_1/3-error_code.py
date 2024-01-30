#!/usr/bin/python3

"""
sends a request to the URL and displays the body of the response
(decoded in utf-8)
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv
if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            output = res.read()
            print(output.decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
