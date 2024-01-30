#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    data = {'email': argv[2]}
    data = urlencode(data).encode('ascii')

    req = Request(argv[1], method="POST", data=data)
    with urlopen(req) as res:
        output = res.read()
        print(output.decode('utf-8'))
