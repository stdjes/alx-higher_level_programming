#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id var found in the header of the response.
"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    with urlopen(sys.argv[1]) as res:
        print(res.getheader('X-Request-Id'))
