#!/bin/bash
# Displays http status codes
curl -sI -o /dev/null - w "%{http_code}" "$1"
