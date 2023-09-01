#!/usr/bin/python3
"""Takes a URL and email address and sends POST request to given URL."""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)
