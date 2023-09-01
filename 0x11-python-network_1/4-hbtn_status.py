#!/usr/bin/python3
"""This script fetches a url and displays the body response."""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = request.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
