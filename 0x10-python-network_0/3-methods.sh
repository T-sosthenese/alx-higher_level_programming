#!/bin/bash
# Takes in a URL and displays all http requests the server accepts
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
