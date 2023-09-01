#!/usr/bin/python3
"""Getting the X-Request-Id using the requests module."""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    request_id = r.headers['X-Request-Id']
    print(request_id)
