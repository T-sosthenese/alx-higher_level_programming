#!/usr/bin/python3
"""Takes in a URL, sends request to the URL and displays response body."""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            print("Error code: {}".format(e.response.status_code))
        else:
            print("Error: {}".format(e))
