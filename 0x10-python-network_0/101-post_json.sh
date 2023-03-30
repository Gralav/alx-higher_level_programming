#!/bin/bash
# Bash script that takes in a URL, sends a JSON POST request to the URL and displays the body of the response
curl -sX POST $1 -H "Content-Type: application/json" -d @$2
