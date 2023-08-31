#!/bin/bash
# Takes in a URL as argument, sends http request to the URL, displays length
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
