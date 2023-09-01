#!/usr/bin/python3
"""Takes in a URL, sends request to the URL and displays response body."""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
